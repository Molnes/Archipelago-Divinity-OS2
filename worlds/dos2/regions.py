from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import DOS2

def create_and_connect_regions(world : "DOS2") -> None:
    create_regions(world)
    connect_regions(world)

def create_regions(world: "DOS2") -> None:
    world.multiworld.regions += [
        create_region("Tutorial", world),
        create_region("Fort Joy", world),
    ]


def create_region(name: str, world: "DOS2"):
    return Region(name, world.player, world.multiworld)

def connect_regions(world: "DOS2") -> None:
    tutorial = world.get_region("Tutorial")
    fort_joy = world.get_region("Fort Joy")
    tutorial.connect(fort_joy, "Tutorial To Fort Joy")