from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from .world import DOS2


from BaseClasses import Location

class DOS2Location(Location):
    game = "Divinty Original Sins 2"

Quest_Tut = {
    "TUT_ShipMurder": "Escaped the Shipped",
    "TUT_ShipInvestigation": "Found the murderer on the ship",
    "CORE_Chapter1": "Core Chapter 1 Done",
}
Quest_Tut_id = {f"TUT - {Quest_Tut[location]}": number for (number, location) in enumerate(Quest_Tut, 0x0)}

Kill_Tut = {
"S_TUT_LowerDeck_PrayingMagister_096479c9-a702-4161-a5ba-fb2b3312bf76": "Magister Viktar - (57; -248)",
"S_TUT_Sheep_122fdf4d-59df-46ea-8192-93700598b51f": "Sheep - (29; -247)",
"S_TUT_MD_DeadMagister7_1403ab9b-aaa8-4aa3-9062-0c04a619e1f1": "Magister Knight - (12; -187)",
"S_TUT_LowerDeck_SherlockMagister_16b46c26-5c0f-4567-84cf-8a1a68134a2e": "Magister Waters - (21; -251)",
"S_TUT_MD_DeadMagister5_2d33316f-d660-4ed7-bd32-e253f54459ba": "Magister Priest Medwyn - (30; -177)",
"S_TUT_TopDeckVoidling11_2fcb5b84-875f-42bd-ac80-6f8495c6a47c": "Viscous Voidling - (28; 18)",
"S_TUT_TopDeckVoidling10_bd0123ae-26fd-4dad-8326-b6ae9a3fc1c5": "Viscous Voidling - (27; 16)",
"S_TUT_Magister5_41d4c470-7aa1-4fba-8d46-16bb761b085a": "Magister Murtof - (77; -191)",
"S_TUT_LowerDeck_Magister_Grunt_Investigator_000_47ab7059-829c-4523-adf2-6cf91fa3b29f": "Magister Jalen - (31; -243)",
"S_TUT_DeadMagister_TentaclesTop_5bb96a55-cd6b-4db0-9af1-f1da42b8971d": "Magister Knight - (18; 19)",
"S_TUT_MD_DeadMagister4_5bf1d00c-8e35-493f-88a0-fc649009763c": "Magister Swordsman - (37; -193)",
"S_TUT_MD_DeadMagister3_7c8990c4-9771-471d-a9f8-f2849463119e": "Magister Knight - (35; -186)",
"S_TUT_MD_DeadMagister2_7d40ca96-bac3-4883-96a0-565f3c06dfe8": "Magister Ranger - (45; -177)",
"S_TUT_LowerDeck_LohseSongBoy1_835a993e-1bf1-4e6f-8922-20dd8b99bca4": "Paulie - (40; -235)",
"S_TUT_LowerDeck_GruelServer_849900b9-e78d-47c7-87f3-c8d97f797d36": "Namiyah - (60; -241)",
"S_TUT_MD_DeadMagister1_84b8d088-2358-4283-a225-7a18128677b0": "Magister Ceri - (48; -191)",
"Humans_Male_RedFaction_Ranger_000_84f56b64-7990-472e-8b62-824c63db3867": "Magister Ranger - (19; -188)",
"S_TUT_Humans_Female_Magister_Priest_000_9d17cf06-6fad-49a8-82de-54518a9bf5df": "Magister Siwan - (15; -308)",
"TUT_CargoDeck_Humans_Male_Magister_Grunt_000_a06e61dd-58c6-4119-99be-716c3a4fc1ef": "Magister Rennart - (67; -301)",
"S_TUT_LowerDeck_MagisterMurderSceneGuard_000_a48a580b-6ba5-4b65-ad71-cc422ccff47b": "Magister Cadoc - (23; -246)",
"S_TUT_LowerDeck_Officer_X_a658e0ea-db65-4be9-82c0-40629a2d0340": "Magister William - (75; -244)",
"S_TUT_LowerDeck_CrossBowMagister_001_b2ec3611-6484-4168-9039-c092bcdea52d": "Magister Ygritte - (76; -243)",
"S_TUT_TopDeck_LivingMagister1_b5e74192-498f-4eb3-844a-4a817f9802d3": "Magister Knight - (23; 17)",
"S_TUT_Magister6_b8e00c9c-8f50-4630-933b-958974866724": "Magister Ricks - (77; -190)",

"S_TUT_LowerDeck_ExitDoorGuard_001_bf967ae2-69a9-4791-8f80-ad72236edaf7": "Magister Payde - (63; -233)",
"S_TUT_LowerDeck_CrossBowMagister_000_c4531ec5-203f-4ff2-95f6-ac14b9cf7994": "Magister Yona - (74; -243)",
"S_TUT_CargoHold_UnrulyPrisoner_d7a61dc6-a249-4e97-9914-53ea24e320ae": "Hemwar - (73; -312)",
"S_TUT_TopDeckMagister1_de400bda-b14e-4cff-b5f5-737781437902": "Magister Knight - (52; 24)",
"S_TUT_TopDeckMagister2_e2d47d73-4f9d-4de2-8a3c-c774a0ea114a": "Captain Kalwyn - (52; 26)",
"Humans_Female_Redfaction_Inquisitor_A_000_f4141f6d-e03e-4179-bb6b-b35f9a0c37d1": "Magister Inquisitor - (12; -181)",
"S_TUT_MD_DeadMagister6_fc0b8aff-7b96-4302-ba2b-94e0a7c3f9fb": "Magister Swordsman - (30; -185)",
"S_TUT_LowerDeck_LohseSongGirl1_a681c125-8493-4046-ab1f-6c2201336a22": "Trice - (41; -236)",

}
Kill_Tut_id = {f"Killed {Kill_Tut[location]} at the boat": number for (number, location) in enumerate(Kill_Tut, 0x40)}

