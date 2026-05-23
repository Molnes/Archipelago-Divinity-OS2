from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, Option, OptionSet, PerGameCommonOptions, Range, Toggle


class Goal(Choice):
    display_name = "Goal"

    option_kill_Voidwoken_Drillworm = 0
    default = option_kill_Voidwoken_Drillworm


class KillSanity(Choice):
    display_name = "KillSanity"
    option_off = 0
    option_murderhobo = 1

    default = option_murderhobo


class QuestSanity(Choice):
    display_name = "QuestSanity"
    option_off = 0
    option_quest_everything = 1

    default = option_quest_everything


class Deathlink(Toggle):
    display_name = "Deathlink"
    default = False


class EnableTraps(OptionSet):
    valid_keys = ["Stun", "Monster"]
    display_name = "Enabled Trap List"
    default = {"Stun", "Monster"}


@dataclass
class DOS2Options(PerGameCommonOptions):
    goal: Goal
    kill_sanity: KillSanity
    quest_sanity: QuestSanity
    deathlink: Deathlink
    enable_traps: EnableTraps
