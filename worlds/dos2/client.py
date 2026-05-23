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
    game_name = "Divinity: Original Sin 2"
    items_handling = 0b111  # full remote
    file_dir = ""
    comm_file_sent_items = "ap_in.json"
    comm_file_locations_checked = "ap_out.json"

    def __init__(self, server_address, password):
        super(DOS2ClientContext, self).__init__(server_address, password)
        self.syncing = False

    def run_gui(self):
        from kvui import GameManager

        class DOS2GameManager(GameManager):
            logging_pairs = [("Client", "Archipelago")]
            base_title = "Archipelago - Divinity: Original Sin 2 Client"

        self.ui = DOS2GameManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


async def game_watcher(ctx: DOS2ClientContext):
    once = False
    while not ctx.exit_event.is_set():
        try:
            if ctx.syncing == True:
                sync_msg = [{"cmd": "Sync"}]
                await ctx.send_msgs(sync_msg)
                ctx.syncing = False
            sending = []
            victory = False
            dos2LocationsToSend = []

            path = os.path.join(ctx.file_dir, ctx.comm_file_locations_checked)
            if os.path.isfile(path):
                with open(path, "r") as f:
                    dos2LocationsToSend = json.load(f)
            else:
                with open(path, "w") as f:
                    f.write("[]")

            if goal != 1:
                for location in dos2LocationsToSend:
                    logger.info("Sending location check for " + location)

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