Quest_FTJ = {
    "FTJ_Escape": "Escaped Fort Joy",
    "FTJ_Escape_Island": "Escaped Fort Joy Island",
    "FTJ_Escape_Island_SUBA": "",
    "FTJ_Escape_Island_SUBB": "",
    "FTJ_Escape_Island_SUBC": "",
    "FTJ_Voice": "Found out where the voices came from",
    "FTJ_Godwoken": "Talked to god",
    "FTJ_Hunted": "",
    "FTJ_Seeker": "",
    "RC_FTJ_OlgoSaheila": "",
    #"RC_FTJ_SourceCollar": "Got rid of their source collar",
    "RC_FTJ_MurderousGheist": "",
    "FTJ_SourceHounds": "",
    "FTJ_Arena": "",
    "RC_FTJ_SoulJar": "",
    "FTJ_SaheilaFate": "",
    "RC_FTJ_SaheilaSignet": "",
    "FTJ_Teleporter": "",
    "FTJ_Elodi": "",
    "FTJ_SW_Illusionist": "",
    "FTJ_SW_HurtSeekers": "",
    "FTJ_SW_StuckHaunting": "",
    "FTJ_SW_Necromancers": "",
    "FTJ_SW_BraccusArmory": "Found braccu's armory",
    "FTJ_SW_CursedRing": "Got a cursed ring",
    "FTJ_SW_UndeadTowerMaze": "Went trough the undead tower maze",
    "FTJ_SW_CursedPig": "Saved (or killed) the pigs",
    "FTJ_SW_PurgedDragon": "Saved (or killed) the dragon",
    "FTJ_SW_CallToArms": "",
    "FTJ_SW_Shriekers": "Dealt with the shriekers",
    "FTJ_SW_Tyrant": "",
    "FTJ_Ifan_DarkFaction": "",
    "FTJ_Ifan_DarkFaction_SUBA": "",
    "FTJ_Ifan_DarkFaction_SUBB": "",
    "FTJ_OriginRedPrince": "",
    "FTJ_OriginRedPrince_HouseOfShadows": "Found a assasinasion cult",
    "FTJ_OriginRedPrince_Princess": "",
    "FTJ_OriginLohse": "",
    "FTJ_OriginSebille": "",
    "FTJ_OriginSebille_SUBA": "",
    "FTJ_OriginSebille_SUBB": "",
    "FTJ_OriginSebille_SUBC": "",
    "FTJ_OriginFane": "",
    "FTJ_OriginFane_SUBA": "",
    "FTJ_OriginBeast": "",
    "FTJ_COM_RedPrince": "",
    "FTJ_COM_RedPrince_Princess": "",
    "FTJ_COM_RedPrince_HouseOfShadows": "",
    "FTJ_COM_Sebille": "",
    "FTJ_COM_Sebille_SUBA": "",
    "FTJ_COM_Sebille_SUBB": "",
    "FTJ_COM_Sebille_SUBC": "",
    "FTJ_COM_Ifan": "",
    "FTJ_COM_Ifan_SUBA": "",
    "FTJ_COM_Ifan_SUBB": "",
    "FTJ_COM_Lohse": "",
    "FTJ_COM_Fane": "",
    "FTJ_COM_Fane_SUBA": "",
    "FTJ_COM_Beast": "",
    "CORE_Chapter2": "Finished chapter 2",
    "ContaminationArmour": "Got the contamination Armour",
    "FTJ_SW_BatteredAndCornered": "",
    "CaptainArmour": "Found the captain armour",
}
Quest_FTJ_id = {f"FTJ - {Quest_FTJ[location]}": number for (number, location) in enumerate(Quest_FTJ, 0x80)}

