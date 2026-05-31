from __future__ import annotations

import asyncio
import json
import logging
import os
import sys
import typing
from itertools import count
from typing import Dict, Iterable, List, Tuple

import ModuleUpdate
import Utils

from . import items as dos2_items
from . import locations as dos2_locations
from .world import DOS2

ModuleUpdate.update()


import Utils

if __name__ == "__main__":
    Utils.init_logging("Dos2Client", exception_logger="Client")


goal = -1


from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, gui_enabled, logger, server_loop
from NetUtils import ClientStatus

wg_logger = logging.getLogger("WG")


class DOS2ClientCommandProcessor(ClientCommandProcessor):
    def _cmd_resync(self):
        """Manually trigger a resync"""
        self.output("Syncing items.")
        self.syncing = True


class DOS2ClientContext(CommonContext):
    command_processor = DOS2ClientCommandProcessor
    game = "Divinity: Original Sin 2"
    items_handling = 0b111  # full remote
    file_dir = ""
    comm_file_sent_items = "ap_in.json"
    comm_file_locations_checked = "ap_out.json"

    def __init__(self, server_address, password):
        super(DOS2ClientContext, self).__init__(server_address, password)
        self.syncing = False
        game_options = DOS2.settings
        if game_options and getattr(game_options, "root_directory", None):
            try:
                self.file_dir = game_options.root_directory
            except FileNotFoundError:
                self.file_dir = ""
        else:
            self.file_dir = ""

    def run_gui(self):
        from kvui import GameManager

        class DOS2GameManager(GameManager):
            logging_pairs = [("Client", "Archipelago")]
            base_title = "Archipelago - Divinity: Original Sin 2 Client"

            def build(self):
                container = super().build()

                from kivy.metrics import dp
                from kivymd.uix.boxlayout import MDBoxLayout
                from kivymd.uix.button import MDButton, MDButtonText
                from kivymd.uix.label import MDLabel
                from kivymd.uix.textfield.textfield import MDTextField

                file_layout = MDBoxLayout(
                    orientation="horizontal",
                    size_hint_y=None,
                    height=dp(48),
                    spacing=dp(8),
                    padding=(dp(8), 0, dp(8), 0),
                )

                label = MDLabel(
                    text="DOS2 File Directory:",
                    size_hint_x=None,
                    width=dp(170),
                    halign="left",
                    valign="center",
                )
                label.bind(size=lambda inst, value: setattr(inst, "text_size", value))

                self.file_dir_input = MDTextField(
                    text=self.ctx.file_dir or "",
                    mode="filled",
                    size_hint_x=1,
                )

                def on_text(_, value):
                    self.ctx.file_dir = value

                self.file_dir_input.bind(text=on_text)

                apply_button = MDButton(
                    MDButtonText(text="Apply"),
                    style="filled",
                    size_hint_x=None,
                    width=dp(90),
                )
                apply_button.bind(on_release=lambda *_: setattr(self.ctx, "file_dir", self.file_dir_input.text))

                file_layout.add_widget(label)
                file_layout.add_widget(self.file_dir_input)
                file_layout.add_widget(apply_button)

                # Insert just above the command input row
                self.grid.add_widget(file_layout, index=1)

                return container

        self.ui = DOS2GameManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


async def game_watcher(ctx: DOS2ClientContext):
    sent_locations = set()
    last_items = []
    while not ctx.exit_event.is_set():
        try:
            # Handle resync
            if ctx.syncing:
                sync_msg = [{"cmd": "Sync"}]
                await ctx.send_msgs(sync_msg)
                ctx.syncing = False

            # Ensure communication directory exists
            if ctx.file_dir:
                try:
                    os.makedirs(ctx.file_dir, exist_ok=True)
                except Exception as dir_err:
                    logger.error(f"Failed to ensure DOS2 file directory '{ctx.file_dir}': {dir_err}")

            # --- Handle outgoing location checks ---
            out_path = os.path.join(ctx.file_dir, ctx.comm_file_locations_checked)
            dos2LocationsToSend = []
            if os.path.isfile(out_path):
                with open(out_path, "r") as f:
                    try:
                        dos2LocationsToSend = json.load(f)
                    except Exception:
                        dos2LocationsToSend = []
            else:
                with open(out_path, "w") as f:
                    f.write("[]")

            new_locations = [loc for loc in dos2LocationsToSend if loc not in sent_locations]
            sending_ids = []
            for location in new_locations:
                loc_id = dos2_locations.location_ids.get(location)
                if loc_id is None:
                    logger.warning(f"Unknown DOS2 location in ap_out.json: {location}")
                    sent_locations.add(location)
                    continue
                if ctx.server_locations and loc_id not in ctx.server_locations:
                    # Location not part of this seed (option-disabled), ignore.
                    sent_locations.add(location)
                    continue
                if loc_id not in ctx.checked_locations:
                    logger.info(f"Sending location check for {location}")
                    sending_ids.append(loc_id)
                    ctx.checked_locations.add(loc_id)
                sent_locations.add(location)

            if sending_ids:
                await ctx.send_msgs([{"cmd": "LocationChecks", "locations": sending_ids}])

            # Optionally clear sent locations from file (so Lua mod doesn't resend)
            if new_locations:
                with open(out_path, "w") as f:
                    json.dump([loc for loc in dos2LocationsToSend if loc not in sent_locations], f)

            # --- Handle incoming items ---
            # Items received from server are in ctx.items_received (list of NetworkItem)
            in_path = os.path.join(ctx.file_dir, ctx.comm_file_sent_items)
            items_to_write = []
            for network_item in ctx.items_received:
                item_name = ctx.item_names.lookup_in_game(network_item.item)
                description = dos2_items.ITEM_NAME_TO_DESCRIPTION.get(item_name, item_name)
                sender = ctx.player_names.get(network_item.player, str(network_item.player))
                items_to_write.append(
                    {
                        "Name": item_name,
                        "Description": description,
                        "Sender": sender,
                    }
                )
            # Only write if changed (or file missing)
            if items_to_write != last_items or not os.path.isfile(in_path):
                with open(in_path, "w") as f:
                    json.dump(items_to_write, f, indent=2)
                last_items = items_to_write.copy()

            await asyncio.sleep(1)
        except Exception as err:
            logger.error("Exception in communication thread, a check may not have been sent: " + str(err))


def launch_dos2_client(*launch_args: str) -> None:
    async def main():
        args = parser.parse_args(launch_args)
        ctx = DOS2ClientContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        progression_watcher = asyncio.create_task(game_watcher(ctx), name="Dos2 Progression Watcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await progression_watcher

        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="Dos2 Client")
    asyncio.run(main())
    colorama.deinit()
