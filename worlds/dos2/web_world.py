from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld


class DOS2WebWorld(WebWorld):
    game = "Divinity: Original Sin 2"
    theme = "grassFlowers"
    setup_en = Tutorial(
        "Divinity: Original Sin 2 Setup Guide",
        "A guide to setting up DOS2 for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Molnes", "JeyKey09"],
    )

    tutorials = [setup_en]
