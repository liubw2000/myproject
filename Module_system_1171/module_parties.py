from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17, 52.5),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

###############################################################  
  ("zendar", "Zendar", 	icon_town|pf_is_static|pf_always_visible|pf_label_large|pf_hide_defenders, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (16.38,50.17), [], 45.0),

  ("town_1", "Sargoth", 	icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-17.6,79.7), [], 170.0),
  ("town_2", "Tihr", 	icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-53.5,78.4), [], 120.0),
  ("town_3", "Veluca", 	icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-57.4,-44.5), [], 80.0),
  ("town_4", "Suno", 	icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-70.0,15.4), [], 290.0),
  ("town_5", "Jelkala", 	icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-74.6,-79.7), [], 90.0),
  ("town_6", "Praven", 	icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-96.0,26.4), [], 155.0),
  ("town_7", "Uxkhal", 	icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-50.0,-8.5), [], 240.0),

  ("town_8", "Reyvadin", 	icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (48.37,39.48), [], 175.0),
  ("town_9", "Khudan", 	icon_town_snow|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (94.0,65.2), [], 90.0),
  ("town_10", "Tulga", 	icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (135.5,-22.0), [], 310.0),
  ("town_11", "Curaw", 	icon_town_snow|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (42.72,66.89), [], 150.0),
  ("town_12", "Wercheg", 	icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-1.2,108.9), [], 25.0),
  ("town_13", "Rivacheg", 	icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (64.8,113.7), [], 60.0),
  ("town_14", "Halmar", 	icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (55.5,-45.0), [], 135.0),

  ("town_15", "Yalen", 	icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-132.8,-47.3), [], 45.0),
  ("town_16", "Dhirim", 	icon_town|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (14.0,-2.0), [], 0.0),
  ("town_17", "Ichamur", 	icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (121.8,8.6), [], 90.0),
  ("town_18", "Narra", 	icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (88.0,-26.5), [], 135.0),

  ("town_19", "Shariz", 	icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (15.0,-107.0), [], 45.0),
  ("town_20", "Durquba", 	icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (90.0,-95.1), [], 270.0),
  ("town_21", "Ahmerrad", 	icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (130.5,-78.5), [], 330.0),
  ("town_22", "Bariyye", 	icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (165.0,-106.7), [], 225.0),

  ("town_23", "Zendar", 	icon_town_desert|pf_town, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (160.0,-150.0), [], 45.0),

