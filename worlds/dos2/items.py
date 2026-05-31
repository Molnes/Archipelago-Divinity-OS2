from __future__ import annotations

from typing import TYPE_CHECKING
from .options import DOS2Options
from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import DOS2


class DOS2ItemMetaData:
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id


class DOS2TreasureMetadata(DOS2ItemMetaData):
    def __init__(self, name: str, id: str, levelsRequired: int):
        super().__init__(name, id)
        self.levelsRequired = levelsRequired


class DOS2SkillMetaData(DOS2TreasureMetadata):
    def __init__(self, name: str, id: str, levelsRequired: int, sourceCost: int):
        super().__init__(name, id, levelsRequired)
        self.sourceCost = sourceCost



SKILLOFFSET = 0xFF
SKILLS = {
    "Cone_": [
        ("RadialBlowback", "?", 0, 0),
        ("Flamebreath", "Dragon's Blaze", 0, 0),
        ("GroundSmash", "?", 0, 0),
        ("SteamLance", "Steam Lance", 3, 2),
        ("CorrosiveSpray", "Corrosive Spray", 4, 0),
        ("Shatter", "?", 0, 0),
        ("SilencingStare", "Silencing Stare", 0, 1),
    ],
    "Dome_": [("CircleOfProtection", "Circle Of Protection", 0, 1)],
    "Jump_": [
        ("CloakAndDagger", "Cloak And Dagger", 2, 0),
        ("TacticalRetreat", "Tactical Retreat", 2, 0),
        ("PhoenixDive", "Phoenix Dive", 2, 0),
        ("BonePileBurrow", "?", 0, 0),
    ],
    "MultiStrike_": [("BlinkStrike", "?", 0, 0), ("Vault", "?", 0, 0)],
    "Projectile_": [
        ("FlareStart", "?", 0, 0),
        ("InfectiousFlame", "?", 0, 0),
        ("ChainHeal", "?", 0, 0),
        ("IceFan", "Ice Fan", 2, 0),
        ("DimensionalBolt", "Dimensional Bolt", 0, 0),
        ("AcidSpores", "Acid Sporce", 3, 2),
        ("ChainLightning", "Chain Lightning", 3, 1),
        ("ThrowDust", "Throw Dust", 2, 0),
        ("DustBlast", "Dust Blast", 4, 1),
        ("SpinWeb", "?", 0, 0),
        ("Multishot", "Barrage", 2, 0),
        ("SkyShot", "Sky Shot", 2, 0),
        ("ArrowSpray", "Arrow Spray", 3, 1),
        ("Fireball", "Fireball", 2, 0),
        ("FlamingDaggers", "Searing Daggers", 1, 0),
        ("PyroclasticRock", "?", 0, 0),
        ("PyroclasticEruption", "PyroClastic Eruption", 5, 3),
        ("LightningBolt", "?", 0, 0),
        ("Superconductor", "Super Conductor", 3, 0),
        ("PiercingShot", "?", 0, 0),
        ("Snipe", "?", 0, 0),
        ("Ricochet", "Ricochet", 1, 0),
        ("BallisticShot", "BallisticShot", 2, 0),
        ("ThrowingKnife", "Throwing Knife", 1, 0),
        ("FanOfKnives", "Fan Of Knives", 3, 1),
        ("Chloroform", "Chloroform", 1, 0),
        ("Mark", "?", 0, 0),
        ("BouncingShield", "BouncingShield", 1, 0),
        ("LaunchBomber", "?", 0, 0),
        ("PoisonDartStart", "?", 0, 0),
        ("PinDown", "Pin Down", 1, 0),
        ("LivingBomb_Explosion", "?", 0, 0),
    ],
    "ProjectileStrike_": [
        ("HailStrike", "Hail Strike", 1, 0),
        ("RainOfArrows", "?", 0, 0),
        ("MeteorShower", "Meteor Shower", 5, 3),
        ("HailAttack", "?", 0, 0),
        ("DazingBolt", "Dazing Bolt", 2, 0),
    ],
    "Quake_": [("Earthquake", "EarthQuake", 2, 0)],
    "Rain_": [("Water", "Rain", 1, 0), ("Blood", "Raining Blood", 2, 0), ("Oil", "?", 0, 0)],
    "Rush_": [
        ("BatteringRam", "Battering Ram", 1, 0),
    ],
    "Shout_": [
        ("BanishSelf", "?", 0, 0),
        ("SpiritVision", "Spirit Vision", 0, 0),
        ("GlobalCooling", "Global Cooling", 1, 0),
        ("IceBreaker", "Ice Breaker", 3, 0),
        ("Contamination", "Contamination", 1, 0),
        ("FavourableWind", "Favourable Wind", 1, 0),
        ("ElectricFence", "?", 0, 0),
        ("BlindingRadiance", "Blinding Radiance", 1, 0),
        ("FleshSacrifice", "Flesh Sacrifice", 0, 0),
        ("Whirlwind", "Whirlwind", 2, 0),
        ("Adrenaline", "Adrenalin", 1, 0),
        ("PlayDead", "Play Dead", 0, 0),
        ("Ignition", "Ignition", 1, 0),
        ("Taunt", "Taunt", 1, 0),
        ("EtherealSoles", "?", 0, 0),
        ("ChameleonSkin", "Chameleon Cloak", 1, 0),
        ("ChainPull", "?", 0, 0),
        ("InspireStart", "Inspire?", 0, 0),
        ("NullResistanceStart", "Flay Skin?", 1, 0),
        ("CauseFear", "?", 0, 0),
        ("Deafen", "?", 0, 0),
        ("RecoverArmour", "Mage Armor?", 1, 0),
        ("BarbedCoat", "?", 0, 0),
        ("DeflectiveBarrier", "Deflective Barrier", 2, 0),
        ("GuardianAngel", "Guardian Angel", 3, 0),
        ("ThickOfTheFight", "Thick Of the Fight", 3, 1),
        ("InnerDemon", "Summon Inner Demon", 0, 1),
        ("Supernova", "SuperNova", 2, 0),
        ("FlamingTongues", "Flaming Tongues", 2, 0),
        ("HealingTears", "Healing Tears", 2, 0),
        ("FrostAura", "?", 0, 0),
        ("FireBrand", "FireBrand", 3, 0),
        ("VacuumAura", "Vacumm Auro", 2, 0),
        ("MendMetal", "Mend Metal", 2, 0),
        ("PoisonWave", "Poison Wave", 2, 0),
        ("BoneCage", "Bone Cave", 1, 0),
        ("NecromancerTotems", "Totems of the Necromancer", 5, 0),
        ("SiphonPoison", "Siphon Poison"),
        ("BullHorns", "Bull Horns", 1, 0),
        ("Wings", "Spread Your Wings", 2, 0),
        ("SteelSkin", "Heart Of Steel", 2, 0),
        ("ShedSkin", "Skin Graft?", 3, 1),
        ("FlamingSkin", "Flaming Skin", 4, 1),
        ("IceSkin", "Icy Skin", 4, 1),
        ("PoisonousSkin", "Poisonous Skin", 4, 1),
        ("JellyfishSkin", "Jellyfish Skin", 4, 1),
        ("MedusaHead", "Medusa Head", 2, 0),
        ("SpiderLegs", "Spider Legs", 2, 0),
        ("Apotheosis", "Apotheosis", 5, 3),
        ("BreakTheShackles", "BreakTheShackles", 0, 1),
        ("SmokeCover", "Smoke Cover", 2, 0),
        ("MassCorpseExplosion", "Mass Corpse Explosion", 4, 1),
        ("MassCleanseWounds", 4, 1),
        ("SparkingSwings", "Sparking Swings", 2, 0),
        ("VampiricHungerAura", "Vampiric Hunger Aura", 4, 1),
        ("Cryotherapy", "Cryotherapy", 2, 0),
        ("MassCryotherapy", "Mass Cryotherapy", 4, 1),
        ("OilyCarapace", "Oily Carapace", 2, 0),
        ("MassOilyCarapace", "Mass Oily Carapace", 4, 1),
        ("EvasiveAura", "EvasiveAuro", 4, 1),
        ("BreathingBubble", "Breathing Bubble", 2, 0),
        ("MassBreathingBubbles", "Mass Breathing Bubbles", 4, 1),
        ("VenomCoating", "Venom Coating", 2, 0),
        ("VenomousAura", "Venomous Aura", 4, 1),
        ("ReactiveArmor", "Reactive Armor", 2, 0),
    ],
    "Storm_": [
        ("Lightning", "ThunderStorm", 5, 3),
        ("Ethereal", "Ethereal Storm", 5, 3),
        ("Blood", "Blood Storm", 5, 3),
    ],
    "Summon_": [
        ("FireSlug", "Summon FireSlug", 3, 1),
        ("ArtilleryPlant", "Summon Artillery Plant", 3, 1),
        ("Cat", "Summon Cat Familiar", 0, 0),
        ("Condor", "Summon Condor", 0, 0),
        ("TotemFromSurface", "Elemental Totem?", 1, 0),
        ("BonePile", "Summon Bone Pile", 0, 0),
        ("BloodHeart", "Summon BloodHeart?", 0, 0),
        ("SoulWolf", "Summon Ifan's Soul Wolf", 0, 1),
        ("PlanarGateway", "Planar Gateway", 3, 2),
    ],
    "Target_": [
        ("SourceVampirism", "Source Vampirism", 0, 0),
        ("SourceDisruption", "?", 0, 0),
        ("ConsumeCorpse", "?", 0, 0),
        ("Bless", "Bless", 0, 0),
        ("Curse", "Curse", 0, 0),
        ("TentacleLash", "Tentacle Lash", 1, 0),
        ("FireWhip", "Fire Whip", 2, 0),
        ("BurnMyEyes", "Peace of mind?", 1, 0),
        ("Haste", "Haste", 1, 0),
        ("TimeWarp", "Time Warp", 0, 0),
        ("RangedInfusion", "FarSight Infusion", 1, 0),
        ("Harmony", "?", 0, 0),
        ("SoulMate", "Soul Mate", 2, 0),
        ("MaddeningSong", "Maddening Song", 0, 0),
        ("Challenge", "Challenge", 3, 0),
        ("Sabotage", "Sabotage", 2, 0),
        ("MassSabotage", "Mass Sabotage", 4, 1),
        ("Farsight", "FarSight", 3, 1),
        ("EvasiveManeuver", "Tactical Retreat?", 2, 0),
        ("StripResistance", "Flay Skin", 3, 0),
        ("CleanseWounds", "Cleanse Wounds", 2, 0),
        ("VampiricHunger", "Vampiric Hunger", 2, 0),
        ("VacuumTouch", "Vacuum Touch", 2, 0),
        ("CorrosiveTouch", "Corrosive Touch", 2, 0),
        ("Fireblood", "Bleed Fire?", 2, 0),
        ("SpontaneousCombustion", "Spontaneous Combustion", 2, 0),
        ("WinterBlast", "WinterBlast", 2, 0),
        ("PressureSpike", "Pressure Spike", 2, 0),
        ("Squall", "Blinding Squall?", 0, 0),
        ("Restoration", "Restoration", 1, 0),
        ("FrostyShell", "Armour Of Frost?", 1, 0),
        ("DeathsDoor", "Living On the edge?", 0, 0),
        ("KneeBreaker", "?", 0, 0),
        ("DemonicBargain", "?", 0, 0),
        ("SleepingArms", "?", 0, 0),
        ("CryogenicStasis", "Cryogenic Stasis", 2, 0),
        ("Fortify", "Fortify", 1, 0),
        ("RockSpikes", "Impalment?", 2, 0),
        ("PetrifyingTouch", "Petrifying Touch", 0, 0),
        ("ShockingTouch", "Shocking Touch", 1, 0),
        ("DecayingTouch", "Decaying Touch", 1, 0),
        ("DemonicStare", "Demonic Stare", 0, 0),
        ("DeathWish", "Death Wish", 2, 0),
        ("GraspOfTheStarved", "Grasp Of The Starved", 3, 2),
        ("ShacklesOfPain", "Shackles Of Pain", 2, 0),
        ("MosquitoSwarm", "MosquitoSwarm", 1, 0),
        ("CripplingBlow", "Crippling Blow", 1, 0),
        ("Enrage", "Enrage", 2, 0),
        ("Overpower", "Overpower", 5, 3),
        ("SerratedEdge", "?", 0, 0),
        ("CorruptedBlade", "Corrupted Blade", 2, 0),
        ("TerrifyingCruelty", "Terrifying Cruelty", 3, 0),
        ("GagOrder", "Gag Order", 2, 0),
        ("FirstAid", "First Aid", 1, 0),
        ("ReactionShot", "Reaction Shot", 1, 0),
        ("Condense", "?", 0, 0),
        ("Vaporize", "?", 0, 0),
        ("ElementalArrowheads", "Elemental ArrowHeads", 1, 0),
        ("BlessedSmokeCloud", "Blessed SmokeCloud", 4, 2),
        ("BlackShroud", "Black Shroud", 3, 1),
        ("Windwalker", "Wind Walker", 1,0),
        ("Fatality", "Fatality", 1, 0),
        ("DaggersDrawn", "Daggers Drawn", 3, 2),
        ("TargetedOilSurface", "?", 0, 0),
        ("InvisibilityTarget", "?", 0, 0),
        ("Equalize", "Equalize", 3, 0),
        ("BanishSummon", "Banish?", 0, 0),
        ("Silence", "Silence?", 0, 0),
        ("Charm", "Charm?", 0, 0),
        ("Infect", "Infect", 2, 0),
        ("ChickenTouch", "Chicken Claw", 1, 0),
        ("FlamingCrescendo", "Flaming Crescendo", 3, 0),
        ("LivingBomb", "LivingBomb?", 0, 0),
        ("ArcaneStitch", "Arcane Stitch", 3, 1),
        ("WormTremor", "Worm Tremor", 2, 0),
        ("CorpseExplosion", "Corpse Explosion", 2, 0),
        ("MasterOfSparks", "Master of Sparks", 4, 0),
        ("BloodBubble", "Blood Bubble?", 0, 0),
        ("Cannibalize", "Cannibalize", 3, 0),
        ("Supercharge", "SuperCharger", 2, 0),
        ("Terrify", "Terrify?", 0, 0),
        ("Apportation", "Apportation?", 0, 0),
        ("BloatedCorpse", "Raise Bloated Corpse?", 1, 0),
    ],
    "Teleportation_": [
        ("FreeFall", "?", 0, 0),
        ("Netherswap", "Nether Swap", 2, 0),
        ("ForcePush", "?", 0, 0),
        ("SwapGround", "Terrain Transmutation", 2, 0),
        ("LastRites", "Last Rites", 3, 0),
    ],
    "Tornado_": [("Air", "Tornado", 3, 0)],
    "Wall_": [("LivingWall", "Living Wall", 3, 0)],
    "Zone_": [
        ("LaserRay", "Laser Ray", 2, 0),
    ],
}

