from worlds.AutoWorld import World


class DOS2(World):
    """
    Divinity: Original Sin 2
    """

    game = "Divinity: Original Sin 2"
    item_name_to_id = {}
    location_name_to_id = {}
    options_dataclass = None
    options: None
    item_name_groups = {}
    web = None

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)

    def create_regions(self):
        return super().create_regions()
    
    def generate_basic(self):
        return super().generate_basic()
    
    