#   Aztaq_Castle       
#  Malabadi_Castle
  ("castle_1", "Culmarr_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-101.3,-21.0), [], 50.0),
  ("castle_2", "Malayurg_Castle", 	icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (97.5,-2.2), [], 75.0),
  ("castle_3", "Bulugha_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (47.5,111.3), [], 100.0),
  ("castle_4", "Radoghir_Castle", 	icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (32.5,47.8), [], 180.0),
  ("castle_5", "Tehlrog_Castle", 	icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-4.8,63.7), [], 90.0),
  ("castle_6", "Tilbaut_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (37.6,17.1), [], 55.0),
  ("castle_7", "Sungetche_Castle", 	icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (109.5,41.5), [], 45.0),
  ("castle_8", "Jeirbe_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (66,96), [], 30.0),
  ("castle_9", "Jamiche_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-7.5,-82.6), [], 100.0),
  ("castle_10", "Alburq_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (24.2,96.85), [], 110.0),
  ("castle_11", "Curin_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-27.5,83.46), [], 75.0),
  ("castle_12", "Chalbek_Castle", 	icon_castle_b|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-84.75,105.5), [], 95.0),
  ("castle_13", "Kelredan_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-10.57,16.97), [], 115.0),
  ("castle_14", "Maras_Castle", 	icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-122.4,-18.1), [], 90.0),
  ("castle_15", "Ergellon_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-52.5,-28.0), [], 235.0),
  ("castle_16", "Almerra_Castle", 	icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-10.6,-65.6), [], 45.0),
  ("castle_17", "Distar_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (140.3,-10.8), [], 15.0),
  ("castle_18", "Ismirala_Castle", 	icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (163.63,70.55), [], 300.0),
  ("castle_19", "Yruma_Castle", 	icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (73.59,47.85), [], 280.0),
  ("castle_20", "Derchios_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (16.0,11.5), [], 260.0),
  ("castle_21", "Ibdeles_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-73.0,-89.5), [], 260.0),
  ("castle_22", "Unuzdaq_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (32.96,-63.89), [], 260.0),
  ("castle_23", "Tevarin_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-124.8,44.3), [], 80.0),
  ("castle_24", "Reindi_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (24.9,-35.6), [], 260.0),
  ("castle_25", "Ryibelet_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-57.0,30.6), [], 260.0),
  ("castle_26", "Senuzgda_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-2.5,-9.5), [], 260.0),
  ("castle_27", "Rindyar_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (63.3,-2.0), [], 260.0),
  ("castle_28", "Grunwalder_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-36.4,-39.3), [], 260.0),

  ("castle_29", "Nelag_Castle", 	icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (147.7,50.4), [], 280.0),
  ("castle_30", "Asugan_Castle", 	icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (176.0,-47.0), [], 260.0),
  ("castle_31", "Vyincourd_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-65.7,-12.5), [], 260.0),
  ("castle_32", "Knudarr_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (2.0,30.1), [], 260.0),
  ("castle_33", "Etrosq_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-101.4,-32.1), [], 80.0),
  ("castle_34", "Hrus_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-72.5,78.6), [], 260.0),
  ("castle_35", "Haringoth_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-110.0,0.0), [], 260.0),
  ("castle_36", "Jelbegi_Castle", 	icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-47.3,53.2), [], 260.0),
  ("castle_37", "Dramug_Castle", 	icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (62.19,23.08), [], 260.0),
  ("castle_38", "Tulbuk_Castle", 	icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (141.7,33.3), [], 260.0),
  ("castle_39", "Slezkh_Castle", 	icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (106.63,93.33), [], 280.0),
  ("castle_40", "Uhhun_Castle", 	icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (62.9,-26.0), [], 260.0),

  ("castle_41", "Jameyyed_Castle", 	icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (71.3,-71.1), [], 260.0),
  ("castle_42", "Teramma_Castle", 	icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (70.0,-96.0), [], 80.0),
  ("castle_43", "Sharwa_Castle", 	icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (172.0,-65.0), [], 260.0),
  ("castle_44", "Durrin_Castle", 	icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (128.0,-87.0), [], 260.0),
  ("castle_45", "Caraf_Castle", 	icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (30.6,-110.6), [], 260.0),
  ("castle_46", "Weyyah_Castle", 	icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (13.3,-84.4), [], 260.0),
  ("castle_47", "Samarra_Castle", 	icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (116.0,-74.0), [], 260.0),
  ("castle_48", "Bardaq_Castle", 	icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (157.0,-80.0), [], 260.0),
 

#     Rinimad      
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
  
  ("village_1", "Yaragar", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-60.0,-9.5), [], 100.0),
  ("village_2", "Burglen", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-13.5,3.5), [], 110.0),
  ("village_3", "Azgad", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-97.4,36.0), [], 120.0),
  ("village_4", "Nomar", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-36.6,-13.2), [], 130.0),
  ("village_5", "Kulum", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-122.7,106.3), [], 170.0),
  ("village_6", "Emirin", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (5.5,-2.5), [], 100.0),
  ("village_7", "Amere", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (39.3,-5.25), [], 110.0),
  ("village_8", "Haen", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-49.7,74.0), [], 120.0),
  ("village_9", "Buvran", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-85.0,-75.35), [], 130.0),
  ("village_10", "Mechin", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (8.8,34.75), [], 170.0),

  ("village_11", "Dusturil", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (137.2,-36.5), [], 100.0),
  ("village_12", "Emer", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-45.8,-58.5), [], 110.0),
  ("village_13", "Nemeja", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-119.0,3.0), [], 120.0),
  ("village_14", "Sumbuja", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (40.0,52.0), [], 130.0),
  ("village_15", "Ryibelet", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-49.3,26.25), [], 170.0),
  ("village_16", "Shapeshte", 	icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (143.01,71.18), [], 170.0),
  ("village_17", "Mazen", 	icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (120.86,98.41), [], 35.0),
  ("village_18", "Ulburban", 	icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (73.7,30.1), [], 170.0),
  ("village_19", "Hanun", 	icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (152.3,53.5), [], 170.0),
  ("village_20", "Uslum", 	icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (116.0,80.3), [], 170.0),

  ("village_21", "Bazeck", 	icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (111.56,106.82), [], 100.0),
  ("village_22", "Shulus", 	icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (125.4,64.0), [], 110.0),
  ("village_23", "Ilvia", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-133.3,-37.6), [], 120.0),
  ("village_24", "Ruldi", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-57.6,-73.0), [], 130.0),
  ("village_25", "Dashbigha", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (125.2,-8.0), [], 170.0),
  ("village_26", "Pagundur", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-58.5,-30.8), [], 170.0),
  ("village_27", "Glunmar", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-146.3,-16.6), [], 170.0),
  ("village_28", "Tash_Kulun", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (95.0,-11.4), [], 170.0),
  ("village_29", "Buillin", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-90.6,110.9), [], 170.0),

  ("village_30", "Ruvar", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (29.2,114.3), [], 170.0),
  ("village_31", "Ambean", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-24.0,53.0), [], 100.0),
  ("village_32", "Tosdhar", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (8.3,14.5), [], 110.0),
  ("village_33", "Ruluns", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-59.0,10.6), [], 120.0),
  ("village_34", "Ehlerdah", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (34.15,-30.0), [], 130.0),
  ("village_35", "Fearichen", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (2.14,86.9), [], 170.0),
  ("village_36", "Jayek", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (17.4,100.7), [], 170.0),
  ("village_37", "Ada_Kulun", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (164.4,26.0), [], 170.0),
  ("village_38", "Ibiran", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-42.8,11.25), [], 170.0),
  ("village_39", "Reveran", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-124.3,-29.5), [], 170.0),
  ("village_40", "Saren", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-12.0,-53.0), [], 170.0),

  ("village_41", "Dugan", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (175.0,-39.5), [], 100.0),
  ("village_42", "Dirigh_Aban", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (115.4,21.6), [], 110.0),
  ("village_43", "Zagush", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (99.4,-21.3), [], 120.0),
  ("village_44", "Peshmi", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (51.8,-50.0), [], 130.0),
  ("village_45", "Bulugur", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (151.5,-3.0), [], 170.0),
  ("village_46", "Fedner", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-82.4,-48.8), [], 170.0),
  ("village_47", "Epeshe", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-101.2,-53.7), [], 170.0),
  ("village_48", "Veidar", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-103.0,15.3), [], 170.0),
  ("village_49", "Tismirr", 	icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (84.81,64.77), [], 10.0),
  ("village_50", "Karindi", 	icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (82.97,51.05), [], 170.0),

  ("village_51", "Jelbegi", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-40.0,62.0), [], 100.0),
  ("village_52", "Amashke", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (38.2,-67.7), [], 110.0),
  ("village_53", "Balanli", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-130.3,42.0), [], 120.0),
  ("village_54", "Chide", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-19.0,15.5), [], 130.0),
  ("village_55", "Tadsamesh", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (37.3,23.7), [], 170.0),
  ("village_56", "Fenada", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-5.55,75.5), [], 170.0),
  ("village_57", "Ushkuru", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (24.75,-7.7), [], 170.0),
  ("village_58", "Vezin", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (78.5,118.3), [], 170.0),
  ("village_59", "Dumar", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-101.0,-45.0), [], 170.0),
  ("village_60", "Tahlberl", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-26.6,30.0), [], 170.0),

  ("village_61", "Aldelen", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-99.8,85.65), [], 100.0),
  ("village_62", "Rebache", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (65,89), [], 100.0),
  ("village_63", "Rduna", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (70.75,1.6), [], 100.0),
  ("village_64", "Serindiar", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-41.5,-35.8), [], 100.0),
  ("village_65", "Iyindah", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-86.3,12.4), [], 100.0),
  ("village_66", "Fisdnar", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (109.0,127.3), [], 100.0),
  ("village_67", "Tebandra", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (69.09,23.02), [], 100.0),
  ("village_68", "Ibdeles", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-72.6,-97.5), [], 100.0),
  ("village_69", "Kwynn", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-26.5,77.6), [], 100.0),
  ("village_70", "Dirigsene", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-94.0,-27.0), [], 100.0),

  ("village_71", "Tshibtin", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-9.0,-20.0), [], 20.0),
  ("village_72", "Elberl", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-144.0,16.15), [], 60.0),
  ("village_73", "Chaeza", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-63.2,-51.4), [], 55.0),
  ("village_74", "Ayyike", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (58.28,38.92), [], 15.0),
  ("village_75", "Bhulaban", 	icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (110.2,48.8), [], 10.0),
  ("village_76", "Kedelke", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (91.5,-34.8), [], 35.0),
  ("village_77", "Rizi", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-64.8,81.5), [], 160.0),
  ("village_78", "Sarimish", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-30.2,-53.3), [], 180.0),
  ("village_79", "Istiniar", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-134.1,-5.5), [], 0.0),
  ("village_80", "Vayejeg", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-1.5,56.0), [], 40.0),

  ("village_81", "Odasan", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-17.2,123.6), [], 20.0),
  ("village_82", "Yalibe", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (12.0,-26.0), [], 60.0),
  ("village_83", "Gisim", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-79.9,55.2), [], 55.0),
  ("village_84", "Chelez", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-45.6,-83.0), [], 15.0),
  ("village_85", "Ismirala", 	icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (155.43,73.68), [], 10.0),
  ("village_86", "Slezkh", 	icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (50.26,66.83), [], 35.0),
  ("village_87", "Udiniad", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (52.3,111.8), [], 160.0),
  ("village_88", "Tulbuk", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (135.8,24.7), [], 180.0),
  ("village_89", "Uhhun", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (70.1,-27.9), [], 0.0),
  ("village_90", "Jamiche", 	icon_village_a|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-12.7,-85.5), [], 40.0),

  ("village_91", "Ayn Assuadi", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (21.6,-95.3), [], 20.0),
  ("village_92", "Dhibbain", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (42.5,-111.6), [], 60.0),
  ("village_93", "Qalyut", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (50.0,-94.8), [], 55.0),
  ("village_94", "Mazigh", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (75.4,-61.65), [], 15.0),
  ("village_95", "Tamnuh", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (99.0,-90.5), [], 10.0),
  ("village_96", "Habba", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (107.0,-75.0), [], 35.0),
  ("village_97", "Sekhtem", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (82.3,-76.8), [], 160.0),
  ("village_98", "Mawiti", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (117.7,-62.2), [], 180.0),
  ("village_99", "Fishara", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (158.35,-98.0), [], 0.0),
  ("village_100", "Iqbayl", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (150.0,-106.5), [], 40.0),

  ("village_101", "Uzgha", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (154.0,-69.5), [], 20.0),
  ("village_102", "Shibal Zumr", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (77.2,-91.0), [], 60.0),
  ("village_103", "Mijayet", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (121.0,-95.6), [], 55.0),
  ("village_104", "Tazjunat", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (159.0,-58.5), [], 15.0),
  ("village_105", "Aab", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (135.0,-88.5), [], 10.0),
  ("village_106", "Hawaha", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (10.3,-91.0), [], 35.0),
  ("village_107", "Unriya", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (156.6,-84.0), [], 160.0),
  ("village_108", "Mit Nun", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (28.8,-107.3), [], 180.0),
  ("village_109", "Tilimsal", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (53.0,-114.5), [], 0.0),
  ("village_110", "Rushdigh", 	icon_village_c|pf_village, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (38.0,-104.0), [], 40.0),

  # ("village_110","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(160, -150),[], 45),
  
  ("salt_mine","Salt_Mine",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]),
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.8, -39.6),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50,-58),[]),
#new site
#banit quest
  ("brotherhood_site","brotherhood_site",icon_castle_c|pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-76, 9),[]),
  ("sea_banit_group_site","sea_banit_group_site",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38, 114),[]),
