from typing import ClassVar

from worlds.AutoWorld import World

from . import items, locations, options, regions, settings, web_world


class DOS2(World):
    """
    Divinity: Original Sin 2
    """
    game = "Divinity: Original Sin 2"
    item_name_to_id = items.ITEM_NAME_TO_ID
    location_name_to_id = locations.location_ids
    origin_region_name = "Tutorial"
    options_dataclass = options.DOS2Options
    options: options.DOS2Options
    item_name_groups = {}
    settings: ClassVar[settings.DOS2Settings]
    web = web_world.DOS2WebWorld()

    def create_regions(self):
        regions.create_regions(self)
        locations.create_locations(self)

    def set_rules(self):
        # No logic rules yet.
        pass

    def create_items(self):
        items.create_all_items(self)

    def create_item(self, name: str):
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self):
        return self.options.as_dict("goal", "kill_sanity", "quest_sanity", "deathlink", "enable_traps")
