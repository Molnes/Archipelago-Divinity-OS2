from BaseClasses import Entrance, Region

from .world import DOS2

TUT_Tutorial = {
    "Starting Deck": "TUT - Starting Deck",
    "Lower Deck": "TUT - Lower Deck",
    "Lower Deck Attacked": "TUT - Lower Deck Attacked",
    "Middle Deck": "TUT - Middle Deck Attacked",
    "Upper Deck": "TUT - Upper Deck Attacked",
}

FTJ = {
    "Beach": "Fort Joy Beach",
    "Fort": "Fort Joy",
    "Past Fort": "Past Fort Joy",
}

def create_regions(world : DOS2):


    Tutorial = create_region(TUT_Tutorial["Starting Deck"], world)
    Tutorial.exits.append(Entrance(world.player, "Ladder To LowerDeck", Tutorial))
    world.regions.append(Tutorial)
    
    Tutorial_LowerDeck = create_region(TUT_Tutorial["Lower Deck"], world)
    
    Tutorial_LowerDeck_Attacked = create_region(TUT_Tutorial["Lower Deck Attacked"], world)
    Tutorial_LowerDeck.exits.append(Entrance(world.player, "Triggered Windego", ""))

def create_region(name : str, world : DOS2):
    return Region(TUT_Tutorial["Starting Deck"], world.player, world.multiworld) 