#knight site
  ("spring_knight_castle", "spring_knight_castle", 	icon_castle_b|pf_is_static|pf_always_visible|pf_label_medium|pf_hide_defenders, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (80.44,5.92), []),
  ("merchant_castle", "merchant_castle", 	icon_castle_b|pf_is_static|pf_always_visible|pf_label_medium|pf_hide_defenders, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-77,46.35), []),
  
#end
  
  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3, -7),[]),

  ("training_ground_1", "Training Field", 	icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (37.4,102.8), [], 100.0),
  ("training_ground_2", "Training Field", 	icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-12.8,33.0), [], 100.0),
  ("training_ground_3", "Training Field", 	icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (69.87,66.62), [], 100.0),
  ("training_ground_4", "Training Field", 	icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (11.5,-75.2), [], 100.0),
  ("training_ground_5", "Training Field", 	icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-125.8,12.5), [], 100.0),


#  bridge_a
  ("Bridge_1", "{!}1", 	icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (39.37,65.1), [], 315.2),
  ("Bridge_2", "{!}2", 	icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (56.44,77.88), [], 4.28),
  ("Bridge_3", "{!}3", 	icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (70.87,87.95), [], 64.5),
  ("Bridge_4", "{!}4", 	icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (93.71,62.13), [], 357.87),
  ("Bridge_5", "{!}5", 	icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (11.02,72.61), [], 21.5),
  ("Bridge_6", "{!}6", 	icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-8.83,52.24), [], 286.5),
  ("Bridge_7", "{!}7", 	icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-29.79,76.84), [], 296.0),
  ("Bridge_8", "{!}8", 	icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-64.05,-6.0), [], 1.72),
  ("Bridge_9", "{!}9", 	icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-64.95,-9.6), [], 326.24),
  ("Bridge_10", "{!}10", 	icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-75.32,-75.27), [], 315.93),
  ("Bridge_11", "{!}11", 	icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-24.39,67.82), [], 81.3),
  ("Bridge_12", "{!}12", 	icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-114.33,-1.94), [], 324.5),
  ("Bridge_13", "{!}13", 	icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-84.02,-7.0), [], 342.3),
  ("Bridge_14", "{!}14", 	icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (-23.36,75.8), [], 66.6),
  ("Bridge_15", "{!}15", 	icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (20.82,-55.09), [], 38.0),
  ("Bridge_16", "{!}16", 	icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral, 0, ai_bhvr_hold, 0, (70.88,-13.08), [], 36.0),

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(26, 77),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(125, 9),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(93, 73),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-35, 18),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-90, -26.8),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(48.5, 110),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-42, 76.7),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(110, -100),[(trp_looter,15,0)]),
 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ]