def _build_skill_items():
    item_names: list[str] = []
    internal_name: dict[str, str] = {}
    for category, skills in SKILLS.items():
        for skill in skills:
            internal_name = skill[1]
            display_name = skill[0] if len(skill) > 1 and isinstance(skill[1], str) else ""
            if display_name and display_name != "?":
                item_name = f"Skill-{display_name}"
                item_names.append(item_name)
                internal_name[item_name] = f"Skill-{category}{internal_name}"
    return item_names, internal_name

_SKILL_ITEM_NAMES, ITEM_NAME_TO_INTERNAL = _build_skill_items()

# Every item must have a unique integer ID associated with it.
ITEM_NAME_TO_ID = {name: index for index, name in enumerate(_SKILL_ITEM_NAMES, SKILLOFFSET)}
ID_TO_ITEM_NAME = {id_: name for name, id_ in ITEM_NAME_TO_ID.items()}

class DOS2Item(Item):
    game = "Divinity: Original Sin 2"


def get_item_name_to_id():
    return ITEM_NAME_TO_ID

def translate_from_display(name : str):
    if name.startswith("Skill-"):
        indexing = name.removeprefix("Skill-")

def get_all_item_names(options=DOS2Options) -> list[str]:
    # For now, all skills are always in the pool. You can add filtering by options if needed.
    return list(ITEM_NAME_TO_ID.keys())


def get_random_filler_item_name(world: "DOS2") -> str:
    return world.random.choice(get_all_item_names(world.options))


def create_item_with_correct_classification(world: "DOS2", name: str) -> DOS2Item:
    classification = ItemClassification.filler
    if name.startswith("Skill") or name.startswith("Treasure"):
        classification = ItemClassification.useful
    elif name.endswith("LevelUp"):
        classification = ItemClassification.progression
    return DOS2Item(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: "DOS2") -> None:
    item_names = get_all_item_names(world.options)
    itempool = [create_item_with_correct_classification(world, name) for name in item_names]

    # Fill remaining locations with repeatable filler items
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    while len(itempool) < number_of_unfilled_locations:
        itempool.append(create_item_with_correct_classification(world, get_random_filler_item_name(world)))

    world.multiworld.itempool += itempool


# Legacy stub
GenerateSkills = get_all_item_names
