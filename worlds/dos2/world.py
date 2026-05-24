from typing import ClassVar

from worlds.AutoWorld import World

from . import items, locations, options, regions, settings, web_world


class DOS2(World):
    """
    Divinity: Original Sin 2
    """

    game = "Divinity: Original Sin 2"
    item_name_to_id = {}
    location_name_to_id = {}
    options_dataclass = options.DOS2Options
    options: options.DOS2Options
    item_name_groups = {}
    settings = ClassVar[settings.DOS2Settings]
    web = web_world.DOS2WebWorld()

    def create_regions(self):
        regions.create_regions(self)

    def generate_basic(self):
        return super().generate_basic()
