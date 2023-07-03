from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",  "{!}culture_1", 0, 0.9, [], []),
  ("culture_2",  "{!}culture_2", 0, 0.9, [], []),
  ("culture_3",  "{!}culture_3", 0, 0.9, [], []),
  ("culture_4",  "{!}culture_4", 0, 0.9, [], []),
  ("culture_5",  "{!}culture_5", 0, 0.9, [], []),
  ("culture_6",  "{!}culture_6", 0, 0.9, [], []),

  ("culture_7",  "{!}culture_7", 0, 0.9, [], []),#Calradic
  ("culture_15",  "{!}culture_15", 0, 0.9, [], []),#Anar
  #some lord will have culture above this at begining
  ("culture_8",  "{!}culture_8", 0, 0.9, [], []),#merchants
  ("culture_9",  "{!}culture_9", 0, 0.9, [], []),#askr
  ("culture_10",  "{!}culture_10", 0, 0.9, [], []),#gulfod_theocracy
  ("culture_11",  "{!}culture_11", 0, 0.9, [], []),#ciambia
  ("culture_12",  "{!}culture_12", 0, 0.9, [], []),#turumia
  ("culture_13",  "{!}culture_13", 0, 0.9, [], []),#destroyer
  ("culture_14",  "{!}culture_14", 0, 0.9, [], []),#wabbaer
  

#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#only add culture there
  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.5),("peasant_rebels", -0.1),("deserters", -0.2),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xFF4433), #changed name so that can tell difference if shows up on map
  ("kingdom_1",  "Kingdom of Swadia", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xEE7744),
  ("kingdom_2",  "Kingdom of Vaegirs",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCCBB99),
  ("kingdom_3",  "Khergit Khanate", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC99FF),
  ("kingdom_4",  "Kingdom of Nords",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x33DDDD),
  ("kingdom_5",  "Kingdom of Rhodoks",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x33DD33),
  ("kingdom_6",  "Sarranid Sultanate",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xDDDD33),
  ("kingdom_7",  "Calradic Empire",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xA020F0),
  ("kingdom_8",  "Anar",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x99FFCC),

##  ("kingdom_1_rebels",  "Swadian rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Vaegir rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_3_rebels",  "Khergit rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Nord rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Rhodok rebels",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),


  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x999966),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
#INVASION MODE START
  ("ccoop_all_stars","All Stars", 0, 0.5,[], []),
#INVASION MODE END
  ("onsved","Onsved",0, 0,[], [],0xCCCCFF),
  ("son_of_starka","Son_of_starka",0, 0,[], [],0xCCCCFF),

  ("wabber","Wabber", 0, 0,[("player_faction",-0.5)], [],0x996600),#first-lower-faction
  ("ortlinde","Ortlinde", 0, 0,[("outlaws",-0.6),("caprine",-0.6),("wabber",-0.6)], [],0x99FFFF),
  ("roskel","Roskel", 0, 0,[], [],0x333333),
  ("ymira","Ymira", 0, 0,[], [],0xFF0099),
  ("caprine","Caprine",0, 0,[("outlaws",-0.6)], [],0x003300),
  ("caprine_prey","Caprine",0, 0,[("caprine",-0.6)], [],0x003300),
  ("spring_knight","spring_knight",0, 0,[("outlaws",-0.6),("caprine",-0.6),("caprine_prey",-0.6),("wabber",-0.6)], [],0x00CC00),
  ("demon_hunter","demon_hunter",0, 0,[("outlaws",-0.6),("caprine",-0.6),("caprine_prey",-0.6),("wabber",-0.6)], [],0xCCFFFF),
  ("dragon_knight","dragon_knight",0, 0,[("outlaws",-0.05),("caprine",-0.6),("caprine_prey",-0.6),("wabber",-0.6)], [],0xCC0000),
  ("witch_finder","witch_finder",0, 0,[], [],0x666666),
  ("necromancer","necromancer",0, 0,[], [],0xFF33FF),
  ("shameless_adventurer","shameless_adventurer",0, 0,[], [],0xCC6600),
  ("adventurer","adventurer",0, 0,[], [],0x336666),
  ("khanjat","khanjat",0, 0,[], [],0xFF99FF),
  ("wizard","wizard",0, 0,[], [],0x3300FF),
  ("mafia1","mafia1",0, 0,[], [],0x6699CC),
  ("mafia2","mafia2",0, 0,[], [],0x00CC99),
  ("mafia3","mafia3",0, 0,[], [],0xCC99CC),
  ("mafia4","mafia4",0, 0,[], [],0x99CCCC),
  ("mafia5","mafia5",0, 0,[], [],0x99CC99),
  ("mafia6","mafia6",0, 0,[], [],0xCC9999),
  #start first prsnt
  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], [],0xFFFFCC),
  ("askr","Askr",0, 0,[("outlaws",-0.6),("player_faction",-0.5),("ortlinde",-0.5)], [],0xCCCCFF),
  ("gulfod_theocracy","acury_theocracy",0, 0,[("outlaws",-0.05),("caprine",-0.05),("caprine_prey",-0.05),("wabber",-0.05)], [],0x330099),
  ("coleta","coleta",0, 0,[], [],0x666699),
  ("ciambia","ciambia",0, 0,[], [],0xFFCCFF),
  ("turumia","turumia",0, 0,[], [],0x990066),
  ("seven_god","seven_god",0, 0,[("outlaws",-0.05),("caprine",-0.05),("caprine_prey",-0.05),("wabber",-0.6)], [],0xCCCCCC),
  ("destroyer","destroyer",0, 0,[], [],0x660066),#above relation same with regular kingdoms
  #end
  ("faction_end","faction_end{!}",0, 0.5,[], []),#for upgrade tree
  ("outlaws_1","Outlaws_1{!}", 0, 0.5,[], []),
  ("others_1","Others_1{!}", 0, 0.5,[], []),
]