Kill_FTJ = {
    
    #Beach Beginning
    "S_FTJ_BeachVw_001_08348b3a-bded-4811-92ce-f127aa4310e0": "Fort Joy Beach - VoidWoken 1",
    "S_FTJ_BeachVw_002_1832a661-0e21-421f-acaa-a7e66e813b14": "Fort Joy Beach - VoidWoken 2",
    # Turtles
    "S_FTJ_SpikedTurtle_01_abd3afae-a6e5-452c-a94a-db57826dd082": "Turtle - (258 363)",
    "S_FTJ_SpikedTurtle_03_fb4618f9-9c61-4640-a32c-e4735783e878": "Ancient Turtle - (271 365)",
    "S_FTJ_SpikedTurtle_04_f37cb16e-027e-4a21-8504-d6cab12d9098": "Turtle - (283 349)",
    
    #Teleporting Crocs
    "S_FTJ_TeleporteQuestrCroc_001_bc1a10a1-51b6-42c5-b517-827565f6512b": "Saltwater Crocodile - (113 217)",
    "S_FTJ_TeleporteQuestrCroc_002_6be95689-ab8f-4edf-ba46-77a068594a19": "Saltwater Crocodile - (124 224)",
    "S_FTJ_TeleporteQuestrCroc_003_7cf7d4d4-de1a-4ac7-999a-1f128fac3789": "Saltwater Crocodile - (116 231)",
    # Harbor
    "S_FTJ_HarbourMagister_001_d6a4e8d9-67bc-4961-95ce-c7016357ea64": "Magister Ranger - (324 244)",
    "S_FTJ_HarbourMagister_002_14581b6d-9423-4e2c-8d19-8f1b222ab760": "Magister Inquisitor - (323 246)",
    "S_FTJ_HarbourMagister_003_75ffb9bd-5ddb-4c2c-8ad0-55c00b34be7b": "Magister Ranger - (322 244)",
    "S_FTJ_HarbourMagister_004_97492757-bbe8-42d8-af6d-35ca0ae96d36": "Magister Knight - (333 235)",
    "S_FTJ_HarbourMagister_005_55c5c79e-2260-40bd-ab1d-c2d05fe31d45": "Magister Dayva - (321 225)",
    "S_FTJ_HarbourSilentMonk_001_f7bd3244-e1e7-4079-ac95-fef6145a236e": "Silent Monk - (328 224)",
    "S_FTJ_HarbourSilentMonk_002_54b9a81b-7926-46b1-ad0d-6213c0d77749": "Silent Monk - (326 224)",
    "S_FTJ_HarbourSilentMonk_003_61bf204e-ba2e-412f-ac86-e132a3930105": "Silent Monk - (323 224)",
    "S_FTJ_HarbourSilentMonk_004_753d80ce-a515-43e3-8085-8ceacb3ceb4f": "Silent Monk - (321 224)",
    "S_FTJ_HarbourSilentMonk_005_4149080d-9cc5-424d-a8fc-c52222bb463a": "Silent Monk - (331 224)",
    # Frogs
    "S_FTJ_FrogAmbush_Melee_01_747af1e4-d204-4564-9a50-9f1955dd4723": "Charged Amphibian - (528 489)",
    "S_FTJ_FrogAmbush_Ranged_02_ffae5e44-ac8a-4f43-ab14-2e684b60d87b": "Venomous Amphibian - (503 491)",
    "S_FTJ_FrogAmbush_Ranged_03_18d2b17c-a400-4e1d-991f-d1cbb44cfac4": "Venomous Amphibian - (518 504)",
    # CourtRoom
    "S_FTJ_CourtRoomGuard_001_c51d581d-9245-431f-a1eb-88adc8149827": "Magister Swordsman - (276 139)",
    "S_FTJ_CourtRoomGuard_002_bb9fd6c4-4231-44ac-a24d-5955dc300147": "Magister Swordsman - (289 139)",
    "S_FTJ_HighPriest_2a09f30c-0a3b-495f-8386-5390a6c4c08d": "High Judge Orivand - (283 129)",
    # Trap SoulRoom
    "S_FTJ_SoulJarTrapSkeleton_001_0375d94c-b588-4a1d-bd62-e8dfbd614df4": "Pyromancer Guardian - (372 577)",
    "S_FTJ_SoulJarTrapSkeleton_002_20d96b30-c279-4f94-8815-8114e48f261e": "Blademaster Guardian - (385 566)",
    "S_FTJ_SoulJarTrapSkeleton_003_5ef951b7-a893-4b48-9ee2-7e5d754c6a83": "Cryomancer Guardian - (390 577)",
    "S_FTJ_SoulJarTrapSkeleton_004_40850e09-8b9f-4b38-8f90-a9499bcb054c": "Aeromancer Guardian - (371 556)",
    "S_FTJ_SoulJarTrapSkeleton_005_b104ee53-94a5-4d2b-a9ed-5345327a4e42": "Blademaster Guardian - (378 565)",
    "S_FTJ_SoulJarTrapSkeleton_006_a46127af-ff0f-452f-a2e1-260abd2a1001": "Eagle-Eyed Guardian - (379 577)",
    "S_FTJ_SoulJarTrapSkeleton_007_deffe0d5-11f5-44a9-b50f-497f200ad4f7": "Traitorous Guardian - (370 550)",

    #Windego
    "S_GLO_Windego_d783285f-d3be-4cba-8333-db8976cef182": "Windego - (357 192)",
    # Undead next to Windego
    "S_FTJ_SW_GuardUndead1_416ab3e9-0547-4dd3-b3b8-8b36f75707c1": "Necromancer Tasmyn - (606 606)",
    "S_FTJ_SW_GuardUndead2_6fe11cab-3331-419b-8ce0-13672a97c915": "Necromancer Gwick - (607 610)",
    "S_FTJ_SW_GuardUndead3_8dadcdd9-08dc-4228-a741-35310b42c16e": "Necromancer Rask - (610 606)",
    # Swamp 1
    "S_FTJ_SwampBuildup_A_Undead_Assassin_a54a04a3-8507-4a37-a8b6-068fd0ec8146": "Decomposing Assassin - (379 152)",
    "S_FTJ_SwampBuildup_A_Undead_Melee_01_8b70b76c-24f8-4b3c-aae8-3c78c93ab2bb": "Decomposing Swashbuckler - (386 155)",
    "S_FTJ_SwampBuildup_A_Undead_Terra_01_7dee6a3d-ef4f-4281-a311-a65d483e13d1": "Decomposing Terramancer - (389 151)",
    # Swamp 2
    "S_FTJ_SwampBuildup_B_Undead_Melee_01_e45ec44b-4033-4994-b6a4-f236dea40561": "Decomposing Swashbuckler - (391 206)",
    "S_FTJ_SwampBuildup_B_Undead_Ranger_01_1195a59b-ba51-4662-afa7-7602b224cfc8": "Decomposing Markswoman - (401 213)",
    "S_FTJ_SwampBuildup_B_Undead_Ranger_02_5468e7d7-8f83-4245-94fc-7303c11612b5": "Decomposing Marksman - (396 216)",
    "S_FTJ_SwampBuildup_B_Undead_Sword_9ee2fb19-5483-42a5-9037-c8147e9695fd": "Decomposing Swashbuckler - (395 210)",
    # Ambush
    "S_FTJ_VoidlingAmbush_000_d61a5845-383b-4759-9fe3-99f519dec4dc": "Viscous Voidling - (461 105)",
    "S_FTJ_VoidlingAmbush_001_eedb56aa-aad1-4de2-8097-3fd7241be1ec": "Viscous Voidling - (443 118)",
    "S_FTJ_VoidlingAmbush_002_a8318c72-e603-4a08-b01d-09232110bccc": "Viscous Voidling - (441 98)",
    "S_FTJ_VoidlingAmbush_003_53680e8b-a4ee-4b00-9419-3860e91e76e6": "Viscous Voidling - (464 109)",
    "S_FTJ_VoidlingAmbush_004_3fe3a69c-97b6-42d5-b1db-bc646a66ab15": "Viscous Voidling - (466 115)",
    "S_FTJ_VoidlingAmbush_005_03ed2bcc-3b3b-4e9c-bfd1-54c7f6a1bcaa": "Viscous Voidling - (451 114)",
    "S_FTJ_VoidlingAmbush_006_0cf5424e-2183-4c52-980e-de156c31f5e4": "Viscous Voidling - (453 92)",
    "S_FTJ_VoidlingAmbush_007_1aa2f181-c36b-4e9e-ae5e-9652fe038824": "Viscous Voidling - (447 95)",
    "S_FTJ_VoidlingAmbush_008_8c83992f-328d-405d-bebd-0f5461d027ad": "Viscous Voidling - (447 120)",
    "S_FTJ_VoidlingAmbush_009_811f904d-4822-463c-b77e-d658a0fb3380": "Viscous Voidling - (454 96)",
    "S_FTJ_VoidlingAmbush_010_7dfba778-1b94-4cf7-8b26-663dfcb760d3": "Viscous Voidling - (460 114)",
    "S_FTJ_VoidlingAmbush_011_a01a4838-c65a-452e-bde5-dc7b8e3dca27": "Viscous Voidling - (440 102)",
    "S_FTJ_VoidlingAmbush_012_360a68c3-e5f1-4834-aa9e-7dc7497d9301": "Viscous Voidling - (464 106)",
    # Boss Battle
    "S_FTJ_SW_VWBoss_Mage_01_5cf41c21-bfed-499e-a6fe-6eda7c24b118": "Decomposing Aeromancer",
    "S_FTJ_SW_VWBoss_Mage_02 2f619e60-5cfc-4323-a094-e285ea922903": "Decomposing Cryomancer",
    "S_FTJ_SW_VWBoss_Melee_01 961c827b-43d1-43c8-8553-6d1d4c8e8aed": "Decomposing Swashbuckler",
    "S_FTJ_SW_VWBoss_Melee_02 8644ff57-7eb3-4ed7-a496-00e977227b53": "Decomposing Swashbuckler",
    "S_FTJ_SW_VWBoss_Ranger_01 e8ad5533-b8f0-4c55-a261-4192f5cf1e48": "Decomposing Marksman",
    "S_FTJ_SW_VWBoss_VoidWoken 112f8c17-ea77-4658-ac72-239154772fb8": "Voidwoken Deep-dweller",
    # Salamanders fight next to illusionist cave
    "S_FTJ_SW_ShelterBackSalamander1 26d2a05f-bd32-408c-adab-c01767271bbf": "Void Salamander",
    "S_FTJ_SW_ShelterBackSalamander2 e3812c55-7530-4d74-b79b-e8f3c91558a4": "Noxious Void Salamander",
    "S_FTJ_SW_ShelterBackSalamander3 62ac9493-260e-40bf-a615-5cdf475208d9": "Void Salamander",
    # Trompdoy
    "S_FTJ_SW_IllusionistAtEntrance e01c3723-872a-454d-a59b-d798b21183cd": "Trompdoy - (676 487)",
    "S_FTJ_SW_IllusionistFinal_1a3b44d4-0ba4-4289-b158-a54111b83e1d": "Trompdoy - (700 497)",
    # Chapel?
    "S_FTJ_ChapelMagister_001_068d4518-9b23-4e2c-a160-8d978d1f78ff": "Magister Ranger - (293 197)",
    "S_FTJ_ChapelMagister_002_090d7104-97f7-4603-a114-47dceaf021e5": "Magister Swordsman - (258 164)",
    "S_FTJ_ChapelMagister_003_b5cb12b2-f347-4415-95ac-8d5ac4fc464b": "Magister Ranger - (302 173)",
    "S_FTJ_ChapelMagister_004_8f330be0-a442-408f-850e-c7fd94e74ada": "Magister Ranger - (262 196)",
    "S_FTJ_ChapelMagister_005_d5ea5e99-2406-4bb9-b2df-5fd975f1b63e": "Magister Swordsman - (260 198)",
    "S_FTJ_ChapelMagister_Captain_c4d751d4-20ff-4281-baf4-8ddeb1383e7e": "Magister Captain Trippel - (279 196)",
    # Temple for rescue
    "S_FTJ_CorneringMagister1_324e8aca-3b0b-430e-b8bb-2f6e9edac3fe": "Magister Inquisitor - (471 254)",
    "S_FTJ_CorneringMagister2_f278b94b-78ac-4cd7-9d8a-1c61e673ead3": "Magister Ranger - (469 253)",
    "S_FTJ_CorneringMagister3_34996c94-6294-45e7-9659-f6fce2a95ea5": "Magister Ranger - (464 254)",
    "S_FTJ_CorneringMagister4_96f35d8a-d38a-4fc1-9b23-bdf4349a16ec": "Magister Swordsman - (462 254)",
    "S_FTJ_OutsideMagister1_51825365-42fd-4b0c-9f35-d21ae40833a3": "Magister Knight - (469 230)",
    "S_FTJ_OutsideMagister2_d3091599-a583-44b8-8ce7-3b7e9d88fdaa": "Magister Ranger - (469 228)",
    "S_FTJ_OutsideMagister3_d584fdbb-1cfa-46d4-add2-5587eafd3e29": "Magister Swordsman - (460 231)",
    "S_FTJ_OutsideMagister4_0a2cf9d4-6631-44c3-aea4-cc5a13f3419b": "Magister Ranger - (460 229)",
    # Witch Battle
    "S_FTJ_SW_Witch_4014aee0-56f1-47e0-a8eb-89c4b5a1da83": "Radeka the Witch - (691 602)",
    "S_FTJ_SW_Witch_Beetle_01_e973d472-f53a-4dee-be60-cd335f3dad7d": "Carrion Beetle - (697 620)",
    "S_FTJ_SW_Witch_Beetle_02_ea698437-fdcc-470f-8f9e-e7640c438690": "Carrion Beetle - (690 597)",
    "S_FTJ_SW_Witch_Beetle_03_a70281cd-a226-434b-b6a6-98ddedd42575": "Carrion Beetle - (679 611)",
    "S_FTJ_SW_Witch_BloodZombie_02_9d512d08-5e51-45ec-b06e-ff90fea7f6de": "Bloody Corpse - (687 611)",
    "S_FTJ_SW_Witch_BloodZombie_03_5549433c-5dec-4701-9733-8fb06009dfff": "Bloody Corpse - (694 614)",
    "S_FTJ_SW_Witch_BloodZombie_04_b714cbca-6c44-4d4d-918c-50269f773584": "Bloody Corpse - (689 600)",
    "S_FTJ_SW_Witch_Zombie_daa5de44-d3b9-47c3-aed5-9969ca29ce61": "Undead Medat - (693 602)",
    # Last Battle
    "S_FTJ_SW_FinalBattleMagister_000_c283e820-0166-4668-8ad4-842085d58de9": "Magister Metamorph - (552 301)",
    "S_FTJ_SW_FinalBattleMagister_001_165f1353-a916-4291-940a-293efbe8f187": "Magister Assassin - (570 299)",
    "S_FTJ_SW_FinalBattleMagister_002_0b7282f6-a131-4441-a113-8f3ea62fa9e3": "Magister Markswoman - (567 309)",
    "S_FTJ_SW_FinalBattleMagister_003_b5dd6af4-6b34-482e-bc0a-72bd6269aaf5": "Magister Knight - (570 304)",
    "S_FTJ_SW_FinalBattleMagister_Gheist_06082187-829f-43e1-b3bb-f3242a70904d": "Gheist - (564 306)",
    "S_FTJ_SW_FinalBattle_Voidwoken_7dcf3cc2-d015-4aff-9949-71fc539fcc73": "Voidwoken Drillworm - (594 408)",
}
Kill_FTJ_id = {f"Killed {Kill_FTJ[location]} at FTJ": number for (number, location) in enumerate(Kill_FTJ, 0xD0)}

location_ids = Quest_Tut_id | Kill_Tut_id | Quest_FTJ_id | Kill_FTJ_id
INTERNAL_TO_DISPLAY = Quest_Tut | Quest_FTJ | Kill_Tut | Kill_FTJ 
ID_LOCATION = {v: k for k, v in location_ids.items()}

def create_locations(world : "DOS2") -> None:
    tutorial = world.get_region("Tutorial")
    fort_joy = world.get_region("Fort Joy")
    if world.options.kill_sanity:
        tutorial.add_locations(Kill_Tut_id, DOS2Location)
        fort_joy.add_locations(Kill_FTJ_id, DOS2Location)
    if world.options.quest_sanity:
        tutorial.add_locations(Quest_Tut_id, DOS2Location)
        fort_joy.add_locations(Quest_FTJ_id, DOS2Location)