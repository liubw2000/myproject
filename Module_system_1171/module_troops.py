import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Troop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below... 
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n
   
def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
knows_common_multiplayer = knows_trade_10|knows_inventory_management_10|knows_prisoner_management_10|knows_leadership_10|knows_spotting_10|knows_pathfinding_10|knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10
def_attrib = str_7 | agi_5 | int_4 | cha_4
def_attrib_multiplayer = int_30 | cha_30

def_farmer = str_8 | agi_6 | int_5 | cha_5#level 4
def_footman = str_11 | agi_8 | int_6 | cha_6#level 10
def_fighter = str_14 | agi_10 | int_6 | cha_6#level 15
def_swordsman = str_16 | agi_11 | int_7 | cha_7#level 20
def_guard = str_18 | agi_14 | int_7 | cha_7#level 25
def_champion = str_21 | agi_15 | int_8 | cha_8#level 30
def_knight = str_23 | agi_18 | int_8 | cha_8#level 35
def_knight_1 = str_26 | agi_19 | int_9 | cha_9#level 40
def_knight_2 = str_29 | agi_21 | int_9 | cha_9#level 45
def_lord = str_31 | agi_22 | int_10 | cha_10#level 50
def_lord_1 = str_34 | agi_24 | int_10 | cha_10#level 55
def_lord_2 = str_36 | agi_26 | int_11 | cha_11#level 60

knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_25|agi_25|int_25|cha_25|level(40)

knight_attrib_1 = str_18|agi_18|int_8|cha_16|level(25)
knight_attrib_2 = str_20|agi_20|int_10|cha_18|level(30)
knight_attrib_3 = str_23|agi_23|int_12|cha_20|level(35)
knight_attrib_4 = str_25|agi_25|int_13|cha_22|level(40)
knight_attrib_5 = str_30|agi_30|int_15|cha_25|level(45)
knight_skills_1 = knows_riding_6|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_6|knows_power_draw_6|knows_horse_archery_4|knows_athletics_5|knows_tactics_4|knows_prisoner_management_4|knows_leadership_5
knight_skills_2 = knows_riding_7|knows_ironflesh_6|knows_power_strike_6|knows_power_throw_7|knows_power_draw_7|knows_horse_archery_5|knows_athletics_6|knows_tactics_5|knows_prisoner_management_5|knows_leadership_7
knight_skills_3 = knows_riding_8|knows_ironflesh_7|knows_power_strike_7|knows_power_throw_8|knows_power_draw_8|knows_horse_archery_6|knows_athletics_7|knows_tactics_6|knows_prisoner_management_6|knows_leadership_8
knight_skills_4 = knows_riding_9|knows_ironflesh_8|knows_power_strike_8|knows_power_throw_9|knows_power_draw_9|knows_horse_archery_7|knows_athletics_8|knows_tactics_7|knows_prisoner_management_7|knows_leadership_8
knight_skills_5 = knows_riding_10|knows_ironflesh_9|knows_power_strike_9|knows_power_throw_10|knows_power_draw_10|knows_horse_archery_8|knows_athletics_9|knows_tactics_8|knows_prisoner_management_8|knows_leadership_10

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

nord_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

nord_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2
#newface
undead_face1  = 0x0000000180000000000000000000000000000000000000000000000000000000
undead_face2  = 0x0000000180000000000000000000000000000000000000000000000000000000

demonslave_face1  = 0x0000000000000000000000000000000000000000000000000000000000000000
demon_face1  = 0x0000000000000001000000000000000000000000000000000000000000000000
demon_face2  = 0x0000000000000006000000000000000000000000000000000000000000000000

demonlord_face1  = 0x0000000000000007000000000000000000000000000000000000000000000000
demonlord_face2  = 0x0000000000000008000000000000000000000000000000000000000000000000

mide_face_younger_1 = 0x000000000904b003140000000000000000000000001c80400000000000000000
mide_face_young_1   = 0x000000044904b003140000000000000000000000001c80400000000000000000
mide_face_middle_1  = 0x000000084904b003140000000000000000000000001c80400000000000000000
mide_face_old_1     = 0x0000000cc904b003140000000000000000000000001c80400000000000000000
mide_face_older_1   = 0x0000000fc904b003140000000000000000000000001c80400000000000000000

mide_face_younger_2 = 0x000000000904c003140000000000000000000000001c80400000000000000000
mide_face_young_2   = 0x00000003c004c2c76ddcdf7feefbffff00000000001efdbc0000000000000000
mide_face_middle_2  = 0x00000007c004c2c76ddcdf7feefbffff00000000001efdbc0000000000000000
mide_face_old_2     = 0x0000000bc004c2c76ddcdf7feefbffff00000000001efdbc0000000000000000
mide_face_older_2   = 0x0000000fc004c2c76ddcdf7feefbffff00000000001efdbc0000000000000000

west_face_younger_1 = 0x0000000009050003140000000000000000000000001c80400000000000000000
west_face_young_1   = 0x0000000449050003140000000000000000000000001c80400000000000000000
west_face_middle_1  = 0x0000000849050003140000000000000000000000001c80400000000000000000
west_face_old_1     = 0x0000000cc9050003140000000000000000000000001c80400000000000000000
west_face_older_1   = 0x0000000fc9050003140000000000000000000000001c80400000000000000000

west_face_younger_2 = 0x0000000009051003140000000000000000000000001c80400000000000000000
west_face_young_2   = 0x00000003c00512c76ddcdf7feefbffff00000000001efdbc0000000000000000
west_face_middle_2  = 0x00000007c00512c76ddcdf7feefbffff00000000001efdbc0000000000000000
west_face_old_2     = 0x0000000bc00512c76ddcdf7feefbffff00000000001efdbc0000000000000000
west_face_older_2   = 0x0000000fc00512c76ddcdf7feefbffff00000000001efdbc0000000000000000

asia_face_younger_1 = 0x0000000009047003140000000000000000000000001c80400000000000000000
asia_face_young_1   = 0x0000000449047003140000000000000000000000001c80400000000000000000
asia_face_middle_1  = 0x0000000849047003140000000000000000000000001c80400000000000000000
asia_face_old_1     = 0x0000000cc9047003140000000000000000000000001c80400000000000000000
asia_face_older_1   = 0x0000000fc9047003140000000000000000000000001c80400000000000000000

asia_face_younger_2 = 0x0000000009048003140000000000000000000000001c80400000000000000000
asia_face_young_2   = 0x00000003c00482c76ddcdf7feefbffff00000000001efdbc0000000000000000
asia_face_middle_2  = 0x00000007c00482c76ddcdf7feefbffff00000000001efdbc0000000000000000
asia_face_old_2     = 0x0000000bc00482c76ddcdf7feefbffff00000000001efdbc0000000000000000
asia_face_older_2   = 0x0000000fc00482c76ddcdf7feefbffff00000000001efdbc0000000000000000

blac_face_younger_1 = 0x000000000904d003140000000000000000000000001c80400000000000000000
blac_face_young_1   = 0x000000044904d003140000000000000000000000001c80400000000000000000
blac_face_middle_1  = 0x000000084904d003140000000000000000000000001c80400000000000000000
blac_face_old_1     = 0x0000000cc904d003140000000000000000000000001c80400000000000000000
blac_face_older_1   = 0x0000000fc904d003140000000000000000000000001c80400000000000000000

blac_face_younger_2 = 0x000000000904e003140000000000000000000000001c80400000000000000000
blac_face_young_2   = 0x00000003c004e2c76ddcdf7feefbffff00000000001efdbc0000000000000000
blac_face_middle_2  = 0x00000007c004e2c76ddcdf7feefbffff00000000001efdbc0000000000000000
blac_face_old_2     = 0x0000000bc004e2c76ddcdf7feefbffff00000000001efdbc0000000000000000
blac_face_older_2   = 0x0000000fc004e2c76ddcdf7feefbffff00000000001efdbc0000000000000000

beauty_face1    = 0x00000001800000010000000000000e0000000000000000000000000000000000
beauty_face2    = 0x00000001800050100000000000000fbf00000000000000000000000000000000

beauty_face_anar2    = 0x0000000fc00000100000000000000fff00000000000000000000000000000000
#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield


troops = [
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [],
   str_4|agi_4|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_leather_jerkin, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_tribal_warrior_outfit, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_club,itm_leather_jerkin,itm_hide_boots],
   str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
  ["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tutorial_short_bow,itm_tutorial_arrows,itm_linen_tunic,itm_hide_boots],
   str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_sword,itm_leather_vest,itm_hide_boots],
   str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2,mercenary_face_1, mercenary_face_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(110),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(22),wp(140),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4,mercenary_face_1, mercenary_face_2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_7|agi_6|level(7),wp(70),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_7|level(9),wp(80),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_9|agi_8|level(13),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_9|level(15),wp(110),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_11|agi_10|level(19),wp(130),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(21),wp(140),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_12|level(23),wp(150),knows_common,mercenary_face_1, mercenary_face_2],

  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


#soldiers:
#This troop is the troop marked as soldiers_begin
  ["farmer","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_farmer|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_club,itm_quarter_staff,itm_dagger,itm_stones,itm_leather_cap,itm_linen_tunic,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots],
   def_farmer|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["watchman","Watchman","Watchmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bolts,itm_spiked_club,itm_fighting_pick,itm_sword_medieval_a,itm_boar_spear,itm_hunting_crossbow,itm_light_crossbow,itm_tab_shield_round_a,itm_tab_shield_round_b,itm_padded_cloth,itm_leather_jerkin,itm_leather_cap,itm_padded_coif,itm_footman_helmet,itm_nomad_boots,itm_wrapping_boots],
   str_11 | agi_8 | int_5 | cha_5|level(9),wp(75),knows_common|knows_shield_1,mercenary_face_1, mercenary_face_2],
  ["caravan_guard","Caravan Guard","Caravan Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,no_scene,0,fac_commoners,
   [itm_spear,itm_fighting_pick,itm_sword_medieval_a,itm_voulge,itm_tab_shield_round_b,itm_tab_shield_round_c,itm_leather_jerkin,itm_leather_vest,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet,itm_saddle_horse],
   def_fighter|level(14),wp(85),knows_common|knows_riding_2|knows_ironflesh_1|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_swordsman","Mercenary Swordsman","Mercenary Swordsmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_tab_shield_heater_c,itm_mercenary_catapharact_armor,itm_leather_boots,itm_mail_chausses,itm_kettle_hat,itm_flat_topped_helmet, itm_helmet_with_neckguard],
   def_swordsman|level(20),wp(100),knows_common|knows_riding_3|knows_ironflesh_3|knows_shield_3|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  ["hired_blade","Hired Blade","Hired Blades",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bastard_sword_b,itm_sword_medieval_c,itm_tab_shield_pavise_c,itm_tab_shield_heater_cav_a,itm_swadian_ceremonial_plate_red,itm_mail_chausses,itm_brig_plate_red,itm_iron_greaves,itm_plate_boots,itm_guard_helmet,itm_great_helmet,itm_bascinet, itm_leather_gloves],
   def_guard|level(25),wp(130),knows_common|knows_riding_3|knows_athletics_5|knows_shield_5|knows_power_strike_5|knows_ironflesh_5,mercenary_face_1, mercenary_face_2],
  ["mercenary_crossbowman","Mercenary Crossbowman","Mercenary Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_bolts,itm_spiked_club,itm_fighting_pick,itm_sword_medieval_a,itm_boar_spear,itm_crossbow,itm_light_crossbow,itm_tab_shield_pavise_a,itm_tab_shield_round_b,itm_padded_cloth,itm_leather_jerkin,itm_leather_cap,itm_padded_coif,itm_footman_helmet,itm_nomad_boots,itm_wrapping_boots],
   def_fighter|level(15),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (80) | wp_crossbow (90) | wp_throwing (90),knows_common|knows_athletics_5|knows_shield_1,mercenary_face_1, mercenary_face_2],
  ["mercenary_crossbowman_1","Mercenary Crossbowman","Mercenary Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
   [itm_crossbow,itm_tab_shield_pavise_a,itm_tab_shield_heater_a,itm_pike,itm_long_spiked_club,itm_sword_viking_2,itm_bascinet,itm_bolts,itm_tribal_warrior_outfit,itm_padded_leather,itm_nomad_boots,itm_bolts,itm_leather_jerkin,itm_footman_helmet,itm_nomad_boots],
   def_swordsman|level(20),wp_one_handed (100) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (105) | wp_throwing (90),knows_common|knows_athletics_5|knows_shield_1,mercenary_face_1, mercenary_face_2],
  ["mercenary_crossbowman_2","Mercenary Crossbowman","Mercenary Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,no_scene,reserved,fac_commoners,
   [itm_crossbow,itm_heavy_crossbow,itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_steel_bolts,itm_bolts,itm_leather_gloves,itm_leather_boots,itm_mail_with_tunic_red,itm_mercenary_catapharact_armor_variant,itm_footman_helmet,itm_kettle_hat,itm_spiked_helmet],
   def_guard|level(25),wp_one_handed (100) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (130) | wp_throwing (90),knows_power_draw_2|knows_ironflesh_2|knows_power_strike_1|knows_athletics_5|knows_shield_1,mercenary_face_1, mercenary_face_2],
  ["mercenary_horseman","Mercenary Horseman","Mercenary Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_lance,itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_mail_shirt,itm_light_mail_and_plate_banner,itm_leather_boots,itm_norman_helmet,itm_helmet_with_neckguard,itm_saddle_horse,itm_courser],
   def_swordsman|level(20),wp(100),knows_common|knows_riding_4|knows_ironflesh_3|knows_shield_2|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_cavalry","Mercenary Cavalry","Mercenary Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_heavy_lance,itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_swadian_ceremonial_plate_black,itm_banded_armor,itm_bascinet_2,itm_splinted_leather_greaves,itm_flat_topped_helmet,itm_warhorse],
   def_guard|level(25),wp(130),knows_common|knows_riding_5|knows_ironflesh_4|knows_shield_5|knows_power_strike_4,mercenary_face_1, mercenary_face_2],
  
  ["mercenary_noleman","Mercenary Cavalry","Mercenary Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_fighting_axe,itm_war_darts,itm_mace_3,itm_sword_medieval_c,itm_sword_medieval_b_small,itm_shortened_voulge,itm_bastard_sword_a,
   itm_leather_gloves,itm_mail_coif,itm_bascinet,itm_leather_boots,itm_white_gambeson_a,itm_rus_cav_boots,itm_courser],
   str_15 | agi_11 | int_6 | cha_6|level(17),wp(130),knows_riding_3|knows_ironflesh_3|knows_shield_3|knows_power_strike_3|knows_power_throw_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_squire","Mercenary Cavalry","Mercenary Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_two_handed_cleaver,itm_javelin,itm_tab_shield_small_round_b,itm_mace_4,itm_bastard_sword_b,itm_sarranid_axe_a,itm_double_sided_lance,
   itm_bascinet_3,itm_mail_chausses,itm_cuirass_on_black,itm_bascinet_coif_01,itm_rus_splint_greaves,itm_warhorse_red2],
   def_guard|level(24),wp(160),knows_riding_5|knows_ironflesh_4|knows_shield_5|knows_power_strike_4|knows_power_throw_4,mercenary_face_1, mercenary_face_2],
  ["mercenary_knight","Mercenary Cavalry","Mercenary Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [itm_throwing_spears,itm_tab_shield_small_round_c,itm_sword_medieval_c_long,itm_sword_viking_3,itm_warhammer,itm_great_lance,
   itm_iron_greaves,itm_lamellar_gauntlets,itm_heraldic_platemail_01,itm_ak_poleaxe,itm_armet_01,itm_wlong17],
    str_22 | agi_17 | int_8 | cha_8|level(33),wp(180),knows_riding_6|knows_ironflesh_6|knows_shield_6|knows_power_strike_6|knows_power_throw_6,mercenary_face_1, mercenary_face_2],
  
  ["female_noleman","Female Noleman","Female Noleman",tf_beautiful|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_sword_two_handed_b,itm_tab_shield_round_c,itm_sword_medieval_b,itm_sword_medieval_c,itm_sword_medieval_b_small,itm_bastard_sword_a,itm_pickaxe,itm_hunting_crossbow,itm_bolts,
   itm_leather_gloves,itm_mail_coif,itm_new_leather_boots,itm_flat_topped_helmet,itm_arena_armor_banner,itm_rus_cav_boots],
   def_fighter|level(15),wp(120),knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_2,beauty_face1, beauty_face2],
  ["female_noleman_archer","female_noleman_archer","female_noleman_archer",tf_beautiful|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_light_crossbow,itm_bolts,itm_tab_shield_round_c,itm_tab_shield_round_d,itm_sword_medieval_c,itm_sword_medieval_c_small,itm_crossbow,itm_steel_bolts,
   itm_leather_gloves,itm_mail_coif,itm_footman_helmet,itm_helmet_with_neckguard,itm_leather_boots,itm_flat_topped_helmet,itm_tribal_warrior_outfit,itm_splinted_leather_greaves],
   def_guard|level(25),wp(150),knows_ironflesh_4|knows_shield_4|knows_power_strike_3|knows_athletics_3,beauty_face1, beauty_face2],
  ["female_noleman_archer_e","female_noleman_archer","female_noleman_archer",tf_beautiful|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tab_shield_round_d,itm_sword_medieval_c_long,itm_bastard_sword_b,itm_heavy_crossbow,itm_steel_bolts,itm_sniper_crossbow,
   itm_leather_gloves,itm_kettle_hat,itm_bascinet,itm_surcoat_over_mail,itm_splinted_leather_greaves,itm_mail_long_surcoat_new_b3],
   def_champion|level(30),wp(180),knows_ironflesh_5|knows_shield_5|knows_power_strike_5|knows_athletics_5,beauty_face1, beauty_face2],
  ["female_noleman_archer_f","female_noleman_archer","female_noleman_archer",tf_beautiful|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tab_shield_round_d,itm_sword_medieval_d_long,itm_bastard_sword_b,itm_steel_bolts,itm_spak_crsb02,itm_despair,
   itm_churburg_13_brass,itm_lamellar_gauntlets,itm_mail_boots,itm_barbutte_01,itm_barbutte_coif_01],
   def_champion|level(35),wp(230),knows_ironflesh_6|knows_shield_6|knows_power_strike_7|knows_athletics_7,beauty_face1, beauty_face2],

  ["female_noleman_sword","female_noleman_sword","female_noleman_sword",tf_beautiful|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_sword_two_handed_b,itm_sword_two_handed_a,itm_sword_medieval_c_long,itm_bastard_sword_a,itm_sword_medieval_d_long,itm_tab_shield_round_d,
   itm_mail_mittens,itm_kettle_hat,itm_splinted_leather_greaves,itm_surcoat_over_mail_banner,itm_lamellar_vest,itm_leather_boots],
   def_guard|level(25),wp(160),knows_ironflesh_5|knows_shield_6|knows_power_strike_5|knows_athletics_3,beauty_face1, beauty_face2],
  ["female_noleman_sword_e","female_noleman_sword","female_noleman_sword",tf_mounted|tf_beautiful|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse,no_scene,reserved,fac_commoners,
   [itm_two_handed_cleaver,itm_military_sickle_a,itm_sword_two_handed_a,itm_bastard_sword_b,itm_sword_medieval_d_long,itm_steel_shield,itm_wlong3,
   itm_scale_gauntlets,itm_bascinet_2,itm_guard_helmet,itm_splinted_leather_greaves,itm_ak_banded_armor_a,itm_ak_brigandine_a,itm_splinted_greaves],
   def_champion|level(30),wp(200),knows_ironflesh_6|knows_shield_7|knows_power_strike_6|knows_athletics_6|knows_riding_5,beauty_face1, beauty_face2],
  ["female_noleman_knight","female_noleman_knight","female_noleman_knight",tf_mounted|tf_beautiful|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse,no_scene,reserved,fac_commoners,
   [itm_sword_of_war,itm_bastard_sword_b,itm_sword_medieval_d_long,itm_steel_shield_kite,itm_sp_2hsw,itm_ak_miecz_b,itm_lance_1,itm_lance_4,itm_jousting_lance,itm_charger_black,itm_charger,
   itm_armet_04,itm_hounskull_bascinet_06,itm_churburg_13_mail,itm_early_transitional_blue,itm_wisby_gauntlets_red,itm_wisby_gauntlets_black,itm_iron_greaves,itm_steel_boots_01,itm_jack_glamdring],
   def_knight|level(35),wp(240),knows_ironflesh_7|knows_shield_8|knows_power_strike_7|knows_athletics_7|knows_riding_7,beauty_face1, beauty_face2],

  ["mercenary_samurai","Mercenary Cavalry","Mercenary Cavalry",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [itm_strange_sword,itm_strange_great_sword,itm_strange_short_sword,itm_strange_helmet,itm_strange_boots,itm_strange_armor,itm_throwing_daggers],
   def_champion|level(30),wp(180),knows_ironflesh_6|knows_power_strike_6|knows_power_throw_6|knows_athletics_6,asia_face_younger_1, asia_face_old_1],
  
  ["mercenary_spearman","Mercenary Spearman","Mercenary Spearman",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_tab_shield_pavise_d,itm_ashwood_pike,itm_lance,itm_war_darts,itm_darts,itm_ak_banded_armor_a,itm_rus_cav_boots,itm_blackscale_gauntlets_b,itm_west_guardsman_helm],
   def_champion|level(30),wp(175),knows_ironflesh_6|knows_power_strike_6|knows_power_throw_6|knows_athletics_6,mercenary_face_1, mercenary_face_2],

  ["mercenary_shooter","Mercenary Shooter","Mercenary Shooter",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_tab_shield_round_d,itm_bastard_sword_a,itm_leather_boots,itm_leather_gloves,itm_cartridges,itm_combed_morion,itm_combed_morion_blued,itm_chapel_de_fer,itm_cuirass_on_black,itm_cuirass_on_white,itm_flintlock_pistol,itm_flintlock_rifle],
   def_champion|level(30),wp(155),knows_ironflesh_6|knows_power_strike_6|knows_power_throw_6|knows_athletics_6,mercenary_face_1, mercenary_face_2],

  ["lost_knight","Mercenary Cavalry","Mercenary Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [itm_mackie_morning_star,itm_mackie_strange_sword,itm_tab_shield_kite_cav_a,itm_javelin,itm_lance,itm_bastard_sword_b,itm_one_handed_war_axe_b,itm_battle_axe,itm_warhorse_holy,
   itm_bascinet_3,itm_steel_gauntlets,itm_steel_boots_01,itm_corrazina_green,itm_scale_shirt,itm_rus_helm,itm_rus_splint_greaves],
   def_knight|level(35),wp(200),knows_riding_7|knows_ironflesh_7|knows_shield_7|knows_power_strike_7|knows_power_throw_7,mercenary_face_1, mercenary_face_2],
  
  ["mercenary_fighter","Mercenary Cavalry","Mercenary Cavalry",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [itm_tourney_helm_blue,itm_arena_armor_blue,itm_iron_staff,itm_leather_gloves,itm_ankle_boots],
   def_guard|level(25),wp(180),knows_ironflesh_6|knows_power_strike_6|knows_power_throw_6|knows_athletics_6,mercenary_face_1, mercenary_face_2],
  ["mercenary_horsearcher","Mercenary horsearcher","Mercenary horsearcher",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_steppe_horse,itm_khergit_arrows,itm_arrows,itm_nomad_boots,itm_khergit_bow,itm_lamellar_vest_khergit,itm_khergit_war_helmet,itm_khergit_cavalry_helmet,itm_light_lance,itm_scimitar,itm_tab_shield_small_round_b],
   def_guard|level(25),wp(140),knows_ironflesh_4|knows_power_strike_4|knows_power_draw_5|knows_horse_archery_5|knows_riding_5,khergit_face_younger_1, khergit_face_older_2],

  ["mercenary_assassin","Mercenary Assassin","Mercenary assassin",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,no_scene,reserved,fac_commoners,
   [itm_blackleather_gloves,itm_blackleather_boots_a,itm_assassin_armor,itm_assassin_helmet,itm_assassin_helmet2,itm_luc_celtic_sword,itm_steel_shield,itm_ganquang_dart,itm_ganquang_dart],
   str_18 | agi_16 | int_7 | cha_7|level(28),wp(200),knows_ironflesh_5|knows_power_strike_7|knows_power_throw_6|knows_athletics_8|knows_shield_5,mercenary_face_1, mercenary_face_2],

  ["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(40),knows_common,refugee_face1,refugee_face2],
  ["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_woolen_dress, itm_skullcap, itm_wrapping_boots],
   def_farmer|level(5),wp(70),knows_common,refugee_face1,refugee_face2],
  ["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_leather_jerkin, itm_skullcap, itm_wrapping_boots],
   def_footman|level(10),wp(85),knows_common|knows_power_strike_1,refugee_face1,refugee_face2],
  ["fighter_woman","Camp Defender","Camp Defenders",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_fur_covered_shield,itm_hide_covered_round_shield,itm_hatchet,itm_voulge,itm_mail_shirt,itm_byrnie, itm_skullcap, itm_wrapping_boots],
   def_fighter|level(16),wp(100),knows_common|knows_riding_3|knows_power_strike_2|knows_athletics_2|knows_ironflesh_1,refugee_face1,refugee_face2],
  ["woman_crossbow","Sword Sister","Sword Sisters",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_bolts,itm_sword_medieval_b,itm_sword_khergit_2,itm_plate_covered_round_shield,itm_crossbow,itm_brigandine_heraldic,itm_leather_boots,itm_helmet_with_neckguard,itm_leather_gloves],
   str_17 | agi_12 | int_7 | cha_7|level(22),wp(140),knows_common|knows_power_strike_3|knows_riding_5|knows_athletics_3|knows_ironflesh_2|knows_shield_2,refugee_face1,refugee_face2],
  ["woman_crossbow_elite","Sword Sister","Sword Sisters",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_bolts,itm_steel_bolts,itm_steel_bolts,itm_sword_two_handed_b,itm_heavy_crossbow,itm_scale_armor,itm_splinted_leather_greaves,itm_guard_helmet,itm_leather_gloves],
   str_20 | agi_15 | int_7 | cha_7|level(28),wp(180),knows_common|knows_power_strike_4|knows_riding_5|knows_athletics_3|knows_ironflesh_4|knows_shield_2,refugee_face1,refugee_face2],
  
  ["sword_sister","Sword Sister","Sword Sisters",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_sword_medieval_b,itm_sword_khergit_3,itm_plate_covered_round_shield,itm_mail_long_surcoat_new_b3,itm_guard_helmet,itm_splinted_greaves,itm_helmet_with_neckguard,itm_leather_gloves],
   str_17 | agi_12 | int_7 | cha_7|level(22),wp(140),knows_common|knows_power_strike_3|knows_riding_5|knows_athletics_3|knows_ironflesh_2|knows_shield_2,refugee_face1,refugee_face2],
  ["war_sister","Sword Sister","Sword Sisters",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_sword_medieval_c_long,itm_steel_shield,itm_brig_plate_blue,itm_guard_helmet,itm_iron_greaves,itm_scale_gauntlets],
   str_20 | agi_14 | int_7 | cha_7|level(27),wp(165),knows_common|knows_power_strike_4|knows_riding_5|knows_athletics_4|knows_ironflesh_4|knows_shield_2,refugee_face1,refugee_face2],
  ["war_sister_elite","Sword Sister","Sword Sisters",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_sword_medieval_d_long,itm_sword_two_handed_a,itm_steel_shield,itm_plate_harness_02,itm_hounskull_bascinet_07,itm_steel_gauntlets,itm_steel_boots_01],
   def_knight|level(35),wp(215),knows_common|knows_power_strike_5|knows_riding_5|knows_athletics_6|knows_ironflesh_7|knows_shield_4,refugee_face1,refugee_face2],
  ["war_sister_horse","Sword Sister","Sword Sisters",tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_sword_medieval_d_long,itm_great_lance,itm_sword_two_handed_a,itm_steel_shield,itm_coat_of_plates,itm_winged_great_helmet,itm_steel_gauntlets,itm_iron_greaves,itm_warhorse_blu2,itm_wplated5],
   str_23 | agi_16 | int_8 | cha_8|level(33),wp(200),knows_common|knows_power_strike_5|knows_riding_5|knows_athletics_5|knows_ironflesh_6|knows_shield_4,refugee_face1,refugee_face2],
  ["war_sister_knight","Sword Sister","Sword Sisters",tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_sp_2hsw,itm_mackie_bastard,itm_flamberg,itm_lance_6,itm_steel_shield_kite,itm_copy_plate_harness_02,itm_hounskull_bascinet_07,itm_steel_gauntlets,itm_iron_greaves,itm_platedw],
   str_27 | agi_20 | int_9 | cha_9|level(42),wp(245),knows_common|knows_power_strike_8|knows_riding_7|knows_athletics_8|knows_ironflesh_8|knows_shield_6,refugee_face1,refugee_face2],

  ["mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners,
   [],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],

#peasant - retainer - footman - man-at-arms -  knight
  ["swadian_recruit","Swadian Recruit","Swadian Recruits",tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_leather_cap,itm_felt_hat,itm_felt_hat,
    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots],
   def_farmer|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
  ["swadian_militia","Swadian Militia","Swadian Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_bolts,itm_spiked_club,itm_fighting_pick,itm_boar_spear,itm_hunting_crossbow,itm_tab_shield_heater_a,
    itm_padded_cloth,itm_red_gambeson,itm_arming_cap,itm_arming_cap,itm_ankle_boots,itm_wrapping_boots],
   def_footman|level(9),wp(75),knows_common,swadian_face_young_1, swadian_face_old_2],
  ["swadian_footman","Swadian Footman","Swadian Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_spear,itm_fighting_pick,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_tab_shield_heater_b,
    itm_mail_with_tunic_red,itm_ankle_boots,itm_mail_coif,itm_norman_helmet],
   def_fighter|level(14),wp_melee(85),knows_common|knows_ironflesh_2|knows_shield_2|knows_athletics_2|knows_power_strike_2,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry","Swadian Infantry","Swadian Infantry",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_pike,itm_fighting_pick,itm_bastard_sword_a,itm_sword_medieval_a,itm_sword_medieval_b_small,itm_tab_shield_heater_c,
    itm_mail_with_surcoat,itm_haubergeon,itm_mail_chausses,itm_leather_boots,itm_segmented_helmet,itm_flat_topped_helmet,itm_helmet_with_neckguard],
   def_swordsman|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_2|knows_shield_3|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_sergeant","Swadian Sergeant","Swadian Sergeants",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_awlpike,itm_bastard_sword_b,itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_d,
    itm_coat_of_plates,itm_brigandine_red,itm_mail_boots,itm_iron_greaves,itm_flat_topped_helmet,itm_guard_helmet,itm_mail_mittens,itm_gauntlets],
   def_guard|level(25),wp_melee(135),knows_common|knows_shield_4|knows_ironflesh_4|knows_power_strike_4|knows_athletics_4,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_skirmisher","Swadian Skirmisher","Swadian Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_club,itm_voulge,itm_tab_shield_heater_a,
    itm_red_gambeson,itm_padded_cloth,itm_ankle_boots,itm_arming_cap,itm_arming_cap],
   def_fighter|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1|knows_power_strike_1,swadian_face_young_1, swadian_face_middle_2],
  ["swadian_crossbowman","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_light_crossbow,itm_fighting_pick,itm_sword_medieval_a,itm_voulge,itm_tab_shield_heater_b,
    itm_leather_jerkin,itm_red_gambeson,itm_leather_boots,itm_ankle_boots,itm_norman_helmet,itm_segmented_helmet],
   def_swordsman|level(19),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (100) | wp_throwing (90),knows_common|knows_riding_2|knows_ironflesh_2|knows_power_strike_2|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_sharpshooter","Swadian Sharpshooter","Swadian Sharpshooters",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_bolts,itm_arrows,itm_crossbow,itm_heavy_crossbow,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_voulge,itm_tab_shield_heater_c,
    itm_haubergeon,itm_leather_boots,itm_mail_chausses,itm_kettle_hat,itm_helmet_with_neckguard,itm_leather_gloves],
   str_17 | agi_14 | int_7 | cha_7|level(24),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (120) | wp_throwing (100),knows_common|knows_power_draw_3|knows_ironflesh_3|knows_power_strike_3|knows_athletics_2,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_man_at_arms","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_lance,itm_fighting_pick,itm_bastard_sword_b,itm_sword_medieval_b,itm_sword_medieval_c_small,itm_tab_shield_heater_cav_a,
    itm_mail_with_surcoat,itm_mail_chausses,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_hunter],
   def_swordsman|level(21),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_knight","Swadian Knight","Swadian Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_heavy_lance,itm_sword_two_handed_b,itm_sword_medieval_d_long,itm_morningstar,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,
    itm_cuir_bouilli,itm_plate_boots,itm_guard_helmet,itm_warhorse,itm_gauntlets,itm_mail_mittens],
   str_20 | agi_15 | int_7 | cha_7|level(28),wp_one_handed (150) | wp_two_handed (130) | wp_polearm (130) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),knows_common|knows_riding_5|knows_shield_5|knows_ironflesh_5|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],
  
  ["swadian_nobleman","Swadian Knight","Swadian Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_double_sided_lance,itm_sword_medieval_c,itm_kettle_hat,itm_flat_topped_helmet,itm_leather_boots,itm_courser,itm_leather_gloves,itm_nobleman_armor_swadian,itm_tab_shield_heater_b],
   def_swordsman|level(19),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (75) | wp_crossbow (75) | wp_throwing (75),knows_athletics_2|knows_riding_4|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_squire","Swadian Knight","Swadian Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_tab_shield_heater_cav_a,itm_tab_shield_heater_d,itm_warhorse_red2,itm_mail_long_surcoat_new3,itm_heavy_lance,itm_sword_medieval_d_long,itm_spiked_mace,itm_spiked_helmet,itm_brigandine_red,itm_splinted_greaves,itm_mail_mittens],
   str_20 | agi_14 | int_7 | cha_7|level(27),wp_one_handed (140) | wp_two_handed (140) | wp_polearm (140) | wp_archery (95) | wp_crossbow (95) | wp_throwing (95),knows_athletics_4|knows_riding_5|knows_shield_4|knows_ironflesh_4|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_knight_n","Swadian Knight","Swadian Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_ganquang_morningstar,itm_morningstar,itm_sword_two_handed_b,itm_charger,itm_coat_of_plates_red_cloak,itm_gauntlets,itm_plate_boots,itm_great_helmet,itm_ak_swad_lance,itm_shb1],
   def_knight|level(35),wp_one_handed (220) | wp_two_handed (220) | wp_polearm (220) | wp_archery (95) | wp_crossbow (95) | wp_throwing (95),knows_athletics_6|knows_riding_7|knows_shield_6|knows_ironflesh_7|knows_power_strike_8,swadian_face_middle_1, swadian_face_older_2],
  #personal troop
  ["swadian_royalty_knight","Swadian Knight","Swadian Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_charger3_new,itm_flamberg,itm_mackie_bastard,itm_ganquang_morningstar,itm_gauntlets,itm_plate_boots,itm_2full_plate_armor,itm_winged_great_helmet,itm_ak_swad_lance,itm_shb1],
   str_28 | agi_19 | int_9 | cha_9|level(42),wp(275),knows_athletics_8|knows_riding_9|knows_shield_9|knows_ironflesh_8|knows_power_strike_9,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_steel_knight","Swadian Knight","Swadian Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_shb2,itm_flamberg,itm_charger_steel,itm_wisby_gauntlets_black,itm_coat_of_plates_steel,itm_maciejowski_helmet_new_b2,itm_mackie_bastard,itm_plate_boots],
   str_25 | agi_19 | int_8 | cha_8|level(38),wp(220),knows_athletics_8|knows_riding_8|knows_shield_7|knows_ironflesh_7|knows_power_strike_7,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_horse_archer","Swadian horse archer","Swadian horse archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_lance,itm_fighting_pick,itm_bastard_sword_b,itm_sword_medieval_c_small,itm_barbed_arrows,itm_bodkin_arrows,itm_arrows,itm_long_bow,
    itm_brigandine_red,itm_hunter,itm_bascinet_3,itm_bascinet_2,itm_splinted_leather_greaves,itm_leather_gloves],
   def_guard|level(25),wp(160),knows_riding_5|knows_ironflesh_2|knows_shield_2|knows_power_strike_3|knows_power_draw_4|knows_horse_archery_4,swadian_face_young_1, swadian_face_old_2],
  ["swadian_sword_master","swadian_sword_master","swadian_sword_master",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_flamberg,itm_swadian_ceremonial_plate_black,itm_plate_boots,itm_col1_gotlandbucket,itm_steel_mittens,itm_sword_of_war,itm_mackie_bastard],
   def_knight|level(35),wp(240),knows_athletics_7|knows_ironflesh_7|knows_power_strike_7,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_steel_guard","swadian_steel_guard","swadian_steel_guard",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_shb2,itm_french_helm,itm_french_helm_closed,itm_swadian_lordly_plate_armor,itm_plate_boots,itm_gauntlets,itm_morningstar,itm_military_hammer,itm_heavy_crossbow,itm_steel_bolts],
   def_knight|level(35),wp(215),knows_athletics_7|knows_ironflesh_7|knows_power_strike_7,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_patrol_leader","Swadian Knight","Swadian Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
   [itm_morningstar,itm_sword_two_handed_b,itm_charger,itm_coat_of_plates_red_cloak,itm_gauntlets,itm_plate_boots,itm_great_helmet,itm_ak_swad_lance],
   def_champion|level(30),wp(180),knows_athletics_5|knows_riding_6|knows_shield_6|knows_ironflesh_5|knows_power_strike_6,swadian_face_middle_1, swadian_face_older_2],
  ["swadian_flag_holder","swadian_flag_holder","swadian_flag_holder",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_coat_of_plates_red,itm_gauntlets,itm_plate_boots,itm_great_helmet,itm_battle_flag_swa],
   def_guard|level(25),wp(150),knows_athletics_5|knows_ironflesh_5|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],

  ["swadian_messenger","Swadian Messenger","Swadian Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_young_1, swadian_face_old_2],
  ["swadian_deserter","Swadian Deserter","Swadian Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_coat_of_plates,itm_plate_armor,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_tab_shield_heater_d,itm_coat_of_plates,itm_plate_armor,itm_plate_boots,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

# Vaegir watchman?
  ["vaegir_recruit","Vaegir Recruit","Vaegir Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_scythe,itm_hatchet,itm_cudgel,itm_axe,itm_stones,itm_tab_shield_kite_a, itm_tab_shield_kite_a,
    itm_linen_tunic, itm_rawhide_coat,itm_nomad_boots],
   def_farmer|level(4),wp(60),knows_common, vaegir_face_younger_1, vaegir_face_middle_2],
  ["vaegir_footman","Vaegir Footman","Vaegir Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spiked_club,itm_hand_axe,itm_sword_viking_1,itm_two_handed_axe,itm_tab_shield_kite_a,itm_tab_shield_kite_b,itm_spear,itm_nomad_cap,itm_vaegir_fur_cap,itm_rawhide_coat,itm_nomad_armor,itm_nomad_boots],
   def_footman|level(9),wp(75),knows_common, vaegir_face_young_1, vaegir_face_middle_2],
  ["vaegir_skirmisher","Vaegir Skirmisher","Vaegir Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   str_13 | agi_10 | int_6 | cha_6|level(14),wp(60),knows_ironflesh_2|knows_power_strike_1|knows_power_draw_1|knows_power_throw_1,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_archer","Vaegir Archer","Vaegir Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_arrows,itm_axe,itm_sword_khergit_1,itm_nomad_bow,itm_nomad_bow,itm_short_bow,
    itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],
   def_swordsman|level(19),wp_one_handed (70) | wp_two_handed (70) | wp_polearm (70) | wp_archery (110) | wp_crossbow (70) | wp_throwing (70),knows_ironflesh_3|knows_power_strike_2|knows_power_draw_3|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_marksman","Vaegir Marksman","Vaegir Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_axe,itm_voulge,itm_sword_khergit_2,itm_war_bow,itm_strong_bow,
    itm_studded_leather_coat,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
   def_guard|level(24),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (140) | wp_crossbow (80) | wp_throwing (80),knows_ironflesh_3|knows_power_strike_3|knows_power_draw_5|knows_athletics_3|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_veteran","Vaegir Veteran","Vaegir Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spiked_mace,itm_two_handed_axe,itm_sword_viking_1,itm_tab_shield_kite_b,itm_tab_shield_kite_c,itm_spear,
    itm_steppe_cap,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_leather_jerkin,itm_studded_leather_coat,itm_nomad_boots,itm_saddle_horse],
   def_fighter|level(14),wp_melee(85),knows_athletics_2|knows_ironflesh_1|knows_power_strike_2|knows_shield_2,vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_infantry","Vaegir Infantry","Vaegir Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_pike,itm_battle_axe,itm_sword_viking_2,itm_sword_khergit_2,itm_tab_shield_kite_c,itm_spear,
    itm_mail_hauberk,itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
   def_swordsman|level(19),wp_melee(100),knows_athletics_3|knows_ironflesh_2|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_guard","Vaegir Guard","Vaegir Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_ashwood_pike,itm_fighting_axe,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_d,
    itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_leather_gloves],
   def_guard|level(24),wp_melee(130),knows_riding_2|knows_athletics_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_horseman","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_sword_khergit_2,itm_lance,itm_tab_shield_kite_cav_a,itm_spear,
    itm_lamellar_vest,itm_leather_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_steppe_horse,itm_hunter],
   def_swordsman|level(21),wp(100),knows_riding_3|knows_ironflesh_3|knows_power_strike_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_knight","Vaegir Knight","Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_bardiche,itm_great_bardiche,itm_war_axe,itm_fighting_axe,itm_lance,itm_lance,itm_tab_shield_kite_cav_b,
    itm_lamellar_armor,itm_mail_boots,itm_plate_boots,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_hunter, itm_wwarhorsemaille1,itm_leather_gloves],
   def_guard|level(26),wp_one_handed (120) | wp_two_handed (140) | wp_polearm (120) | wp_archery (120) | wp_crossbow (120) | wp_throwing (120),knows_riding_4|knows_shield_2|knows_ironflesh_4|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2],
  
  ["vaegir_nobleman","Vaegir Nobleman","Vaegir Noblemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_sword_khergit_2,itm_lance,itm_tab_shield_kite_cav_a,itm_tab_shield_heater_d,itm_javelin,itm_war_darts,
    itm_lamellar_vest,itm_leather_boots,itm_vaegir_fur_helmet],
   str_16 | agi_10 | int_6 | cha_6|level(17),wp(100),knows_riding_3|knows_ironflesh_3|knows_power_strike_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_noble_warrior","Vaegir Noble Warrior","Vaegir Noble Warrior",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_mail_boots,itm_barbed_arrows,itm_nomad_bow,itm_javelin,itm_jarid,itm_tab_shield_heater_cav_a,itm_vaegir_noble_helmet,itm_tab_shield_heater_d,itm_lance,itm_bardiche,itm_vaegir_lamellar_helmet,itm_vaegir_noble_helmet,itm_lamellar_armor],
   def_guard|level(24),wp(150),knows_riding_3|knows_ironflesh_4|knows_power_strike_4|knows_athletics_1|knows_power_draw_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_holy_warrior","Vaegir Holy Warrior","Vaegir Holy Warrior",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_mail_boots,itm_barbed_arrows,itm_barbed_arrows,itm_war_bow,itm_lamellar_armor,itm_vaegir_mask,itm_lamellar_gauntlets,itm_great_long_bardiche],
   str_22 | agi_16 | int_8 | cha_8|level(32),wp(190),knows_riding_3|knows_ironflesh_6|knows_power_strike_6|knows_power_draw_6|knows_athletics_5,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_noble_knight","Vaegir Knight","Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_great_bardiche,itm_great_bardiche,itm_great_bardiche,itm_great_long_bardiche,itm_heavy_lance,itm_tab_shield_kite_cav_b,itm_lamellar_gauntlets,itm_iron_greaves,itm_vaegir_mask,itm_vaegir_elite_armor,itm_wwarhorsemaille3],
   str_23 | agi_16 | int_8 | cha_8|level(33),wp_one_handed (190) | wp_two_handed (180) | wp_polearm (180) | wp_archery (120) | wp_crossbow (120) | wp_throwing (120),knows_riding_5|knows_shield_4|knows_ironflesh_6|knows_power_strike_6,vaegir_face_middle_1, vaegir_face_older_2],
  #personal troop
  ["vaegir_archer_knight","Vaegir Holy Warrior","Vaegir Holy Warrior",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_great_bardiche,itm_great_bardiche,itm_great_bardiche,itm_iron_greaves,itm_barbed_arrows,itm_barbed_arrows,itm_war_bow,itm_vaegir_mask,itm_lamellar_gauntlets,itm_great_long_bardiche,itm_vaegir_elite_armor,itm_wwarhorsemaille3],
   def_knight_1|level(40),wp(255),knows_riding_9|knows_ironflesh_8|knows_power_strike_8|knows_power_draw_8|knows_athletics_8|knows_horse_archery_8,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_snow_patroler","vaegir_snow_patroler","vaegir_snow_patroler",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_courser,itm_akosmo_cap_b,itm_dorn_spearbearer_guant,itm_dorn_spearbearer_boots,itm_lamellar_vest,itm_bow3_spak,itm_bow3_arr_spak,itm_pa_sword_07,itm_fur_covered_shield],
   def_knight|level(35),wp(250),knows_riding_9|knows_ironflesh_7|knows_power_strike_7|knows_power_draw_7|knows_athletics_7|knows_horse_archery_7,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_snow_sister","vaegir_snow_sister","vaegir_snow_sister",tf_beautiful|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_steel_bolts,itm_sniper_crossbow,itm_vaeg_helmet5,itm_scimitar_b,itm_lamellar_armor,itm_lamellar_gauntlets,itm_rus_splint_greaves,itm_tab_shield_kite_cav_b],
   def_knight|level(35),wp(225),knows_ironflesh_7|knows_power_strike_7|knows_power_draw_7|knows_athletics_7,beauty_face1, beauty_face2],
  ["vaegir_axe_warrior","vaegir_axe_warrior","vaegir_axe_warrior",tf_tall|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_lamellar_gauntlets,itm_mail_boots,itm_great_long_bardiche,itm_luc_axe_knight_z,itm_kuyak_a,itm_vaeg_helmet8,itm_tab_shield_round_d],
   def_knight|level(35),wp(240),knows_ironflesh_8|knows_power_strike_8|knows_athletics_7|knows_shield_7,vaegir_face_young_1, vaegir_face_older_2],

  ["vaegir_patrol_leader","Vaegir Knight","Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_great_bardiche,itm_heavy_lance,itm_tab_shield_kite_cav_b,itm_lamellar_gauntlets,itm_iron_greaves,itm_vaeg_helmet5,itm_vaegir_elite_armor,itm_wwarhorsemaille3],
   def_champion|level(30),wp(170),knows_riding_5|knows_shield_4|knows_ironflesh_5|knows_power_strike_6,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_flag_holder","Vaegir Knight","Vaegir Knights",tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_lamellar_gauntlets,itm_iron_greaves,itm_vaegir_mask,itm_vaegir_elite_armor,itm_battle_flag_v],
   def_champion|level(25),wp(155),knows_ironflesh_5|knows_power_strike_5|knows_athletics_6,vaegir_face_middle_1, vaegir_face_older_2],

  ["vaegir_messenger","Vaegir Messenger","Vaegir Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_2,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_deserter","Vaegir Deserter","Vaegir Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_b,itm_studded_leather_coat,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["vaegir_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_d,itm_studded_leather_coat,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],

  ["khergit_tribesman","Khergit Tribesman","Khergit Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
   [itm_arrows,itm_club,itm_spear,itm_hunting_bow,
    itm_steppe_cap,itm_nomad_cap_b,itm_leather_vest,itm_steppe_armor,itm_nomad_boots,itm_khergit_leather_boots],
   str_8 | agi_7 | int_5 | cha_5|level(5),wp(50),knows_common|knows_riding_3|knows_power_draw_2|knows_horse_archery_2,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_skirmisher","Khergit Skirmisher","Khergit Skirmishers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear,itm_nomad_bow,itm_javelin,itm_tab_shield_small_round_a,
    itm_steppe_cap,itm_nomad_cap_b,itm_leather_steppe_cap_a,itm_khergit_armor,itm_steppe_armor,itm_leather_vest,itm_nomad_boots,itm_khergit_leather_boots,itm_steppe_horse,itm_saddle_horse],
   def_footman|level(10),wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (80) | wp_crossbow (60) | wp_throwing (80),knows_common|knows_riding_4|knows_power_draw_3|knows_power_throw_1|knows_horse_archery_3,khergit_face_younger_1, khergit_face_old_2],
  ["khergit_horseman","Khergit Horseman","Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
  [itm_arrows,itm_light_lance,itm_nomad_bow,itm_sword_khergit_2,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_spear,
   itm_leather_steppe_cap_a, itm_leather_steppe_cap_b,itm_nomad_robe,itm_nomad_vest,itm_khergit_leather_boots,itm_hide_boots,itm_spiked_helmet,itm_nomad_cap,itm_steppe_horse,itm_hunter],
   def_fighter|level(14),wp(80),knows_common|knows_riding_5|knows_power_draw_4|knows_ironflesh_2|knows_power_throw_2|knows_horse_archery_3|knows_shield_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_horse_archer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_arrows,itm_sword_khergit_2,itm_winged_mace,itm_spear,itm_khergit_bow,itm_tab_shield_small_round_a,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_bodkin_arrows,itm_arrows,itm_javelin,
    itm_leather_steppe_cap_b,itm_nomad_cap_b,itm_tribal_warrior_outfit,itm_nomad_robe,itm_khergit_leather_boots,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_steppe_horse],
   str_15 | agi_11 | int_6 | cha_6|level(17),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (120) | wp_crossbow (80) | wp_throwing (120),knows_riding_5|knows_power_draw_3|knows_ironflesh_2|knows_power_strike_2|knows_horse_archery_4|knows_power_throw_3,khergit_face_young_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer","Khergit Veteran Horse Archer","Khergit Veteran Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_winged_mace,itm_spear,itm_khergit_bow,itm_arrows,itm_khergit_arrows,itm_khergit_arrows,itm_khergit_arrows,itm_tab_shield_small_round_c,
    itm_khergit_cavalry_helmet,itm_lamellar_vest_khergit,itm_rich_tunic_a_lamellar_armour,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_leather_gloves,itm_steppe_horse,itm_courser],
   str_18 | agi_13 | int_7 | cha_7|level(24),wp_one_handed (120) | wp_two_handed (120) | wp_polearm (120) | wp_archery (150) | wp_crossbow (90) | wp_throwing (130),knows_riding_7|knows_power_draw_5|knows_ironflesh_3|knows_power_strike_3|knows_horse_archery_7|knows_power_throw_5|knows_shield_3,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_veteran_horseman","Khergit Veteran Horseman","Khergit Veteran Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_winged_mace,itm_spear
   ,itm_nomad_bow,itm_arrows,itm_javelin,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,
    itm_khergit_cavalry_helmet,itm_khergit_cavalry_helmet,itm_lamellar_vest_khergit,itm_rich_tunic_a_lamellar_armour,itm_khergit_leather_boots,itm_leather_gloves,itm_steppe_horse,itm_courser],
   def_swordsman|level(19),wp_one_handed (100) | wp_two_handed (110) | wp_polearm (120) | wp_archery (100) | wp_crossbow (90) | wp_throwing (100),knows_riding_6|knows_power_draw_5|knows_ironflesh_3|knows_power_strike_2|knows_horse_archery_6|knows_power_throw_4|knows_shield_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,itm_javelin,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_rich_tunic_a_lamellar_armour,itm_nomad_vest_lamellar,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_scale_gauntlets,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_warhorse_steppe],
   str_19 | agi_14 | int_7 | cha_7|level(26),wp_one_handed (150) | wp_two_handed (150) | wp_polearm (150) | wp_archery (110) | wp_crossbow (150) | wp_throwing (150),knows_riding_7|knows_power_strike_4|knows_power_draw_4|knows_power_throw_4|knows_ironflesh_4|knows_horse_archery_3|knows_shield_2,khergit_face_middle_1, khergit_face_older_2],
  
  ["khergit_nobleman","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_khergit_arrows,itm_sword_khergit_2,itm_winged_mace,itm_spear,itm_khergit_bow,itm_tab_shield_small_round_a,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_bodkin_arrows,itm_arrows,itm_javelin,
    itm_leather_steppe_cap_b,itm_nomad_cap_b,itm_khergit_lamellar_leather_armor,itm_nomad_robe,itm_khergit_leather_boots,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_steppe_horse],
   def_swordsman|level(19),wp(100),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_3|knows_power_throw_3,khergit_face_young_1, khergit_face_older_2],
  ["khergit_nobleman_warrior","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_khergit_arrows,itm_sword_khergit_2,itm_winged_mace,itm_spear,itm_khergit_bow,itm_tab_shield_small_round_a,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_arrows,itm_javelin,
    itm_rich_tunic_a_lamellar_armour,itm_nomad_vest_lamellar,itm_khergit_guard_helmet,itm_khergit_leather_boots,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_steppe_horse,itm_warhorse_steppe],
   def_guard|level(26),wp(100),knows_riding_7|knows_power_draw_3|knows_ironflesh_3|knows_horse_archery_5|knows_power_throw_3|knows_power_draw_4,khergit_face_young_1, khergit_face_older_2],
  ["khergit_nobleman_horse_archer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_khergit_arrows,itm_khergit_arrows,itm_spak_bow7,itm_hafted_blade_a,itm_warhorse_steppe,itm_mongol_pike_a,
   itm_khergit_guard_armor,itm_mongol_helmet_xf,itm_khergit_leather_boots,itm_leather_gloves],
   def_knight|level(35),wp(210),knows_riding_9|knows_power_draw_6|knows_ironflesh_6|knows_power_strike_7|knows_horse_archery_8|knows_shield_2,khergit_face_young_1, khergit_face_older_2],
  ["khergit_nobleman_knight","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_javelin,itm_brass_shield1,itm_heavy_lance,itm_sword_khergit_4,itm_lamellar_charger_a,
   itm_mongol_helmet_xf,itm_khergit_elite_armor,itm_khergit_guard_boots,itm_lamellar_gauntlets],
   def_knight|level(35),wp(210),knows_riding_9|knows_ironflesh_6|knows_power_strike_7|knows_horse_archery_7|knows_power_throw_7|knows_shield_5,khergit_face_young_1, khergit_face_older_2],
  #personal troop
  ["khergit_kehan_guard","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_khergit_arrows,itm_khergit_arrows,itm_spak_bow7,itm_mongol_pike_a,itm_warhorse_steppe,itm_mongol_pike_b,
   itm_mongol_armor_heavy,itm_mask_helmet1,itm_khergit_leather_boots,itm_leather_gloves],
   str_24 | agi_20 | int_8 | cha_8|level(38),wp(230),knows_riding_9|knows_power_draw_8|knows_ironflesh_8|knows_power_strike_8|knows_horse_archery_9,khergit_face_young_1, khergit_face_older_2],
  ["khergit_spear_warrior","Khergit Horse Archer","Khergit Horse Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_mongol_armor_heavy,itm_khergit_guard_helmet,itm_khergit_leather_boots,itm_leather_gloves,itm_amroth_lance,itm_javelin,itm_throwing_spears],
   def_knight|level(35),wp(200),knows_riding_9|knows_ironflesh_6|knows_power_strike_7|knows_power_throw_7|knows_athletics_8,khergit_face_young_1, khergit_face_older_2],
  ["khergit_darhan","Khergit Darhan","Khergit Darhans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_khergit_elite_armor,itm_mask_helmet1,itm_khergit_leather_boots,itm_lamellar_gauntlets,itm_throwing_spears,itm_throwing_spears,itm_tab_shield_small_round_c,itm_gondor_spear],
   def_knight|level(35),wp(200),knows_ironflesh_7|knows_power_strike_6|knows_power_throw_9|knows_athletics_5,khergit_face_young_1, khergit_face_older_2],
  ["khergit_iron_knight","Khergit Iron Knight","Khergit Iron Knights",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_3,
   [itm_wgoldcata,itm_mongol_armor_heavy,itm_mongol_helmet_xf,itm_black_greaves,itm_gauntlets,itm_blood_spear,itm_pa_sword_02,itm_toumao,itm_dec_steel_shield],
   def_knight_1|level(40),wp(275),knows_ironflesh_8|knows_power_strike_9|knows_power_throw_9|knows_athletics_6|knows_riding_11|knows_shield_6,khergit_face_young_1, khergit_face_older_2],

  ["khergit_patrol_leader","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_javelin,itm_brass_shield1,itm_heavy_lance,itm_sword_khergit_4,itm_lamellar_charger_a,
   itm_mongol_helmet_xf,itm_khergit_elite_armor,itm_khergit_guard_boots,itm_lamellar_gauntlets],
   def_champion|level(30),wp(175),knows_riding_8|knows_ironflesh_5|knows_power_strike_6|knows_horse_archery_6|knows_power_throw_5|knows_shield_5,khergit_face_young_1, khergit_face_older_2],
  ["khergit_flag_holder","Khergit Horse Archer","Khergit Horse Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_javelin,itm_battle_flag_k,itm_khergit_guard_helmet,itm_khergit_guard_armor,itm_khergit_guard_boots,itm_lamellar_gauntlets],
   def_guard|level(25),wp(160),knows_ironflesh_5|knows_power_strike_6|knows_power_throw_5,khergit_face_young_1, khergit_face_older_2],

  ["khergit_messenger","Khergit Messenger","Khergit Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(125),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,khergit_face_young_1, khergit_face_older_2],
  ["khergit_deserter","Khergit Deserter","Khergit Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_tribal_warrior_outfit,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,khergit_face_young_1, khergit_face_older_2],
  ["khergit_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_lamellar_armor,itm_khergit_leather_boots,itm_iron_greaves,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap],
   def_attrib|level(24),wp(130),knows_athletics_5|knows_shield_2|knows_ironflesh_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_lamellar_armor,itm_khergit_leather_boots,itm_iron_greaves,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap],
   def_attrib|level(24),wp(130),knows_athletics_5|knows_shield_2|knows_ironflesh_5,khergit_face_middle_1, khergit_face_older_2],

  ["nord_recruit","Nord Recruit","Nord Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_axe,itm_hatchet,itm_spear,itm_tab_shield_round_a,itm_tab_shield_round_a,
    itm_blue_tunic,itm_coarse_tunic,itm_hide_boots,itm_nomad_boots],
   str_9 | agi_7 | int_5 | cha_5|level(6),wp(50),knows_power_strike_1|knows_power_throw_1|knows_riding_1|knows_athletics_1,nord_face_younger_1, nord_face_old_2],
  ["nord_footman","Nord Footman","Nord Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_4,
   [itm_fighting_axe,itm_one_handed_war_axe_a,itm_spear,itm_tab_shield_round_a,itm_tab_shield_round_b,itm_javelin,itm_throwing_axes,
    itm_leather_cap,itm_skullcap,itm_nomad_vest,itm_leather_boots,itm_nomad_boots],
   def_footman|level(10),wp(70),knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_2|knows_shield_1,nord_face_young_1, nord_face_old_2],
  ["nord_trained_footman","Nord Trained Footman","Nord Trained Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_a,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_tab_shield_round_b,
    itm_skullcap,itm_nasal_helmet,itm_nordic_footman_helmet,itm_byrnie,itm_studded_leather_coat,itm_leather_boots],
   def_fighter|level(14),wp(100),knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_riding_2|knows_athletics_3|knows_shield_2,nord_face_young_1, nord_face_old_2],
  ["nord_warrior","Nord Warrior","Nord Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_tab_shield_round_c,itm_javelin,
    itm_nordic_footman_helmet,itm_nordic_fighter_helmet,itm_mail_shirt,itm_studded_leather_coat,itm_hunter_boots,itm_leather_boots],
   def_swordsman|level(19),wp(115),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_riding_2|knows_athletics_4|knows_shield_3,nord_face_young_1, nord_face_older_2],
  ["nord_veteran","Nord Veteran","Nord Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_sword_viking_2_small,itm_one_handed_battle_axe_b,itm_spiked_mace,itm_tab_shield_round_d,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
   def_guard|level(24),wp(145),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_riding_3|knows_athletics_5|knows_shield_4,nord_face_young_1, nord_face_older_2],
  ["nord_champion","Nord Huscarl","Nord Huscarls",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_3,itm_great_axe,itm_one_handed_battle_axe_c,itm_tab_shield_round_e,itm_throwing_spears,itm_heavy_throwing_axes,itm_heavy_throwing_axes,
    itm_nordic_huscarl_helmet,itm_nordic_warlord_helmet,itm_banded_armor,itm_mail_boots,itm_mail_chausses,itm_mail_mittens],
   str_20 | agi_15 | int_7 | cha_7|level(28),wp(170),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_riding_2|knows_athletics_7|knows_shield_6,nord_face_middle_1, nord_face_older_2],
  ["nord_huntsman","Nord Huntsman","Nord Huntsmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_arrows,itm_rawhide_coat,itm_hatchet,itm_hunting_bow,itm_hide_boots],
   str_12 | agi_8 | int_6 | cha_6|level(11),wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (70) | wp_crossbow (60) | wp_throwing (60),knows_ironflesh_1|knows_power_draw_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],
  ["nord_archer_1","Nord Archer","Nord Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_4,
   [itm_arrows,itm_axe,itm_northerner_horse,itm_northerner_horse_black,itm_arrows,itm_short_bow,itm_leather_jerkin,itm_tribal_warrior_outfit,itm_padded_leather,itm_leather_boots,itm_nasal_helmet,itm_nordic_archer_helmet,itm_leather_cap],
   str_16 | agi_10 | int_6 | cha_6|level(17),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (105) | wp_crossbow (80) | wp_throwing (105),knows_riding_2|knows_ironflesh_2|knows_power_strike_1|knows_power_draw_3|knows_horse_archery_2|knows_power_throw_3|knows_athletics_5,nord_face_young_1, nord_face_old_2],
  ["nord_archer_2","Nord Veteran","Nord Veterans",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_nomad_bow,itm_barbed_arrows,itm_long_bow,itm_sword_viking_2_small,itm_one_handed_battle_axe_b,itm_spiked_mace,itm_northerner_horse_white,itm_tab_shield_round_d,itm_javelin,itm_throwing_axes,itm_northerner_horse_hunter,
    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
   str_17 | agi_12 | int_7 | cha_7|level(22),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (115) | wp_crossbow (80) | wp_throwing (115),knows_riding_4|knows_ironflesh_4|knows_power_strike_3|knows_power_draw_4|knows_horse_archery_4|knows_power_throw_4|knows_riding_3|knows_athletics_5|knows_shield_2,nord_face_young_1, nord_face_older_2],
  ["nord_archer","Nord Archer","Nord Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
   [itm_arrows,itm_axe,itm_short_bow,itm_padded_leather,itm_leather_jerkin,itm_padded_leather,itm_leather_boots,itm_nasal_helmet,itm_nordic_archer_helmet,itm_leather_cap],
   def_fighter|level(15),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (95) | wp_crossbow (80) | wp_throwing (80),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_athletics_5,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_archer","Nord Veteran Archer","Nord Veteran Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_bodkin_arrows,itm_sword_viking_2,itm_fighting_axe,itm_two_handed_axe,itm_long_bow,itm_mail_shirt,itm_mail_shirt,itm_byrnie,itm_leather_boots,itm_nordic_archer_helmet,itm_nordic_veteran_archer_helmet],
   def_swordsman|level(19),wp_one_handed (95) | wp_two_handed (95) | wp_polearm (95) | wp_archery (120) | wp_crossbow (95) | wp_throwing (95),knows_power_strike_3|knows_ironflesh_4|knows_power_draw_5|knows_athletics_7,nord_face_middle_1, nord_face_older_2],
  
  ["nord_nobleman","Nord Nobleman","Nord Noblemen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_3,itm_sword_viking_2,itm_nordic_helmet,itm_splinted_leather_greaves,itm_two_handed_battle_axe_2,itm_mail_mittens,itm_nobleman_armor_nord,itm_shield_kite_g],
   def_swordsman|level(21),wp(120),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_riding_2|knows_athletics_3|knows_shield_3,nord_face_middle_1, nord_face_older_2],
  ["nord_nobleman_warrior","Nord Huscarl","Nord Huscarls",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_mackie_celtic_axe,itm_one_handed_battle_axe_c,itm_battle_shield,itm_heavy_throwing_axes,itm_heavy_throwing_axes,itm_northerner_horse_black,itm_northerner_horse,
    itm_nordic_huscarl_helmet,itm_mail_hauberk,itm_mail_chausses,itm_mail_mittens],
   def_champion|level(29),wp(170),knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_riding_4|knows_athletics_4|knows_shield_6,nord_face_middle_1, nord_face_older_2],
  ["nord_nobleman_champion_horse","Nord Huscarl","Nord Huscarls",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_sword_viking_3,itm_great_axe,itm_one_handed_battle_axe_c,itm_steel_shield,itm_throwing_spears,itm_heavy_throwing_axes,
    itm_banded_armor_a_cloak,itm_valsgarde_guards2,itm_nordic_warlord_helmet,itm_dejawolf_vikingbyrnie,itm_mail_boots,itm_mail_mittens,itm_wlong16,itm_heavy_lance],
   str_25 | agi_18 | int_8 | cha_8|level(37),wp(235),knows_ironflesh_8|knows_power_strike_7|knows_power_throw_6|knows_riding_5|knows_athletics_7|knows_shield_7,nord_face_middle_1, nord_face_older_2],
  #personal troop
  ["nord_king_guard","Nord Huscarl","Nord Huscarls",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_tall,0,0,fac_kingdom_4,
   [itm_pa_axe_06,itm_heavy_throwing_axes,itm_throwing_spears,itm_tab_shield_round_e,itm_valsgarde_new,itm_wei_xiadi_valk,itm_plate_boots,itm_mail_mittens,itm_charger2],
   def_knight_1|level(40),wp(240),knows_ironflesh_9|knows_power_strike_9|knows_power_throw_9|knows_riding_3|knows_athletics_7|knows_shield_7,nord_face_middle_1, nord_face_older_2],
    ["nord_fians","Nord Fians","Nord Fians",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_4,
   [itm_bear_warrior,itm_mail_mittens,itm_mail_chausses,itm_barbuta2,itm_pa_axe_01,itm_throwing_spears,itm_throwing_spears,itm_tab_shield_round_e],
   def_knight|level(35),wp(215),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_7|knows_riding_3|knows_athletics_7|knows_shield_7,nord_face_middle_1, nord_face_older_2],
  
  ["nord_storm_guard","Nord storm guard","Nord storm guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_4,
   [itm_wei_xiadi_nord_cuir_bouilli,itm_mail_mittens,itm_mail_chausses,itm_norman_mask,itm_pa_axe_05,itm_tab_shield_round_e,itm_spak_crsb01,itm_steel_bolts],
   def_knight|level(35),wp(200),knows_ironflesh_7|knows_power_strike_7|knows_athletics_7|knows_shield_7,nord_face_middle_1, nord_face_older_2],
  ["nord_axe_warrior","Nord Huscarl","Nord Huscarls",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves|tf_tall,0,0,fac_kingdom_4,
   [itm_2dblhead_ax,itm_2dblhead_ax_1,itm_throwing_spears,itm_heavy_throwing_axes,itm_throwing_spears,itm_valhelm_e,itm_rhodok_cuir_bouilli,itm_splinted_leather_greaves,itm_mail_mittens],
   def_knight_1|level(40),wp(250),knows_ironflesh_9|knows_power_strike_9|knows_power_throw_9|knows_riding_3|knows_athletics_7,nord_face_middle_1, nord_face_older_2],

  ["nord_patrol_leader","Nord Huscarl","Nord Huscarls",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_one_handed_battle_axe_c,itm_steel_shield,itm_throwing_spears,itm_heavy_throwing_axes,
    itm_valsgarde_guards2,itm_dejawolf_vikingbyrnie,itm_mail_boots,itm_mail_mittens,itm_wlong16,itm_heavy_lance],
   def_champion|level(30),wp(180),knows_ironflesh_6|knows_power_strike_6|knows_power_throw_6|knows_riding_5|knows_athletics_5|knows_shield_5,nord_face_middle_1, nord_face_older_2],
  ["nord_flag_holder","Nord Huscarl","Nord Huscarls",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_battle_flag_nord,itm_throwing_spears,itm_heavy_throwing_axes,itm_williamconqueror_helm,itm_williamconquer,itm_mail_boots,itm_mail_mittens],
   def_guard|level(25),wp(150),knows_ironflesh_6|knows_power_strike_4|knows_power_throw_6|knows_athletics_5,nord_face_middle_1, nord_face_older_2],

  ["nord_messenger","Nord Messenger","Nord Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   str_7 | agi_21 | int_4 | cha_4|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,nord_face_young_1, nord_face_older_2],
  ["nord_deserter","Nord Deserter","Nord Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   str_10 | agi_5 | int_4 | cha_4|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,nord_face_young_1, nord_face_older_2],
  ["nord_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_round_d,itm_mail_hauberk,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],
  ["nord_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_round_d,itm_tab_shield_round_e,itm_mail_hauberk,itm_heraldic_mail_with_tabard,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],

  ["rhodok_tribesman","Rhodok Tribesman","Rhodok Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_pitch_fork,itm_tab_shield_pavise_a,
    itm_shirt,itm_coarse_tunic,itm_wrapping_boots,itm_nomad_boots,itm_head_wrappings,itm_straw_hat],
   def_farmer|level(4),wp(55),knows_common|knows_power_draw_2|knows_ironflesh_1,rhodok_face_younger_1, rhodok_face_old_2],
  ["rhodok_spearman","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
   [itm_spear,itm_pike,itm_spear,itm_tab_shield_pavise_a,itm_falchion,
    itm_felt_hat_b,itm_common_hood,itm_leather_armor,itm_arena_tunic_green,itm_wrapping_boots,itm_nomad_boots],
   def_footman|level(9),wp(80),knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_2|knows_athletics_1,rhodok_face_young_1, rhodok_face_old_2],
  ["rhodok_trained_spearman","Rhodok Trained Spearman","Rhodok Trained Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_pike,itm_war_spear,itm_tab_shield_heater_a,
    itm_footman_helmet,itm_padded_coif,itm_aketon_green,itm_aketon_green,itm_ragged_outfit,itm_nomad_boots,itm_leather_boots],
   def_fighter|level(14),wp_one_handed (105) | wp_two_handed (105) | wp_polearm (115) | wp_archery (105) | wp_crossbow (105) | wp_throwing (105),knows_common|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_2,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_trained_horseman","Rhodok Trained Spearman","Rhodok Trained Spearmen",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_hunter,itm_war_spear,itm_tab_shield_pavise_b,itm_military_cleaver_b,itm_falchion,
    itm_kettle_hat,itm_mail_coif,itm_mail_with_tunic_green,itm_splinted_leather_greaves,itm_leather_boots],
   str_15 | agi_12 | int_6 | cha_6|level(18),wp_one_handed (115) | wp_two_handed (115) | wp_polearm (115) | wp_archery (105) | wp_crossbow (105) | wp_throwing (105),knows_common|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_2|knows_riding_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_trained_horseman_1","Rhodok Trained Spearman","Rhodok Trained Spearmen",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_warhorse_grn2,itm_glaive,itm_military_hammer,itm_tab_shield_pavise_c,
    itm_kettle_hat,itm_full_helm,itm_surcoat_over_mail,itm_splinted_leather_greaves,itm_mail_chausses],
   str_18 | agi_12 | int_7 | cha_7|level(23),wp_one_handed (125) | wp_two_handed (125) | wp_polearm (135) | wp_archery (105) | wp_crossbow (105) | wp_throwing (105),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_2|knows_riding_4,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman","Rhodok Veteran Spearman","Rhodok Veteran Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_glaive,itm_tab_shield_pavise_c,
    itm_kettle_hat,itm_mail_coif,itm_mail_with_tunic_green,itm_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves],
   def_swordsman|level(19),wp_one_handed (115) | wp_two_handed (115) | wp_polearm (130) | wp_archery (115) | wp_crossbow (115) | wp_throwing (115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_sergeant","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_glaive,itm_military_hammer,itm_military_cleaver_c,itm_tab_shield_pavise_d,
    itm_full_helm, itm_bascinet_3,itm_bascinet_2,itm_surcoat_over_mail,itm_surcoat_over_mail,itm_heraldic_mail_with_surcoat,itm_mail_chausses,itm_leather_gloves,itm_mail_mittens],
   def_guard|level(25),wp_one_handed (130) | wp_two_handed (115) | wp_polearm (155) | wp_archery (115) | wp_crossbow (115) | wp_throwing (115),knows_common|knows_ironflesh_6|knows_shield_5|knows_power_strike_5|knows_athletics_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_crossbowman","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_falchion,itm_club_with_spike_head,itm_tab_shield_pavise_a,itm_crossbow,itm_bolts,
    itm_arena_tunic_green,itm_felt_hat_b,itm_common_hood,itm_nomad_boots,itm_wrapping_boots],
   def_footman|level(10),wp(85),knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_1|knows_athletics_2,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_trained_crossbowman","Rhodok Trained Crossbowman","Rhodok Trained Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_club_with_spike_head,itm_tab_shield_pavise_a,itm_crossbow,itm_bolts,
    itm_common_hood,itm_leather_armor,itm_arena_tunic_green,itm_nomad_boots],
   def_fighter|level(15),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (105) | wp_throwing (90),knows_common|knows_ironflesh_1|knows_shield_2|knows_power_strike_2|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_crossbowman","Rhodok Veteran Crossbowman","Rhodok Veteran Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_fighting_pick,itm_club_with_spike_head,itm_tab_shield_pavise_b,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts,
    itm_leather_cap,itm_felt_hat_b,itm_aketon_green,itm_leather_boots],
   def_swordsman|level(20),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (120) | wp_throwing (100),knows_common|knows_ironflesh_2|knows_shield_3|knows_power_strike_3|knows_athletics_4,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sharpshooter","Rhodok Sharpshooter","Rhodok Sharpshooters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_military_pick,itm_military_hammer,itm_tab_shield_pavise_c,itm_sniper_crossbow,itm_steel_bolts,
    itm_kettle_hat,itm_mail_with_tunic_green,itm_leather_boots,itm_splinted_leather_greaves],
   def_guard|level(25),wp_one_handed (110) | wp_two_handed (110) | wp_polearm (110) | wp_archery (100) | wp_crossbow (140) | wp_throwing (100),knows_common|knows_ironflesh_3|knows_shield_4|knows_power_strike_4|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  
  ["rhodok_nobleman","Rhodok Veteran Crossbowman","Rhodok Veteran Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_fighting_pick,itm_club_with_spike_head,itm_tab_shield_pavise_b,itm_tab_shield_pavise_c,itm_crossbow,itm_bolts,
    itm_nobleman_armor_rhodok,itm_kettle_hat,itm_leather_boots],
   str_15 | agi_11 | int_6 | cha_6|level(17),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (100) | wp_crossbow (100) | wp_throwing (100),knows_common|knows_ironflesh_2|knows_shield_3|knows_power_strike_3|knows_athletics_4,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_squire","Rhodok Veteran Crossbowman","Rhodok Veteran Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_military_pick,itm_tab_shield_kite_cav_a,itm_crossbow,itm_bolts,
    itm_mail_long_surcoat_new_c3,itm_bascinet_2,itm_mail_chausses,itm_hunter,itm_mail_mittens,itm_brigandine_heraldic],
   def_guard|level(24),wp_one_handed (120) | wp_two_handed (120) | wp_polearm (120) | wp_archery (120) | wp_crossbow (120) | wp_throwing (120),knows_ironflesh_4|knows_shield_3|knows_power_strike_3|knows_athletics_4|knows_riding_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_knight","Rhodok Veteran Crossbowman","Rhodok Veteran Crossbowmen",tf_mounted|tf_guarantee_horse| tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_ganquang_pick,itm_tab_shield_kite_cav_b,itm_military_pick,itm_military_hammer,itm_heavy_lance,itm_wlong15,
    itm_heraldic_mail_with_tabard,itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tunic_b,itm_full_helm,itm_iron_greaves,itm_gauntlets,itm_lamellar_gauntlets],
   def_knight|level(33),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),knows_ironflesh_6|knows_shield_6|knows_power_strike_6|knows_athletics_5|knows_riding_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_walk_knight","Rhodok Veteran Crossbowman","Rhodok Veteran Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_ganquang_pick,itm_tab_shield_pavise_d,itm_brigandine_plate_heraldic,itm_military_hammer,itm_throwing_spears,itm_ak_poleaxe,
   itm_mail_boots,itm_full_helm,itm_lamellar_gauntlets,itm_gauntlets,itm_bec_de_corbin_a,itm_poleaxe],
   def_knight|level(33),wp_one_handed (200) | wp_two_handed (200) | wp_polearm (200) | wp_archery (200) | wp_crossbow (200) | wp_throwing (200),knows_ironflesh_6|knows_shield_6|knows_power_strike_6|knows_athletics_5|knows_power_throw_5,rhodok_face_middle_1, rhodok_face_older_2],
  #personal troop
  ["rhodok_gurd_knight","rhodok_guard_knight","rhodok_guard_knight",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_heraldic_plate_01,itm_iron_greaves,itm_visored_bascinet_02,itm_ak_poleaxe,itm_spak_crsb02,itm_steel_bolts,itm_steel_bolts,itm_steel_gauntlets,itm_gauntlets],
   def_knight_1|level(40),wp(250),knows_ironflesh_8|knows_shield_8|knows_power_strike_8|knows_athletics_8|knows_power_throw_8,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_shooter","rhodok_shooter","rhodok_shooter",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_flintlock_rifle,itm_cartridges,itm_tab_shield_pavise_d,itm_luc_knightly_axe_one_handed,itm_surcoat_over_mail_banner,itm_leather_gloves,itm_splinted_greaves,itm_sallet_03],
   def_knight|level(35),wp(200),knows_ironflesh_7|knows_shield_7|knows_power_strike_7|knows_athletics_7,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_hunter","rhodok_hunter","rhodok_hunter",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_strong_bow,itm_bodkin_arrows,itm_barbed_arrows,itm_tab_shield_pavise_c,itm_military_cleaver_b,itm_arena_armor_banner,itm_mail_coif,itm_new_leather_boots,],
   def_champion|level(30),wp(160),knows_ironflesh_5|knows_shield_5|knows_power_strike_5|knows_athletics_5|knows_power_draw_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_elite_knight","rhodok_elite_knight","rhodok_elite_knight",tf_mounted|tf_guarantee_horse| tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_tab_shield_kite_cav_b,itm_charger4_new,itm_wisby_gauntlets_red,itm_wisby_gauntlets_black,itm_frenchpepperpot2,itm_steel_greaves,itm_sorrow,itm_early_transitional_banner,itm_blood_spear,itm_toumao],
   def_knight_1|level(40),wp(275),knows_ironflesh_9|knows_shield_8|knows_power_strike_9|knows_athletics_8|knows_riding_8|knows_power_throw_10,rhodok_face_middle_1, rhodok_face_older_2],

  ["rhodok_patrol_leader","Rhodok Veteran Crossbowman","Rhodok Veteran Crossbowmen",tf_mounted|tf_guarantee_horse| tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_tab_shield_kite_cav_b,itm_military_pick,itm_military_hammer,itm_heavy_lance,itm_wlong15,
    itm_heraldic_mail_with_tabard,itm_full_helm,itm_iron_greaves,itm_lamellar_gauntlets],
   def_champion|level(30),wp(170),knows_ironflesh_6|knows_shield_5|knows_power_strike_5|knows_athletics_5|knows_riding_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_flag_holder","Rhodok Veteran Crossbowman","Rhodok Veteran Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_5,
   [itm_battle_flag_l,itm_heraldic_mail_with_tunic,itm_full_helm,itm_iron_greaves,itm_mail_mittens],
   def_guard|level(25),wp(150),knows_ironflesh_5|knows_power_strike_5|knows_athletics_5,rhodok_face_middle_1, rhodok_face_older_2],

  ["rhodok_messenger","Rhodok Messenger","Rhodok Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_5,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_deserter","Rhodok Deserter","Rhodok Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_pavise_b,itm_bascinet_2,itm_surcoat_over_mail,itm_mail_chausses,itm_iron_greaves,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_pavise_c,itm_bascinet_2,itm_surcoat_over_mail,itm_mail_chausses,itm_iron_greaves,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],
#peasant - retainer - footman - man-at-arms -  knight

 ["sarranid_recruit","Sarranid Recruit","Sarranid Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_sarranid_felt_hat,itm_turban,itm_sarranid_boots_a,
    itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_farmer|level(4),wp(60),knows_common|knows_athletics_1,swadian_face_younger_1, swadian_face_middle_2],
 ["sarranid_footman","Sarranid Footman","Sarranid Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_bamboo_spear,itm_arabian_sword_a,itm_tab_shield_kite_a,itm_desert_turban,
    itm_skirmisher_armor,itm_turban,itm_sarranid_boots_a,itm_sarranid_boots_b],
   def_footman|level(9),wp(75),knows_common|knows_athletics_2,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_veteran_footman","Sarranid Veteran Footman","Sarranid Veteran Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_bamboo_spear,itm_arabian_sword_a,itm_arabian_sword_b,itm_tab_shield_kite_b,
    itm_sarranid_boots_b,itm_sarranid_warrior_cap,itm_sarranid_leather_armor,itm_jarid,itm_arabian_sword_a,itm_mace_3],
   def_fighter|level(14),wp_one_handed (85) | wp_two_handed (85) | wp_polearm (85) | wp_archery (75) | wp_crossbow (75) | wp_throwing (100),knows_common|knows_athletics_2|knows_power_throw_2|knows_ironflesh_1|knows_power_strike_2|knows_shield_2,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_infantry","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_sarranid_mail_shirt,itm_sarranid_mail_coif,itm_jarid,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_sarranid_axe_a,itm_arabian_sword_b,itm_mace_3,itm_spear,itm_tab_shield_kite_c],
   def_swordsman|level(20),wp_one_handed (105) | wp_two_handed (105) | wp_polearm (105) | wp_archery (75) | wp_crossbow (75) | wp_throwing (110),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_shield_3 | knows_power_throw_3|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
 ["sarranid_guard","Sarranid Guard","Sarranid Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_military_pick,itm_sarranid_two_handed_axe_a,itm_jarid,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_d, itm_sarranid_boots_c,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_veiled_helmet,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
   def_guard|level(25),wp_one_handed (135) | wp_two_handed (135) | wp_polearm (135) | wp_archery (75) | wp_crossbow (75) | wp_throwing (140),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_4|knows_athletics_5,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_skirmisher","Sarranid Skirmisher","Sarranid Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_turban,itm_desert_turban,itm_skirmisher_armor,itm_jarid,itm_jarid,itm_arabian_sword_a,itm_spiked_club,itm_tab_shield_small_round_a,itm_sarranid_warrior_cap,itm_sarranid_boots_a],
   def_fighter|level(14),wp(80),knows_common|knows_riding_2|knows_power_throw_2|knows_ironflesh_1|knows_power_strike_1|knows_athletics_3,swadian_face_young_1, swadian_face_middle_2],
 ["sarranid_archer","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_arrows,itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_archers_vest,itm_sarranid_boots_b,itm_sarranid_helmet1,itm_sarranid_warrior_cap,itm_desert_turban],
   def_swordsman|level(19),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (100) | wp_crossbow (90) | wp_throwing (100),knows_common|knows_power_draw_3|knows_ironflesh_2|knows_power_strike_2|knows_power_throw_3|knows_athletics_4,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_master_archer","Sarranid Master Archer","Sarranid Master Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_barbed_arrows,itm_barbed_arrows,itm_arabian_sword_b,itm_mace_3,itm_strong_bow,itm_nomad_bow,
    itm_arabian_armor_b,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_sarranid_mail_coif],
   def_guard|level(24),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (130) | wp_crossbow (100) | wp_throwing (130),knows_common|knows_power_draw_4|knows_power_throw_4|knows_riding_5|knows_ironflesh_3|knows_power_strike_3|knows_athletics_5,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_master_archerwithhorse","sarranid_master_archerwithhorse","sarranid_master_archerwithhorse",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_6,
   [itm_barbed_arrows,itm_camel1,itm_camel2,itm_barbed_arrows,itm_arabian_sword_b,itm_mace_3,itm_strong_bow,itm_nomad_bow,
    itm_arabian_armor_b,itm_sarranid_cavalry_robe,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_sarranid_mail_coif],
   def_guard|level(24),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (130) | wp_crossbow (100) | wp_throwing (130),knows_common|knows_power_draw_4|knows_power_throw_4|knows_riding_5|knows_ironflesh_3|knows_power_strike_4|knows_horse_archery_5|knows_athletics_5,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_horseman","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_sarranid_boots_c,itm_sarranid_boots_b, itm_sarranid_horseman_helmet,itm_leather_gloves,itm_arabian_horse_a,itm_courser],
   def_swordsman|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_mamluke","Sarranid Horseman","Sarranid Horsemans",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_scimitar_b,itm_sarranid_two_handed_mace_1,itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c,
    itm_mamluke_mail,itm_sarranid_boots_d,itm_lamellar_charger_y,itm_sarranid_veiled_helmet,itm_mail_mittens],
   str_20 | agi_14 | int_7 | cha_7|level(27),wp_one_handed (150) | wp_two_handed (130) | wp_polearm (130) | wp_archery (75) | wp_crossbow (75) | wp_throwing (110),knows_common|knows_riding_6|knows_shield_5|knows_ironflesh_5|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],

 ["sarranid_nobleman","Sarranid Horseman","Sarranid Horsemans",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_sarranid_cavalry_sword,itm_sarranid_mace_1,itm_sarranid_two_handed_axe_b,itm_plate_covered_round_shield,itm_arabian_horse_a,
   itm_sarranid_helmet1,itm_sarranid_cavalry_robe,itm_leather_gloves,itm_sarranid_boots_b],
   def_swordsman|level(19),wp_melee(100),knows_riding_3|knows_shield_2|knows_ironflesh_2|knows_power_strike_2,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_nobleman_warrior","Sarranid Horseman","Sarranid Horsemans",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_arabian_sword_d,itm_lance,itm_sarranid_two_handed_axe_a,itm_tab_shield_small_round_b,itm_arabian_horse_a,itm_jarid,itm_lamellar_charger_y,
   itm_sarranid_mail_coif,itm_arab_mail_3,itm_leather_gloves,itm_mail_mittens,itm_sarranid_boots_c],
   def_guard|level(26),wp_melee(130),knows_riding_3|knows_shield_2|knows_ironflesh_2|knows_power_strike_2,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_nobleman_knight","Sarranid Horseman","Sarranid Horsemans",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_warhorse_sarranid,itm_jarid,itm_tab_shield_small_round_c,itm_heavy_lance,itm_sarranid_two_handed_axe_a,itm_scimitar_b,itm_sarranid_two_handed_mace_1,
   itm_sarranid_veiled_helmet,itm_sarranid_boots_d,itm_sarranid_elite_armor,itm_lamellar_gauntlets],
   def_knight|level(35),wp_melee(200),knows_riding_7|knows_shield_5|knows_ironflesh_6|knows_power_strike_8|knows_power_throw_7,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_nobleman_knight_archor","Sarranid Horseman","Sarranid Horsemans",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_barbed_arrows,itm_tab_shield_small_round_c,itm_strong_bow,itm_heavy_lance,itm_scimitar_b,
   itm_arab_mail_plate_3,itm_lamellar_charger_x,itm_sarranid_boots_c,itm_leather_gloves,itm_sarranid_royal_helmet],
   def_knight|level(35),wp_melee(200),knows_riding_8|knows_shield_5|knows_ironflesh_6|knows_power_strike_7|knows_power_draw_6,swadian_face_middle_1, swadian_face_older_2],
 #personal troop
 ["sarranid_king_guard","Sarranid Horseman","Sarranid Horsemans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_steel_shield,itm_sarranid_axe_b,itm_sarranid_two_handed_axe_a,itm_jarid,itm_jarid,
   itm_sarranid_elite_armor,itm_sarranid_boots_d,itm_lamellar_gauntlets,itm_dorn_immortal_helmet],
   def_knight_1|level(40),wp_melee(240),knows_riding_8|knows_shield_8|knows_ironflesh_8|knows_power_strike_9|knows_power_throw_8,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_camel_warrior","sarranid_camel_warrior","sarranid_camel_warrior",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_kingdom_6,
   [itm_camel1,itm_camel2,itm_sarranid_elite_round_spaulders,itm_sarranid_royal_helmet,itm_sarranid_boots_c,itm_jack_glamdring,itm_plate_covered_round_shield],
   str_25 | agi_19 | int_8 | cha_8|level(38),wp_melee(235),knows_riding_8|knows_shield_8|knows_ironflesh_8|knows_power_strike_8,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_desert_archer","Sarranid Master Archer","Sarranid Master Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_barbed_arrows,itm_barbed_arrows,itm_war_bow,itm_sarranid_two_handed_axe_a,itm_sarranid_mail_coif,itm_sarranid_cavalry_robe,itm_sarranid_boots_b],
   def_guard|level(30),wp(180),knows_power_draw_6|knows_ironflesh_6|knows_power_strike_6|knows_athletics_6,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_ghazis_warrior","sarranid_ghazis_warrior","sarranid_ghazis_warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_arab_mail_plate_3,itm_pa_sword_07,itm_sarranid_veiled_helmet,itm_sarranid_boots_d,itm_lamellar_gauntlets,itm_brass_shield1],
   def_knight|level(35),wp(235),knows_ironflesh_7|knows_power_strike_7|knows_athletics_7|knows_shield_7,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_ghulam","sarranid Ghulam","sarranid Ghulams",tf_mounted|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_kingdom_6,
   [itm_broigne_shirt_metal_ring,itm_arabian_sword_d,itm_sarranid_mail_coif,itm_sarranid_boots_c,itm_tab_shield_small_round_b,itm_spak_bow7,itm_barbed_arrows,itm_khergit_arrows,itm_arabian_horse_b],
   def_guard|level(30),wp(215),knows_ironflesh_6|knows_power_strike_6|knows_athletics_7|knows_riding_8|knows_power_draw_7|knows_horse_archery_7,swadian_face_middle_1, swadian_face_older_2],
 
 ["sarranid_wind_guard","sarranid_wind_guard","sarranid_wind_guard",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_6,
   [itm_dorn_sand_snakes_armor,itm_dorn_sand_snakes_helm,itm_dorn_sand_snakes_gauntles,itm_dorn_spearbearer_boots,itm_darksabre,itm_jarid],
   def_knight|level(35),wp(250),knows_ironflesh_6|knows_power_strike_8|knows_athletics_8|knows_power_throw_8,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_fire_guard","sarranid_fire_guard","sarranid_fire_guard",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_luc_celtic_sword,itm_wei_xiadi_kher_skirmisher_armor,itm_sarranid_mail_coif,itm_sarranid_boots_c,itm_fire_arrows,itm_fire_arrows,itm_leather_gloves,itm_spak_bow7],
   def_knight|level(35),wp(250),knows_ironflesh_7|knows_power_strike_7|knows_athletics_7|knows_power_draw_7,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_rock_guard","sarranid_rock_guard","sarranid_rock_guard",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_dorn_wiper,itm_sarranid_veiled_helmet,itm_dorn_spearbearer_guant,itm_dorn_spearbearer_boots,itm_steel_shield,itm_sarranid_axe_b,itm_luc_throwing_hammer],
   def_knight|level(35),wp(225),knows_ironflesh_8|knows_power_strike_6|knows_athletics_7|knows_power_throw_8,swadian_face_middle_1, swadian_face_older_2],
 ["sarranid_river_guard","sarranid_river_guard","sarranid_river_guard",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_kingdom_6,
   [itm_wei_xiadi_lamellar_armor03,itm_sarranid_royal_helmet,itm_sarranid_boots_d,itm_lamellar_charger_y,itm_arabian_sword_d,itm_brass_shield,itm_lamellar_gauntlets],
   def_knight|level(35),wp(250),knows_ironflesh_7|knows_power_strike_7|knows_athletics_7|knows_riding_7|knows_shield_7,swadian_face_middle_1, swadian_face_older_2],

 ["sarranid_patrol_leader","Sarranid Horseman","Sarranid Horsemans",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_warhorse_sarranid,itm_jarid,itm_tab_shield_small_round_c,itm_heavy_lance,itm_sarranid_two_handed_axe_a,itm_scimitar_b,
   itm_sarranid_veiled_helmet,itm_sarranid_boots_d,itm_sarranid_elite_armor,itm_lamellar_gauntlets,],
   def_champion|level(30),wp_melee(165),knows_riding_7|knows_shield_5|knows_ironflesh_5|knows_power_strike_6,swadian_face_middle_1, swadian_face_older_2],
  ["sarranid_flag_holder","Sarranid Horseman","Sarranid Horsemans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_sarranid_royal_helmet,itm_sarranid_boots_c,itm_mamluke_mail,itm_scale_gauntlets,itm_battle_flag_s],
   def_guard|level(25),wp_melee(160),knows_ironflesh_5|knows_power_strike_5|knows_athletics_4,swadian_face_middle_1, swadian_face_older_2],

 ["sarranid_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_sarranid_helmet1,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
 ["sarranid_deserter","Sarranid Deserter","Sarranid Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_mail_chausses,itm_desert_turban,itm_arabian_horse_a],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_arabian_sword_b,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_c,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_sarranid_horseman_helmet,itm_mail_boots,itm_iron_greaves,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],
  ["sarranid_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_arabian_sword_b,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_c, itm_sarranid_boots_d,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_sarranid_horseman_helmet,itm_mail_boots,itm_iron_greaves,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],

 ["calradic_recruit","Calradic Recruit","Calradic Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_7,
   [itm_scythe,itm_hatchet,itm_pickaxe,itm_sickle,itm_stones,
    itm_wrapping_boots,itm_tabard,itm_pelt_coat,itm_straw_hat],
   def_farmer|level(4),wp(60),knows_common|knows_athletics_1,bandit_face1, bandit_face2],
 ["calradic_footman","Calradic Footman","Calradic Footmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_7,
   [itm_spear,itm_wooden_shield,itm_falchion,
    itm_padded_leather_jco,itm_wrapping_boots,itm_nomad_boots,itm_gambeson,itm_leather_vest,itm_padded_coif,itm_fur_hat],
   def_footman|level(10),wp(75),knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_2|knows_athletics_1,bandit_face1, bandit_face2],
 ["calradic_trained_footman","Calradic Trained Footman","Calradic Trained Footman",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_javelin,itm_pike,itm_tab_shield_kite_a,itm_scimitar,itm_sword_medieval_b,itm_sword_medieval_b_small,
    itm_pointyhelm,itm_nomad_boots,itm_leather_boots,itm_padded_leather_jco,itm_broigne_shirt_spiked_leather,itm_segmented_helmet],
   def_fighter|level(14),wp(90),knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_2,bandit_face1, bandit_face2],
 ["calradic_heavy_infantry","calradic_heavy_infantry","Calradic Trained Footman",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_javelin,itm_jarid,itm_tab_shield_kite_c,itm_shield_kite_k,itm_mackie_godenak,itm_sword_medieval_c,itm_sword_medieval_c_long,
    itm_scale_gauntlets,itm_leather_boots,itm_scale_shirt,itm_kettlehat1],
   def_swordsman|level(20),wp(130),knows_ironflesh_4|knows_shield_2|knows_power_strike_3|knows_athletics_2|knows_power_throw_3,bandit_face1, bandit_face2],
  ["calradic_legionary","calradic_heavy_infantry","Calradic Trained Footman",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_jarid,itm_jarid,itm_tab_shield_kite_d,itm_awlpike_long,itm_sword_medieval_d_long,
    itm_splinted_leather_greaves,itm_tagancha_helm_a,itm_scale_gauntlets,itm_copy_rus_lamellar_a,itm_byzantion],
   str_19 | agi_14 | int_7 | cha_7|level(26),wp(160),knows_ironflesh_5|knows_shield_5|knows_power_strike_5|knows_athletics_3|knows_power_throw_5,bandit_face1, bandit_face2],
  ["calradic_horseman","Calradic Horseman","Calradic Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_7,
   [itm_javelin,itm_shield_kite_k,itm_sword_medieval_c,itm_sword_medieval_c_long,itm_lance,itm_steppe_horse,itm_hunter,
    itm_scale_gauntlets,itm_leather_boots,itm_scale_shirt,itm_kettlehat1],
   def_swordsman|level(20),wp(125),knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_2|knows_power_throw_3|knows_riding_4,bandit_face1, bandit_face2],
  ["calradic_cavalry","calradic_cavalry","Calradic Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_7,
   [itm_jarid,itm_jarid,itm_tab_shield_kite_d,itm_sword_medieval_d_long,itm_sword_medieval_c_long,itm_lance,
    itm_splinted_leather_greaves,itm_scale_gauntlets,itm_scale_mail,itm_byzantion,itm_2lamellar_charger,itm_3lamellar_charger],
   def_champion|level(25),wp(150),knows_ironflesh_4|knows_shield_2|knows_power_strike_4|knows_athletics_2|knows_power_throw_4|knows_riding_4,bandit_face1, bandit_face2],
  
  ["calradic_skirmisher","Calradic Footman","Calradic Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_tab_shield_kite_a,itm_falchion,itm_nomad_bow,itm_short_bow,itm_sword_medieval_b_small,itm_arrows,itm_arrows,
    itm_footman_helmet,itm_skullcap,itm_leather_armor,itm_padded_leather_jco,itm_wrapping_boots,itm_nomad_boots],
   def_fighter|level(16),wp_one_handed (60) | wp_two_handed (60) | wp_polearm (60) | wp_archery (90) | wp_crossbow (60) | wp_throwing (60),knows_common|knows_athletics_1|knows_power_draw_2,bandit_face1, bandit_face2],
  ["calradic_archer","Calradic Archer","Calradic Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_tab_shield_kite_b,itm_nomad_bow,itm_sword_medieval_c,itm_arrows,itm_barbed_arrows,
    itm_pointyhelm,itm_padded_leather,itm_broigne_shirt_leather_plate,itm_leather_boots,itm_nomad_boots],
   str_17 | agi_13 | int_7 | cha_7|level(23),wp_one_handed (80) | wp_two_handed (80) | wp_polearm (80) | wp_archery (110) | wp_crossbow (80) | wp_throwing (80),knows_ironflesh_2|knows_shield_1|knows_power_strike_2|knows_athletics_1|knows_power_draw_3,bandit_face1, bandit_face2],
  ["calradic_veteran_archer","Calradic Footman","Calradic Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_tab_shield_kite_d,itm_short_imperial_bow,itm_sword_medieval_c_long,itm_bastard_sword_a,itm_barbed_arrows,itm_bodkin_arrows,
    itm_kettlehat2,itm_kettlehat1,itm_kuyak_a,itm_leather_gloves,itm_rus_cav_boots],
   str_20 | agi_15 | int_7 | cha_7|level(28),wp_one_handed (100) | wp_two_handed (100) | wp_polearm (100) | wp_archery (150) | wp_crossbow (100) | wp_throwing (100),knows_ironflesh_5|knows_shield_2|knows_power_strike_3|knows_athletics_2|knows_power_draw_4,bandit_face1, bandit_face2],
  
  ["calradic_nobleman","Calradic Trained Footman","Calradic Trained Footman",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_javelin,itm_pike,itm_tab_shield_kite_b,itm_sword_medieval_b,
    itm_pointyhelm,itm_leather_boots,itm_broigne_shirt_leather_plate,itm_leather_gloves],
   def_swordsman|level(19),wp(100),knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_2|knows_power_throw_3,bandit_face1, bandit_face2],
  ["calradic_nobleman_warrior","Calradic Trained Footman","Calradic Trained Footman",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_kingdom_7,
   [itm_javelin,itm_jarid,itm_pike,itm_tab_shield_kite_d,itm_sword_medieval_c_long,
    itm_gnezdovo_helm_b,itm_kuyak_a,itm_rus_cav_boots,itm_scalecharger2w],
   def_guard|level(26),wp(130),knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_2|knows_power_throw_6,bandit_face1, bandit_face2],
  ["calradic_knight","Calradic Trained Footman","Calradic Trained Footman",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_kingdom_7,
   [itm_jarid,itm_jarid,itm_tab_shield_kite_d,itm_sword_medieval_d_long,
    itm_rus_splint_greaves,itm_scale_gauntlets,itm_copy_rus_scale,itm_tagancha_helm_b,itm_jewlw,itm_scalecharger3w],
   def_knight|level(34),wp(200),knows_ironflesh_6|knows_shield_2|knows_power_strike_7|knows_athletics_4|knows_riding_6|knows_power_throw_9,bandit_face1, bandit_face2],
  ["calradic_nobleman_archer","Calradic Footman","Calradic Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_tab_shield_kite_c,itm_short_imperial_bow,itm_sword_medieval_c_long,itm_bastard_sword_a,itm_barbed_arrows,itm_bodkin_arrows,
    itm_kettlehat2,itm_kettlehat1,itm_broigne_shirt_metal_plate,itm_leather_gloves,itm_rus_cav_boots],
   def_champion|level(28),wp(140),knows_ironflesh_4|knows_shield_2|knows_power_strike_4|knows_athletics_2|knows_power_draw_4,bandit_face1, bandit_face2],
  ["calradic_roaly_archer","Calradic Royal Guardian","Calradic Royal Guardian",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_tab_shield_kite_d,itm_imperial_bow,itm_sword_medieval_d_long,itm_barbed_arrows,itm_bodkin_arrows,
    itm_rus_splint_greaves,itm_col1_byzantion,itm_copy_rus_lamellar_b,itm_leather_gloves],
   def_knight|level(35),wp(220),knows_ironflesh_7|knows_shield_2|knows_power_strike_7|knows_athletics_5|knows_power_draw_7,bandit_face1, bandit_face2],
  
  ["calradic_varangian","Calradic Varangian","Calradic Varangians",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_7,
   [itm_jarid,itm_jarid,itm_tab_shield_kite_d,itm_sword_medieval_d_long,itm_long_axe_c,itm_rus_splint_greaves,itm_lamellar_gauntlets,itm_williamconquer,itm_norman_mask],
   def_knight|level(40),wp(280),knows_ironflesh_8|knows_shield_8|knows_power_strike_8|knows_athletics_8|knows_power_throw_10,nord_face_middle_1, nord_face_older_2],

  ["calradic_patrol_leader","calradic_patrol_leader","calradic_patrol_leaders",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_7,
   [itm_jarid,itm_jarid,itm_tab_shield_kite_d,itm_sword_medieval_d_long,
    itm_rus_splint_greaves,itm_scale_gauntlets,itm_copy_rus_scale,itm_tagancha_helm_b,itm_jewlw,itm_scalecharger3w],
   def_champion|level(30),wp_melee(175),knows_riding_7|knows_shield_5|knows_ironflesh_5|knows_power_strike_6,bandit_face1, bandit_face2],

  #just in case
  ["calradic_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_7,
   [itm_spear,itm_wooden_shield,itm_falchion,
    itm_padded_leather_jco,itm_wrapping_boots,itm_nomad_boots,itm_gambeson,itm_leather_vest,itm_padded_coif,itm_fur_hat,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["calradic_deserter","Sarranid Deserter","Sarranid Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
   [itm_spear,itm_wooden_shield,itm_falchion,
    itm_padded_leather_jco,itm_wrapping_boots,itm_nomad_boots,itm_gambeson,itm_leather_vest,itm_padded_coif,itm_fur_hat,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["calradic_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_jarid,itm_jarid,itm_tab_shield_kite_d,itm_awlpike_long,itm_sword_medieval_d_long,itm_sword_medieval_c_long,
    itm_splinted_leather_greaves,itm_tagancha_helm_a,itm_scale_gauntlets,itm_copy_rus_lamellar_a,itm_byzantion],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,bandit_face1, bandit_face2],
  ["calradic_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_7,
   [itm_jarid,itm_jarid,itm_tab_shield_kite_d,itm_awlpike_long,itm_sword_medieval_d_long,itm_sword_medieval_c_long,
    itm_splinted_leather_greaves,itm_tagancha_helm_a,itm_scale_gauntlets,itm_copy_rus_lamellar_a,itm_byzantion],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,bandit_face1, bandit_face2],
  #anar
  # ["anar_lower","Anar Recruit","Anar Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
  #  [itm_scythe,itm_hatchet,itm_maul,itm_sickle,itm_stones,itm_shirt,itm_linen_tunic,itm_short_tunic,itm_blue_tunic,itm_wrapping_boots],
  #  def_farmer|level(4),wp(60),knows_common|knows_athletics_1,bandit_face1, bandit_face2],
  # ["anar_footman","Anar Footman","Anar Footmans",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
  #  [itm_hunter_boots,itm_red_gambeson,itm_hide_boots,itm_woolen_hood,itm_falchion,itm_hunting_bow,itm_arrows,itm_wooden_shield],
  #  def_footman|level(9),wp(80),knows_shield_2|knows_ironflesh_1|knows_power_strike_1,bandit_face1, bandit_face2],

  # ["anar_soilder","Anar Soilder","Anar Soilders",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
  #  [itm_padded_leather_jco,itm_padded_leather,itm_leather_boots,itm_nomad_boots,itm_helmet_with_neckguard,itm_segmented_helmet,
  #  itm_sword_khergit_2,itm_sword_khergit_1,itm_hide_covered_round_shield,itm_fur_covered_shield],
  #  str_13 | agi_10 | int_6 | cha_6|level(14),wp(100),knows_shield_2|knows_ironflesh_2|knows_power_strike_2,bandit_face1, bandit_face2],
  # ["anar_veteran_soilder","Anar Veteran Soilder","Anar Veteran Soilders",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
  #  [itm_leather_armor_padded,itm_broigne_shirt_spiked_leather,itm_studded_leather_coat,itm_splinted_leather_greaves,itm_bascinet_coif_01,
  #  itm_sword_khergit_3,itm_khergit_sword_two_handed_a,itm_leather_covered_round_shield,itm_plate_covered_round_shield,itm_scimitar],
  #  def_swordsman|level(20),wp(120),knows_shield_3|knows_ironflesh_3|knows_power_strike_4,bandit_face1, bandit_face2],

  # ["anar_archer","Anar Archer","Anar Archers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
  #  [itm_red_gambeson,itm_hood_b,itm_hood_c,itm_hood_d,itm_light_leather_boots,itm_nomad_boots,itm_sword_khergit_2,itm_short_bow,itm_arrows,itm_barbed_arrows],
  #  def_fighter|level(15),wp_archery(120) |wp(80),knows_power_draw_2|knows_ironflesh_1|knows_power_strike_1,bandit_face1, bandit_face2],
  # ["anar_veteran_archer","Anar Veteran Archer","Anar Veteran Archers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
  #  [itm_light_mail_and_plate,itm_black_hood,itm_light_leather_boots,itm_leather_boots,itm_sword_khergit_3,itm_long_bow,itm_arrows,itm_barbed_arrows],
  #  def_swordsman|level(21),wp_archery(135) |wp(95),knows_power_draw_3|knows_ironflesh_3|knows_power_strike_2,bandit_face1, bandit_face2],

  ["anar_nobleman","anar_nobleman","anar_nobleman",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_8,
   [itm_riv_leather,itm_riv_leather_cloak,itm_new_leather_boots,itm_helmet_tully_archer_new_2,itm_lorien_kite_small,itm_gondor_spear,itm_scimitar,itm_leather_gauntlets_new],
   def_swordsman|level(20),wp(140),knows_ironflesh_4|knows_shield_3|knows_power_strike_3|knows_athletics_3|knows_riding_5,west_face_younger_1, west_face_middle_2],
  ["anar_ranger","anar Ranger","anar Rangers",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_8,
   [itm_arnor_ranger_b,itm_arnor_ranger,itm_arnor_splinted,itm_arnor_hood,itm_elf_spear_2,itm_long_bow,itm_bodkin_arrows,itm_barbed_arrows,itm_blackleather_gloves],
   def_champion|level(30),wp(180),knows_ironflesh_5|knows_power_strike_5|knows_athletics_6|knows_power_draw_4,west_face_younger_1, west_face_middle_2],
  ["anar_shadow_walker","anar Shadow Walker","anar Shadow Walkers",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_8,
   [itm_dorn_knight_helmet_black_b,itm_riv_surcoat_a_cloak,itm_elfbow,itm_bodkin_arrows,itm_bow4_arr_spak,itm_rus_cav_boots_black,itm_dorn_spearbearer_guant,itm_jack_sting,itm_jack_faramir],
   def_knight|level(35),wp(225),knows_ironflesh_6|knows_power_strike_6|knows_athletics_7|knows_power_draw_7,west_face_younger_1, west_face_middle_2],
  ["anar_shadow_walker_master","anar Shadow Walker","anar Shadow Walkers",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_8,
   [itm_dorn_knight_helmet_black_c,itm_riv_surcoat_b_cloak,itm_rivendellbow,itm_bow4_arr_spak,itm_bow4_arr_spak,itm_rus_cav_boots_black,itm_dorn_spearbearer_guant,itm_jack_glamdring],
   def_knight_1|level(40),wp(260),knows_ironflesh_7|knows_power_strike_8|knows_athletics_9|knows_power_draw_9,west_face_younger_1, west_face_middle_2],
  
  ["anar_silver_rider","Anar Silver Rider","Anar Silver Riders",tf_mounted|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_kingdom_8,
   [itm_elf_spear_2,itm_rivendellarcherhelmet,itm_riv_foot_scale_b_cloak,itm_rus_cav_boots_black,itm_courser,itm_pa_sword_03,itm_lorien_kite,itm_leather_gauntlets_new],
   def_champion|level(30),wp(180),knows_ironflesh_6|knows_power_strike_7|knows_athletics_6|knows_riding_5|knows_shield_5,west_face_younger_1, west_face_middle_2],
  ["anar_silver_knight","Anar Silver Knight","Anar Silver Knights",tf_mounted|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_kingdom_8,
   [itm_elf_spear_2,itm_rivendellswordfighterhelmet,itm_riv_knight_a_cloak,itm_rus_cav_boots_black,itm_ak_courser,itm_pa_sword_02,itm_lorien_kite,itm_leather_gauntlets_new],
   def_knight|level(35),wp(230),knows_ironflesh_7|knows_power_strike_8|knows_athletics_6|knows_riding_8|knows_shield_7,west_face_younger_1, west_face_middle_2],

  ["anar_fnobleman","anar_fnobleman","anar_fnobleman",tf_beautiful|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_8,
   [itm_riv_light,itm_riv_light_cloak,itm_new_leather_boots,itm_tiara,itm_silver_lorien_round_shield,itm_scimitar,itm_strong_bow,itm_bow3_arr_spak],
   def_swordsman|level(24),wp(175),knows_ironflesh_4|knows_shield_3|knows_power_strike_4|knows_athletics_3|knows_power_draw_4,beauty_face1, beauty_face_anar2],
  ["anar_fnobleman_archer","anar_fnobleman_archer","anar_fnobleman_archer",tf_beautiful|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_kingdom_8,
   [itm_riv_foot_mail_b_cloak,itm_rus_cav_boots_black,itm_tiara,itm_silver_lorien_round_shield,itm_scimitar_b,itm_arrows_ghost,itm_war_bow_ghost],
   def_swordsman|level(33),wp(205),knows_ironflesh_5|knows_shield_4|knows_power_strike_5|knows_athletics_5|knows_power_draw_4|knows_reserved_5_6|knows_reserved_6_6,beauty_face1, beauty_face_anar2],
  ["anar_fnobleman_archer_e","anar_fnobleman_archer_e","anar_fnobleman_archer_e",tf_beautiful|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_kingdom_8,
   [itm_riv_foot_scale_b_cloak,itm_rus_cav_boots_black,itm_tiara,itm_silver_lorien_round_shield,itm_pa_sword_07,itm_arrows_ghost,itm_war_bow_ghost_1],
   def_swordsman|level(38),wp(235),knows_ironflesh_6|knows_shield_6|knows_power_strike_6|knows_athletics_7|knows_power_draw_4|knows_reserved_5_8|knows_reserved_6_8,beauty_face1, beauty_face_anar2],

  ["anar_fnobleman_sword","anar_fnobleman_sword","anar_fnobleman_sword",tf_beautiful|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_8,
   [itm_riv_foot_mail_b_cloak,itm_rus_cav_boots_black,itm_tiara,itm_tiara_green,itm_tiara_new,itm_tiara_new1,itm_silver_lorien_kite_small,itm_pa_sword_ghost],
   def_swordsman|level(30),wp(200),knows_ironflesh_5|knows_shield_6|knows_power_strike_5|knows_athletics_7|knows_reserved_5_6|knows_reserved_6_5,beauty_face1, beauty_face_anar2],
  ["anar_fnobleman_sword_e","anar_fnobleman_sword_e","anar_fnobleman_sword_e",tf_beautiful|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_8,
   [itm_riv_foot_scale_b_cloak,itm_rus_cav_boots_black,itm_tiara,itm_tiara_green,itm_tiara_new,itm_tiara_new1,itm_silver_lorien_kite,itm_pa_sword_ghost_1],
   def_swordsman|level(36),wp(250),knows_ironflesh_6|knows_shield_7|knows_power_strike_6|knows_athletics_9|knows_reserved_5_8|knows_reserved_6_7,beauty_face1, beauty_face_anar2],

  ["anar_patrol_leader","Anar patrol leader","Anar patrol leaders",tf_beautiful|tf_mounted|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_kingdom_8,
   [itm_elf_spear_2,itm_rivendellarcherhelmet,itm_riv_foot_scale_b_cloak,itm_rus_cav_boots_black,itm_courser,itm_pa_sword_03,itm_lorien_kite,itm_leather_gauntlets_new],
   def_champion|level(30),wp(180),knows_ironflesh_6|knows_power_strike_6|knows_athletics_6|knows_riding_5|knows_shield_6,beauty_face1, beauty_face_anar2],

  ["anar_silver_soilder","Anar Silver Soilder","Anar Silver Soilders",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_8,
   [itm_elf_spear_2,itm_rivendellarcherhelmet,itm_riv_foot_scale_b_cloak,itm_rus_cav_boots_black,itm_lorien_kite,itm_leather_gauntlets_new],
   def_champion|level(30),wp(180),knows_ironflesh_6|knows_power_strike_6|knows_athletics_6|knows_shield_6,west_face_younger_1, west_face_middle_2],

  ["anar_executioner","anar_executioner","anar_executioner",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_8,
   [itm_dorn_knight_armor_black,itm_dorn_spearbearer_boots,itm_dorn_spearbearer_guant,itm_dorn_knight_helmet_black,itm_jack_anduril],
   def_knight_2|level(45),wp(275),knows_ironflesh_9|knows_power_strike_10|knows_athletics_10,west_face_younger_1, west_face_middle_2],
  ["anar_sword_dancer","anar_sword_dancer","anar_sword_dancer",tf_beautiful|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_8,
   [itm_xena_boots,itm_xena_armor,itm_pa_sword_03,itm_pa_sword_03_shield],
   def_knight_1|level(40),wp(300),knows_ironflesh_10|knows_power_strike_10|knows_athletics_12,beauty_face1, beauty_face_anar2],
  ["anar_sword_dancer1","anar_sword_dancer1","anar_sword_dancer1",tf_beautiful|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [itm_xena_boots,itm_anar2_dress1,itm_pa_sword_04],
   def_knight_1|level(40),wp(300),knows_ironflesh_10|knows_power_strike_10|knows_athletics_12,beauty_face1, beauty_face_anar2],
  ["anar_sword_dancer2","anar_sword_dancer2","anar_sword_dancer2",tf_beautiful|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [itm_rus_cav_boots_black,itm_riv_foot_scale_b_cloak,itm_pa_sword_02,itm_dec_steel_shield],
   def_knight_1|level(40),wp(270),knows_ironflesh_8|knows_power_strike_8|knows_athletics_5|knows_shield_9,beauty_face1, beauty_face_anar2],
  ["anar_sword_dancer3","anar_sword_dancer3","anar_sword_dancer3",tf_beautiful|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_8,
   [itm_dorn_knight_boots_gold,itm_rivendellrewardarmour,itm_pa_sword_07,itm_sh3,itm_dorn_knight_helmet_gold_a,itm_dorn_knight_helmet_gold_b],
   def_knight_1|level(40),wp(255),knows_ironflesh_8|knows_power_strike_6|knows_athletics_5|knows_shield_9,beauty_face1, beauty_face_anar2],

  ["anar_archer_knight","anar_archer_knight","anar_archer_knight",tf_mounted|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_8,
   [itm_helmet_north_clanman,itm_elf_spear_2,itm_pa_sword_03,itm_armour_tyrell_rider,itm_rus_cav_boots_black,itm_wlong3,itm_lorien_kite_small,itm_leather_gauntlets_new,itm_elfbow,itm_bow4_arr_spak],
   def_knight|level(35),wp(225),knows_ironflesh_7|knows_power_strike_7|knows_athletics_7|knows_riding_7|knows_horse_archery_7|knows_power_draw_7|knows_shield_7,beauty_face1, beauty_face_anar2],
  ["anar_archer_knight_e","anar_archer_knight","anar_archer_knights",tf_mounted|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_8,
   [itm_rivendellswordfighterhelmet,itm_elf_spear_2,itm_pa_sword_02,itm_armour_tyrell_rider_black,itm_rus_cav_boots_black,itm_wlong3,itm_lorien_kite_small,itm_dorn_spearbearer_guant,itm_rivendellbow,itm_bow4_arr_spak],
   def_knight_2|level(45),wp(275),knows_ironflesh_9|knows_power_strike_9|knows_athletics_9|knows_riding_9|knows_horse_archery_9|knows_power_draw_9|knows_shield_9,beauty_face1, beauty_face_anar2],
  ["blood_wolf","blood_wolf","blood_wolf",tf_tall|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_kingdom_8,
   [itm_platemail_harness_05,itm_steel_boots_01,itm_leduc_closed,itm_henrysword,itm_steel_mittens,itm_toumao],
   def_lord|level(50),wp(350),knows_ironflesh_10|knows_power_strike_10|knows_athletics_12|knows_power_throw_12,nord_face_young_1, nord_face_old_2],
  #new culture#askr are first new calture
  ["askr_recruit","Askr Recruit","Askr Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_askr,
   [itm_club,itm_stones,itm_cudgel,itm_wooden_stick,itm_arrows,itm_hunting_bow,itm_arrows,itm_arrows,
    itm_hunter_boots,itm_steppe_armor,itm_nomad_vest,itm_northerner_horse],
   def_farmer|level(4),wp(70),knows_common|knows_athletics_1|knows_riding_2,nord_face_middle_1, nord_face_older_2],
  ["askr_hunter","Askr Hunter","Askr Hunters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_askr,
   [itm_wooden_shield,itm_hatchet,itm_rhun_shortsword,itm_club,itm_hunting_bow,itm_arrows,itm_arrows,itm_sh_oval,
    itm_northmen_light_b1,itm_nomad_cap_b,itm_northmen_light_b2,itm_nomad_cap,itm_hide_boots,itm_northerner_horse_black,itm_northerner_horse],
   def_footman|level(10),wp(85),knows_ironflesh_1|knows_shield_1|knows_power_strike_2|knows_athletics_1|knows_power_draw_1|knows_riding_3|knows_horse_archery_1,nord_face_middle_1, nord_face_older_2],
  ["askr_skirmisher","Askr skirmisher","Askr skirmishers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_askr,
   [itm_rhun_shortsword,itm_mackie_bat,itm_short_bow,itm_nomad_bow,itm_arrows,itm_arrows,itm_sh_oval,
    itm_northmen_light_a3_cloak,itm_mongol_helmet_xc,itm_hide_boots,itm_northerner_horse_black,itm_northerner_horse_white],
   str_15 | agi_11 | int_6 | cha_6|level(17),wp(105),knows_ironflesh_3|knows_shield_1|knows_power_strike_2|knows_athletics_1|knows_power_draw_2|knows_riding_4|knows_horse_archery_3,nord_face_middle_1, nord_face_older_2],
  ["askr_archer","Askr archer","Askr archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_askr,
   [itm_rhun_sword,itm_mackie_bat,itm_nomad_bow,itm_mongol_bow_x,itm_arrows,itm_arrows,itm_sh_oval,
    itm_northmen_light_a3_cloak,itm_northmen_light_a3_cloak,itm_mongol_helmet_xc,itm_nomad_boots,itm_stark_hanter_boots,itm_northerner_horse_white,itm_northerner_horse_hunter],
   str_17 | agi_13 | int_7 | cha_7|level(23),wp(125),knows_ironflesh_3|knows_shield_1|knows_power_strike_4|knows_athletics_3|knows_power_draw_3|knows_riding_5|knows_horse_archery_4,nord_face_middle_1, nord_face_older_2],
  ["askr_veteran_archer","Askr veteran archer","Askr veteran archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_askr,
   [itm_rhun_sword,itm_mackie_bat_nailed,itm_rhun_battle_axe,itm_long_bow,itm_mongol_bow_x,itm_arrows,itm_arrows,itm_sh_oval,
    itm_northmen_light_a3_cloak,itm_northmen_med_a1_cloak,itm_mongol_helmet_xa,itm_stark_hanter_boots,itm_bear_warior_helm,itm_northerner_horse_white,itm_northerner_horse_hunter],
   str_21 | agi_14 | int_7 | cha_7|level(28),wp(150),knows_ironflesh_5|knows_shield_1|knows_power_strike_5|knows_athletics_5|knows_power_draw_4|knows_riding_7|knows_horse_archery_6,nord_face_middle_1, nord_face_older_2],

  ["askr_axeman","Askr Axeman","Askr Axeman",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_askr,
   [itm_mackie_double_axe,itm_fighting_axe,itm_axe,itm_sh_oval,itm_sh_oval,itm_northerner_horse,itm_northerner_horse_black,
    itm_northmen_light_a2,itm_northmen_light_b2,itm_mongol_helmet_xc,itm_nomad_cap,itm_hide_boots],
   def_fighter|level(15),wp(100),knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_2|knows_riding_3,nord_face_middle_1, nord_face_older_2],
  ["askr_warrior","Askr warrior","Askr Warrior",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_askr,
   [itm_lightedge_spak,itm_rhun_sword,itm_battle_axe,itm_sh_oval,itm_sh_oval,itm_northerner_horse_black,itm_northerner_horse_white,
    itm_northmen_light_a1,itm_northmen_med_a2,itm_mongol_helmet_xd,itm_mongol_helmet_x,itm_hide_boots],
   def_swordsman|level(20),wp(140),knows_ironflesh_3|knows_shield_2|knows_power_strike_4|knows_athletics_3|knows_riding_4,nord_face_middle_1, nord_face_older_2],
  ["askr_guard","Askr guard","Askr guard",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_askr,
   [itm_rhun_sword,itm_rhun_greatfalchion,itm_rhun_battle_axe,itm_sh_oval,itm_sh_oval,itm_rhun_falchion,itm_northerner_horse_hunter,itm_northerner_horse_white,
    itm_northmen_med_a1,itm_northmen_light_a1,itm_mongol_helmet_xa1,itm_nomad_boots,itm_wolf_helm4],
   def_guard|level(25),wp(170),knows_ironflesh_4|knows_shield_2|knows_power_strike_6|knows_athletics_5|knows_riding_6,nord_face_middle_1, nord_face_older_2],
  ["askr_champion","Askr champion","Askr champion",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_askr,
   [itm_rhun_battle_axe,itm_rhun_greatsword,itm_rhun_glaive,itm_sh_oval,itm_sh_oval,itm_luc_axe_knight_z,itm_northerner_horse_hunter,itm_yak2,itm_yak3,
    itm_northmen_med_a1_pelt,itm_mongol_helmet_xb,itm_stark_hanter_boots,itm_wolf_helm4],
   def_champion|level(30),wp(215),knows_ironflesh_7|knows_shield_2|knows_power_strike_7|knows_athletics_7|knows_riding_8,nord_face_middle_1, nord_face_older_2],
#nobleman
  ["askr_nobleman","Askr nobleman","Askr nobleman",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_tall,0,0,fac_askr,
   [itm_luc_axe_knight_z,itm_battle_axe,itm_two_handed_axe,itm_sh_oval,itm_northerner_horse_black,
    itm_northmen_light_a3_cloak,itm_northmen_light_a1_cloak,itm_wolf_helm4,itm_hide_boots,itm_bear_warior_helm],
   def_swordsman|level(20),wp(150),knows_ironflesh_3|knows_shield_2|knows_power_strike_4|knows_athletics_3,nord_face_middle_1, nord_face_older_2],
  ["askr_nobleman_warrior","Askr nobleman warrior","Askr nobleman warrior",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_tall|tf_guarantee_horse,0,0,fac_askr,
   [itm_luc_axe_knight_z,itm_luc_two_handed_axe_2,itm_two_handed_battle_axe_2,itm_wolf_helm1,itm_wolf_helm3,itm_bear_warior_helm,itm_wolf_helm4,itm_sh_oval,itm_northerner_horse_hunter,
    itm_northmen_med_a1_pelt,itm_northmen_light_a1_cloak,itm_northmen_med_a1_cloak,itm_stark_hanter_boots,itm_bear_warior_helm,itm_wolf_helm4],
   def_champion|level(30),wp(200),knows_ironflesh_6|knows_shield_2|knows_power_strike_6|knows_athletics_6|knows_riding_4,nord_face_middle_1, nord_face_older_2],
  ["askr_nobleman_knight","Askr knight","Askr knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_tall,0,0,fac_askr,
   [itm_luc_axe_knight_z,itm_rhun_greatsword,itm_rhun_glaive,itm_luc_two_handed_axe_2,itm_sh_oval,itm_copy_bear,
    itm_bear_warrior,itm_bear_boots,itm_beargauntlets,itm_wolf_helm1,itm_wolf_helm3],
   def_knight_1|level(39),wp(275),knows_ironflesh_8|knows_shield_2|knows_power_strike_8|knows_athletics_8|knows_riding_6,nord_face_middle_1, nord_face_older_2],

  ["askr_warchief","Askr Warchief","Askr warchiefs",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_tall|tf_guarantee_shield,0,0,fac_askr,
   [itm_luc_axe_knight_z,itm_luc_two_handed_axe_2,itm_sh_oval,itm_northerner_horse_hunter,itm_bear_warrior_b,itm_black_greaves,itm_beargauntlets,itm_mongol_helmet_xb,itm_throwing_spears],
   def_lord|level(50),wp(400),knows_ironflesh_10|knows_shield_8|knows_power_strike_10|knows_athletics_9|knows_riding_11|knows_power_throw_11|knows_horse_archery_6,nord_face_middle_1, nord_face_older_2],
  ["onsved_knight","onsved_knight","onsved_knight",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_tall|tf_allways_fall_dead,0,0,fac_askr,
   [itm_rhun_greatsword,itm_luc_axe_knight_z,itm_sh_oval,itm_toumao,itm_charger_plate_1,
    itm_bear_warrior_b,itm_black_greaves,itm_blackgauntlets,itm_valhelm_c],
   str_65 | agi_25 | int_10 | cha_10|level(50),wp(325),knows_ironflesh_10|knows_shield_5|knows_power_strike_10|knows_athletics_10|knows_riding_10,nord_face_middle_1, nord_face_older_2],
  ["askr_wolf_guard","Askr wolf guard","Askr wolf guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_askr,
   [itm_rhun_greatsword,itm_northmen_med_a1_pelt,itm_wolf_helm3,itm_stark_hanter_boots],
   def_knight|level(35),wp(250),knows_ironflesh_8|knows_shield_2|knows_power_strike_8|knows_athletics_8,nord_face_middle_1, nord_face_older_2],
  ["askr_strong_warrior","askr_strong_warrior","askr_strong_warriors",tf_tall|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_askr,
   [itm_long_axe_c,itm_nomad_stripped_armor,itm_sp_helm1,itm_black_greaves],
   str_35 | agi_25 | int_10 | cha_10|level(45),wp(350),knows_ironflesh_12|knows_shield_2|knows_power_strike_12|knows_athletics_12,nord_face_middle_1, nord_face_older_2],
  ["askr_horse_warrior","askr_horse_warrior","askr_horse_warriors",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_askr,
   [itm_helm07,itm_kuyak_a,itm_stark_hanter_boots,itm_northerner_horse_hunter,itm_northerner_horse_white,itm_amazon_bow,itm_spak_bow7,itm_arrows,itm_arrows,itm_fur_covered_shield,itm_lance,itm_rhun_glaive],
   def_knight_1|level(40),wp(270),knows_ironflesh_8|knows_power_draw_8|knows_power_strike_9|knows_athletics_5|knows_horse_archery_9|knows_riding_8,nord_face_middle_1, nord_face_older_2],
  ["arbal_guard","arbal_guard","arbal_guard",tf_tall|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_askr,
   [itm_mail_boots,itm_barbar_body,itm_valhelm_f,itm_pa_axe_02],
   str_75 | agi_55 | int_10 | cha_10|level(65),wp(400),knows_ironflesh_12|knows_power_strike_12|knows_athletics_12,nord_face_middle_1, nord_face_older_2],

  ["askr_patrol_leader","askr_patrol_leader","askr_patrol_leader",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_tall|tf_guarantee_horse,0,0,fac_askr,
   [itm_luc_axe_knight_z,itm_luc_two_handed_axe_2,itm_wolf_helm3,itm_sh_oval,itm_northerner_horse_hunter,
    itm_bear_warrior,itm_bear_boots,itm_beargauntlets],
   def_champion|level(30),wp(180),knows_ironflesh_6|knows_shield_2|knows_power_strike_6|knows_athletics_6|knows_riding_4,nord_face_middle_1, nord_face_older_2],

###
  ["askr_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_askr,
   [itm_spear,itm_wooden_shield,itm_falchion,
    itm_padded_leather_jco,itm_wrapping_boots,itm_nomad_boots,itm_gambeson,itm_leather_vest,itm_padded_coif,itm_fur_hat,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,nord_face_middle_1, nord_face_older_2],
  ["askr_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_askr,
   [itm_luc_axe_knight_z,itm_sh_oval,itm_bear_warrior,itm_bear_boots,itm_beargauntlets,itm_mongol_helmet_xb],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,nord_face_middle_1, nord_face_older_2],
  ["askr_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_askr,
   [itm_rhun_greatsword,itm_bear_warrior,itm_bear_boots,itm_beargauntlets,itm_wolf_helm1,itm_wolf_helm3],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,nord_face_middle_1, nord_face_older_2],
#fac_gulfod_theocracy
  ["gulfod_citizen","Gulfod citizen","Gulfod citizens",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_gulfod_theocracy,
   [itm_sword_medieval_b_small,itm_ankle_boots,itm_linen_tunic,itm_headcloth,itm_hosen_brown,itm_staff],
   def_farmer|level(4),wp(60),knows_common|knows_athletics_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["gulfod_militia","Gulfod militia","Gulfod militias",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_gulfod_theocracy,
   [itm_light_leather_boots,itm_aketon_green,itm_gambeson,itm_arming_cap,itm_padded_coif,
   itm_military_fork,itm_sarranid_mace_1,itm_light_lance,itm_hammer,],
   def_footman|level(10),wp(70),knows_ironflesh_1|knows_shield_1|knows_power_strike_2|knows_athletics_1|knows_power_draw_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["gulfod_footman","Gulfod footman","Gulfod footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_gulfod_theocracy,
   [itm_new_leather_boots,itm_mail_coif,itm_mercenary_studded_leather_jacket,itm_leather_armor_padded,itm_leather_gauntlets_new,itm_chapel_de_fer_cloth1,itm_chapel_de_fer_cloth2,
   itm_plate_covered_round_shield,itm_maul,itm_spiked_mace],
   def_fighter|level(15),wp(100),knows_ironflesh_3|knows_shield_1|knows_power_strike_2|knows_athletics_1|knows_power_draw_2,rhodok_face_middle_1, rhodok_face_older_2],
  ["gulfod_soldier","Gulfod soldier","Gulfod soldiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_gulfod_theocracy,
   [itm_dorn_spearbearer_guant,itm_chapel_de_fer_mail3,itm_chapel_de_fer_mail2,itm_rus_cav_boots,itm_mail_long_surcoat_new_e,
   itm_luc_knightly_hammer,itm_steel_shield,itm_battle_axe,itm_luc_knightly_axe_one_handed],
   def_swordsman|level(21),wp(125),knows_ironflesh_3|knows_shield_1|knows_power_strike_4|knows_athletics_3|knows_power_draw_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["gulfod_heavy_soldier","Gulfod Heavy soldier","AGulfod Heavy soldiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_gulfod_theocracy,
   [itm_ned_stark_armor,itm_steel_gauntlets,itm_sallet_a_open1,itm_sallet_a_open2,itm_dorn_spearbearer_boots,itm_bec_de_corbin_a,itm_poleaxe,itm_luc_partisan],
   str_19 | agi_15 | int_7 | cha_7|level(27),wp(150),knows_ironflesh_5|knows_shield_1|knows_power_strike_5|knows_athletics_5|knows_power_draw_4,rhodok_face_middle_1, rhodok_face_older_2],
  
  ["gulfod_militia_skirmisher","Gulfod militia skirmisher","Gulfod militia skirmishers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_gulfod_theocracy,
   [itm_bolts,itm_light_crossbow,itm_luc_hafted_blade_1,itm_sarranid_mace_1,itm_light_lance,itm_wooden_shield,itm_one_handed_war_axe_a,
   itm_leather_gauntlets_new,itm_new_leather_boots,itm_aketon_green,itm_skullcap,],
   str_15 | agi_11 | int_5 | cha_5|level(17),wp(105),knows_ironflesh_3|knows_shield_1|knows_power_strike_2|knows_athletics_1|knows_power_draw_2,rhodok_face_middle_1, rhodok_face_older_2],
  ["gulfod_musketeer","Gulfod musketeer","Gulfod musketeers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_gulfod_theocracy,
   [itm_cartridges,itm_flintlock_pistol,itm_luc_hafted_blade_4,itm_one_handed_war_axe_b,itm_tab_shield_round_c,itm_leather_covered_round_shield,
   itm_chapel_de_fer_cloth1,itm_new_leather_boots,itm_leather_armor_padded,itm_chapel_de_fer_cloth1,itm_combed_morion,itm_sallet_d,itm_chapel_de_fer_cloth3],
   str_17 | agi_14 | int_7 | cha_7|level(24),wp(125),knows_ironflesh_3|knows_shield_1|knows_power_strike_4|knows_athletics_3|knows_power_draw_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["gulfod_veteran_musketeer","Gulfod veteran musketeer","Gulfod veteran musketeers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_gulfod_theocracy,
   [itm_cartridges,itm_flintlock_rifle,itm_luc_knightly_axe_one_handed,itm_plate_covered_round_shield,
   itm_cuirass_on_white,itm_sallet_a_open2,itm_leather_gauntlets_new,itm_new_leather_boots,itm_combed_morion],
   def_champion|level(30),wp(170),knows_ironflesh_5|knows_shield_1|knows_power_strike_5|knows_athletics_5|knows_power_draw_4,rhodok_face_middle_1, rhodok_face_older_2],

  ["gulfod_musketeer_cavalry","Gulfod veteran musketeer","Gulfod veteran musketeers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_gulfod_theocracy,
   [itm_cartridges,itm_flintlock_pistol,itm_luc_knightly_axe_one_handed,itm_steel_shield,
   itm_cuirass_on_black,itm_sallet_c,itm_sallet_c_bevor,itm_leather_gauntlets_new,itm_steel_greaves2,itm_hunter],
   def_champion|level(30),wp(170),knows_ironflesh_5|knows_shield_1|knows_power_strike_5|knows_athletics_5|knows_power_draw_4,rhodok_face_middle_1, rhodok_face_older_2],
  
  ["gulfod_nobleman_warrior1","Gulfod nobleman warrior","Gulfod nobleman warrior",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_gulfod_theocracy,
   [itm_cartridges,itm_ned_stark_armor,itm_sallet_b_closed2,itm_sallet_b_open2,itm_dorn_spearbearer_guant,itm_dorn_spearbearer_boots,itm_luc_knightly_axe_one_handed,itm_steel_shield,itm_flintlock_pistol,itm_flintlock_rifle],
   def_champion|level(29),wp(175),knows_ironflesh_6|knows_shield_2|knows_power_strike_6|knows_athletics_6|knows_riding_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["gulfod_nobleman_knight1","Gulfod knight","Gulfod knight",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_gulfod_theocracy,
   [itm_cartridges,itm_cartridges,itm_sallet_b_closed1,itm_sallet_b_closed2,itm_marmont_armor,itm_dorn_spearbearer_boots,itm_dorn_spearbearer_guant,itm_luc_knightly_axe_two_handed,itm_long_rifle],
   def_knight_1|level(38),wp(235),knows_ironflesh_8|knows_shield_2|knows_power_strike_8|knows_athletics_8|knows_riding_6,rhodok_face_middle_1, rhodok_face_older_2],
  
  ["gulfod_nobleman","Gulfod nobleman","Gulfod nobleman",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_gulfod_theocracy,
   [itm_eyeslot_kettlehat,itm_new_leather_boots,itm_leather_armor_padded,itm_cuirass_on_white,itm_luc_knightly_axe_one_handed,itm_steel_shield,itm_courser],
   def_swordsman|level(19),wp(100),knows_ironflesh_3|knows_shield_2|knows_power_strike_4|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["gulfod_nobleman_warrior","Gulfod nobleman warrior","Gulfod nobleman warrior",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_gulfod_theocracy,
   [itm_coat_of_plates_f,itm_chapel_de_fer_mail3,itm_demi_gauntlets,itm_steel_greaves2,itm_warhorse,itm_luc_knightly_axe_one_handed,itm_steel_shield,itm_lance_1],
   str_20 | agi_14 | int_7 | cha_7|level(27),wp(160),knows_ironflesh_5|knows_shield_5|knows_power_strike_5|knows_athletics_5|knows_riding_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["gulfod_nobleman_knight","Gulfod knight","Gulfod knight",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_gulfod_theocracy,
   [itm_steel_greaves,itm_finger_gauntlets,itm_gothic_plate,itm_sallet_02,itm_wplatedcharger7,itm_lance_1,itm_ganquang_axe,itm_steel_shield,itm_luc_flanged_mace_iron,itm_luc_knightly_axe_two_handed],
   def_knight|level(35),wp(180),knows_ironflesh_7|knows_shield_7|knows_power_strike_7|knows_athletics_7|knows_riding_7,rhodok_face_middle_1, rhodok_face_older_2],
  
  ["gulfod_nblack_knight","Gulfod knight","Gulfod knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_gulfod_theocracy,
   [itm_gothic_plate_black,itm_blackgauntlets,itm_sallet_b_closed1,itm_sallet_b_closed2,itm_black_greaves,itm_wplatedcharger9,itm_pistol,itm_cartridges,itm_cartridges,itm_lightedge_spak_black],
   def_knight_2|level(45),wp(255),knows_ironflesh_9|knows_shield_8|knows_power_strike_8|knows_athletics_8|knows_riding_10|knows_horse_archery_5,rhodok_face_middle_1, rhodok_face_older_2],
  
  ["sun_knight","Sun knight","Sun knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_gulfod_theocracy,
   [itm_henryv_helm_black,itm_agincourt_plate_black,itm_blackgauntlets,itm_spak_charger_plate,itm_black_greaves,itm_jack_glamdring,itm_sh3,itm_lance_1],
   def_lord_2|level(50),wp(285),knows_ironflesh_12|knows_shield_8|knows_power_strike_9|knows_athletics_8|knows_riding_9,rhodok_face_middle_1, rhodok_face_older_2],
  ["holy_judge","Judge","Judges",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_gulfod_theocracy,
   [itm_gothic_plate_silver,itm_pa_sword_03_shield,itm_dorn_knight_boots,itm_dorn_knight_gant,itm_holy_holo,itm_pa_maul_02],
   def_lord_2|level(50),wp(300),knows_ironflesh_12|knows_shield_11|knows_power_strike_10|knows_athletics_10,rhodok_face_middle_1, rhodok_face_older_2],

  ["gulfod_patrol_leader","gulfod_patrol_leader","gulfod_patrol_leaders",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_gulfod_theocracy,
   [itm_steel_greaves,itm_finger_gauntlets,itm_gothic_plate,itm_sallet_02,itm_warhorse,itm_lance_1,itm_ganquang_axe,itm_steel_shield,itm_luc_flanged_mace_iron,itm_luc_knightly_axe_two_handed],
   def_champion|level(30),wp(170),knows_ironflesh_5|knows_shield_1|knows_power_strike_5|knows_athletics_5|knows_power_draw_4,rhodok_face_middle_1, rhodok_face_older_2],

  ["gulfod_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_gulfod_theocracy,
   [itm_spear,itm_wooden_shield,itm_falchion,
    itm_padded_leather_jco,itm_wrapping_boots,itm_nomad_boots,itm_gambeson,itm_leather_vest,itm_padded_coif,itm_fur_hat,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,nord_face_middle_1, nord_face_older_2],
  ["gulfod_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_gulfod_theocracy,
   [itm_sallet_b_closed1,itm_sallet_b_closed2,itm_marmont_armor,itm_dorn_spearbearer_boots,itm_dorn_spearbearer_guant,itm_steel_shield,itm_luc_flanged_mace_iron],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,nord_face_middle_1, nord_face_older_2],
  ["gulfod_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_gulfod_theocracy,
   [itm_sallet_b_closed1,itm_sallet_b_closed2,itm_marmont_armor,itm_dorn_spearbearer_boots,itm_dorn_spearbearer_guant,itm_steel_shield,itm_luc_flanged_mace_iron],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,nord_face_middle_1, nord_face_older_2],
#coleta
  ["coleta_citizen","coleta citizen","coleta citizen",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_coleta,
   [itm_leather_apron,itm_club,itm_ankle_boots,itm_common_hood,itm_hatchet,itm_sword_medieval_b_small,],
   def_farmer|level(4),wp(75),knows_common,vaegir_face_middle_1, vaegir_face_older_2],
  ["coleta_militia","coleta militia","coleta militia",tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_boots,0,0,fac_coleta,
   [itm_b_h1,itm_a_h4_1,itm_dirk,itm_s_h2,itm_s_h2_1,itm_s_h2_2,itm_bastard_sword_a,itm_leather_gloves,itm_skullcap],
   def_footman|level(10),wp(120),knows_ironflesh_1|knows_power_strike_1|knows_athletics_1,vaegir_face_middle_1, vaegir_face_older_2],
  ["coleta_swordman","coleta swordman","coleta swordman",tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_boots,0,0,fac_coleta,
   [itm_b_h1,itm_a_h1,itm_s_h2,itm_s_h2_1,itm_s_h2_2,itm_highlad_broadsword,itm_great_sword,itm_leather_gloves],
   def_fighter|level(15),wp(145),knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["coleta_skilled_swordman","coleta swordman","coleta swordman",tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_boots,0,0,fac_coleta,
   [itm_b_h2,itm_a_h2,itm_s_h1,itm_s_h1_1,itm_s_h1_2,itm_2h_claymore,itm_sword_two_handed_b,itm_lamellar_gauntlets],
   def_swordsman|level(20),wp(175),knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["coleta_swordmaster","coleta swordmaster","coleta swordmaster",tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_boots,0,0,fac_coleta,
   [itm_b_h2,itm_a_h3,itm_s_h1,itm_s_h1_1,itm_s_h1_2,itm_2h_claymore,itm_flamberge,itm_lamellar_gauntlets],
   def_guard|level(26),wp(200),knows_ironflesh_5|knows_shield_5|knows_power_strike_5|knows_athletics_5,vaegir_face_middle_1, vaegir_face_older_2],

  ["coleta_crossbowman","Coleta Crossbowman","Coleta Crossbowmen",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_coleta,
   [itm_b_h1_1,itm_light_crossbow,itm_hunting_crossbow,itm_bolts,itm_darts,itm_war_darts,itm_hammer,itm_club,itm_mackie_morning_star,itm_battle_fork,itm_green_tunic,itm_red_tunic,itm_skullcap],
   str_12 | agi_9 | int_6 | cha_6|level(12),wp_crossbow(95)|wp(75),knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_power_throw_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["coleta_engineer","Coleta Engineer","Coleta Engineers",tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_coleta,
   [itm_arena_armor_red,itm_arena_armor_green,itm_b_h1_1,itm_tab_shield_pavise_a,itm_bolts,itm_crossbow,itm_luc_studded_club,itm_luc_battle_axe,itm_luc_saxon_voulge,itm_footman_helmet],
   str_15 | agi_12 | int_6 | cha_6|level(18),wp_crossbow(120)|wp(85),knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_3,vaegir_face_middle_1, vaegir_face_older_2],
  ["coleta_trained_engineer","Coleta Trained Engineer","Coleta Trained Engineers",tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_coleta,
   [itm_mail_with_tunic_red,itm_mail_with_tunic_green,itm_new_leather_boots,itm_tab_shield_pavise_b,itm_steel_bolts,itm_bolts,itm_heavy_crossbow,itm_luc_knightly_hammer,itm_military_hammer,itm_helmet_tully_archer1],
   str_17 | agi_14 | int_7 | cha_7|level(24),wp_crossbow(135) |wp(100),knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_4,vaegir_face_middle_1, vaegir_face_older_2],
  ["coleta_veteran_engineer","Coleta Veteran Engineer","Coleta Veteran Engineers",tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_coleta,
   [itm_dol_red_hauberk,itm_surcoat_over_mail,itm_rus_cav_boots,itm_tab_shield_pavise_c,itm_steel_bolts,itm_sniper_crossbow,itm_luc_iron_morningstar,itm_helmet_tully_archer_2],
   def_champion|level(30),wp_crossbow(160)|wp(120),knows_ironflesh_5|knows_shield_5|knows_power_strike_5|knows_athletics_5,vaegir_face_middle_1, vaegir_face_older_2],
  ["coleta_engineer_master","Coleta Royal Engineer","Coleta Royal Engineers",tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_coleta,
   [itm_dol_red_heavy_mail,itm_mail_with_surcoat,itm_surcoat_over_mail,itm_rus_splint_greaves,itm_tab_shield_pavise_d,itm_morningstar,itm_luc_flanged_mace_iron,itm_steel_bolts,itm_spak_crsb02,itm_helmet_tully_archer_3],
   def_knight|level(35),wp_crossbow(180)|wp(135),knows_ironflesh_6|knows_shield_6|knows_power_strike_6|knows_athletics_6,vaegir_face_middle_1, vaegir_face_older_2],
  ["coleta_royal_engineer","Coleta Royal Blaster","Coleta Royal Blasters",tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_coleta,
   [itm_dol_red_very_heavy_mail,itm_steel_boots_01,itm_tab_shield_pavise_d,itm_ganquang_morningstar,itm_luc_spiked_mace_5p_b,itm_spak_crsb01_fire,itm_bolts_fire,itm_copy_dwarven_inf_helmet_t4],
   def_knight_1|level(40),wp_crossbow(220) |wp(155),knows_ironflesh_7|knows_shield_7|knows_power_strike_7|knows_athletics_7,vaegir_face_middle_1, vaegir_face_older_2],
  ["coleta_royal_mechanic","Coleta Royal Mechanic","Coleta Royal Mechanics",tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_coleta,
   [itm_rhodok_elite_surcoat,itm_steel_boots_01,itm_luc_horsemans_hammer,itm_copy_dwarven_inf_helmet_t4,itm_van_helsing_crossbow_01,itm_van_helsing_crossbow_bolt,itm_leather_gauntlets_new],
   def_knight_1|level(40),wp_crossbow(200)|wp(175),knows_ironflesh_8|knows_shield_8|knows_power_strike_8|knows_athletics_8,vaegir_face_middle_1, vaegir_face_older_2],

#ciambia
  ["ciambia_slave","Ciambia Slave","Ciambia Slaves",tf_guarantee_armor,0,0,fac_ciambia,
   [itm_wooden_stick,itm_cudgel],
   def_attrib|level(1),wp(60),knows_common,mide_face_middle_1, mide_face_older_2],
  ["ciambia_slave_soldier","Ciambia Slave Soldier","Ciambia Slave Soldiers",tf_guarantee_armor,0,0,fac_ciambia,
   [itm_shirt,itm_shortened_spear,itm_club,itm_sarranid_thief_coat],
   def_farmer|level(5),wp(70),knows_ironflesh_1|knows_power_draw_1,mide_face_middle_1, mide_face_older_2],
  ["ciambia_slave_soldier_1","Ciambia Slave Soldier","Ciambia Slave Soldier",tf_guarantee_armor|tf_guarantee_shield,0,0,fac_ciambia,
   [itm_falchion,itm_spear,itm_hatchet,itm_arena_turban_yellow,itm_arena_tunic_yellow,itm_wrapping_boots,itm_sarranid_thief_coat,itm_wooden_shield],
   def_footman|level(11),wp(100),knows_ironflesh_1|knows_shield_1|knows_power_strike_2|knows_athletics_1,mide_face_middle_1, mide_face_older_2],
  ["ciambia_slave_soldier_2","Ciambia Slave Soldier","Ciambia Slave Soldier",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_ciambia,
   [itm_leather_covered_round_shield,itm_pike,itm_bamboo_spear,itm_falchion,itm_ankle_boots,itm_leather_jerkin,itm_footman_helmet,itm_javelin],
   def_fighter|level(18),wp(140),knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_2|knows_power_throw_2,mide_face_middle_1, mide_face_older_2],
  ["ciambia_slave_warrior","Ciambia Slave warrior","Ciambia Slave warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_ciambia,
   [itm_balion_lamellar_vest,itm_balion_mail_coat,itm_nomad_boots,itm_spiked_helmet,itm_awlpike,itm_plate_covered_round_shield,itm_sarranid_mace_1,itm_ashwood_pike,itm_javelin],
   def_guard|level(25),wp(180),knows_ironflesh_3|knows_shield_3|knows_power_strike_3|knows_athletics_4|knows_power_throw_4,mide_face_middle_1, mide_face_older_2],
  ["ciambia_trained_soldier","ciambia_trained_soldier","ciambia_trained_soldier",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_ciambia,
   [itm_dorn_squire_helm_0,itm_balion_plate_armor,itm_mail_mittens,itm_splinted_greaves,itm_dorn_wiper_helmet,itm_vaegir_spiked_helmet,itm_ashwood_pike,itm_dorn_wiper_helmet_c,itm_blood_spear,itm_throwing_spears,itm_steel_shield],
   str_23 | agi_16 | int_8 | cha_8|level(33),wp(235),knows_ironflesh_5|knows_shield_6|knows_power_strike_6|knows_athletics_6|knows_power_throw_6,mide_face_middle_1, mide_face_older_2],
  ["ciambia_guard","ciambia_guard","ciambia_guard",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_ciambia,
   [itm_dorn_wiper,itm_dorn_squire_helm,itm_dorn_spearbearer_boots,itm_dorn_spearbearer_guant,itm_amroth_lance,itm_throwing_spears,itm_dec_steel_shield],
   def_knight_1|level(40),wp(300),knows_ironflesh_8|knows_shield_8|knows_power_strike_8|knows_athletics_8|knows_power_throw_9,mide_face_middle_1, mide_face_older_2],

  ["ciambia_gladiatus","ciambia_gladiatus","ciambia_gladiatus",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_ciambia,
   [itm_tribal_warrior_outfit,itm_barbuta1,itm_great_sword,itm_two_handed_battle_axe_2,itm_throwing_axes,itm_lightedge_spak,itm_luc_bastard_axe,itm_hide_boots],
   def_guard|level(25),wp(180),knows_ironflesh_3|knows_shield_3|knows_power_strike_3|knows_athletics_3|knows_power_throw_5,mide_face_middle_1, mide_face_older_2],
  ["ciambia_veteran_gladiatus","ciambia_veteran_gladiatus","ciambia_veteran_gladiatus",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_ciambia,
   [itm_sword_two_handed_b,itm_long_axe_c,itm_heavy_throwing_axes,itm_flamberg,itm_luc_iron_hand_axe_h,itm_barbuta2,itm_sarranid_elite_mail_shirt,itm_mail_chausses],
   def_knight|level(35),wp(240),knows_ironflesh_6|knows_shield_6|knows_power_strike_7|knows_athletics_7|knows_power_throw_7,mide_face_middle_1, mide_face_older_2],
  ["ciambia_gladiatus_champion","ciambia_gladiatus_champion","ciambia_gladiatus_champion",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_ciambia,
   [itm_henrysword,itm_heavy_throwing_axes,itm_2dblhead_ax,itm_pa_axe_03,itm_leduc_helm,itm_leduc_closed,itm_dk_armor,itm_mail_boots],
   def_knight_1|level(40),wp(280),knows_ironflesh_9|knows_shield_8|knows_power_strike_8|knows_athletics_9|knows_power_throw_9,mide_face_middle_1, mide_face_older_2],

  ["ciambia_slave_skirmisher","ciambia_slave_skirmisher","ciambia_slave_skirmishers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_ciambia,
   [itm_leather_jerkin,itm_arrows,itm_ankle_boots,itm_short_bow,itm_hunting_bow,itm_fur_covered_shield,itm_hatchet,itm_club],
   def_footman|level(12),wp(100),knows_ironflesh_2|knows_shield_1|knows_athletics_1|knows_power_draw_2,mide_face_middle_1, mide_face_older_2],
  ["ciambia_archer","ciambia_archer","ciambia_archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_ciambia,
   [itm_byrnie,itm_arrows,itm_leather_boots,itm_long_bow,itm_nomad_bow,itm_fur_covered_shield,itm_hand_axe,itm_falchion,itm_leather_cap],
   def_swordsman|level(20),wp(130),knows_ironflesh_3|knows_shield_1|knows_power_strike_2|knows_athletics_1|knows_power_draw_3,mide_face_middle_1, mide_face_older_2],

  ["ciambia_nobleman","ciambia_nobleman","ciambia_nobleman",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_ciambia,
   [itm_cinuz_helm_2,itm_sarranid_elite_mail_shirt,itm_mail_mittens,itm_mail_boots,itm_exp_warhorse_w,itm_war_darts,itm_spiked_mace,itm_maul,itm_plate_covered_round_shield],
   def_footman|level(20),wp(120),knows_ironflesh_3|knows_shield_3|knows_athletics_3|knows_power_draw_3,blac_face_middle_1, blac_face_older_2],
  ["ciambia_nobleman_hunter","ciambia_nobleman_hunter","ciambia_nobleman_hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_ciambia,
   [itm_dorn_knight_helmet_a,itm_dorn_knight_helmet_b,itm_dorn_knight_gant,itm_dorn_knight_boots,itm_dorn_knight_armor,itm_exp_charger_w,itm_spak_crsb01,itm_steel_bolts,itm_steel_shield,itm_military_hammer],
   def_swordsman|level(30),wp(180),knows_ironflesh_5|knows_shield_5|knows_power_strike_5|knows_athletics_3|knows_riding_5,blac_face_middle_1, blac_face_older_2],
  ["ciambia_nobleman_watcher","ciambia_nobleman_watcher","ciambia_nobleman_watcher",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_ciambia,
   [itm_cinuz_helm_1,itm_medusa_armor,itm_plate_boots,itm_scale_gauntlets,itm_exp_charger_w,itm_luc_throwing_hammer,itm_luc_great_hammer_b,itm_luc_spiked_mace_5p_b,itm_dec_steel_shield,itm_jousting_lance],
   def_swordsman|level(30),wp(180),knows_ironflesh_6|knows_shield_5|knows_power_strike_6|knows_athletics_5|knows_power_throw_6,blac_face_middle_1, blac_face_older_2],

  ["ciambia_shadow_assassin","ciambia_shadow_assassin","ciambia_shadow_assassin",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_ciambia,
   [itm_dorn_assasin_armor_helmet,itm_dorn_assasin_gant,itm_dorn_assasin_armor_boots,itm_dorn_assasin_armor,itm_ganquang_dart,itm_asmoday_sword,itm_sp_shr1],
   def_knight_2|level(45),wp(335),knows_ironflesh_6|knows_shield_10|knows_power_strike_10|knows_athletics_10|knows_power_throw_10,mide_face_middle_1, mide_face_older_2],
  ["ciambia_peacock_guard","ciambia_peacock_guard","ciambia_peacock_guard",tf_beautiful|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_ciambia,
   [itm_armor_23_green_1,itm_armor_23_green,itm_rus_splint_greaves,itm_dorn_spearbearer_guant,itm_dorn_knight_helmet_black_a,itm_bow4_arr_spak,itm_bow4_spak,itm_pa_sword_07,itm_dec_steel_shield],
   def_knight_1|level(40),wp(275),knows_ironflesh_7|knows_shield_8|knows_power_strike_8|knows_athletics_9|knows_power_draw_8,beauty_face1, beauty_face2],

  ["ciambia_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_gulfod_theocracy,
   [itm_spear,itm_wooden_shield,itm_falchion,
    itm_padded_leather_jco,itm_wrapping_boots,itm_nomad_boots,itm_gambeson,itm_leather_vest,itm_padded_coif,itm_fur_hat,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,blac_face_middle_1, blac_face_older_2],
  ["ciambia_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_ciambia,
   [itm_dorn_knight_helmet_a,itm_dorn_knight_gant,itm_dorn_knight_boots,itm_dorn_knight_armor,itm_steel_shield,itm_military_hammer],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,blac_face_middle_1, blac_face_older_2],
  ["ciambia_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_ciambia,
   [itm_cinuz_helm_1,itm_medusa_armor,itm_plate_boots,itm_scale_gauntlets,itm_luc_throwing_hammer,itm_luc_great_hammer_b,itm_luc_spiked_mace_5p_b,itm_dec_steel_shield],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,blac_face_middle_1, blac_face_older_2],

#turumia
  ["turumia_recruit","turumia_recruit","turumia_recruit",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_turumia,
   [itm_linen_tunic_banner,itm_arming_cap,itm_rus_shoes,itm_woolen_hose,itm_sword_medieval_b_small,itm_tab_shield_heater_a,itm_shortened_spear,itm_bolts,itm_hunting_crossbow],
   def_farmer|level(5),wp(60),knows_common,west_face_middle_1, west_face_old_2],
  ["turumia_militia","turumia_militia","turumia_militia",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_turumia,
   [itm_arena_tunic_banner2,itm_arena_tunic_banner1,itm_mail_coif,itm_padded_coif,itm_new_leather_boots,itm_leather_gauntlets_new,
   itm_sword_medieval_a,itm_tab_shield_heater_b,itm_bamboo_spear,itm_bolts,itm_hunting_crossbow],
   def_footman|level(10),wp(80),knows_ironflesh_1|knows_power_draw_1,west_face_middle_1, west_face_old_2],
  ["turumia_soldier","turumia_soldier","turumia_soldier",tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_boots,0,0,fac_turumia,
   [itm_arena_armor_banner,itm_chapel_de_fer_cloth1,itm_segmented_helmet,itm_leather_gauntlets_new,itm_rus_cav_boots,itm_mail_mittens,
   itm_sword_medieval_c_small,itm_tab_shield_heater_c,itm_war_spear,itm_pike,itm_bolts,itm_steel_bolts,itm_light_crossbow],
   def_fighter|level(15),wp(100),knows_ironflesh_1|knows_shield_1|knows_power_strike_2|knows_athletics_1,west_face_middle_1, west_face_old_2],
  ["turumia_trained_soldier","turumia_trained_soldier","turumia_trained_soldier",tf_mounted|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_turumia,
   [itm_light_mail_and_plate_banner,itm_mail_long_surcoat_banner,itm_zitta_bascinet_novisor,itm_bascinet_2,itm_bascinet,itm_mail_chausses,itm_mail_mittens,
   itm_sword_medieval_c_long,itm_bastard_sword_a,itm_tab_shield_heater_d,itm_double_sided_lance,itm_light_lance,itm_saddle_horse,itm_courser,itm_warhorse_red2,itm_barded1w,itm_barded3w],
   def_swordsman|level(21),wp(125),knows_ironflesh_3|knows_shield_2|knows_power_strike_3|knows_athletics_2|knows_riding_5,west_face_middle_1, west_face_old_2],
  ["turumia_cavalry","turumia_cavalry","turumia_cavalry",tf_mounted|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_turumia,
   [itm_mail_long_surcoat_banner,itm_surcoat_over_mail_banner,itm_great_helmet,itm_grhelm_03,itm_topfhelm5,itm_maciejowski_helmet_newmod1,itm_iron_greaves,itm_mail_boots,itm_scale_gauntlets,
   itm_sword_medieval_c_long,itm_mackie_kriegsmesser,itm_great_sword,itm_bastard_sword_b,itm_tab_shield_heater_cav_a,itm_lance,itm_courser,itm_hunter,itm_warhorse_blu2,itm_wbardedshort4,itm_warhorse_ylw2,itm_wlong12,itm_barded3w],
   str_20 | agi_14 | int_7 | cha_7|level(27),wp(155),knows_ironflesh_4|knows_shield_3|knows_power_strike_4|knows_athletics_4|knows_riding_6,west_face_middle_1, west_face_old_2],
  ["turumia_elite_cavalry","turumia_elite_cavalry","turumia_elite_cavalry",tf_mounted|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_turumia,
   [itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tabard,itm_helmhorn3,itm_teutonichelm_g,itm_topfhelm8,itm_col1_madelnbucket2,itm_plate_boots,itm_gauntlets,itm_steel_gauntlets,
   itm_sword_medieval_d_long,itm_despair,itm_sp_2hsw,itm_sword_of_war,itm_sword_two_handed_a,itm_lance_5,itm_tab_shield_heater_cav_b,itm_heavy_lance,itm_great_lance,itm_hunter,itm_wbardedshort4,itm_warhorse_blk,itm_wlong11,itm_wlong1,itm_wlong12,itm_wlong20,itm_wlong17],
   str_23 | agi_16 | int_8 | cha_8|level(33),wp(200),knows_ironflesh_5|knows_shield_6|knows_power_strike_6|knows_athletics_6|knows_riding_7,west_face_middle_1, west_face_old_2],
  ["turumia_man_at_arm","turumia_man_at_arm","turumia_man_at_arm",tf_mounted|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_turumia,
   [itm_early_transitional_banner,itm_topfhelm7,itm_col1_gotlandbucket,itm_col1_crusaderbucket2,itm_col1_crusaderbucket1,itm_teutonichelm_d,itm_steel_boots_01,itm_dorn_knight_boots,itm_gauntlets,itm_steel_mittens,
   itm_sword_medieval_d_long,itm_flamberg,itm_sp_2hsw,itm_mercy,itm_pa_sword_04,itm_lance_4,itm_lance_5,itm_tab_shield_heater_cav_b,itm_wlong1,itm_wlong2,itm_wlong4,itm_wlong20,itm_wlong17,itm_wlong11,itm_wlong9],
   str_25 | agi_19 | int_8 | cha_8|level(38),wp(245),knows_ironflesh_8|knows_shield_8|knows_power_strike_8|knows_athletics_8|knows_riding_9,west_face_middle_1, west_face_old_2],

 ["turumia_nobleman","turumia_nobleman","turumia_nobleman",tf_mounted|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_turumia,
   [itm_armor_14_banner,itm_zitta_bascinet_novisor,itm_mail_chausses,itm_wisby_gauntlets_red,itm_mail_mittens,itm_sword_medieval_c_long,itm_bastard_sword_b,itm_tab_shield_heater_d,itm_jousting_lance,itm_courser],
   def_swordsman|level(20),wp(140),knows_ironflesh_4|knows_shield_3|knows_power_strike_3|knows_athletics_3|knows_riding_5,west_face_middle_1, west_face_old_2],
 ["turumia_squire","turumia_squire","turumia_squire",tf_mounted|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_turumia,
   [itm_guesclin_banner,itm_zitta_bascinet_novisor,itm_bascinet_coif_01,itm_wisby_gauntlets_black,itm_iron_greaves,itm_mail_boots,
   itm_sword_medieval_d_long,itm_great_lance,itm_great_sword,itm_tab_shield_heater_cav_b,itm_warhorse_holy],
   str_20 | agi_15 | int_7 | cha_7|level(28),wp(180),knows_ironflesh_5|knows_shield_6|knows_power_strike_5|knows_athletics_6|knows_riding_7,west_face_middle_1, west_face_old_2],
 ["turumia_knight","turumia_knight","turumia_knight",tf_mounted|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_turumia,
   [itm_spak_2full_plate_armor_banner,itm_full_plate_armor_banner,itm_zitta_bascinet,itm_hounskull_bascinet,itm_armet_01,itm_wisby_gauntlets_black,itm_steel_gauntlets,itm_plate_boots,
   itm_lance_4,itm_lance_5,itm_tab_shield_heater_cav_b,itm_sword_two_handed_a,itm_sword_of_war,itm_flamberg,itm_mercy,itm_warhorse],
   def_knight|level(35),wp(230),knows_ironflesh_7|knows_shield_7|knows_power_strike_7|knows_athletics_7|knows_riding_8,west_face_middle_1, west_face_old_2],
 ["turumia_conquer_knight","turumia_conquer_knight","turumia_conquer_knight",tf_mounted|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_turumia,
   [itm_heraldic_platemail_02,itm_heraldic_plate_01,itm_armet_01,itm_hounskull_bascinet_01,itm_hounskull_bascinet_02,itm_armet_02,itm_steel_boots_01,itm_steel_mittens,
   itm_tab_shield_heater_cav_b,itm_jack_glamdring,itm_jack_faramir,itm_black_lance_banner,itm_sorrow,itm_wplatedcharger2],
   str_28 | agi_20 | int_9 | cha_9|level(43),wp(260),knows_ironflesh_8|knows_shield_8|knows_power_strike_8|knows_athletics_8|knows_riding_10,west_face_middle_1, west_face_old_2],
 ["turumia_guard_knight","turumia_guard_knight","turumia_guard_knight",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_turumia,
   [itm_heraldic_platemail_01,itm_heraldic_plate_02,itm_armet_01,itm_tournament_helmb,itm_hounskull_bascinet_01,itm_hounskull_bascinet_02,itm_steel_boots_01,itm_steel_gauntlets,
   itm_tab_shield_heater_cav_b,itm_jack_anduril,itm_jack_glamdring,itm_jack_faramir,itm_sorrow,itm_steel_bolts,itm_steel_bolts,itm_spak_crsb02],
   def_knight_2|level(45),wp(280),knows_ironflesh_9|knows_shield_9|knows_power_strike_9|knows_athletics_9,west_face_middle_1, west_face_old_2],
  
 ["turumia_walk_knight","turumia_walk_knight","turumia_walk_knight",tf_mounted|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_turumia,
   [itm_heraldic_plate_02,itm_armet_01,itm_tournament_helmb,itm_hounskull_bascinet_01,itm_hounskull_bascinet_02,itm_steel_boots_01,itm_steel_gauntlets,itm_jack_anduril,itm_pa_sword_04,itm_plate_charger_white],
   def_lord_1|level(50),wp(340),knows_ironflesh_10|knows_power_strike_10|knows_athletics_10|knows_riding_12,west_face_middle_1, west_face_old_2],

  ["turumia_patrol_leader","turumia_patrol_leader","turumia_patrol_leader",tf_mounted|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_turumia,
   [itm_heraldic_mail_with_surcoat,itm_helmhorn3,itm_topfhelm8,itm_plate_boots,itm_gauntlets,
   itm_sword_medieval_d_long,itm_sword_of_war,itm_sword_two_handed_a,itm_lance_5,itm_tab_shield_heater_cav_b,itm_warhorse_blk],
   def_champion|level(30),wp(170),knows_ironflesh_5|knows_shield_6|knows_power_strike_6|knows_athletics_6|knows_riding_7,west_face_middle_1, west_face_old_2],

  ["turumia_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_turumia,
   [itm_spear,itm_wooden_shield,itm_falchion,
    itm_padded_leather_jco,itm_wrapping_boots,itm_nomad_boots,itm_gambeson,itm_leather_vest,itm_padded_coif,itm_fur_hat,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,west_face_middle_1, west_face_old_2],
  ["turumia_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_turumia,
   [itm_early_transitional_banner,itm_topfhelm7,itm_teutonichelm_d,itm_dorn_knight_boots,itm_gauntlets,itm_flamberg],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,west_face_middle_1, west_face_old_2],
  ["turumia_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_turumia,
   [itm_early_transitional_banner,itm_col1_crusaderbucket2,itm_steel_boots_01,itm_dorn_knight_boots,itm_steel_mittens,itm_sword_medieval_d_long,itm_flamberg,itm_tab_shield_heater_cav_b],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,west_face_middle_1, west_face_old_2],

#default
  ["de_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_commoners,
   [itm_spear,itm_wooden_shield,itm_falchion,
    itm_padded_leather_jco,itm_wrapping_boots,itm_nomad_boots,itm_gambeson,itm_leather_vest,itm_padded_coif,itm_fur_hat,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,bandit_face1, bandit_face2],
  ["de_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_bastard_sword_b,itm_sword_medieval_c,itm_tab_shield_pavise_c,itm_tab_shield_heater_cav_a,itm_swadian_ceremonial_plate_red,itm_mail_chausses,itm_brig_plate_red,itm_iron_greaves,itm_plate_boots,itm_guard_helmet,itm_great_helmet,itm_bascinet, itm_leather_gloves],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,bandit_face1, bandit_face2],
  ["de_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_heavy_lance,itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_swadian_ceremonial_plate_black,itm_banded_armor,itm_bascinet_2,itm_splinted_leather_greaves,itm_flat_topped_helmet],
   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,bandit_face1, bandit_face2],
  ["de_flag_holder","de_flag_holder","de_flag_holder",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_brigandine_plate_heraldic,itm_guard_helmet,itm_iron_greaves,itm_gauntlets,itm_battle_flag_d_banner],
   def_guard|level(25),wp(150),knows_ironflesh_5|knows_shield_6|knows_power_strike_5|knows_athletics_6,bandit_face1, bandit_face2],

#bandit
  ["looter","Looter","Looters",0,0,0,fac_outlaws,
   [itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_rawhide_skirt,itm_stones,itm_nomad_skirt,itm_nomad_stripped_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(20),knows_common,bandit_face1, bandit_face2],
  ["bandit","Bandit","Bandits",tf_guarantee_armor,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_sword_viking_1,itm_short_bow,itm_falchion,itm_nordic_shield,itm_rawhide_coat,itm_leather_cap,itm_leather_jerkin,itm_nomad_stripped_armor,itm_nomad_boots,itm_wrapping_boots,itm_saddle_horse],
   def_attrib|level(10),wp(60),knows_common|knows_power_draw_1,bandit_face1, bandit_face2],
  ["brigand","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_mercenary_studded_leather_jacket,itm_rawhide_sleeveless_coat,itm_sword_viking_1,itm_falchion,itm_wooden_shield,itm_hide_covered_round_shield,itm_long_bow,itm_mail_shirt,itm_leather_cap,itm_leather_jerkin,itm_nomad_boots,itm_saddle_horse],
   def_attrib|level(16),wp(90),knows_power_draw_3,bandit_face1, bandit_face2],
  ["brigand_0","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_arrows,itm_double_sided_lance,itm_hunter,itm_lamellar_vest,itm_tribal_warrior_outfit,itm_arabian_horse_b,itm_scimitar,itm_vaegir_spiked_helmet,itm_tab_shield_round_c,itm_arabian_armor_b,itm_spiked_mace,itm_tab_shield_kite_b,itm_nomad_boots,itm_saddle_horse,itm_strange_sword,itm_nomad_bow],
   def_attrib|level(21),wp(130),knows_power_draw_4|knows_shield_3|knows_ironflesh_4|knows_riding_3|knows_power_strike_4,bandit_face1, bandit_face2],
  ["brigand_1","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_arabian_horse_a,itm_rhodok_hauberk,itm_lance,itm_spiked_helmet,itm_vaegir_lamellar_helmet,itm_arabian_horse_b,itm_hunter,itm_javelin,itm_lamellar_vest,itm_mail_hauberk,itm_leather_boots,itm_nomad_boots,itm_arabian_armor_b],
   def_attrib|level(26),wp(155),knows_power_draw_5|knows_shield_3|knows_ironflesh_5|knows_riding_5|knows_power_strike_5|knows_horse_archery_4|knows_power_throw_4,bandit_face1, bandit_face2],
  ["brigand_2","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_balion_plate_armor,itm_wlong21,itm_warhorse,itm_heavy_lance,itm_guard_helmet,itm_full_helm,itm_khergit_guard_boots,itm_mail_boots,itm_scale_armor,itm_warhorse_steppe,itm_lamellar_armor,itm_tab_shield_small_round_c,
   itm_strange_great_sword,itm_khergit_helmet,itm_scimitar_b,itm_great_sword,itm_heavy_lamellar_armor,itm_vaegir_war_helmet,itm_javelin,itm_throwing_spears],
   def_attrib|level(30),wp(185),knows_power_draw_6|knows_shield_6|knows_ironflesh_6|knows_riding_8|knows_power_strike_6|knows_horse_archery_6|knows_power_throw_6,bandit_face1, bandit_face2],

  ["flooter","Looter","Looters",tf_guarantee_armor|tf_female|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_blue_dress,itm_dress,itm_peasant_dress,itm_woolen_dress,itm_leather_apron,itm_blue_hose,itm_hosen_brown,itm_hosen_green,itm_hosen_red,itm_hosen_grey,itm_woolen_hood,itm_hood_b,itm_hood_c,
   itm_dagger,itm_knife,itm_sickle,itm_butchering_knife,itm_club,itm_cudgel,itm_pitch_fork,itm_arrows,itm_hunting_bow,itm_stones],
   def_attrib|level(4),wp(50),knows_common,bandit_face1, bandit_face2],
  ["fbandit","Bandit","Bandits",tf_guarantee_armor|tf_female|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_rawhide_coat,itm_sarranid_cloth_robe,itm_arena_tunic_banner2,itm_coarse_tunic,itm_leather_apron,itm_hunter_boots,itm_hide_boots,itm_hosen_green,itm_hosen_red,itm_hosen_grey,itm_woolen_hood,itm_hood_b,itm_straw_hat,
   itm_sword_medieval_b_small,itm_pitch_fork,itm_sword_medieval_a,itm_hand_axe,itm_falchion,itm_short_bow,itm_arrows,itm_nomad_bow],
   def_attrib|level(12),wp(90),knows_power_draw_1|knows_ironflesh_1,bandit_face1, bandit_face2],
  ["fbrigand","Brigand","Brigands",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_mercenary_studded_leather_jacket,itm_rawhide_sleeveless_coat,itm_sword_viking_1,itm_falchion,itm_wooden_shield,itm_hide_covered_round_shield,
   itm_long_bow,itm_mail_shirt,itm_skullcap,itm_ragged_outfit,itm_nomad_boots,itm_nomad_bow,itm_mail_coif],
   def_attrib|level(19),wp(120),knows_power_draw_3|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,bandit_face1, bandit_face2],
  ["fbrigand_leader","Brigand","Brigands",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_barbed_arrows,itm_spiked_mace,itm_mercenary_catapharact_armor,itm_mercenary_catapharact_armor_variant,itm_sword_viking_3_small,itm_hide_covered_round_shield,itm_tab_shield_round_c,itm_tab_shield_round_d,
   itm_long_bow,itm_mail_with_surcoat,itm_nasal_helmet,itm_tribal_warrior_outfit,itm_splinted_leather_greaves,itm_strong_bow,itm_byrnie,itm_segmented_helmet],
   def_attrib|level(25),wp(150),knows_power_draw_4|knows_shield_4|knows_ironflesh_4|knows_power_strike_4,bandit_face1, bandit_face2],

  ["mountain_bandit","Mountain Bandit","Mountain Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_spear,itm_winged_mace,itm_maul,itm_falchion,itm_short_bow,itm_javelin,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_felt_hat,itm_head_wrappings,itm_skullcap,itm_ragged_outfit,itm_rawhide_coat,itm_leather_armor,itm_hide_boots,itm_nomad_boots,itm_wooden_shield,itm_nordic_shield],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_2,rhodok_face_young_1, rhodok_face_old_2],
  ["mountain_bandit_1","Mountain Bandit","Mountain Bandits",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_spear,itm_spiked_mace,itm_scimitar,itm_falchion,itm_nomad_bow,itm_javelin,itm_plate_covered_round_shield,itm_leather_covered_round_shield,
    itm_felt_hat,itm_leather_warrior_cap,itm_mail_coif,itm_ragged_outfit,itm_tribal_warrior_outfit,itm_khergit_armor,itm_nomad_boots,itm_leather_boots,itm_nordic_shield,itm_shield_heater_c],
   def_attrib|level(17),wp(110),knows_common|knows_power_draw_2,rhodok_face_young_1, rhodok_face_old_2],
  ["mountain_bandit_2","Mountain Bandit","Mountain Bandits",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_arrows,itm_lance,itm_tab_shield_round_d,itm_sword_viking_1,itm_war_spear,itm_awlpike,itm_khergit_bow,itm_jarid,itm_tab_shield_small_round_b,itm_darts,
    itm_flat_topped_helmet,itm_spiked_helmet,itm_haubergeon,itm_mail_shirt,itm_nomad_robe,itm_splinted_leather_greaves,itm_nomad_boots,itm_tab_shield_heater_c],
   def_attrib|level(21),wp(120),knows_common|knows_power_throw_4|knows_shield_5|knows_ironflesh_5|knows_riding_1|knows_power_strike_4,rhodok_face_young_1, rhodok_face_old_2],

  ["forest_bandit","Forest Bandit","Forest Bandits",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_axe,itm_hatchet,itm_quarter_staff,itm_short_bow,itm_hunting_bow,
    itm_common_hood,itm_black_hood,itm_shirt,itm_padded_leather,itm_leather_jerkin,itm_ragged_outfit,itm_hide_boots,itm_leather_boots],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_3,swadian_face_young_1, swadian_face_old_2],
  ["forest_bandit_1","Forest Bandit","Forest Bandits",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_arrows,itm_barbed_arrows,itm_battle_axe,itm_voulge,itm_war_spear,itm_nomad_bow,itm_short_bow,
    itm_skullcap,itm_black_hood,itm_padded_leather,itm_tribal_warrior_outfit,itm_blue_gambeson,itm_leather_boots],
   def_attrib|level(15),wp(120),knows_ironflesh_2|knows_power_draw_3|knows_power_strike_2|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["forest_bandit_2","Forest Bandit","Forest Bandits",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_bodkin_arrows,itm_barbed_arrows,itm_sword_two_handed_b,itm_two_handed_cleaver,itm_hafted_blade_a,itm_long_bow,itm_nomad_bow,itm_long_spiked_club,
    itm_leather_gloves,itm_splinted_leather_greaves,itm_mail_with_surcoat,itm_haubergeon,itm_black_hood,itm_leather_boots,itm_vaegir_spiked_helmet],
   def_attrib|level(21),wp(140),knows_ironflesh_4|knows_power_draw_5|knows_power_strike_5|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],

  ["sea_raider","Sea Raider","Sea Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_helmet,itm_nasal_helmet,itm_nomad_vest,itm_byrnie,itm_mail_shirt,itm_leather_boots, itm_nomad_boots],
   def_attrib|level(16),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],
  ["sea_raider_1","Sea Raider","Sea Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_sword_viking_1,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_tab_shield_round_c,itm_javelin,itm_throwing_axes,itm_round_shield,itm_long_bow,itm_arrows,
    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_shirt,itm_leather_boots],
   def_attrib|level(21),wp(130),knows_ironflesh_3|knows_power_strike_3|knows_power_draw_4|knows_power_throw_3|knows_riding_1|knows_athletics_4,nord_face_young_1, nord_face_old_2],
  ["sea_raider_2","Sea Raider","Sea Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_sword_viking_1,itm_sword_viking_2,itm_two_handed_battle_axe_2,itm_one_handed_war_axe_b,itm_tab_shield_round_d,itm_tab_shield_round_e,itm_javelin,itm_throwing_axes,itm_heavy_throwing_axes,itm_battle_shield,itm_round_shield,
    itm_nordic_huscarl_helmet,itm_nordic_warlord_helmet,itm_banded_armor,itm_mail_boots,itm_mail_chausses,itm_mail_mittens,itm_long_bow,itm_arrows],
   def_attrib|level(24),wp(150),knows_ironflesh_6|knows_power_strike_4|knows_power_draw_4|knows_power_throw_4|knows_riding_1|knows_athletics_5,nord_face_young_1, nord_face_old_2],

  ["steppe_bandit","Steppe Bandit","Steppe Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_jarid,itm_leather_steppe_cap_a,itm_leather_steppe_cap_b,itm_nomad_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_leather_vest,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_steppe_horse,itm_steppe_horse],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  ["steppe_bandit_1","Steppe Bandit","Steppe Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_lance,itm_sword_khergit_2,itm_winged_mace,itm_spear
   ,itm_nomad_bow,itm_arrows,itm_khergit_arrows,itm_javelin,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_javelin,itm_war_darts,
    itm_khergit_cavalry_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_leather_gloves,itm_steppe_horse],
   def_attrib|level(16),wp(125),knows_ironflesh_2|knows_riding_4|knows_horse_archery_4|knows_power_draw_3|knows_power_strike_3,khergit_face_young_1, khergit_face_old_2],
  ["steppe_bandit_2","Steppe Bandit","Steppe Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_lance,itm_sword_khergit_3,itm_winged_mace,itm_spear
   ,itm_nomad_bow,itm_arrows,itm_khergit_arrows,itm_javelin,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,
    itm_khergit_cavalry_helmet,itm_lamellar_armor,itm_khergit_lamellar_leather_armor,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap,itm_lamellar_vest_khergit,itm_khergit_leather_boots,itm_leather_gloves,itm_steppe_horse,itm_courser,itm_warhorse_steppe],
   def_attrib|level(22),wp(135),knows_ironflesh_4|knows_power_strike_4|knows_riding_4|knows_horse_archery_6|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],

  ["taiga_bandit","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_sumpter_horse,itm_saddle_horse,itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_jarid,itm_javelin,itm_vaegir_fur_cap,itm_leather_steppe_cap_c,itm_nomad_armor,itm_leather_jerkin,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield],
   def_attrib|level(15),wp(110),knows_common|knows_power_draw_4|knows_power_throw_3,vaegir_face_young_1, vaegir_face_old_2],
  ["taiga_bandit_1","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_steppe_horse,itm_arrows,itm_barbed_arrows,itm_spiked_mace,itm_two_handed_axe,itm_sword_khergit_1,itm_tab_shield_kite_b,itm_tab_shield_kite_c,itm_nomad_bow,itm_nomad_bow,itm_light_lance,itm_plate_covered_round_shield,itm_javelin,itm_jarid,
    itm_steppe_cap,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_lamellar_vest,itm_studded_leather_coat,itm_nomad_boots,itm_saddle_horse],
   def_attrib|level(18),wp(125),knows_power_strike_3|knows_power_draw_4|knows_power_throw_4|knows_ironflesh_2,vaegir_face_young_1, vaegir_face_old_2],
  ["taiga_bandit_2","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_hunter,itm_steppe_horse,itm_arrows,itm_long_bardiche,itm_barbed_arrows,itm_ashwood_pike,itm_fighting_axe,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_d,itm_nomad_bow,itm_strong_bow,itm_javelin,itm_jarid,
    itm_lamellar_armor,itm_lamellar_vest,itm_mail_chausses,itm_splinted_leather_greaves,itm_splinted_greaves,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_leather_gloves],
   def_attrib|level(23),wp(140),knows_power_strike_4|knows_power_draw_4|knows_power_throw_3|knows_ironflesh_4,vaegir_face_young_1, vaegir_face_old_2],

  ["desert_bandit","Desert Bandit","Desert Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_arabian_sword_a,itm_winged_mace,itm_spear,itm_sarranid_thief_coat,itm_light_lance,itm_jarid,itm_nomad_bow,itm_short_bow,itm_jarid,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe, itm_skirmisher_armor, itm_desert_turban, itm_turban,itm_leather_steppe_cap_b,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_arabian_horse_a],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  ["desert_bandit_1","Desert Bandit","Desert Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_arrows,itm_leather_gloves,itm_arabian_sword_a,itm_mail_mittens,itm_light_lance,itm_jarid,itm_nomad_bow,itm_jarid,itm_sarranid_leather_armor,itm_sarranid_cavalry_robe,itm_leather_covered_round_shield,itm_arabian_horse_a,itm_arabian_horse_b,itm_sarranid_horseman_helmet,itm_sarranid_warrior_cap,itm_sarranid_boots_b],
   def_attrib|level(16),wp(130),knows_power_strike_2|knows_riding_5|knows_horse_archery_3|knows_power_draw_4|knows_ironflesh_2,khergit_face_young_1, khergit_face_old_2],
  ["desert_bandit_2","Desert Bandit","Desert Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet,0,0,fac_outlaws,
   [itm_arrows,itm_bodkin_arrows,itm_lamellar_gauntlets,itm_sarranid_elite_mail_shirt,itm_arabian_sword_b,itm_arabian_sword_d, itm_light_lance,itm_jarid,itm_nomad_bow,itm_jarid,itm_arabian_armor_b,itm_sarranid_mail_shirt,itm_leather_covered_round_shield,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_arabian_horse_b,itm_arabian_horse_b,itm_hunter,itm_arabian_horse_a,itm_sarranid_boots_c],
   def_attrib|level(22),wp(150),knows_power_strike_4|knows_riding_7|knows_horse_archery_6|knows_power_draw_5|knows_ironflesh_3,khergit_face_young_1, khergit_face_old_2],
  #extra_start
  ["black_khergit_horseman","Black Khergit Horseman","Black Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_mafia1,
   [itm_arrows,itm_sword_khergit_2,itm_scimitar,itm_scimitar,itm_winged_mace,itm_spear,itm_lance,itm_khergit_bow,itm_khergit_bow,itm_nomad_bow,itm_nomad_bow,itm_steppe_cap,itm_nomad_cap,itm_khergit_war_helmet,itm_khergit_war_helmet,itm_mail_hauberk,itm_lamellar_armor,itm_hide_boots,itm_plate_covered_round_shield,itm_plate_covered_round_shield,itm_saddle_horse,itm_steppe_horse],
   def_attrib|level(21),wp(100),knows_riding_3|knows_ironflesh_3|knows_horse_archery_3|knows_power_draw_3|knows_power_strike_2,khergit_face_young_1, khergit_face_old_2],
  ["brotherhood_member","Brotherhood Member","Brotherhood Members",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_mafia2,
   [itm_woolen_hose_a3,itm_hood_newgrn,itm_peasant_man_b,itm_leather_gloves,itm_bodkin_arrows,itm_bodkin_arrows,itm_barbed_arrows,itm_long_bow,itm_bastard_sword_a],
   def_attrib|level(20),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (155) | wp_crossbow (155) | wp_throwing (110),knows_ironflesh_4|knows_power_strike_5|knows_power_draw_5|knows_athletics_5,swadian_face_young_1, swadian_face_old_2],
  ["shadow_member","shadow_member","shadow_members",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet,0,0,fac_mafia3,
   [itm_arabian_horse_a,itm_steel_bolts,itm_steel_bolts,itm_sarranid_boots_b,itm_sarranid_mail_coif,itm_sarranid_leather_armor,itm_leather_gauntlets_new,itm_light_crossbow,itm_sarranid_two_handed_mace_1],
   def_attrib|level(20),wp(120),knows_power_strike_2|knows_riding_7|knows_horse_archery_6|knows_ironflesh_2,khergit_face_young_1, khergit_face_old_2],
  ["mafia4_member","mafia4_member","mafia4_member",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_mafia4,
   [itm_sword_viking_1,itm_tab_shield_round_c,itm_javelin,itm_javelin,itm_throwing_axes,itm_tab_shield_round_d,
    itm_nordic_helmet,itm_mail_hauberk,itm_mail_chausses,itm_mail_mittens],
   def_attrib|level(21),wp(130),knows_ironflesh_5|knows_power_throw_2|knows_athletics_2,nord_face_young_1, nord_face_old_2],
  ["slave_driver","Slave Driver","Slave Drivers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse ,0,0,fac_mafia5,
   [itm_club_with_spike_head,itm_segmented_helmet,itm_blue_gambeson_a,itm_nordic_shield,itm_leather_boots,itm_leather_gloves,itm_khergit_leather_boots,itm_steppe_horse],
   def_attrib|level(14),wp(80),knows_common|knows_ironflesh_1,bandit_face1, bandit_face2],
  ["bloodlion_recuirt","bloodlion_recuirt","bloodlion_recuirts",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves ,0,0,fac_mafia6,
   [itm_hood_b,itm_common_hood,itm_red_tunic,itm_red_shirt,itm_leather_boots,itm_leather_gloves,itm_mackie_mangler_short,itm_club,itm_dagger,itm_cudgel,itm_mace_1],
   def_attrib|level(14),wp(100),knows_common|knows_power_strike_1|knows_ironflesh_2|knows_athletics_3,rhodok_face_young_1, rhodok_face_old_2],
 #dont change order#mafia
  #mafia dedalend
  ["black_khergit_horseman_leader","Black Khergit Horseman","Black Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_mafia1,
   [itm_arrows,itm_sword_khergit_3,itm_khergit_sword_two_handed_b,itm_scimitar_b,itm_spiked_mace,itm_heavy_lance,itm_lance,itm_khergit_bow,itm_strong_bow,itm_strong_bow,itm_nomad_bow,itm_khergit_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_khergit_guard_helmet,itm_heavy_lamellar_armor,itm_lamellar_armor,itm_nomad_boots,itm_plate_covered_round_shield,itm_steel_shield,itm_warhorse_steppe,itm_steppe_horse],
   def_attrib|level(30),wp(180),knows_riding_6|knows_ironflesh_5|knows_horse_archery_8|knows_power_draw_6|knows_power_strike_5,khergit_face_young_1, khergit_face_old_2],
  
  ["brotherhood_marksman","Brotherhood Marksman","Brotherhood Marksman",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_mafia2,
   [itm_woolen_hose_a3,itm_hood_newgrn,itm_peasant_man_b,itm_leather_gloves,itm_bodkin_arrows,itm_bodkin_arrows,itm_barbed_arrows,itm_war_bow,itm_bastard_sword_b],
   def_attrib|level(30),wp_one_handed (120) | wp_two_handed (120) | wp_polearm (120) | wp_archery (225) | wp_crossbow (225) | wp_throwing (110),knows_ironflesh_5|knows_power_strike_7|knows_power_draw_7|knows_athletics_7,swadian_face_young_1, swadian_face_old_2],
  
  ["shadow_warrior","shadow_warrior","shadow_warriors",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted|tf_guarantee_helmet,0,0,fac_mafia3,
   [itm_arabian_horse_b,itm_steel_bolts,itm_steel_bolts,itm_sarranid_boots_c,itm_sarranid_mail_shirt10,itm_sarranid_veiled_helmet,itm_leather_gauntlets_new,itm_spak_crsb01,itm_sarranid_two_handed_mace_1],
   def_attrib|level(30),wp(200),knows_power_strike_5|knows_riding_7|knows_horse_archery_6|knows_ironflesh_4,khergit_face_young_1, khergit_face_old_2],

  ["mafia4_warrior","mafia4_warrior","mafia4_warrior",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_mafia4,
   [itm_iron_greaves,itm_mail_mittens,itm_williamconquer,itm_williamconqueror_helm,itm_throwing_axes,itm_javelin,itm_javelin,itm_tab_shield_round_e,itm_sword_viking_3_small],
   def_attrib|level(30),wp(185),knows_ironflesh_8|knows_power_strike_4|knows_power_throw_5|knows_athletics_7,nord_face_young_1, nord_face_old_2],
  
  ["slave_hunter","Slave Hunter","Slave Hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_mafia5,
   [itm_winged_mace,itm_maul,itm_kettle_hat,itm_studded_leather_coat,itm_tab_shield_round_c,itm_leather_boots,itm_leather_gloves,itm_courser],
   def_attrib|level(18),wp(90),knows_common|knows_power_strike_1|knows_ironflesh_2,bandit_face1, bandit_face2],
  ["slave_crusher","Slave Crusher","Slave Crushers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_mafia5,
   [itm_sledgehammer,itm_spiked_mace,itm_surcoat_over_mail,itm_bascinet,itm_bascinet_2,itm_mail_mittens,itm_tab_shield_round_d,itm_mail_chausses,itm_splinted_leather_greaves,itm_hunter],
   def_attrib|level(22),wp(110),knows_common|knows_riding_4|knows_power_strike_3|knows_ironflesh_3,bandit_face1, bandit_face2],
  ["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_mafia5,
   [itm_military_hammer,itm_warhammer,itm_rhodok_elite_surcoat,itm_steel_shield,itm_scale_gauntlets,itm_mail_mittens,itm_bascinet_3,itm_plate_boots,itm_mail_boots,itm_warhorse_holy],
   def_attrib|level(26),wp(135),knows_common|knows_riding_4|knows_power_strike_5|knows_ironflesh_5,bandit_face1, bandit_face2],

  ["bloodlion_member","bloodlion_member","bloodlion_member",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves ,0,0,fac_mafia6,
   [itm_mackie_falcata01,itm_club,itm_mace_1,itm_mackie_mangler_short,itm_red_gambeson,itm_leather_boots,itm_leather_gloves,itm_hood_d,itm_black_hood],
   def_attrib|level(20),wp(140),knows_common|knows_power_strike_3|knows_ironflesh_3|knows_athletics_4,rhodok_face_young_1, rhodok_face_old_2],
  ["bloodlion_killer","bloodlion_killer","bloodlion_killer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves ,0,0,fac_mafia6,
   [itm_mackie_falcata01,itm_brigandine_red,itm_leather_gloves,itm_skullcap,itm_footman_helmet,itm_splinted_leather_greaves,itm_sword_medieval_a,itm_mackie_bat,itm_club_with_spike_head,itm_falchion],
   def_attrib|level(27),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_5|knows_athletics_6,rhodok_face_young_1, rhodok_face_old_2],
  ["bloodlion_capo","bloodlion_capo","bloodlion_capos",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves ,0,0,fac_mafia6,
   [itm_brig_plate_red,itm_leather_gloves,itm_segmented_helmet,itm_splinted_greaves,itm_flat_topped_helmet,itm_bastard_sword_a,itm_sword_medieval_c,itm_mackie_bat_nailed],
   def_attrib|level(33),wp(225),knows_common|knows_power_strike_7|knows_ironflesh_7|knows_athletics_8,rhodok_face_young_1, rhodok_face_old_2],
  
  ["outlaw_squire","outlaw_squire","outlaw_squire",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_warhorse_prp,itm_mail_long_surcoat_new_f,itm_cuirass_on_black,itm_warhorse_holy,itm_splinted_leather_greaves,itm_spiked_helmet,itm_vaegir_spiked_helmet,itm_lance,itm_bascinet,
   itm_tab_shield_kite_cav_a,itm_tab_shield_round_c,itm_awlpike,itm_club_with_spike_head,itm_two_handed_cleaver,itm_fighting_pick,itm_war_darts,itm_war_darts,itm_strange_sword],
   def_guard|level(24),wp(145),knows_ironflesh_4|knows_power_strike_4|knows_athletics_5|knows_riding_5|knows_horse_archery_3|knows_power_draw_4|knows_power_throw_3,vaegir_face_young_1, vaegir_face_old_2],
  ["outlaw_knight","outlaw_squire","outlaw_squire",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_military_pick,itm_tab_shield_kite_cav_b,itm_tab_shield_small_round_c,itm_shield_kite_k,itm_shield_kite_i,itm_warhorse_holy,itm_charger_black,itm_jarid,itm_tab_shield_heater_cav_b,itm_awlpike_long,itm_military_scythe,itm_sword_medieval_d_long,
   itm_guard_helmet,itm_winged_great_helmet,itm_maciejowski_helmet_new_b2,itm_coat_of_plates_g,itm_brig_plate_blue,itm_steel_boots_01,itm_steel_gauntlets,itm_wlong12,itm_javelin,itm_throwing_spears,itm_heavy_lance,itm_two_handed_cleaver],
   def_champion|level(32),wp(200),knows_ironflesh_5|knows_power_strike_7|knows_athletics_7|knows_riding_6|knows_horse_archery_6|knows_power_draw_7|knows_power_throw_6,bandit_face1, bandit_face2],
  
  ["black_knight_1","black_knight","black_knight",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_joan_black,itm_sorrow,itm_wplatedcharger9,itm_dorn_spearbearer_guant,itm_lance_1,itm_sp_shr1,itm_tournament_helmb_black,itm_black_greaves],
   def_knight_1|level(40),wp(255),knows_ironflesh_7|knows_power_strike_9|knows_athletics_9|knows_riding_9,bandit_face1|knows_shield_8, bandit_face2],

  #extra_end
  #outlaw end
  ["manhunt_squire","manhunt_squire","manhunt_squire",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_manhunters,
   [itm_mail_chausses,itm_bastard_sword_b,itm_surcoat_over_mail_blue,itm_mail_with_surcoat,itm_warhorse_holy,itm_cuirass_on_white,itm_warhorse_blu2,itm_helmet_with_neckguard,itm_bascinet,itm_bascinet_coif_01,itm_sarranid_studded_leather,itm_leather_gloves,
   itm_double_sided_lance,itm_mace_4,itm_sword_viking_2,itm_hunter,itm_tab_shield_heater_cav_a,itm_tab_shield_round_d,itm_shield_kite_i],
   def_guard|level(24),wp(120),knows_ironflesh_4|knows_power_strike_4|knows_athletics_3|knows_riding_5|knows_horse_archery_3|knows_power_draw_3|knows_power_throw_3,bandit_face1, bandit_face2],
  ["manhunt_knight","manhunt_knight","manhunt_knight",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_steel_shield,itm_sword_medieval_d_long,itm_morningstar,itm_warhammer,itm_mackie_bastard,itm_sword_of_war,itm_xeno_war_pick01,itm_mackie_kriegsmesser,itm_shield_kite_i,itm_jousting_lance,itm_warhorse,itm_wlong1,
   itm_heraldic_mail_with_surcoat,itm_gauntlets,itm_iron_greaves,itm_steel_gauntlets,itm_armet_04,itm_brigandine_plate_heraldic,itm_steel_boots_01,itm_plate_boots,itm_iron_greaves,itm_charger],
   str_22 | agi_17 | int_8 | cha_8|level(33),wp(200),knows_ironflesh_7|knows_power_strike_5|knows_athletics_7|knows_riding_7|knows_horse_archery_6|knows_power_draw_7|knows_power_throw_6,bandit_face1, bandit_face2],
  ["manhunt_knight_b","manhunt_knight","manhunt_knight",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_iron_greaves,itm_wbardedshort4,itm_gauntlets,itm_steel_bolts,itm_spak_crsb01,itm_early_transitional_blue,itm_early_transitional_banner,itm_early_transitional_orange,itm_frenchpepperpot2,itm_west_man_at_arms_open_f,itm_west_man_at_arms_closed_f,itm_steel_greaves,itm_finger_gauntlets,itm_charger,
   itm_ganquang_pick,itm_warhammer,itm_ganquang_axe,itm_ganquang_morningstar,itm_sp_2hsw,itm_armet_04,itm_steel_shield_kite,itm_steel_shield_heater,itm_caveirabastard,itm_2imperial_warhorse,itm_lance_6],
   def_knight_1|level(40),wp(255),knows_ironflesh_8|knows_power_strike_8|knows_athletics_8|knows_riding_9|knows_horse_archery_9,bandit_face1, bandit_face2],

  ["volunteer","Volunteer","Volunteer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_mace_3,itm_falchion,itm_winged_mace,itm_skullcap,itm_leather_vest,itm_wooden_shield,itm_wrapping_boots],
   def_farmer|level(5),wp(45),knows_common,bandit_face1, bandit_face2],
  ["city_guard","City Guard","City Guard",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_winged_mace,itm_helmet_with_neckguard,itm_padded_cloth,itm_leather_covered_round_shield,itm_wooden_shield,itm_nomad_boots,itm_pike],
   def_footman|level(11),wp(65),knows_common,bandit_face1, bandit_face2],
  ["city_guard_veteran","City Guard Veteran","City Guard Veteran",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_tab_shield_heater_c,itm_tab_shield_heater_b,itm_light_leather_boots,itm_battle_fork,itm_studded_leather_coat,itm_segmented_helmet,itm_norman_helmet,itm_leather_boots,itm_mace_3,itm_spiked_mace],
   def_fighter|level(17),wp(95),knows_athletics_2|knows_ironflesh_2|knows_power_draw_2|knows_power_strike_2|knows_riding_1,bandit_face1, bandit_face2],
  ["city_elite_guard","City Elite Guard","City Elite Guard",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_manhunters,
   [itm_mail_long_surcoat_new_b3,itm_bascinet_coif_01,itm_tab_shield_heater_cav_b,itm_tab_shield_heater_d,itm_awlpike_long,itm_sword_medieval_d_long,itm_military_cleaver_b,itm_bascinet_2,itm_splinted_greaves,itm_leather_gloves,itm_mail_mittens],
   def_guard|level(24),wp(135),knows_athletics_3|knows_ironflesh_4|knows_power_draw_3|knows_power_strike_3|knows_riding_4,bandit_face1, bandit_face2],
  ["city_guard_captain","City Guard Captain","City Guard Captain",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_manhunters,
   [itm_military_hammer,itm_morningstar,itm_sarranid_axe_a,itm_steel_shield,itm_maciejowski_helmet_new_b,itm_steel_gauntlets,itm_brig_plate_blue,itm_sallet_01,itm_steel_boots_01],
   def_champion|level(30),wp(185),knows_athletics_6|knows_ironflesh_6|knows_power_draw_6|knows_power_strike_6|knows_riding_4,bandit_face1, bandit_face2],

  ["city_patroller","City patroller","City patroller",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_black_gambeson_a,itm_shield_kite_h,itm_war_spear,itm_mail_coif,itm_saddle_horse,itm_hide_boots,itm_falchion],
   def_footman|level(11),wp(60),knows_athletics_1|knows_ironflesh_1|knows_power_draw_1|knows_power_strike_1|knows_riding_3,bandit_face1, bandit_face2],
  ["city_patroller_veteran","City patroller veteran","City patroller veteran",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_bascinet,itm_cuirass_on_black,itm_bascinet_coif_01,itm_warhorse_ylw2,itm_mackie_morning_star,itm_shield_kite_h,itm_awlpike,itm_mail_chausses,itm_mail_mittens],
   def_fighter|level(17),wp(80),knows_athletics_1|knows_ironflesh_2|knows_power_draw_1|knows_power_strike_1|knows_riding_4,bandit_face1, bandit_face2],
  ["constable","Constable","Constable",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_great_helmet,itm_mail_long_surcoat_new3,itm_steel_gauntlets,itm_steel_boots_01,itm_xeno_war_pick01,itm_shield_kite_h,itm_awlpike_long,itm_charger,itm_warhorse_holy],
   def_guard|level(26),wp(125),knows_athletics_3|knows_ironflesh_4|knows_power_draw_3|knows_power_strike_3|knows_riding_5,bandit_face1, bandit_face2],
  
  ["manhunter_0","Manhunter New","Manhunter New",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_club_with_spike_head,itm_segmented_helmet,itm_tribal_warrior_outfit,itm_nordic_shield,itm_leather_boots,itm_leather_gloves,itm_khergit_leather_boots,itm_steppe_horse],
   def_fighter|level(16),wp(100),knows_common,bandit_face1, bandit_face2],
  ["manhunter","Manhunter","Manhunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_sledgehammer,itm_spiked_mace,itm_mail_hauberk,itm_bascinet_2,itm_bascinet_3,itm_mail_mittens,itm_tab_shield_round_d,itm_mail_chausses,itm_splinted_leather_greaves,itm_hunter],
   str_17 | agi_12 | int_7 | cha_7|level(22),wp(120),knows_athletics_3|knows_ironflesh_2|knows_power_draw_3|knows_power_strike_3|knows_riding_3,bandit_face1, bandit_face2],
  ["manhunter_elite","Manhunter Elite","Manhunters Elite",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_military_hammer,itm_warhammer,itm_brig_plate_black,itm_steel_shield,itm_scale_gauntlets,itm_mail_mittens,itm_guard_helmet,itm_mail_boots,itm_splinted_greaves,itm_warhorse],
   str_20 | agi_15 | int_7 | cha_7|level(28),wp(160),knows_athletics_5|knows_ironflesh_4|knows_power_draw_5|knows_power_strike_4|knows_riding_5,bandit_face1, bandit_face2],

  ##  ["deserter","Deserter","Deserters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_swadian_deserters,
##   [itm_arrows,itm_spear,itm_fighting_pick,itm_short_bow,itm_sword,itm_voulge,itm_nordic_shield,itm_round_shield,itm_kettle_hat,itm_leather_cap,itm_padded_cloth,itm_leather_armor,itm_scale_armor,itm_saddle_horse],
##   def_attrib|level(12),wp(60),knows_common,bandit_face1, bandit_face2],

#fac_slavers
#  ["slave_keeper","Slave Keeper","Slave Keepers",tf_guarantee_armor ,0,0,fac_slavers,
#   [itm_cudgel,itm_club,itm_woolen_cap,itm_rawhide_coat,itm_coarse_tunic,itm_nomad_armor,itm_nordic_shield,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
#   def_attrib|level(10),wp(60),knows_common,bandit_face1, bandit_face2],

  # ["slave_driver_0","slavehunter","slavehunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_slavers,
  #  [itm_mace_3,itm_winged_mace,itm_nasal_helmet,itm_padded_cloth,itm_aketon_green,itm_aketon_green,itm_wooden_shield,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
  #  def_attrib|level(10),wp(50),knows_common,bandit_face1, bandit_face2],
  # ["slave_driver","Slave Driver","Slave Drivers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse ,0,0,fac_slavers,
  #  [itm_club_with_spike_head,itm_segmented_helmet,itm_tribal_warrior_outfit,itm_nordic_shield,itm_leather_boots,itm_leather_gloves,itm_khergit_leather_boots,itm_steppe_horse],
  #  def_fighter|level(14),wp(80),knows_common,bandit_face1, bandit_face2],
  # ["slave_hunter","Slave Hunter","Slave Hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
  #  [itm_winged_mace,itm_maul,itm_kettle_hat,itm_mail_shirt,itm_tab_shield_round_c,itm_leather_boots,itm_leather_gloves,itm_courser],
  #  def_swordsman|level(18),wp(90),knows_common,bandit_face1, bandit_face2],
  # ["slave_crusher","Slave Crusher","Slave Crushers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
  #  [itm_sledgehammer,itm_spiked_mace,itm_mail_hauberk,itm_bascinet_2,itm_bascinet_3,itm_mail_mittens,itm_tab_shield_round_d,itm_mail_chausses,itm_splinted_leather_greaves,itm_hunter],
  #  str_17 | agi_11 | int_7 | cha_7|level(22),wp(110),knows_common|knows_riding_4|knows_power_strike_3,bandit_face1, bandit_face2],
  # ["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_slavers,
  #  [itm_military_hammer,itm_warhammer,itm_brigandine_red,itm_steel_shield,itm_scale_gauntlets,itm_mail_mittens,itm_guard_helmet,itm_plate_boots,itm_mail_boots,itm_warhorse],
  #  def_guard|level(26),wp(135),knows_common|knows_riding_4|knows_power_strike_5,bandit_face1, bandit_face2],

#Rhodok tribal, Hunter, warrior, veteran, warchief

#wabbaer
  ["phantom_of_wabbaer","Phantom of Wabbaer","Phantom of Wabbaer",tf_undead|tf_mounted|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_wabber,
  [itm_ganquang_melee,itm_barbuta_b_2,itm_obsidianaxe,itm_sp_shr1,itm_ak_wlocznie_b,itm_twiligh_armor,itm_twilight_gloves,itm_twilight_boots,itm_ripper_chain], 
  str_50 | agi_12 |level(45),wp(150),knows_athletics_1|knows_ironflesh_10|knows_power_strike_5|knows_riding_7|knows_shield_5,0x0000000180000000000000000000000000000000000000000000000000000000],

  ["pilgrim_of_wabbaer","Wabbaer Pilgrim","Wabbaer Pilgrim",tf_guarantee_armor ,0,0,fac_wabber,
   [itm_ankle_boots,itm_wooden_stick,itm_wrapping_boots,itm_robe,itm_coarse_tunic,itm_leather_apron,itm_woolen_cap,itm_straw_hat,itm_pitch_fork,itm_staff],
   def_farmer|level(5),wp(30),knows_common,bandit_face1, bandit_face2],
  ["wabbaer_follower","Wabbaer Follower","Wabbaer Follower",tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet ,0,0,fac_wabber,
   [itm_hunting_crossbow,itm_bolts,itm_black_hood,itm_bamboo_spear,itm_quarter_staff,itm_wooden_shield,itm_leather_covered_round_shield,itm_club_with_spike_head,itm_sword_medieval_b_small,
   itm_leather_vest,itm_leather_cap,itm_black_gambeson_a,itm_padded_cloth,itm_leather_jerkin,itm_hood_b,itm_winged_mace,itm_hammer,itm_ankle_boots,itm_leather_boots],
   def_footman|level(12),wp(60),knows_common,bandit_face1, bandit_face2],
  ["wabbaer_worshiper","Wabbaer Worshiper","Wabbaer Worshiper",tf_undead|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet ,0,0,fac_wabber,
   [itm_leather_gloves,itm_mail_coif,itm_segmented_helmet,itm_flat_topped_helmet,itm_mail_long_surcoat_new_f,itm_leather_boots,itm_splinted_leather_greaves,
   itm_voulge,itm_hafted_blade_a,itm_iron_staff,itm_xeno_war_pick02,itm_pickaxe],
   def_swordsman|level(20),wp(90),knows_ironflesh_4,bandit_face1, bandit_face2], 
  ["wabbaer_grace_receiver","Wabbaer Worshiper","Wabbaer Worshiper",tf_undead|tf_allways_fall_dead|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet ,0,0,fac_wabber,
   [itm_ak_wlocznie_d,itm_ak_poleaxe,itm_mackie_bastard,itm_steel_mittens,itm_steel_boots_01,itm_brig_plate_black,itm_bascinet_coif_01,itm_brigandine_heraldic,
   itm_great_helmet_newj,itm_poleaxe,itm_sarranid_two_handed_axe_b,itm_great_bardiche,itm_guard_helmet,itm_bascinet_2,itm_coat_of_plates],
   str_40 | agi_9 |level(30),wp(120),knows_ironflesh_6|knows_power_strike_2,bandit_face1, bandit_face2], 

#undead  
  ["undead_walker","Undead Walker","Undead Walkers",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
  [itm_human_meat,itm_mackie_beefsplitter01,itm_war_spear,itm_mackie_bat,itm_mackie_pendulum_axe,itm_shk_01,itm_tab_shield_round_a,itm_tab_shield_kite_a,itm_wooden_shield,itm_one_handed_war_axe_a,itm_hand_axe,itm_axe,itm_battle_fork,itm_wooden_stick,
  itm_hide_boots,itm_mackie_tomahawk,itm_hide_covered_round_shield,itm_rawhide_coat,itm_hunter_boots,itm_ankle_boots,itm_sarranid_common_dress,itm_nomad_armor,itm_khergit_armor,itm_leather_jacket,itm_turban,itm_vaegir_fur_cap,itm_skullcap,itm_mail_coif], 
  str_20|level(5),wp(60),knows_ironflesh_1,undead_face1, undead_face2],
  ["undead_warrior","Undead Warrior","Undead Warrior",tf_undead|tf_allways_fall_dead|tf_guarantee_armor,0,0,fac_undeads,
  [itm_human_meat,itm_g_pavise_01,itm_mackie_short_voulge,itm_mackie_mangler_short,itm_tab_shield_small_round_a,itm_tab_shield_heater_a,itm_tab_shield_pavise_a,itm_lance,itm_ashwood_pike,itm_sarranid_two_handed_mace_1,itm_mace_4,itm_mace_1,itm_sword_khergit_2,
  itm_sword_viking_2,itm_mackie_tomahawk,itm_sword_medieval_c_small,itm_shortened_military_scythe,itm_two_handed_battle_axe_2,
  itm_mail_coif,itm_footman_helmet,itm_fur_hat,itm_spiked_helmet,itm_desert_turban,itm_turban,itm_nordic_archer_helmet,itm_vaegir_fur_helmet,itm_ragged_outfit,itm_skirmisher_armor,itm_nordic_helmet,itm_nordic_footman_helmet,itm_leather_boots], 
  str_25|level(13),wp(75),knows_ironflesh_3,undead_face1, undead_face2],
  ["undead_strong_warrior","Undead Strong Warrior","Undead Strong Warrior",tf_undead|tf_allways_fall_dead|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_undeads,
  [itm_human_meat,itm_leather_armor_padded,itm_spiked_helmet,itm_nordic_footman_helmet,itm_vaegir_lamellar_helmet,itm_kettle_hat,itm_sarranid_horseman_helmet,itm_nomad_robe,itm_sarranid_cavalry_robe,itm_nordic_helmet,itm_vaegir_noble_helmet,itm_mail_shirt,itm_splinted_greaves,
  itm_mackie_mangler_short,itm_mackie_bearded_axe,itm_mackie_mangler,itm_mackie_mangler_short,itm_tab_shield_kite_d,itm_tab_shield_round_c,itm_tab_shield_pavise_c,itm_plate_covered_round_shield,itm_awlpike,itm_military_scythe,itm_sword_khergit_4,
  itm_sword_medieval_c_long,itm_long_axe_b_alt,itm_bardiche,itm_two_handed_cleaver,itm_war_axe,itm_mail_mittens,itm_zombi_horse], 
  str_30|level(20),wp(95),knows_ironflesh_4|knows_riding_2,undead_face1, undead_face2],
  ["undead_armored_soldier","Undead Armored Soldier","Undead Armored Soldier",tf_undead|tf_allways_fall_dead|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet,0,0,fac_undeads,
  [itm_human_meat,itm_surcoat_over_mail,itm_sword_of_war,itm_arabian_sword_d,itm_scimitar_b,itm_morningstar,itm_tab_shield_pavise_d,itm_tab_shield_round_e,itm_steel_shield,itm_heraldic_mail_with_surcoat,itm_arabian_armor_b,itm_cuir_bouilli,itm_brigandine_red,itm_lamellar_armor,
  itm_khergit_sword_two_handed_b,itm_guard_helmet,itm_vaegir_war_helmet,itm_nordic_huscarl_helmet,itm_khergit_war_helmet,itm_strange_great_sword,itm_awlpike_long,itm_sarranid_two_handed_axe_b,itm_sarranid_mace_1,itm_long_spiked_club,itm_iron_staff,itm_sarranid_royal_helmet,
  itm_sword_medieval_d_long,itm_hafted_blade_a,itm_long_bardiche,itm_military_cleaver_c,itm_bastard_sword_b,itm_iron_greaves,itm_splinted_greaves,itm_lamellar_gauntlets,itm_scale_gauntlets,itm_zombi_horse], 
  str_35|level(25),wp(110),knows_ironflesh_5|knows_power_strike_1|knows_riding_3,undead_face1, undead_face2],

  ["undead_champion","Undead Champion","Undead Champion",tf_undead|tf_mounted|tf_allways_fall_dead|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_undeads,
  [itm_human_meat,itm_black_greaves,itm_gauntlets,itm_black_armor,itm_black_helmet,itm_military_hammer,itm_sword_two_handed_a,itm_sword_medieval_d_long,itm_great_lance,itm_steel_shield,itm_mackie_kriegsmesser,itm_mackie_morning_star_long,itm_ak_wlocznie_c,itm_ak_wlocznie_b,itm_zombi_horse], 
  str_55|level(35),wp(140),knows_ironflesh_8|knows_power_strike_2|knows_riding_5,undead_face1, undead_face2],

  ["undead_giant","Undead Giant","Undead Giant",tf_giant|tf_allways_fall_dead|tf_guarantee_helmet,0,0,fac_undeads,
  [itm_human_meat,itm_poleaxe,itm_polehammer,itm_black_greaves,itm_black_greaves,itm_gauntlets,itm_g_helm_spak2], 
  str_150|level(55),wp(150),knows_ironflesh_14|knows_power_strike_2|knows_riding_1,undead_face1, undead_face2],

  ["skeleton_new","Skeleton","Skeletons",tf_skeleton|tf_allways_fall_dead|tf_guarantee_ranged,0,0,fac_undeads,
  [itm_hunting_bow,itm_arrows], str_3|agi_3|level(1),wp(30),knows_athletics_2,undead_face1, undead_face2],
  ["skeleton_soilder","Skeleton","Skeletons",tf_skeleton|tf_allways_fall_dead|tf_guarantee_ranged,0,0,fac_undeads,
  [itm_wooden_stick,itm_hunting_bow,itm_arrows,itm_barf_skeleton_greaves,itm_skullcap], str_6|agi_4|level(5),wp(60),knows_power_strike_1|knows_athletics_4|knows_power_draw_2,undead_face1, undead_face2],
  ["skeleton_archer","Skeleton","Skeletons",tf_skeleton|tf_allways_fall_dead|tf_guarantee_ranged,0,0,fac_undeads,
  [itm_sword_medieval_a,itm_short_bow,itm_arrows,itm_nasal_helmet,itm_barf_skeleton_armor,itm_norman_helmet,itm_flat_topped_helmet], 
  str_9|agi_4|level(12),wp(85),knows_power_strike_2|knows_athletics_8|knows_power_draw_3,undead_face1, undead_face2],
  ["skeleton_high_archer","Skeleton","Skeletons",tf_skeleton|tf_allways_fall_dead|tf_guarantee_ranged,0,0,fac_undeads,
  [itm_sword_medieval_c,itm_long_bow,itm_arrows,itm_spiked_helmet,itm_bascinet,itm_barf_skeleton_armor_full], 
  str_15|agi_10|level(21),wp(120),knows_power_strike_3|knows_athletics_10|knows_power_draw_5,undead_face1, undead_face2],
  ["skeleton_knight","Skeleton","Skeletons",tf_mounted|tf_skeleton|tf_guarantee_all|tf_allways_fall_dead|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_undeads,
  [itm_long_bow,itm_arrows,itm_barf_skeleton_armor_full,itm_barf_skeletal_horse,itm_mackie_bat,itm_mackie_bat_nailed,itm_mackie_bastard,itm_black_helmet,itm_plate_covered_round_shield], 
  str_21|agi_12|level(30),wp(150),knows_power_strike_4|knows_athletics_10|knows_power_draw_6|knows_riding_10|knows_ironflesh_5,undead_face1, undead_face2],
  ["skeleton_knight_e","Skeleton","Skeletons",tf_mounted|tf_skeleton|tf_allways_fall_dead|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_undeads,
  [itm_twiligh_armor,itm_twilight_gloves,itm_twilight_boots,itm_henryv_helm_black,itm_pa_axe_02,itm_pa_sword_04,itm_pa_sword_02,itm_pa_sword_03,itm_asmoday_seel,itm_whg2], 
  str_50|agi_50|level(65),wp(300),knows_power_strike_11|knows_athletics_10|knows_shield_8|knows_riding_10|knows_ironflesh_11,undead_face1, undead_face2],
  ["skeleton_knight_s","Skeleton","Skeletons",tf_mounted|tf_skeleton|tf_allways_fall_dead|tf_guarantee_horse|tf_guarantee_armor|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_gloves,0,0,fac_undeads,
  [itm_twilight_boots_g,itm_twilight_gloves_g,itm_order_charge,itm_twiligh_armor_ghost,itm_demon_hood_ghost,itm_bastard_sword_b_ghost,itm_denethor_shield_ghost], 
  str_80|agi_80|int_35|cha_35|level(75),wp(400),knows_power_strike_12|knows_athletics_10|knows_shield_10|knows_riding_12|knows_ironflesh_12,undead_face1, undead_face2],

  ["askr_undead_warrior","askr_horse_warrior","askr_horse_warriors",tf_mounted|tf_giant|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_gloves,0,0,fac_askr,
   [itm_czarne_gauntlets,itm_spak_coat_of_plates_b,itm_czarne_platebut,itm_helm_b_crusher_b_01,itm_northerner_horse_hunter,itm_luc_two_handed_axe_2,itm_luc_axe_knight_z,itm_plate_covered_round_shield],
   str_75 | agi_25|level(60),wp(150),knows_ironflesh_12|knows_power_strike_12|knows_riding_5|knows_shield_5,undead_face1],
  ["askr_undead_warrior_f","askr_horse_warrior","askr_horse_warriors",tf_giant|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_askr,
   [itm_czarne_gauntlets,itm_spak_coat_of_plates_b,itm_czarne_platebut,itm_helm_b_crusher_b_01,itm_ganquang_great_sword_1,itm_ganquang_melee,itm_ganquang_melee],
   str_75 | agi_25|level(60),wp(150),knows_ironflesh_12|knows_power_strike_12|knows_power_throw_12,undead_face1],
  ["askr_undead_warrior_n","askr_horse_warrior","askr_horse_warriors",tf_giant|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_askr,
   [itm_ak_wlocznie_d,itm_ak_wlocznie_c,itm_mail_boots,itm_g_scale_gauntlets_a,itm_splate_armor2],
   str_75 | agi_25|level(45),wp(150),knows_ironflesh_10|knows_power_strike_10,undead_face1],
  ["askr_undead_warrior_b","askr_horse_warrior","askr_horse_warriors",tf_giant|tf_allways_fall_dead,0,0,fac_askr,
   [itm_polehammer],
   str_55 | agi_10|level(25),wp(150),knows_ironflesh_6|knows_power_strike_6,undead_face1],

  ["caprine_dead_wild_hunt_warrior","Caprine Wild Hunt Warrior","Caprine Wild Hunt Warrior",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_undead|tf_guarantee_horse|tf_allways_fall_dead ,0,0,fac_caprine,
   [itm_wolf_helm4,itm_elite_cavalary,itm_bear_boots,itm_beargauntlets,itm_leather_gloves,itm_asmoday_sword,itm_sp_shr1,itm_nibbler],
   str_35 | agi_20 | int_8 | cha_8|level(35),wp(200),knows_ironflesh_6|knows_power_strike_6|knows_riding_5|knows_shield_2,undead_face1],

  ["dark_swordman","Dark Swordman","Dark Swordmen",tf_undead|tf_allways_fall_dead|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_destroyer,
   [itm_jack_faramir_shield,itm_jack_faramir,itm_demon_hood,itm_demonrobe,itm_blackleather_boots_a,itm_blackscale_gauntlets_a],
   str_55 | agi_8|level(35),wp(200),knows_ironflesh_8|knows_shield_6|knows_power_strike_8|knows_athletics_5,bandit_face1, bandit_face2],
  ["dark_spearman","Dark Spearman","Dark Spearmen",tf_undead|tf_allways_fall_dead|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_destroyer,
   [itm_sp_shr1,itm_blood_spear,itm_black_helmet,itm_spak_coat_of_plates_a,itm_black_greaves,itm_blackscale_gauntlets_b],
   str_55 | agi_8|level(35),wp(230),knows_ironflesh_8|knows_shield_6|knows_power_strike_8|knows_athletics_5,bandit_face1, bandit_face2],
  ["dark_horseman","Dark Horseman","Dark Horseman",tf_undead|tf_allways_fall_dead|tf_mounted|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_destroyer,
   [itm_sp_shr1,itm_blood_spear,itm_black_helmet,itm_coat_of_plates,itm_black_greaves,itm_blackgauntlets,itm_zombi_horse,itm_asmoday_sword,itm_lightedge_spak_black],
   str_55 | agi_8|level(35),wp(200),knows_ironflesh_8|knows_shield_6|knows_power_strike_8|knows_athletics_5|knows_riding_5,bandit_face1, bandit_face2],
  
  ["gulfod_nobleman_knight1_un","Gulfod dead knight","Gulfod dead knight",tf_undead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_roskel,
   [itm_sallet_b_closed1,itm_sallet_b_closed2,itm_marmont_armor,itm_dorn_spearbearer_boots,itm_dorn_spearbearer_guant,itm_luc_knightly_axe_two_handed,itm_long_rifle,itm_cartridges],
   str_55 | agi_8|level(38),wp(180),knows_ironflesh_8|knows_shield_2|knows_power_strike_8|knows_athletics_8,rhodok_face_middle_1, rhodok_face_older_2],
  ["gulfod_nblack_knight_un","Gulfod dead knight","Gulfod dead knights",tf_undead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_roskel,
   [itm_gothic_plate_black,itm_blackgauntlets,itm_sallet_b_closed1,itm_sallet_b_closed2,itm_black_greaves,itm_riper,itm_lightedge_spak_black,itm_pistol,itm_cartridges],
   str_65 | agi_8|level(45),wp(200),knows_ironflesh_9|knows_shield_8|knows_power_strike_8|knows_athletics_8|knows_riding_10,rhodok_face_middle_1, rhodok_face_older_2],

  ["undead_end","Undead End","Undead End",tf_giant|tf_allways_fall_dead|tf_guarantee_helmet,0,0,fac_undeads,
  [], 
  str_20|level(35),wp(125),knows_ironflesh_8|knows_power_strike_2|knows_riding_5,undead_face1, undead_face2],
#caprine
  ["caprine_hunter","Caprine Hunter","Caprine Hunter",tf_guarantee_boots|tf_guarantee_armor ,0,0,fac_caprine,
   [itm_hide_boots,itm_fur_coat,itm_fur_hat,itm_falchion,itm_shortened_spear,itm_arrows,itm_arrows,itm_short_bow],
   def_footman|level(10),wp(60),knows_common,bandit_face1, bandit_face2],
  ["caprine_senior_hunter","Caprine Senior Hunter","Caprine Senior Hunter",tf_guarantee_boots|tf_guarantee_armor ,0,0,fac_caprine,
   [itm_hide_boots,itm_nomad_boots,itm_nomad_cap,itm_leather_jerkin,itm_war_spear,itm_fur_hat,itm_falchion,itm_scimitar,itm_arrows,itm_barbed_arrows,itm_arrows,itm_nomad_bow,itm_short_bow],
   def_fighter|level(15),wp(90),knows_ironflesh_1|knows_power_draw_2|knows_power_strike_2|knows_athletics_2,bandit_face1, bandit_face2],
  ["caprine_archer","Caprine Archer","Caprine Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged ,0,0,fac_caprine,
   [itm_leather_boots,itm_tribal_warrior_outfit,itm_leather_cap,itm_vaegir_fur_cap,itm_pike,itm_sarranid_two_handed_axe_a,itm_bastard_sword_b,itm_arrows,itm_barbed_arrows,itm_bodkin_arrows,itm_long_bow,itm_khergit_bow],
   str_17 | agi_12 | int_7 | cha_7|level(22),wp(120),knows_ironflesh_3|knows_power_draw_4|knows_power_strike_3|knows_athletics_3,bandit_face1, bandit_face2],
  ["caprine_marksman","Caprine Marksman","Caprine Marksman",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged ,0,0,fac_caprine,
   [itm_splinted_leather_greaves,itm_studded_leather_coat,itm_vaegir_fur_helmet,itm_ashwood_pike,itm_leather_gloves,itm_sword_two_handed_a,itm_military_sickle_a,itm_arrows,itm_bodkin_arrows,itm_war_bow,itm_strong_bow],
   str_20 | agi_15 | int_7 | cha_7|level(28),wp(165),knows_ironflesh_5|knows_power_draw_6|knows_power_strike_6|knows_athletics_6,bandit_face1, bandit_face2],
  ["caprine_wild_hunt_warrior","Caprine Wild Hunt Warrior","Caprine Wild Hunt Warrior",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged ,0,0,fac_caprine,
   [itm_bear_warior_helm,itm_wolf_helm4,itm_elite_cavalary,itm_bear_boots,itm_beargauntlets,itm_leather_gloves,itm_bow3_spak,itm_spak_bow7,itm_lonely_ar,itm_bow3_arr_spak,itm_bodkin_arrows,itm_two_handed_axe,itm_mackie_bastard,itm_flamberg],
   def_knight|level(35),wp(200),knows_ironflesh_6|knows_power_draw_8|knows_power_strike_7|knows_athletics_7,bandit_face1, bandit_face2],
  ["caprine_wild_hunt_champion","Caprine Wild Hunt Champion","Caprine Wild Hunt Champion",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged ,0,0,fac_caprine,
   [itm_wolf_helm1,itm_wolf_helm3,itm_elite_cavalary,itm_bear_boots,itm_beargauntlets,itm_duskfall,itm_bow3_arr_spak,itm_lonely_ar,itm_ak_miecz_mis,itm_lonely_ar],
   str_35 | agi_25 | int_10 | cha_10|level(45),wp(250),knows_ironflesh_8|knows_power_draw_10|knows_power_strike_10|knows_athletics_8,bandit_face1, bandit_face2],
#khanjat
  ["khanjat_recruit","khanjat_recruit","khanjat_recruit",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_ranged ,0,0,fac_khanjat,
   [itm_leather_gloves,itm_hide_boots,itm_hunter_boots,itm_wei_xiadi_kher_lamellar_vest02,itm_mongol_helmet_x,itm_light_lance,itm_falchion,itm_arrows,itm_arrows,itm_nomad_bow,itm_courser,itm_steppe_horse,itm_steppe_horse,itm_wooden_shield],
   def_footman|level(11),wp(80),knows_common|knows_riding_3|knows_power_draw_2,khergit_face_young_1, khergit_face_old_2],
  ["khanjat_horseman","khanjat_horseman","khanjat_horseman",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_ranged ,0,0,fac_khanjat,
   [itm_leather_gloves,itm_nomad_boots,itm_light_lance,itm_mongol_helmet_x1,itm_mongol_helmet_xh,itm_wei_xiadi_kher_lamellar_vest01,itm_khergit_arrows,itm_arrows,itm_arrows,
   itm_lamellar_charger_a,itm_leather_covered_round_shield,itm_hide_covered_round_shield,itm_khergit_bow,itm_khalradia_swordc],
   def_swordsman|level(20),wp(125),knows_ironflesh_2|knows_power_draw_3|knows_horse_archery_3|knows_power_strike_3|knows_riding_6,khergit_face_young_1, khergit_face_old_2],
  ["khanjat_warrior","khanjat_warrior","khanjat_warrior",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_ranged ,0,0,fac_khanjat,
   [itm_leather_gloves,itm_khergit_leather_boots,itm_wei_xiadi_lamellar_armor01,itm_mongol_helmet_xe,itm_mongol_helmet_xh1,itm_khergit_arrows,itm_arrows,
   itm_rohan_spear,itm_easterling_warhorse01,itm_plate_covered_round_shield,itm_strong_bow,itm_khalradia_sworda],
   str_19 | agi_15 | int_7 | cha_7|level(27),wp(155),knows_ironflesh_3|knows_power_draw_5|knows_horse_archery_6|knows_power_strike_5|knows_riding_7,khergit_face_young_1, khergit_face_old_2],
  ["khanjat_champion","khanjat_champion","khanjat_champion",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_helmet|tf_guarantee_ranged ,0,0,fac_khanjat,
   [itm_leather_gloves,itm_sarranid_boots_c,itm_mongol_armor_heavy,itm_mongol_helmet_xg2,itm_khergit_arrows,itm_khergit_arrows,itm_rohan_spear,itm_sarranid_warhorse1,itm_sarranid_warhorse2,itm_brass_shield1,itm_spak_bow7,itm_khalradia_2hander_b],
   str_23 | agi_16 | int_8 | cha_8|level(33),wp(185),knows_ironflesh_5|knows_power_draw_6|knows_horse_archery_6|knows_power_strike_7|knows_riding_9,khergit_face_young_1, khergit_face_old_2],

  ["khanjat_guard_0","khanjat_champion","khanjat_champion",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves ,0,0,fac_khanjat,
   [itm_wei_xiadi_nord_lamellar_purple,itm_sp_pikea,itm_nomad_boots,itm_khergit_guard_helmet,itm_lamellar_gauntlets],
   def_champion|level(25),wp(175),knows_ironflesh_6|knows_power_strike_6|knows_athletics_6,khergit_face_young_1, khergit_face_old_2],
  ["khanjat_guard","khanjat_champion","khanjat_champion",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves ,0,0,fac_khanjat,
   [itm_wei_xiadi_samurai_armor01,itm_sp_pikef,itm_mail_boots,itm_mongol_helmet_xf,itm_lamellar_gauntlets],
   str_22 | agi_16 | int_8 | cha_8|level(32),wp(175),knows_ironflesh_6|knows_power_strike_6|knows_athletics_6,khergit_face_young_1, khergit_face_old_2],
  ["khanjat_guard_b","khanjat_champion","khanjat_champion",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves ,0,0,fac_khanjat,
   [itm_wei_xiadi_samurai_armor02,itm_sp_pikee,itm_black_greaves,itm_mask_helmet1,itm_lamellar_gauntlets],
   def_knight_1|level(40),wp(175),knows_ironflesh_8|knows_power_strike_8|knows_athletics_8,khergit_face_young_1, khergit_face_old_2],

#random
["lion_guard","Lion guard","Lion guard",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_adventurer,
   [itm_west_swordsman,itm_new_leather_boots,itm_leather_gauntlets_new,itm_west_heavy_rider_helmet_closed,itm_tab_shield_kite_d,itm_morningstar,itm_hunter,itm_steel_bolts,itm_spak_crsb01],
   def_guard|level(25),wp(150),knows_ironflesh_5|knows_shield_5|knows_power_strike_5|knows_athletics_5|knows_riding_5,bandit_face1, bandit_face2],
["fire_archer","Fire Archer","Fire Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged,0,0,fac_adventurer,
   [itm_fire_arrows,itm_fire_arrows,itm_spak_bow8,itm_new_leather_boots,itm_leather_gauntlets_new,itm_armor_23,itm_montforthelm,itm_gondor_tower_spear,itm_gondor_spear],
   def_champion|level(30),wp(160),knows_ironflesh_5|knows_power_strike_5|knows_athletics_5|knows_power_draw_5,bandit_face1, bandit_face2],

["depravity_member","Depravity member","Depravity members",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_ymira,
   [itm_archers_vest_3,itm_sarranid_boots_c,itm_sarranid_helmet1,itm_leather_gloves,itm_military_scythe],
   def_guard|level(15),wp(100),knows_ironflesh_3|knows_shield_3|knows_power_strike_3|knows_athletics_3,swadian_face_middle_1, swadian_face_older_2],
["depravity_member_f","Depravity member","Depravity members",tf_beautiful|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_ymira,
   [itm_archers_vest_3,itm_sarranid_boots_b,itm_sarranid_horseman_helmet,itm_leather_gloves,itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_tab_shield_small_round_a],
   def_guard|level(15),wp(85),knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_2|knows_power_draw_2,swadian_face_middle_1, swadian_face_older_2],
["depravity_guard","Depravity guard","Depravity guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_ymira,
   [itm_sarranid_mail_shirt6,itm_sarranid_boots_d,itm_sarranid_veiled_helmet,itm_lamellar_gauntlets,itm_ak_wlocznie_d],
   def_guard|level(25),wp(145),knows_ironflesh_6|knows_shield_6|knows_power_strike_6|knows_athletics_6,swadian_face_middle_1, swadian_face_older_2],
["depravity_guard_f","Depravity guard","Depravity guards",tf_beautiful|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_ymira,
   [itm_sarranid_mail_shirt5,itm_sarranid_boots_b,itm_sarranid_mail_coif,itm_leather_gloves,itm_bodkin_arrows,itm_strong_bow,itm_sarranid_cavalry_sword,itm_tab_shield_small_round_b],
   def_guard|level(25),wp(135),knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_4|knows_power_draw_4,swadian_face_middle_1, swadian_face_older_2],
#magic
["magic_apprentice","Spprentice","Apprentice",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_wizard,
   [itm_ankle_boots,itm_wrapping_boots,itm_staff,itm_robe,itm_protect_1],
   def_footman|level(10),wp(100),knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_1|knows_shield_1,bandit_face1, bandit_face2],
["wizard","Wizard","Wizard",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_wizard,
   [itm_leather_boots,itm_quarter_staff,itm_courtly_outfit,itm_nobleman_outfit,itm_protect_2],
   def_footman|level(20),wp(130),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_2|knows_riding_4|knows_athletics_3,bandit_face1, bandit_face2],
["wizard_e","Wizard","Wizard",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_wizard,
   [itm_rus_cav_boots,itm_iron_staff,itm_rich_outfit,itm_protect_3],
   def_footman|level(30),wp(160),knows_ironflesh_6|knows_power_strike_6|knows_power_throw_2|knows_riding_6|knows_athletics_5,bandit_face1, bandit_face2],

["dark_apprentice","Dark Apprentice","Dark Apprentice",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_necromancer,
   [itm_ankle_boots,itm_staff,itm_robe],
   def_footman|level(10),wp(100),knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_1|knows_shield_1,bandit_face1, bandit_face2],
["darkwizard","Dark Wizard","Dark Wizard",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_necromancer,
   [itm_new_leather_boots,itm_quarter_staff,itm_demonrobe0,itm_demon_hood_1],
   def_footman|level(20),wp(145),knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_1|knows_shield_1,bandit_face1, bandit_face2],
["darkwizard_e","Dark Wizard","Dark Wizard",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_necromancer,
   [itm_rus_cav_boots,itm_iron_staff,itm_demonrobe,itm_demon_hood],
   def_footman|level(30),wp(180),knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_1|knows_shield_1,bandit_face1, bandit_face2],
#Ortlinde
  ["nord_female","Nord Female","Nord Females",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_ortlinde,
   [itm_hunter_boots,itm_hide_boots,itm_fur_coat,itm_nordic_archer_helmet,itm_nordic_veteran_archer_helmet,
   itm_sword_viking_1,itm_wooden_shield,itm_spear,itm_light_throwing_axes],
   def_footman|level(10),wp(100),knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_1|knows_shield_1,nord_face_young_1, nord_face_old_2],
  ["nord_female_hunter","Nord Female Hunter","Nord Female Hunters",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_ortlinde,
   [itm_leather_gloves,itm_hide_boots,itm_tribal_warrior_outfit,itm_nordic_footman_helmet,
   itm_sword_viking_2_small,itm_nordic_shield,itm_war_spear,itm_light_throwing_axes],
   def_fighter|level(15),wp(120),knows_ironflesh_3|knows_power_strike_3|knows_power_throw_3|knows_riding_2|knows_athletics_3|knows_shield_3,nord_face_young_1, nord_face_old_2],
  ["nord_female_warrior","Nord Female Warrior","Nord Female Warrior",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_ortlinde,
   [itm_leather_gloves,itm_splinted_leather_greaves,itm_byrnie,itm_nordic_fighter_helmet,itm_nordic_helmet,
   itm_sword_viking_3,itm_leather_covered_round_shield,itm_war_spear,itm_throwing_axes],
   str_17 | agi_12 | int_7 | cha_7|level(22),wp(150),knows_ironflesh_8|knows_power_strike_4|knows_power_throw_4|knows_riding_2|knows_athletics_4|knows_shield_5,nord_face_young_1, nord_face_old_2],
  ["nord_war_sister","Nord War Sister","Nord War Sisters",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_ortlinde,
   [itm_mail_mittens,itm_mail_chausses,itm_mail_hauberk,itm_nordic_warlord_helmet,
   itm_sword_viking_3_small,itm_plate_covered_round_shield,itm_heavy_throwing_axes,itm_lance],
   def_champion|level(30),wp(200),knows_ironflesh_7|knows_power_strike_6|knows_power_throw_6|knows_riding_2|knows_athletics_6|knows_shield_6,nord_face_young_1, nord_face_old_2],
  ["nord_valkyrie","Nord Valkyrie","Nord Valkyries",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_ortlinde,
   [itm_mail_mittens,itm_mail_boots,itm_barf_helm,itm_woman,itm_sword_viking_3,itm_steel_shield,itm_heavy_throwing_axes,itm_ak_wlocznie_a,itm_vsword01],
   def_knight_1|level(40),wp(250),knows_ironflesh_8|knows_power_strike_8|knows_power_throw_8|knows_riding_2|knows_athletics_8|knows_shield_9,nord_face_young_1, nord_face_old_2],
  
  ["nord_valkyrie_m","Nord Valkyrie","Nord Valkyries",tf_mounted|tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_ortlinde,
   [itm_mail_mittens,itm_mail_boots,itm_barf_helm,itm_woman,itm_steel_shield,itm_heavy_throwing_axes,itm_ak_wlocznie_a,itm_vsword01,itm_northerner_horse_hunter],
   def_knight_2|level(45),wp(300),knows_ironflesh_9|knows_power_strike_9|knows_power_throw_9|knows_riding_6|knows_athletics_9|knows_shield_9|knows_horse_archery_6,nord_face_young_1, nord_face_old_2],

  #spring_knight
  ["spring_pilgrim","Spring Pilgrim","Spring Pilgrims",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_spring_knight,
   [itm_hosen_green,itm_green_tunic,itm_aketon_green,itm_woolen_cap_newgrn,itm_bastard_sword_a,itm_voulge],
   str_12 | agi_9 | int_6 | cha_6|level(12),wp(100),knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_1|knows_shield_1,bandit_face1, bandit_face2],
  ["spring_warrior","Spring Warrior","Spring Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_spring_knight,
   [itm_mail_with_tunic_green,itm_new_leather_boots,itm_splinted_greaves,itm_flattop_helmet_new_grn,itm_great_sword],
   def_swordsman|level(20),wp(140),knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_1|knows_shield_1,bandit_face1, bandit_face2],
  ["spring_squire","Spring Squire","Spring Squires",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_spring_knight,
   [itm_mail_long_surcoat_flower,itm_lamellar_gauntlets,itm_mail_boots,itm_great_helmet_newflower,itm_sword_two_handed_a,itm_warhorse_grn2],
   def_champion|level(30),wp(175),knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_1|knows_shield_1,bandit_face1, bandit_face2],
  ["spring_knight","Spring Knight","Spring knights",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_spring_knight,
   [itm_early_transitional_flower,itm_steel_boots_01,itm_steel_gauntlets,itm_great_helmet_newflower,itm_wlong3,itm_caveirabastard],
   def_knight_1|level(38),wp(210),knows_ironflesh_7|knows_power_strike_7|knows_riding_7|knows_athletics_7|knows_shield_1,bandit_face1, bandit_face2],
  ["spring_lake_guard","Spring lake guard","Spring lake guards",tf_mounted|tf_guarantee_horse|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet,0,0,fac_spring_knight,
   [itm_cloak_early_transitional_flower_magic,itm_cloak_early_transitional_flower,itm_steel_boots_01,itm_steel_gauntlets,itm_teutonichelm_flower,itm_wplatedcharger5,itm_caveirabastard_magic],
   def_knight_2|level(45),wp(255),knows_ironflesh_9|knows_power_strike_8|knows_riding_10|knows_athletics_10,bandit_face1, bandit_face2],
  
  ["spring_knight_f","Spring Knight","Spring knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_spring_knight,
   [itm_early_transitional_banner,itm_steel_boots_01,itm_steel_gauntlets,itm_great_helmet_newflower,itm_caveirabastard,itm_war_bow,itm_new1,itm_new1,itm_wlong3],
   def_knight_1|level(40),wp(240),knows_ironflesh_7|knows_power_strike_7|knows_athletics_6|knows_power_draw_8|knows_horse_archery_8|knows_riding_7,bandit_face1, bandit_face2],

  #demonhunter
  ["demonhunterapprentice","demonhunterapprentice","demonhunterapprentice",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_demon_hunter,
   [itm_light_leather,itm_light_leather_boots,itm_leather_gloves,itm_flat_topped_helmet,itm_bolts,itm_crossbow,itm_heavy_crossbow,itm_tab_shield_pavise_b,itm_sword_medieval_c],
   def_fighter|level(15),wp(100),knows_ironflesh_3|knows_power_strike_3|knows_riding_2|knows_athletics_3|knows_shield_3,bandit_face1, bandit_face2],
  ["demonhunter","demonhunter","demonhunter",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_demon_hunter,
   [itm_armor_17,itm_leather_gloves,itm_new_leather_boots,itm_great_helmet,itm_topfhelm,itm_topfhelm5,itm_steel_bolts,itm_heavy_crossbow,itm_sniper_crossbow,itm_tab_shield_pavise_c,itm_sword_medieval_c_long],
   def_guard|level(25),wp(150),knows_ironflesh_5|knows_power_strike_5|knows_riding_2|knows_athletics_5|knows_shield_5,bandit_face1, bandit_face2],
  ["demonhunterveteran","demonhunterveteran","demonhunterveteran",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_demon_hunter,
   [itm_armor_18,itm_leather_gloves,itm_mail_chausses,itm_topfhelm5,itm_topfhelm8,itm_steel_bolts,itm_sniper_crossbow,itm_spak_crsb02,itm_tab_shield_pavise_d,itm_sword_medieval_d_long],
   def_knight|level(35),wp(200),knows_ironflesh_7|knows_power_strike_7|knows_riding_2|knows_athletics_7|knows_shield_7,bandit_face1, bandit_face2],
  ["demonhuntermaster","demonhuntermaster","demonhuntermaster",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_demon_hunter,
   [itm_armor_19,itm_leather_gloves,itm_steel_greaves2,itm_topfhelm7,itm_topfhelm8,itm_teutonichelm_g,itm_van_helsing_crossbow_01,itm_van_helsing_crossbow_bolt,itm_tab_shield_pavise_d,itm_truth],
   str_28 | agi_20 | int_9 | cha_9|level(43),wp(250),knows_ironflesh_10|knows_power_strike_9|knows_riding_9|knows_athletics_9|knows_shield_10,bandit_face1, bandit_face2],
#dragon knight
  ["dragonretinue","dragonretinue","dragonretinue",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_dragon_knight,
   [itm_mail_long_surcoat_new_c3,itm_flintlock_pistol,itm_cartridges,itm_cartridges,itm_leather_boots,itm_luc_english_polehammer,itm_maul,itm_helm11,itm_copy_helm11],
   def_swordsman|level(20),wp(100),knows_ironflesh_3|knows_power_strike_3|knows_riding_2|knows_athletics_3|knows_shield_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["dragoncavalry","dragoncavalry","dragoncavalry",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_dragon_knight,
   [itm_flintlock_rifle,itm_pistol,itm_cartridges,itm_cartridges,itm_splinted_greaves,itm_warhammer,itm_coat_of_plates_g,itm_great_helmet_newe],
   def_champion|level(30),wp(150),knows_ironflesh_5|knows_power_strike_5|knows_riding_2|knows_athletics_5|knows_shield_5,rhodok_face_middle_1, rhodok_face_older_2],
  ["dragonknight","dragonknight","dragonknight",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_dragon_knight,
   [itm_copy_great_helmet_newe,itm_early_transitional_dragon,itm_heavy_muscket1,itm_cartridges1,itm_cartridges1,itm_steel_greaves2,itm_luc_horsemans_hammer],
   def_knight|level(40),wp(200),knows_ironflesh_7|knows_power_strike_7|knows_riding_2|knows_athletics_7|knows_shield_7,rhodok_face_middle_1, rhodok_face_older_2],
  ["dragonknightleader","dragonknightleader","dragonknightleader",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_dragon_knight,
   [itm_copy_sugarloaf_helmet_new2,itm_stonemaul,itm_heavy_muscket2,itm_cartridges1,itm_cartridges1,itm_joan_dragon,itm_dorn_deadshot_gant,itm_dorn_knight_boots_blue],
   def_knight_2|level(45),wp(250),knows_ironflesh_8|knows_power_strike_9|knows_riding_9|knows_athletics_9|knows_shield_9,rhodok_face_middle_1, rhodok_face_older_2],
#sevengod
  ["sevengod_pilgrim","Sevengod Pilgrim","Sevengod Pilgrims",tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_seven_god,
   [itm_pilgrim_disguise,itm_pilgrim_hood,itm_staff],
   def_farmer|level(4),wp(60),knows_common|knows_athletics_1,bandit_face1, bandit_face2],
  ["sevengod_monk","Sevengod Monk","Sevengod Monks",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_seven_god,
   [itm_ragged_outfit,itm_bolts,itm_leather_gloves,itm_ankle_boots,itm_padded_coif,itm_hunting_crossbow,itm_quarter_staff],
   def_footman|level(10),wp(70),knows_ironflesh_1|knows_shield_1|knows_power_strike_2|knows_athletics_1|knows_power_draw_1,bandit_face1, bandit_face2],
  ["sevengod_priest","Sevengod Priest ","Sevengod Priests",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_seven_god,
   [itm_leather_gloves,itm_new_leather_boots,itm_mail_coif,itm_iron_staff,itm_light_crossbow,itm_bolts,itm_studded_leather_coat,itm_ragged_outfit],
   def_fighter|level(16),wp(100),knows_ironflesh_3|knows_shield_1|knows_power_strike_2|knows_athletics_1|knows_power_draw_2,bandit_face1, bandit_face2],
  ["sevengod_warrior","Sevengod warrior","Sevengod warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_seven_god,
   [itm_leather_gauntlets_new,itm_new_leather_boots,itm_teu_sariant_surcoat,itm_chapel_de_fer_cloth3,itm_col1_kettlehat1,itm_col1_kettlehat2,itm_broigne_shirt_spiked_leather,
   itm_shield_kite_h,itm_mackie_morning_star,itm_sledgehammer,itm_spiked_mace,itm_luc_knightly_hammer],
   str_17 | agi_13 | int_7 | cha_7|level(23),wp(125),knows_ironflesh_4|knows_shield_3|knows_power_strike_4|knows_athletics_3|knows_power_draw_3,bandit_face1, bandit_face2],
  ["sevengod_elite_warrior","Sevengod elite warrior","Sevengod elite warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_seven_god,
   [itm_col1_kettlehat1,itm_col1_kettlehat2,itm_mail_mittens,itm_steel_greaves2,itm_chapel_de_fer_mail3,itm_teu_hochmeister_surcoat,itm_mail_long_surcoat_new_g,
   itm_luc_flanged_mace_iron,itm_luc_iron_morningstar,itm_tab_shield_heater_d],
   str_20 | agi_15 | int_7 | cha_7|level(28),wp(165),knows_ironflesh_5|knows_shield_5|knows_power_strike_5|knows_athletics_5,bandit_face1, bandit_face2],
  ["sevengod_elite_guard","Sevengod elite guard","Sevengod elite guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_seven_god,
   [itm_lamellar_gauntlets,itm_steel_greaves2,itm_topfhelm4,itm_great_helmet_newi,itm_copy_coat_of_plates_f,itm_luc_flanged_mace_iron,itm_steel_shield,itm_warhammer,itm_morningstar],
   str_23 | agi_16 | int_8 | cha_8|level(33),wp(210),knows_ironflesh_6|knows_shield_6|knows_power_strike_6|knows_athletics_6,bandit_face1, bandit_face2],
  
  ["sevengod_knight","Sevengod knight","Sevengod knights",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_seven_god,
   [itm_wlong10,itm_demi_gauntlets,itm_steel_greaves2,itm_topfhelm4,itm_teu_coat_of_plates_a,itm_luc_flanged_mace_iron,itm_luc_iron_morningstar,itm_steel_shield_kite,itm_morningstar],
   def_champion|level(30),wp(200),knows_ironflesh_6|knows_shield_5|knows_power_strike_5|knows_athletics_5|knows_riding_5,bandit_face1, bandit_face2],
  ["sevengod_holy_knight","sevengod_holy_knight","sevengod_holy_knight",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_seven_god,
   [itm_charger_03,itm_mail_mittens,itm_steel_boots_01,itm_luc_flanged_mace_iron,itm_steel_shield_kite,itm_morningstar,itm_plate_armor,itm_visored_bascinet_02,itm_visored_bascinet_01,itm_luc_spiked_mace_5p_b],
   def_knight|level(35),wp(235),knows_ironflesh_7|knows_shield_7|knows_power_strike_7|knows_athletics_7|knows_riding_7,bandit_face1, bandit_face2],

  ["sevengod_zealot","Sevengod Zealot","Sevengod Zealots",tf_guarantee_armor,0,0,fac_seven_god,
   [itm_rawhide_blood,itm_morningstar],
   def_champion|level(30),wp(250),knows_ironflesh_10|knows_power_strike_10|knows_athletics_12,bandit_face1, bandit_face2],
  ["sevengod_pilgrim_a","Sevengod Pilgrim","Sevengod Pilgrims",tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_seven_god,
   [itm_pilgrim_disguise,itm_pilgrim_hood,itm_wooden_shield,itm_luc_iron_morningstar],
   def_swordsman|level(20),wp(165),knows_ironflesh_6|knows_power_strike_6|knows_athletics_6,bandit_face1, bandit_face2],

  ["sevengod_sister","Sevengod elite guard","Sevengod elite guards",tf_beautiful|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_witch_finder,
   [itm_sissofbattle_armor,itm_steel_greaves,itm_mail_mittens,itm_holy_holo_with_hair,itm_pa_maul_02,itm_steel_shield],
   def_knight_1|level(40),wp(275),knows_ironflesh_9|knows_shield_8|knows_power_strike_8|knows_athletics_6,bandit_face1, bandit_face2],
  ["witch_hunter","witch_hunter","witch_hunters",tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_witch_finder,
   [itm_bastard_sword_a,itm_bastard_sword_b,itm_pilgrim_outfit,itm_wrapping_boots,itm_leather_gloves,itm_kettle_hat,itm_flintlock_pistol,itm_pistol,itm_cartridges,itm_cartridges],
   def_guard|level(25),wp(180),knows_ironflesh_5|knows_power_strike_5|knows_athletics_5,bandit_face1, bandit_face2],
  ["witch_hunter_e","witch_hunter","witch_hunters",tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_boots|tf_guarantee_ranged,0,0,fac_witch_finder,
   [itm_armor_14,itm_teu_surcoat_a_kt_e,itm_rus_cav_boots,itm_pistol,itm_cartridges,itm_cartridges,itm_kettlehatfacebyrnie,itm_fullfacecoif,itm_leather_gloves,itm_royalsword,itm_royal_sword02],
   def_knight|level(35),wp(240),knows_ironflesh_7|knows_power_strike_7|knows_athletics_7,bandit_face1, bandit_face2],
#destory
  ["dark_pilgrim","Dark Pilgrim","Dark Pilgrims",tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_destroyer,
   [itm_pilgrim_disguise,itm_pilgrim_hood,itm_hatchet,itm_wooden_shield,itm_throwing_knives,itm_throwing_knives],
   def_farmer|level(4),wp(60),knows_common|knows_athletics_1,bandit_face1, bandit_face2],
  ["dark_monk","Dark Monk","Dark Monks",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_destroyer,
   [itm_light_throwing_axes,itm_black_gambeson_a,itm_bolts,itm_hide_boots,itm_hunting_crossbow,itm_axe,itm_hand_axe,itm_shk_01,itm_black_hood],
   def_footman|level(10),wp(70),knows_ironflesh_1|knows_shield_1|knows_power_strike_1|knows_athletics_2|knows_power_draw_1|knows_power_throw_2,bandit_face1, bandit_face2],
  ["dark_follower","Dark Follower","Dark Followers",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_destroyer,
   [itm_teu_sariant_surcoat,itm_throwing_axes,itm_sarranid_axe_a,itm_one_handed_war_axe_a,itm_mace_4,itm_brienne_spurs_black,itm_hide_boots,itm_nordic_footman_helmet,itm_leather_warrior_cap,itm_leather_steppe_cap_c,itm_fur_covered_shield,itm_leather_covered_round_shield],
   def_fighter|level(16),wp(100),knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_1|knows_power_draw_1|knows_power_throw_2,bandit_face1, bandit_face2],
  ["dark_warrior","Dark Warrior","Dark Warriors",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_destroyer,
   [itm_heavy_throwing_axes,itm_two_handed_axe,itm_war_axe,itm_bardiche,itm_club_with_spike_head,itm_plate_covered_round_shield,itm_long_hafted_spiked_mace,
   itm_cuir_bouilli_a_skull,itm_mail_hauberk,itm_blackleather_boots_a,itm_bascinet_coif_new_2,itm_black_helmet,itm_mail_mittens,itm_bascinet_coif_new_1],
   str_17 | agi_13 | int_7 | cha_7|level(23),wp(150),knows_ironflesh_3|knows_shield_3|knows_power_strike_4|knows_athletics_3|knows_power_throw_4,bandit_face1, bandit_face2],
  
  ["dark_elite_warrior","Dark elite Warrior","Dark elite Warriors",tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_destroyer,
   [itm_tab_shield_round_e,itm_ak_wlocznie_c,itm_ak_wlocznie_d,itm_throwing_spears,itm_heavy_throwing_axes,itm_luc_axe_knight_z,itm_luc_two_handed_axe_2,
   itm_mail_long_surcoat_skull,itm_brig_plate_black,itm_dorn_spearbearer_boots,itm_black_helmet,itm_bascinet_coif_new_2,itm_bascinet_coif_new_1,itm_helm_horned03,itm_blackscale_gauntlets_a],
   def_champion|level(30),wp(195),knows_ironflesh_6|knows_shield_5|knows_power_strike_5|knows_athletics_5|knows_power_throw_5,bandit_face1, bandit_face2],
  ["dark_champion_warrior","Dark champion Warrior","Dark champion Warriors",tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_destroyer,
   [itm_black_greaves,itm_asmoday_helmet2,itm_spak_coat_of_plates_a,itm_blackscale_gauntlets_a,itm_sp_shr1,itm_asmoday_sword,itm_ganquang_melee,itm_ganquang_melee],
   def_knight|level(35),wp(230),knows_ironflesh_8|knows_shield_7|knows_power_strike_7|knows_athletics_7|knows_power_throw_7,bandit_face1, bandit_face2],
  ["dark_champion_warrior_1","Dark champion Warrior","Dark champion Warriors",tf_guarantee_gloves|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_destroyer,
   [itm_black_greaves,itm_helm_a_crusher_a_01,itm_g_reinf_jerkin,itm_blackscale_gauntlets_a,itm_lightedge_spak_black],
   str_30 | agi_10 | int_8 | cha_8|level(35),wp(210),knows_ironflesh_7|knows_power_strike_7|knows_athletics_7,bandit_face1, bandit_face2],

  ["dark_worshiper","Dark Worshiper","Dark Worshipers",tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_destroyer,
   [itm_warhorse_blk,itm_strange_great_sword,itm_strange_sword,itm_tab_shield_small_round_b,itm_javelin,itm_heavy_throwing_axes,itm_two_handed_axe,itm_war_axe,itm_double_sided_lance,itm_club_with_spike_head,
   itm_mail_long_surcoat_skull,itm_cuir_bouilli_a_skull,itm_stark_hanter_boots,itm_black_helmet,itm_barbuta2,itm_mail_mittens],
   def_guard|level(26),wp(180),knows_ironflesh_5|knows_shield_5|knows_power_strike_5|knows_athletics_5|knows_power_throw_5|knows_riding_5|knows_horse_archery_5,bandit_face1, bandit_face2],
  ["dark_knight","Dark Knight","Dark Knights",tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_destroyer,
   [itm_charger_black,itm_coat_of_plates,itm_helm_horned02,itm_maciejowski_helmet_newmod1,itm_blackgauntlets,itm_black_greaves,itm_heavy_lance,
   itm_luc_two_handed_axe_2,itm_luc_axe_knight_z,itm_steel_shield,itm_tab_shield_round_e,itm_ak_wlocznie_c,itm_great_lance,itm_ak_wlocznie_a],
   def_champion|level(30),wp(200),knows_ironflesh_6|knows_shield_6|knows_power_strike_6|knows_athletics_6|knows_power_throw_6|knows_riding_6|knows_horse_archery_6,bandit_face1, bandit_face2],
  ["dark_knight_champion","dark_knight_champion","dark_knight_champions",tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_destroyer,
   [itm_wplatedcharger9,itm_black_greaves,itm_asmoday_helmet2,itm_g_scale_gauntlets_a,itm_spak_coat_of_plates_a,itm_g_iron_greaves_a,itm_ganquang_melee,itm_ak_miecz_a,itm_sp_shr1,itm_ak_wlocznie_b],
   def_knight|level(35),wp(235),knows_ironflesh_7|knows_shield_7|knows_power_strike_8|knows_athletics_7|knows_power_throw_7|knows_riding_7|knows_horse_archery_7,bandit_face1, bandit_face2],

  ["degenerate_nobleman","degenerate_nobleman","degenerate_noblemans",tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_destroyer,
   [itm_cuir_bouilli_a_skull,itm_black_hood,itm_flat_topped_helmet,itm_blackleather_boots_a,itm_blackleather_gloves,itm_saddle_horse,itm_tab_shield_round_c,itm_bastard_sword_a,itm_mace_3,itm_war_darts,itm_awlpike],
   str_16 | agi_11 | int_6 | cha_6|level(18),wp(120),knows_ironflesh_3|knows_shield_4|knows_power_strike_4|knows_athletics_3|knows_power_throw_4|knows_riding_3|knows_horse_archery_3,bandit_face1, bandit_face2],
  ["degenerate_squire","Dark Squire","Dark Squires",tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_destroyer,
   [itm_barded2w,itm_brienne_spurs_black,itm_black_helmet,itm_brig_plate_black,itm_dorn_spearbearer_guant,itm_plate_covered_round_shield,itm_bastard_sword_b,itm_sword_two_handed_b,itm_mackie_bat_nailed,itm_throwing_spears,itm_awlpike_long],
   str_19 | agi_14 | int_7 | cha_7|level(26),wp(160),knows_ironflesh_5|knows_shield_5|knows_power_strike_5|knows_athletics_5|knows_power_throw_6|knows_riding_6|knows_horse_archery_5,bandit_face1, bandit_face2],
  ["black_knight","black_knight","black_knights",tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_destroyer,
   [itm_black_armor,itm_black_greaves,itm_helm_horned02,itm_blackgauntlets,itm_charger_02,itm_morningstar,itm_steel_shield,itm_mackie_kriegsmesser,itm_luc_two_handed_axe_2,itm_toumao,itm_blood_spear],
   def_knight|level(35),wp(215),knows_ironflesh_7|knows_shield_7|knows_power_strike_7|knows_athletics_7|knows_power_throw_9|knows_riding_8|knows_horse_archery_8,bandit_face1, bandit_face2],

  ["dark_knight_god","dark_knight_god","dark_knight_gods",tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_destroyer,
   [itm_ganquang_melee,itm_czarne_gauntlets,itm_czarne_platebut,itm_sub_shield_01,itm_spak_coat_of_plates_b,itm_helm_b_elite_crusher_a_01,itm_sub_helm4,itm_sub_helm,itm_ak_miecz_a,itm_asmoday_sword,itm_horny_charger_plate,itm_blood_spear],
   str_50 | agi_35 | int_10 | cha_10|level(60),wp(355),knows_ironflesh_11|knows_shield_10|knows_power_strike_11|knows_athletics_10|knows_power_throw_10|knows_riding_10|knows_horse_archery_8,bandit_face1, bandit_face2],
#demon 
  ["demon_slave","demon_slave","demon_slave",tf_demon|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_allways_fall_dead,0,0,fac_destroyer,
   [itm_demonheart,itm_ak_wlocznie_d,itm_two_handed_battle_axe_2,itm_ak_wlocznie_c,itm_javelin,itm_javelin],
   str_35 | agi_10|level(20),wp(120),knows_ironflesh_5|knows_power_strike_5|knows_riding_5|knows_athletics_5|knows_shield_5|knows_power_throw_5|knows_horse_archery_7,demonslave_face1,demonslave_face1],
  ["demon_warrior","demon_warrior","demon_warrior",tf_demon|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_allways_fall_dead,0,0,fac_destroyer,
   [itm_demonheart,itm_throwing_spears,itm_throwing_spears,itm_ak_wlocznie_c,itm_czarne_gauntlets,itm_waorchaosaxea,itm_czarne_platebut,itm_sp_shr1,itm_g_reinf_jerkin,itm_g_tabard_a,itm_helm_a_elite_chaos_warrior_b_01],
   str_65 | agi_20|level(40),wp(200),knows_ironflesh_8|knows_power_strike_8|knows_riding_8|knows_athletics_8|knows_shield_8|knows_power_throw_8|knows_horse_archery_8,demon_face1,demon_face2],
  ["demon_high_warrior","demon_high_warrior","demon_high_warrior",tf_demon|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_allways_fall_dead,0,0,fac_destroyer,
   [itm_blackdemonheart,itm_demonheart,itm_ganquang_melee,itm_ganquang_melee,itm_czarne_gauntlets,itm_czarne_platebut,itm_waorchaosaxeb,itm_sub_shield_01,itm_spak_coat_of_plates_b,itm_g_reinf_jerkin,itm_helm_a_elite_chaos_warrior_a_01],
   str_95 | agi_30|level(60),wp(300),knows_ironflesh_11|knows_power_strike_11|knows_riding_11|knows_athletics_11|knows_shield_11|knows_power_throw_11|knows_horse_archery_9,demon_face1,demon_face2],
  
  ["demon_knight","demon_knight","demon_knight",tf_demon|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse|tf_allways_fall_dead,0,0,fac_destroyer,
   [itm_demonheart,itm_throwing_spears,itm_throwing_spears,itm_ak_wlocznie_b,itm_czarne_gauntlets,itm_waorchaosaxea,itm_czarne_platebut,itm_riper,itm_sp_shr1,itm_g_reinf_jerkin,itm_g_tabard_a,itm_helm_a_elite_chaos_warrior_b_01],
   str_65 | agi_20|level(40),wp(200),knows_ironflesh_8|knows_power_strike_8|knows_riding_8|knows_athletics_8|knows_shield_8|knows_power_throw_8|knows_horse_archery_8,demon_face1,demon_face2],
  ["demon_elite_knight","demon_elite_knight","demon_elite_knight",tf_demon|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse|tf_allways_fall_dead,0,0,fac_destroyer,
   [itm_blackdemonheart,itm_demonheart,itm_ganquang_melee,itm_ganquang_melee,itm_czarne_gauntlets,itm_czarne_platebut,itm_ripper_chain,itm_waorchaosaxeb,itm_sub_shield_01,itm_spak_coat_of_plates_b,itm_g_tabard_a,itm_helm_b_elite_chaos_warrior_a_01],
   str_95 | agi_30|level(60),wp(300),knows_ironflesh_11|knows_power_strike_11|knows_riding_11|knows_athletics_11|knows_shield_11|knows_power_throw_11|knows_horse_archery_9,demon_face1,demon_face2],
  
  ["demon_lord","demon_lord","demon_lord",tf_demon|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse|tf_allways_fall_dead,0,0,fac_destroyer,
   [itm_blackdemonheart,itm_ganquang_melee,itm_ganquang_melee,itm_czarne_gauntlets,itm_czarne_platebut,itm_heavy_riper,itm_spak_coat_of_plates_e,itm_spak_coat_of_plates_f,itm_sub_shield_01,itm_helm_a_elite_chaos_lord,itm_waorchaosaxec],
   str_125 | agi_40|level(80),wp(400),knows_ironflesh_14|knows_power_strike_14|knows_riding_12|knows_athletics_12|knows_shield_12|knows_power_throw_12|knows_horse_archery_9,demonlord_face1,demonlord_face2],
  ["demon_lord_e","demon_lord","demon_lord",tf_demon|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_horse|tf_allways_fall_dead,0,0,fac_roskel,
   [itm_blackdemonheart,itm_ganquang_melee,itm_twiligh_armor,itm_twilight_gloves,itm_twilight_boots,itm_demon_protection,itm_sub_shield_01,itm_pa_sword_06,itm_heavy_riper],
   str_135 | agi_50|level(85),wp(425),knows_ironflesh_14|knows_power_strike_14|knows_riding_12|knows_athletics_12|knows_shield_12|knows_power_throw_12|knows_horse_archery_9,demonlord_face1,demonlord_face2],
  
  ["roskel_champion","roskel_champion","roskel_champions",tf_tall|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_roskel,
   [itm_bascinet_coif_new_1,itm_bascinet_coif_new_2,itm_rhodok_cuir_bouilli_b,itm_g_scale_gauntlets_a,itm_g_iron_greaves_a,itm_northerner_horse_black,itm_throwing_spears,itm_throwing_spears,itm_2dblhead_ax_1,itm_sword_medieval_d_long,itm_plate_covered_round_shield],
   def_champion|level(30),wp(200),knows_ironflesh_6|knows_power_strike_6|knows_athletics_6|knows_power_throw_6|knows_riding_6|knows_horse_archery_6,bandit_face1, bandit_face2],
  ["roskel_champion_e","roskel_champion","roskel_champions",tf_tall|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_roskel,
   [itm_g_reinf_jerkin_pu,itm_g_tabard_a_pu,itm_g_iron_greaves_a,itm_asmoday_helmet2,itm_g_scale_gauntlets_a,itm_spak_coat_of_plates_a,itm_riper,itm_jack_faramir_shield,itm_jack_glamdring,itm_throwing_spears],
   def_knight_1|level(40),wp(260),knows_ironflesh_8|knows_power_strike_8|knows_athletics_8|knows_shield_8|knows_power_throw_8|knows_riding_8|knows_horse_archery_8,bandit_face1, bandit_face2],

  # ["lower_succubus","lower_succubus","lower_succubus",tf_succubus|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_allways_fall_dead,0,0,fac_destroyer,
  #  [],
  #  str_35 | agi_10|level(20),wp(120),knows_ironflesh_5|knows_power_strike_5|knows_riding_5|knows_athletics_5|knows_shield_5|knows_power_throw_5|knows_horse_archery_7,demonslave_face1,demonslave_face1],

#  ["undead_walker","undead_walker","undead_walkers",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["undead_horseman","undead_horseman","undead_horsemen",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_undeads,
#   [], 
#   def_attrib|level(19),wp(100),knows_common,undead_face1, undead_face2],
#  ["undead_nomad","undead_nomad","undead_nomads",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
#   [], 
#   def_attrib|level(21),wp(100),knows_common|knows_riding_4,khergit_face1, khergit_face2],
#  ["undead","undead","undead",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["hell_knight","hell_knight","hell_knights",tf_undead|tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads,
#   [], 
#   def_attrib|level(23),wp(100),knows_common|knows_riding_3,undead_face1, undead_face2],

  ["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(45),knows_common,refugee_face1,refugee_face2],
  
  ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
   [itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,
    itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,
    itm_leather_jacket, itm_leather_cap],
   def_attrib|level(9),wp(100),knows_common|knows_riding_4|knows_ironflesh_3,mercenary_face_1, mercenary_face_2],

  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
   [itm_dress,itm_leather_boots],
   def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1, woman_face_2],


#This troop is the troop marked as soldiers_end and town_walkers_begin
 ["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic,itm_fur_coat, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_arena_tunic_white, itm_leather_apron, itm_shirt, itm_arena_tunic_green, itm_arena_tunic_blue, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
 ["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["khergit_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_khergit_leather_boots,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_sarranid_boots_a,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sarranid_common_dress, itm_sarranid_common_dress_b,itm_woolen_hose,itm_sarranid_boots_a, itm_sarranid_felt_head_cloth, itm_sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
  #new
  ["turumia_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [itm_linen_tunic,itm_linen_tunic_banner,itm_arena_tunic_banner2,itm_arena_tunic_banner1, itm_arena_tunic_white, itm_arena_tunic_green, itm_arena_tunic_blue, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
    def_attrib|level(4),wp(60),knows_common,west_face_middle_1, west_face_old_2],
  ["turumia_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
    def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
  ["askr_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [itm_linen_tunic, itm_leather_vest,itm_steppe_armor, itm_nomad_boots, itm_hide_boots, itm_fur_hat, itm_leather_cap, itm_sarranid_cloth_robe_b, itm_khergit_leather_boots,],
    def_attrib|level(4),wp(60),knows_common,nord_face_middle_1, nord_face_older_2],
  ["askr_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
    [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
    def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
  
#This troop is the troop marked as town_walkers_end and village_walkers_begin
 ["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_leather_vest, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_older_2],
 ["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
 ["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_robe, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
 ["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_nomad_armor,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x00000001b20c230345ab8cd172ad3b1200000000001de0e50000000000000000],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x00000001a40040c7328c59a4a652c8e900000000001e32c30000000000000000],
# Ryan BEGIN
  ["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero, no_scene,reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

  ["guide","Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac_commoners,[itm_coarse_tunic,itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c318301f24e38a36e38e3],
# Ryan END

  ["Xerina","Xerina","Xerina",tf_hero|tf_female,0, 0,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_5|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_3,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["Dranton","Dranton","Dranton",tf_hero,0, 0,  fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["Kradus","Kradus","Kradus",tf_hero,0, 0,  fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],


#Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_robe,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
  ["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x000000000004718201c073191a9bb10c],

#Dhorak keep

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_linen_tunic,itm_coarse_tunic,itm_shirt,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],

  ["trainer_1","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_nomad_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
  ["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_red_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_tactics, itm_book_persuasion, itm_book_wound_treatment_reference, itm_book_leadership, 
               itm_book_intelligence, itm_book_training_reference, itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_wound_treatment_reference, itm_book_leadership, itm_book_intelligence, itm_book_trade, 
               itm_book_engineering, itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_leather_jacket, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute
  ["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_tunic_with_green_cape, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],  #early harp/lyre
  ["tavern_minstrel_3","Wandering Ashik","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_nomad_robe, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute/oud or rebab
  ["tavern_minstrel_4","Wandering Skald","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_fur_coat, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #No instrument or lyre
  ["tavern_minstrel_5","Wandering Troubadour","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_short_tunic, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #Lute or Byzantine/Occitan lyra
  

#NPC system changes begin
#Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

  # Adventurer end=npc1
  ["alayen","Alayen","Alayen",tf_hero, 0, reserved,  fac_manhunters,
  [itm_gauntlets,itm_iron_greaves,itm_full_plate_armor_banner,itm_jack_anduril,itm_helmhorn3,itm_charger_black,itm_tab_shield_heater_cav_b,itm_heavy_lance],
knight_attrib_5,wp(300),knows_riding_10|knows_athletics_10|knows_ironflesh_8|knows_power_strike_8|knows_athletics_9|knows_prisoner_management_7|knows_leadership_10,0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["jeremus","Jeremus","Jeremus",tf_hero, 0, reserved,  fac_manhunters,
[itm_leather_gloves,itm_nobleman_outfit,],
knight_attrib_4,wp(30),knight_skills_3|knows_surgery_6|knows_wound_treatment_6|knows_first_aid_6,0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["deshavi","Deshavi","Deshavi",tf_beautiful|tf_hero, 0, reserved,  fac_outlaws,
[itm_bow3_spak,itm_bow3_arr_spak,itm_bow3_arr_spak,itm_rhun_glaive,itm_rus_scale,itm_col1_byzantion,itm_rus_splint_greaves,itm_leather_gloves],
knight_attrib_4,wp(255),knows_ironflesh_8|knows_power_strike_8|knows_tracking_4|knows_athletics_5|knows_spotting_5|knows_pathfinding_5|knows_power_draw_8|knows_tactics_5|knows_prisoner_management_4|knows_leadership_7,0x00000001fc08400e33a15297634d44f400000000001e02db0000000000000000],
  ["baheshtur","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_outlaws,
[itm_lamellar_gauntlets,itm_khergit_leather_boots,itm_pa_sword_07,itm_heavy_lamellar_armor,itm_khergit_guard_helmet,itm_tab_shield_small_round_c,itm_bow4_spak,itm_bow4_arr_spak],
knight_attrib_4,wp(250),knight_skills_3|knows_power_draw_2|knows_horse_archery_2,0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["edrick","Edrick","Edrick",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_adventurer,
[itm_west_swordsman_white,itm_west_heavy_rider_helmet_mod_open,itm_brienne_spurs,itm_wisby_gauntlets_red,itm_steel_bolts,itm_spak_crsb01,itm_tab_shield_kite_d,itm_morningstar,itm_wlong9],
knight_attrib_3,wp(200),knight_skills_3,0x00000003480d1144395a565af34ca46400000000001caadb0000000000000000],
  ["scarborough","Scarborough","Scarborough",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_turumia,
[itm_wlong2,itm_black_lance_banner,itm_heraldic_platemail_02,itm_steel_boots_01,itm_steel_mittens,itm_tournament_helmb,itm_tab_shield_heater_cav_b,itm_pa_sword_03,itm_pa_sword_04],
knight_attrib_3,wp(200),knight_skills_3,0x0000000a801112c834b23254243a996600000000001e38da0000000000000000],

  ["npc1","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_nomad_boots,itm_knife],
   str_9|agi_9|int_12|cha_7|level(3),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_linen_tunic,itm_hide_boots,itm_club],
   str_7|agi_7|int_11|cha_6|level(1),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3","Rosey","Ymira",tf_beautiful|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_dress,itm_woolen_hose,itm_knife],
   str_6|agi_9|int_11|cha_6|level(1),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040008583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_jerkin,itm_nomad_boots, itm_sword_medieval_a],
   str_10|agi_9|int_13|cha_10|level(10),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_vest,itm_nomad_boots, itm_sword_khergit_1],
   str_20 | agi_24 | int_12 | cha_9|level(25),wp(200),
   knows_riding_6|knows_horse_archery_6|knows_power_draw_6|knows_leadership_5|knows_trainer_3|knows_weapon_master_5|knows_ironflesh_5|knows_power_strike_6|knows_power_throw_6,
   0x000000081810e10a3629b9275451211c00000000001dd4ec0000000000000000],
  ["npc6","Angelo","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_a],
   str_24 | agi_19 | int_15 | cha_15|level(32),wp(235),
   knows_riding_7|knows_weapon_master_7|knows_power_strike_7|knows_athletics_7|knows_trainer_7|knows_leadership_7|knows_ironflesh_7|knows_power_throw_2,
  0x0000000ca905101162ed6d0a6d72991b00000000001d38660000000000000000],
  ["npc7","Rena","Deshavi",tf_beautiful|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_ragged_outfit,itm_wrapping_boots, itm_hunting_bow, itm_arrows, itm_quarter_staff],
   str_14 | agi_14 | int_12 | cha_12|level(18),wp(180),
   knows_tracking_5|knows_athletics_5|knows_spotting_5|knows_pathfinding_5|knows_power_draw_4|knows_ironflesh_3|knows_power_throw_3|knows_athletics_3|knows_ironflesh_3,
   0x00000001c504300f0000000000000ed400000000000000000000000000000000],
  ["npc8","Helmwige","Matheld",tf_beautiful|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tribal_warrior_outfit,itm_nomad_boots, itm_sword_viking_1],
   str_38|agi_24|int_21|cha_21|level(35),wp(300),
   knows_weapon_master_10|knows_power_strike_10|knows_athletics_8|knows_leadership_7|knows_tactics_5,
   0x00000001cd0c00050000000000000f4000000000000000000000000000000000],
  ["npc9","Raymood","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_b_small],
   str_24|agi_15|int_18|cha_21|level(29),wp(100),
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x00000007e111114f274472c8bb52c88200000000001dc4a10000000000000000],
  ["npc10","Riccardo","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_padded_leather,itm_nomad_boots, itm_crossbow, itm_bolts, itm_pickaxe],
   str_45|agi_30|int_27|cha_27|level(45),wp(385),
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000e7c08c5c946ab923c14aa315a00000000001db7110000000000000000],
  ["npc11","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_apron, itm_falchion, itm_wrapping_boots],
   str_8|agi_13|int_10|cha_10|level(8),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12","Florian","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_disguise,itm_nomad_boots, itm_staff],
   str_8|agi_7|int_13|cha_7|level(4),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x0000000e4801118565144e3756e8c6e1000000000016d3350000000000000000],
  ["npc13","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_robe,itm_nomad_boots, itm_scimitar, itm_courser],
   str_15|agi_15|int_12|cha_8|level(15),wp(150),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nobleman_outfit,itm_nomad_boots, itm_sword_medieval_b_small],
   str_10|agi_8|int_12|cha_10|level(5),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_rich_outfit,itm_nomad_boots, itm_sword_medieval_b_small],
   str_12|agi_9|int_13|cha_8|level(7),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_peasant_dress,itm_nomad_boots, itm_dagger, itm_throwing_knives],
   str_8|agi_12|int_8|cha_8|level(2),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],

  ["npc17","Klethi","Klethi",tf_beautiful|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_peasant_dress,itm_nomad_boots, itm_dagger, itm_throwing_knives],
   str_8|agi_12|int_8|cha_8|level(2),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x000000002808000f0000000000000e4000000000000000000000000000000000],
#NPC system changes end
#add new companions here

#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
  ["kingdom_1_lord",  "King Harlaus",  "Harlaus",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_plate_charger_white,   itm_rich_outfit,        itm_blue_hose,                  itm_plate_boots,          itm_spak_2full_plate_armor_banner, itm_gauntlets,    itm_ak_miecz_b,      itm_tab_shield_heater_cav_b,itm_black_lance_banner,       itm_longshanks_helm,itm_jack_faramir],          knight_attrib_5,wp(220),knight_skills_5|knows_trainer_5, 0x0000000f45041105241acd2b5a66a86900000000001e98310000000000000000,swadian_face_older_2],
  ["kingdom_2_lord",  "King Yaroglek",  "Yaroglek",  tf_hero, 0,reserved,  fac_kingdom_2,[itm_charger_steel,    itm_courtly_outfit,      itm_leather_boots,              itm_plate_boots,              itm_early_transitional_banner, itm_gauntlets,      itm_flamberg,      itm_tab_shield_kite_cav_b,      itm_henryv_helm,itm_jack_glamdring],    knight_attrib_5,wp(220),knight_skills_5|knows_trainer_4, 0x0000000ec50001400a2269f919dee11700000000001cc57d0000000000000000, vaegir_face_old_2],
  ["kingdom_3_lord",  "Sanjar Khan",  "Sanjar",  tf_hero, 0,reserved,  fac_kingdom_3,[itm_warhorse_steppe,   itm_nomad_robe,             itm_leather_boots,              itm_steel_boots_01,           itm_khergit_guard_armor,  itm_lamellar_gauntlets,       itm_pa_sword_02,   itm_tab_shield_small_round_c,   itm_mongol_helmet_xf,itm_spak_bow7,itm_bow3_arr_spak],      knight_attrib_5,wp(220),knight_skills_5|knows_trainer_6, 0x0000000cee0051cc44be2d14d370c65c00000000001ed6df0000000000000000,khergit_face_old_2],
  ["kingdom_4_lord",  "King Ragnar",  "Ragnar",  tf_hero, 0,reserved,  fac_kingdom_4,[itm_wlong16,    itm_nobleman_outfit,    itm_leather_boots,              itm_mail_boots,                 itm_wei_xiadi_valk,  itm_gauntlets,    itm_vsword03,itm_pa_axe_03,           itm_tab_shield_round_e,    itm_valsgarde_new],            knight_attrib_5,wp(220),knight_skills_5|knows_trainer_4, 0x0000000e2c0c028a068e8c18557b12a500000000001c0fe80000000000000000, nord_face_older_2],
  ["kingdom_5_lord",  "King Graveth",  "Graveth",  tf_hero, 0,reserved,  fac_kingdom_5,[itm_plate_charger_brown,  itm_tabard,             itm_leather_boots,              itm_brienne_spurs,   itm_heraldic_platemail_02,  itm_gauntlets,         itm_lightedge_spak_black,itm_sp_2hsw,         itm_tab_shield_heater_cav_b,        itm_florisivhelm],         knight_attrib_4,wp(220),knight_skills_4|knows_trainer_5, 0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000, rhodok_face_old_2],
  ["kingdom_6_lord",  "Sultan Hakim",  "Hakim",  tf_hero, 0,reserved,  fac_kingdom_6,[itm_warhorse_sarranid,     itm_rich_outfit,itm_mamluke_mail,          itm_sarranid_boots_c,       itm_dorn_immortal_helmet,  itm_mail_mittens,      itm_mackie_bastard,    itm_brass_shield1,itm_lonely,itm_bow4_arr_spak],         knight_attrib_4,wp(220),knight_skills_5|knows_trainer_5, 0x0000000a4b10a354189c71d6d386e8ac00000000001e24eb0000000000000000],

  ["kingdom_7_lord","Lady Hyla", "Lady",tf_beautiful|tf_hero, 0,0, fac_kingdom_7,
   [itm_splinted_greaves,itm_scale_armor,itm_lamellar_gauntlets,itm_col1_byzantion,itm_tab_shield_kite_d,itm_imperial_bow,itm_sword_medieval_d_long,itm_barbed_arrows,itm_courtly_outfit,itm_ankle_boots],
   knight_attrib_3,wp(200),knight_skills_4,0x00000001fc0000080000000000000f1300000000000000000000000000000000],
  ["kingdom_8_lord","King Vorian", "Vorian",tf_hero, 0,0, fac_kingdom_8,
   [itm_noblemanshirt,itm_rus_cav_boots_black,itm_elf_spear_2,itm_lorien_kite,itm_rivendellrewardarmour,itm_rivendellswordfighterhelmet,itm_leather_gauntlets_new,itm_pa_sword_02],
   knight_attrib_4,wp(200),knight_skills_4,0x0000000180091008175272d55cb5a6ec00000000001e361d0000000000000000],
#    Imbrea   Belinda Ruby Qaelmas Rose    Willow 
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina  
# Dunga        Agatha     Dibus Crahask
  
#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
  #Swadian civilian clothes: itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard
  #Older knights with higher skills moved to top
  ["knight_1_1", "Count Klargus", "Klargus", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger,      itm_courtly_outfit,      itm_heraldic_platemail_01,   itm_nomad_boots, itm_iron_greaves,       itm_great_helmet, itm_ganquang_morningstar, itm_sword_medieval_c,  itm_scale_gauntlets,itm_ak_miecz_mis,         itm_tab_shield_heater_cav_a],   knight_attrib_5,wp(230),knight_skills_5|knows_trainer_1|knows_trainer_3, 0x0000000c3e08601414ab4dc6e39296b200000000001e231b0000000000000000, swadian_face_older_2],
  ["knight_1_2", "Count Delinard", "Delinard", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse,           itm_red_gambeson,      itm_guesclin_banner,               itm_nomad_boots,            itm_iron_greaves,                    itm_guard_helmet,  itm_gauntlets,        itm_bastard_sword_a,itm_ak_miecz_a,    itm_tab_shield_heater_cav_b],       knight_attrib_5,wp(240),knight_skills_5, 0x0000000c0f0c320627627238dcd6599400000000001c573d0000000000000000, swadian_face_young_2],
  ["knight_1_3", "Count Haringoth", "Haringoth", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse,          itm_nobleman_outfit,     itm_swadian_ceremonial_plate_black,                 itm_leather_boots,          itm_splinted_leather_greaves,        itm_sallet_02, itm_gauntlets, itm_bastard_sword_b,   itm_tab_shield_heater_d],  knight_attrib_5,wp(260),knight_skills_5|knows_trainer_3, 0x0000000cb700210214ce89db276aa2f400000000001d36730000000000000000, swadian_face_young_2],
  ["knight_1_4", "Count Clais", "Clais", tf_hero, 0, reserved,  fac_kingdom_1, [itm_wplatedcharger2,      itm_short_tunic,       itm_heraldic_mail_with_surcoat,           itm_leather_boots,          itm_mail_chausses,                   itm_winged_great_helmet, itm_gauntlets,       itm_bastard_sword_a,  itm_sword_two_handed_a,  itm_tab_shield_heater_d],    knight_attrib_5,wp(180),knight_skills_5|knows_trainer_4, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_older_2],
  ["knight_1_5", "Count Deglan", "Deglan", tf_hero, 0, reserved,  fac_kingdom_1, [itm_wplatedcharger9,            itm_rich_outfit,        itm_mail_hauberk,itm_woolen_hose, itm_mail_chausses, itm_guard_helmet, itm_steel_mittens,         itm_sword_medieval_c,itm_sword_two_handed_a, itm_ak_joust_lance,   itm_tab_shield_heater_d],      knight_attrib_4,wp(200),knight_skills_4|knows_trainer_6, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_older_2],
  ["knight_1_6", "Count Tredian", "Tredian", tf_hero, 0, reserved,  fac_kingdom_1, [itm_wlong2,            itm_tabard,      itm_williamdouglas2_banner,               itm_leather_boots,          itm_mail_boots,                      itm_tournament_helmb, itm_gauntlets, itm_bastard_sword_b, itm_sword_two_handed_b,  itm_tab_shield_heater_cav_b,itm_steel_bolts,itm_sniper_crossbow], knight_attrib_5,wp(240),knight_skills_4|knows_trainer_4, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_older_2],
  ["knight_1_7", "Count Grainwad", "Grainwad", tf_hero, 0, reserved,  fac_kingdom_1, [itm_wlong9,            itm_tabard,      itm_heraldic_plate_01,               itm_leather_boots,          itm_mail_boots,                      itm_bascinet_coif_01, itm_gauntlets, itm_bastard_sword_b,   itm_sword_two_handed_b, itm_tab_shield_heater_cav_b], knight_attrib_5,wp(290),knight_skills_4|knows_trainer_4, 0x0000000c1e001500589dae4094aa291c00000000001e37a80000000000000000, swadian_face_young_2],
  ["knight_1_8", "Count Ryis", "Ryis", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse,          itm_nobleman_outfit,     itm_coat_of_plates,                 itm_leather_boots,          itm_splinted_leather_greaves,        itm_visored_bascinet_02,  itm_gauntlets,itm_bastard_sword_b,  itm_sword_two_handed_a, itm_tab_shield_heater_d],  knight_attrib_4,wp(250),knight_skills_4, 0x0000000c330855054aa9aa431a48d74600000000001ed5240000000000000000, swadian_face_older_2],

#Swadian younger knights  
  ["knight_1_9", "Count Plais", "Plais", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger_black,      itm_gambeson,     itm_early_transitional_banner,                 itm_blue_hose,              itm_mail_boots,                      itm_tournament_helmb,  itm_scale_gauntlets,     itm_pa_sword_03,itm_ak_swad_lance,   itm_tab_shield_heater_c],    knight_attrib_3,wp(160),knight_skills_3, 0x0000000c0f08000458739a9a1476199800000000001fb6f10000000000000000, swadian_face_old_2],
  ["knight_1_10", "Count Mirchaud", "Mirchaud", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger2,           itm_blue_gambeson,        itm_copy_early_transitional_white,           itm_woolen_hose,            itm_mail_chausses,                   itm_guard_helmet,    itm_gauntlets,    itm_sword_two_handed_b, itm_ganquang_morningstar,  itm_tab_shield_heater_cav_b],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000c0610351048e325361d7236cd00000000001d532a0000000000000000, swadian_face_older_2],
  ["knight_1_11", "Count Stamar", "Stamar", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger3_new,           itm_red_gambeson,      itm_coat_of_plates_steel,               itm_nomad_boots,            itm_iron_greaves,                    itm_hounskull_bascinet_06,   itm_gauntlets,       itm_mackie_bastard,    itm_tab_shield_heater_cav_b],       knight_attrib_3,wp(220),knight_skills_3, 0x0000000c03104490280a8cb2a24196ab00000000001eb4dc0000000000000000, swadian_face_older_2],
  ["knight_1_12", "Count Meltor", "Meltor", tf_hero, 0, reserved,  fac_kingdom_1, [itm_barded1w,      itm_rich_outfit,        itm_brig_plate_black,                    itm_nomad_boots,            itm_mail_boots,                      itm_guard_helmet,   itm_gauntlets,         itm_fighting_pick,   itm_tab_shield_heater_c],    knight_attrib_3,wp(130),knight_skills_3, 0x0000000c2a0805442b2c6cc98c8dbaac00000000001d389b0000000000000000, swadian_face_older_2],
  ["knight_1_13", "Count Beranz", "Beranz", tf_hero, 0, reserved,  fac_kingdom_1, [itm_platedw,      itm_ragged_outfit,      itm_coat_of_plates_a_cloak,           itm_nomad_boots,            itm_splinted_greaves,                itm_sallet_02,   itm_gauntlets,         itm_sword_medieval_c,  itm_sword_two_handed_a,     itm_tab_shield_heater_c],   knight_attrib_2,wp(160),knight_skills_2, 0x0000000c380c30c2392a8e5322a5392c00000000001e5c620000000000000000, swadian_face_older_2],
  ["knight_1_14", "Count Rafard", "Rafard", tf_hero, 0, reserved,  fac_kingdom_1, [itm_scalecharger2w,      itm_short_tunic,       itm_heraldic_mail_with_tabard,           itm_leather_boots,          itm_mail_chausses,                   itm_armet_01,  itm_scale_gauntlets,     itm_bastard_sword_a,    itm_tab_shield_heater_cav_a,itm_steel_bolts,itm_sniper_crossbow],    knight_attrib_2,wp(190),knight_skills_3|knows_trainer_6, 0x0000000c3f10000532d45203954e192200000000001e47630000000000000000, swadian_face_older_2],
  ["knight_1_15", "Count Regas", "Regas", tf_hero, 0, reserved,  fac_kingdom_1, [itm_wlong10,            itm_rich_outfit,        itm_coat_of_plates_red_cloak,                   itm_woolen_hose,            itm_mail_chausses,                   itm_armet_03,   itm_gauntlets,       itm_jack_glamdring,  itm_tab_shield_heater_d],      knight_attrib_4,wp(140),knight_skills_2, 0x0000000c5c0840034895654c9b660c5d00000000001e34530000000000000000, swadian_face_young_2],
  ["knight_1_16", "Count Devlian", "Devlian", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse_red2,      itm_courtly_outfit,      itm_swadian_lordly_plate_armor,                     itm_nomad_boots,            itm_splinted_greaves,                itm_great_helmet,   itm_gauntlets, itm_ganquang_morningstar,       itm_sword_medieval_c,           itm_tab_shield_heater_c],   knight_attrib_1,wp(130),knight_skills_2, 0x000000095108144657a1ba3ad456e8cb00000000001e325a0000000000000000, swadian_face_young_2],
  ["knight_1_17", "Count Rafarch", "Rafarch", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse_holy,      itm_gambeson,     itm_williamdouglas2_banner,                 itm_blue_hose,              itm_mail_boots,                      itm_topfhelm7,   itm_scale_gauntlets,    itm_luc_flanged_mace_iron,   itm_tab_shield_heater_cav_b],    knight_attrib_2,wp(190),knight_skills_1|knows_trainer_4, 0x0000000c010c42c14d9d6918bdb336e200000000001dd6a30000000000000000, swadian_face_young_2],
  ["knight_1_18", "Count Rochabarth", "Rochabarth", tf_hero, 0, reserved,  fac_kingdom_1, [itm_charger4_new,           itm_blue_gambeson,        itm_coat_of_plates_a_cloak,                   itm_woolen_hose,            itm_mail_chausses,                   itm_winged_great_helmet,   itm_gauntlets,     itm_sword_two_handed_a, itm_mackie_bastard,     itm_tab_shield_heater_cav_a],   knight_attrib_3,wp(210),knight_skills_1, 0x0000000c150045c6365d8565932a8d6400000000001ec6940000000000000000, swadian_face_young_2],
  ["knight_1_19", "Count Despin", "Despin", tf_hero, 0, reserved,  fac_kingdom_1, [itm_barded2w,      itm_rich_outfit,        itm_plate_harness_03,                    itm_nomad_boots,            itm_mail_boots,                      itm_great_helmet, itm_gauntlets,           itm_fighting_pick,  itm_sword_two_handed_a, itm_tab_shield_heater_cav_a],    knight_attrib_1,wp(120),knight_skills_1, 0x00000008200012033d9b6d4a92ada53500000000001cc1180000000000000000, swadian_face_young_2],
  ["knight_1_20", "Count Montewar", "Montewar", tf_hero, 0, reserved,  fac_kingdom_1, [itm_warhorse_wht,      itm_ragged_outfit,      itm_full_plate_armor_banner,           itm_nomad_boots,            itm_splinted_greaves,                itm_armet_04, itm_gauntlets,           itm_sorrow,   itm_jack_anduril,   itm_tab_shield_heater_cav_a],   knight_attrib_2,wp(150),knight_skills_1, 0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000, swadian_face_young_2],

  
#  ["knight_1_21", "Lord Swadian 21", "knight_1_7", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_ragged_outfit,      itm_heraldic_mail_with_surcoat,           itm_nomad_boots,            itm_splinted_greaves,                itm_great_helmet, itm_gauntlets,           itm_sword_medieval_c,   itm_sword_two_handed_a,   itm_tab_shield_heater_cav_a],   knight_attrib_2,wp(150),knight_skills_2, 0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000, swadian_face_young_2],
 # ["knight_1_22", "Lord Swadian 22", "knight_1_8", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_short_tunic,       itm_heraldic_mail_with_surcoat,           itm_leather_boots,          itm_mail_chausses,                   itm_winged_great_helmet, itm_gauntlets,       itm_bastard_sword_a,  itm_sword_two_handed_a,  itm_tab_shield_heater_d],    knight_attrib_3,wp(180),knight_skills_3|knows_trainer_4, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_older_2],
#  ["knight_1_23", "Lord Swadian 23", "knight_1_9", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_rich_outfit,        itm_mail_hauberk,                   itm_woolen_hose,            itm_mail_chausses,                   itm_guard_helmet, itm_gauntlets,         itm_sword_medieval_c,    itm_tab_shield_heater_d],      knight_attrib_4,wp(200),knight_skills_4|knows_trainer_6, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_older_2],
#  ["knight_1_24", "Lord Swadian 24", "knight_1_0", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_tabard,      itm_heraldic_mail_with_surcoat,               itm_leather_boots,          itm_mail_boots,                      itm_winged_great_helmet, itm_gauntlets, itm_bastard_sword_b, itm_sword_two_handed_b,  itm_tab_shield_heater_cav_b], knight_attrib_5,wp(240),knight_skills_5|knows_trainer_5, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_older_2],

  
  
  ["knight_2_1", "Boyar Vuldrat", "Vuldrat", tf_hero, 0, reserved,  fac_kingdom_2, [itm_wwarhorsemaille1,      itm_fur_coat,     itm_vaegir_elite_armor,                   itm_nomad_boots,            itm_splinted_leather_greaves,        itm_tagancha_helm_a,    itm_mail_mittens,       itm_sword_viking_3,           itm_tab_shield_kite_c],    knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x00000005590011c33d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_middle_2],
  ["knight_2_2", "Boyar Naldera", "Naldera", tf_hero, 0, reserved,  fac_kingdom_2, [itm_wwarhorsemaille3,      itm_rich_outfit,        itm_lamellar_armor,               itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_noble_helmet,  itm_mail_mittens,      itm_shortened_military_scythe,    itm_dec_steel_shield],    knight_attrib_2,wp(160),knight_skills_2, 0x0000000c2a0015d249b68b46a98e176400000000001d95a40000000000000000, vaegir_face_old_2],
  ["knight_2_3", "Boyar Meriga", "Meriga", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_steppe,            itm_short_tunic,        itm_broigne_shirt_metal_plate,                   itm_woolen_hose,            itm_mail_chausses,                   itm_novogrod_helm, itm_lamellar_gauntlets,           itm_great_bardiche,           itm_tab_shield_kite_cav_b],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c131031c546a38a2765b4c86000000000001e58d30000000000000000, vaegir_face_older_2],
  ["knight_2_4", "Boyar Khavel", "Khavel", tf_hero, 0, reserved,  fac_kingdom_2, [itm_wwarhorsemaille3,      itm_courtly_outfit,     itm_lamellar_armor,               itm_leather_boots,          itm_mail_boots,                      itm_vaegir_noble_helmet, itm_lamellar_gauntlets,         itm_mongol_spear_x,itm_bastard_sword_b,   itm_tab_shield_kite_cav_b],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c2f0832c748f272540d8ab65900000000001d34e60000000000000000, vaegir_face_older_2],
  ["knight_2_5", "Boyar Doru", "Doru", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_steppe,            itm_rich_outfit,        itm_rus_lamellar_a,                     itm_leather_boots,          itm_mail_chausses,                   itm_vaegir_noble_helmet, itm_scale_gauntlets,   itm_bastard_sword_b,   itm_tab_shield_kite_d],       knight_attrib_5,wp(250),knight_skills_5, 0x0000000e310061435d76bb5f55bad9ad00000000001ed8ec0000000000000000, vaegir_face_older_2],
  ["knight_2_6", "Boyar Belgaru", "Belgaru", tf_hero, 0, reserved,  fac_kingdom_2, [itm_wlong17,      itm_nomad_vest,      itm_vaegir_elite_armor,                   itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_lamellar_helmet,  itm_mail_mittens, itm_luc_flanged_mace_iron,         itm_sword_viking_3,           itm_tab_shield_kite_c],   knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a0100421038da7157aa4e430a00000000001da8bc0000000000000000, vaegir_face_middle_2],
  ["knight_2_7", "Boyar Ralcha", "Ralcha", tf_hero, 0, reserved,  fac_kingdom_2, [itm_wlong5,      itm_leather_jacket,     itm_kuyak_a,                   itm_leather_boots,          itm_mail_boots,                      itm_tagancha_helm_a,  itm_lamellar_gauntlets,          itm_great_bardiche,    itm_dec_steel_shield],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c04100153335ba9390b2d277500000000001d89120000000000000000, vaegir_face_old_2],
  ["knight_2_8", "Boyar Vlan", "Vlan", tf_hero, 0, reserved,  fac_kingdom_2, [itm_charger_black,            itm_nomad_robe,             itm_rus_scale,                     itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_noble_helmet, itm_lamellar_gauntlets,       itm_shortened_military_scythe,    itm_tab_shield_kite_d],    knight_attrib_3,wp(200),knight_skills_3|knows_trainer_5, 0x0000000c00046581234e8da2cdd248db00000000001f569c0000000000000000, vaegir_face_older_2],
  ["knight_2_9", "Boyar Mleza", "Mleza", tf_hero, 0, reserved,  fac_kingdom_2, [itm_charger2,      itm_rich_outfit,        itm_vaegir_elite_armor,                     itm_leather_boots,          itm_mail_chausses,                   itm_novogrod_helm,  itm_lamellar_gauntlets,        itm_great_bardiche,   itm_tab_shield_kite_d, itm_lonely, itm_arrows],    knight_attrib_4,wp(230),knight_skills_4, 0x0000000c160451d2136469c4d9b159ad00000000001e28f10000000000000000, vaegir_face_older_2],
  ["knight_2_10", "Boyar Nelag", "Nelag", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_steppe,          itm_fur_coat,        itm_balion_mail_coat,               itm_woolen_hose,            itm_mail_boots,                      itm_vaegir_noble_helmet,  itm_scale_gauntlets,      itm_rhun_glaive,itm_military_pick,   itm_steel_shield_kite],      knight_attrib_5,wp(260),knight_skills_5|knows_trainer_6, 0x0000000f7c00520e66b76edd5cd5eb6e00000000001f691e0000000000000000, vaegir_face_older_2],
  ["knight_2_11", "Boyar Crahask", "Crahask", tf_hero, 0, reserved,  fac_kingdom_2, [itm_2lamellar_charger,      itm_leather_jacket,     itm_vaegir_elite_armor,                   itm_nomad_boots,            itm_splinted_leather_greaves,        itm_vaegir_noble_helmet, itm_scale_gauntlets,           itm_sword_viking_3,  itm_short_imperial_bow  , itm_bow3_arr_spak ,      itm_tab_shield_kite_cav_a],    knight_attrib_1,wp(130),knight_skills_1, 0x0000000c1d0821d236acd6991b74d69d00000000001e476c0000000000000000, vaegir_face_middle_2],
  ["knight_2_12", "Boyar Bracha", "Bracha", tf_hero, 0, reserved,  fac_kingdom_2, [itm_wwarhorsemaille3,      itm_rich_outfit,        itm_swadian_ceremonial_plate_red,               itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_noble_helmet,  itm_mail_mittens,      itm_great_bardiche,    itm_tab_shield_kite_cav_a],    knight_attrib_2,wp(170),knight_skills_2, 0x0000000c0f04024b2509d5d53944c6a300000000001d5b320000000000000000, vaegir_face_old_2],
  ["knight_2_13", "Boyar Druli", "Druli", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_holy,            itm_short_tunic,        itm_brigandine_plate_heraldic,                   itm_woolen_hose,            itm_mail_chausses,                   itm_mask_helmet1,  itm_lamellar_gauntlets,          itm_great_bardiche,           itm_steel_shield_heater],     knight_attrib_3,wp(190),knight_skills_3, 0x0000000c680432d3392230cb926d56ca00000000001da69b0000000000000000, vaegir_face_older_2],
  ["knight_2_14", "Boyar Marmun", "Marmun", tf_hero, 0, reserved,  fac_kingdom_2, [itm_3lamellar_charger,      itm_courtly_outfit,     itm_lamellar_armor,               itm_leather_boots,          itm_mail_boots,                      itm_rus_helm,  itm_lamellar_gauntlets,        itm_shortened_military_scythe,   itm_tab_shield_kite_cav_b],    knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x0000000c27046000471bd2e93375b52c00000000001dd5220000000000000000, vaegir_face_older_2],
  ["knight_2_15", "Boyar Gastya", "Gastya", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_prp,            itm_rich_outfit,        itm_copy_rus_lamellar_b,                     itm_leather_boots,          itm_mail_chausses,                   itm_tagancha_helm_b, itm_lamellar_gauntlets,   itm_bastard_sword_b,  itm_shortened_military_scythe, itm_tab_shield_kite_cav_b],       knight_attrib_5,wp(250),knight_skills_5, 0x0000000de50052123b6bb36de5d6eb7400000000001dd72c0000000000000000, vaegir_face_older_2],
  ["knight_2_16", "Boyar Harish", "Harish", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_holy,      itm_nomad_vest,      itm_vaegir_elite_armor,                   itm_woolen_hose,            itm_mail_chausses,                   itm_vaegir_noble_helmet,  itm_mail_mittens,          itm_great_bardiche,           itm_tab_shield_kite_c],   knight_attrib_1,wp(120),knight_skills_1, 0x000000085f00000539233512e287391d00000000001db7200000000000000000, vaegir_face_middle_2],
  ["knight_2_17", "Boyar Taisa", "Taisa", tf_hero, 0, reserved,  fac_kingdom_2, [itm_wwarhorsemaille1,      itm_leather_jacket,     itm_copy_rus_scale,                   itm_leather_boots,          itm_mail_boots,                      itm_rus_helm,   itm_scale_gauntlets,         itm_great_bardiche,    itm_tab_shield_kite_cav_a],     knight_attrib_2,wp(150),knight_skills_2, 0x0000000a070c4387374bd19addd2a4ab00000000001e32cc0000000000000000, vaegir_face_old_2],
  ["knight_2_18", "Boyar Valishin", "Valishin", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_blu2,            itm_nomad_robe,             itm_brigandine_plate_heraldic,                     itm_woolen_hose,            itm_mail_chausses,                   itm_mongol_helmet_xf,  itm_lamellar_gauntlets,      itm_great_bardiche,    itm_tab_shield_kite_cav_a],    knight_attrib_3,wp(180),knight_skills_3, 0x0000000b670012c23d9b6d4a92ada53500000000001cc1180000000000000000, vaegir_face_older_2],
  ["knight_2_19", "Boyar Rudin", "Rudin", tf_hero, 0, reserved,  fac_kingdom_2, [itm_wwarhorsemaille1,      itm_rich_outfit,        itm_vaegir_elite_armor,                     itm_leather_boots,          itm_mail_chausses,                   itm_vaegir_noble_helmet, itm_scale_gauntlets,         itm_rhun_greatsword,itm_fighting_pick,  itm_shortened_military_scythe, itm_tab_shield_kite_d],    knight_attrib_4,wp(210),knight_skills_4|knows_trainer_4, 0x0000000e070050853b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],
  ["knight_2_20", "Boyar Kumipa", "Kumipa", tf_hero, 0, reserved,  fac_kingdom_2, [itm_warhorse_steppe,          itm_fur_coat,        itm_lamellar_armor,               itm_woolen_hose,            itm_mail_boots,                      itm_mask_helmet1,  itm_lamellar_gauntlets,      itm_great_bardiche,   itm_lonely, itm_bodkin_arrows],      knight_attrib_5,wp(240),knight_skills_5|knows_trainer_5, 0x0000000f800021c63b0a6e4994ae272a00000000001db4e10000000000000000, vaegir_face_older_2],

#khergit civilian clothes: itm_leather_vest, itm_nomad_vest, itm_nomad_robe, itm_lamellar_vest,itm_tribal_warrior_outfit
  ["knight_3_1", "Alagur Noyan", "Alagur", tf_hero, 0, reserved,  fac_kingdom_3, [itm_easterling_warhorse01, itm_leather_vest,  itm_lamellar_armor_cloak,itm_nomad_boots,  itm_mail_boots, itm_mask_helmet1, itm_lamellar_gauntlets, itm_leather_gloves,  itm_jack_anduril, itm_tab_shield_small_round_c, itm_spak_bow7, itm_khergit_arrows],  knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x000000043000318b54b246b7094dc39c00000000001d31270000000000000000, khergit_face_middle_2],
  ["knight_3_2", "Tonju Noyan",  "Tonju", tf_hero, 0, reserved,  fac_kingdom_3, [itm_easterling_warhorse01, itm_nomad_vest,   itm_lamellar_armor, itm_hide_boots,  itm_mail_boots, itm_mask_helmet1, itm_lamellar_gauntlets, itm_leather_gloves, itm_khergit_sword_two_handed_b,  itm_painted_brass_shield, itm_khergit_bow, itm_arrows], knight_attrib_2,wp(160),knight_skills_2, 0x0000000c280461004929b334ad632aa200000000001e05120000000000000000, khergit_face_old_2],
  ["knight_3_3", "Belir Noyan",  "Belir", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe, itm_nomad_robe, itm_lamellar_armor,itm_nomad_boots,  itm_splinted_leather_greaves,  itm_khergit_guard_helmet, itm_lamellar_gauntlets, itm_jack_faramir,  itm_tab_shield_small_round_c, itm_spak_bow7, itm_barbed_arrows],  knight_attrib_3,wp(190),knight_skills_3|knows_trainer_5, 0x0000000e880062c53b0a6e4994ae272a00000000001db4e10000000000000000, khergit_face_older_2],
  ["knight_3_4", "Asugan Noyan", "Asugan", tf_hero, 0, reserved,  fac_kingdom_3, [itm_lamellar_charger_a, itm_mongol_armor_heavy,  itm_nomad_robe, itm_hide_boots,  itm_splinted_greaves,   itm_khergit_cavalry_helmet, itm_lamellar_gauntlets, itm_khergit_sword_two_handed_b, itm_rhun_glaive,  itm_dec_steel_shield],  knight_attrib_4,wp(220),knight_skills_4, 0x0000000c23085386391b5ac72a96d95c00000000001e37230000000000000000, khergit_face_older_2],
  ["knight_3_5", "Brula Noyan",  "Brula", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe, itm_ragged_outfit,  itm_lamellar_vest_khergit, itm_hide_boots,  itm_mail_boots, itm_khergit_guard_helmet, itm_lamellar_gauntlets, itm_sword_khergit_3, itm_rhun_glaive, itm_tab_shield_small_round_c],  knight_attrib_5,wp(250),knight_skills_5, 0x0000000efe0051ca4b377b4964b6eb6500000000001f696c0000000000000000, khergit_face_older_2],
  ["knight_3_6", "Imirza Noyan", "Imirza", tf_hero, 0, reserved,  fac_kingdom_3, [itm_courser, itm_tribal_warrior_outfit,itm_rich_tunic_a_lamellar_armour,itm_hide_boots, itm_splinted_leather_greaves,  itm_mongol_helmet_xf,  itm_lamellar_gauntlets, itm_jack_glamdring,itm_lance,  itm_tab_shield_small_round_b], knight_attrib_1,wp(130),knight_skills_1, 0x00000006f600418b54b246b7094dc31a00000000001d37270000000000000000, khergit_face_middle_2],
  ["knight_3_7", "Urumuda Noyan","Urumuda", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe,  itm_leather_vest,itm_nomad_vest_lamellar,itm_leather_boots, itm_hide_boots, itm_skullcap, itm_mask_helmet1, itm_lamellar_gauntlets,itm_rhun_glaive,  itm_sword_khergit_3, itm_tab_shield_small_round_b], knight_attrib_2,wp(160),knight_skills_2, 0x0000000bdd00510a44be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_old_2],
  ["knight_3_8", "Kramuk Noyan", "Kramuk", tf_hero, 0, reserved,  fac_kingdom_3, [itm_wplatedcharger9,  itm_nomad_vest, itm_lamellar_armor, itm_woolen_hose, itm_splinted_greaves, itm_khergit_cavalry_helmet, itm_lamellar_gauntlets,itm_mongol_pike_a,   itm_pa_sword_07,itm_great_bardiche,  itm_tab_shield_small_round_c],  knight_attrib_3,wp(190),knight_skills_3, 0x0000000abc00518b5af4ab4b9c8e596400000000001dc76d0000000000000000, khergit_face_older_2],
  ["knight_3_9", "Chaurka Noyan","Chaurka", tf_hero, 0, reserved,  fac_kingdom_3, [itm_lamellar_charger_a,  itm_nomad_robe, itm_lamellar_armor_cloak,  itm_leather_boots, itm_splinted_leather_greaves,  itm_mongol_helmet_x, itm_lamellar_gauntlets,  itm_khergit_sword_two_handed_b,  itm_dec_steel_shield],  knight_attrib_4,wp(220),knight_skills_4, 0x0000000a180441c921a30ea68b54971500000000001e54db0000000000000000, khergit_face_older_2],
  ["knight_3_10", "Sebula Noyan","Sebula", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe,  itm_mongol_armor_heavy, itm_nomad_robe, itm_hide_boots, itm_mail_chausses,  itm_mask_helmet1, itm_lamellar_gauntlets,  itm_sword_khergit_4, itm_khergit_sword_two_handed_b,  itm_tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5|knows_trainer_6, 0x0000000a3b00418c5b36c686d920a76100000000001c436f0000000000000000, khergit_face_older_2],
  ["knight_3_11", "Tulug Noyan", "Tulug", tf_hero, 0, reserved,  fac_kingdom_3, [itm_lamellar_charger_a, itm_leather_vest, itm_nomad_vest_lamellar, itm_nomad_boots, itm_mail_boots,  itm_khergit_cavalry_helmet,  itm_leather_gloves, itm_sword_khergit_4,  itm_brass_shield, itm_lonely, itm_khergit_arrows],  knight_attrib_1,wp(150),knight_skills_1, 0x00000007d100534b44962d14d370c65c00000000001ed6df0000000000000000, khergit_face_middle_2],
  ["knight_3_12", "Nasugei Noyan", "Nasugei", tf_hero, 0, reserved,  fac_kingdom_3, [itm_wwarhorsemaille3, itm_nomad_vest, itm_lamellar_armor, itm_hide_boots, itm_mail_boots,  itm_mongol_helmet_x,  itm_leather_gloves,itm_mongol_pike_a, itm_pa_sword_02,  itm_brass_shield], knight_attrib_2,wp(190),knight_skills_2, 0x0000000bf400610c5b33d3c9258edb6c00000000001eb96d0000000000000000, khergit_face_old_2],
  ["knight_3_13", "Urubay Noyan","Urubay", tf_hero, 0, reserved,  fac_kingdom_3, [itm_easterling_warhorse01, itm_nomad_robe,  itm_lamellar_armor_cloak, itm_nomad_boots, itm_splinted_leather_greaves,  itm_khergit_cavalry_helmet, itm_lamellar_gauntlets, itm_pa_sword_07,  itm_tab_shield_small_round_c, itm_spak_bow7, itm_bodkin_arrows],  knight_attrib_3,wp(200),knight_skills_3|knows_trainer_3, 0x0000000bfd0061c65b6eb33b25d2591d00000000001f58eb0000000000000000, khergit_face_older_2],
  ["knight_3_14", "Hugu Noyan",  "Hugu", tf_hero, 0, reserved,  fac_kingdom_3, [itm_wwarhorsemaille3,  itm_mongol_armor_heavy, itm_nomad_robe,itm_hide_boots, itm_splinted_greaves, itm_khergit_guard_helmet, itm_lamellar_gauntlets, itm_shortened_military_scythe,itm_pa_sword_02,  itm_dec_steel_shield, itm_khergit_bow, itm_arrows],  knight_attrib_4,wp(300),knight_skills_4|knows_trainer_6, 0x0000000b6900514144be2d14d370c65c00000000001ed6df0000000000000000, khergit_face_older_2],
  ["knight_3_15", "Tansugai Noyan", "Tansugai", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe,   itm_ragged_outfit, itm_heavy_lamellar_armor, itm_hide_boots, itm_mail_boots,  itm_mask_helmet1, itm_sword_khergit_4, itm_khergit_sword_two_handed_b, itm_tab_shield_small_round_c],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_4, 0x0000000c360c524b6454465b59b9d93500000000001ea4860000000000000000, khergit_face_older_2],
  ["knight_3_16", "Tirida Noyan","Tirida", tf_hero, 0, reserved,  fac_kingdom_3, [itm_jewlw, itm_tribal_warrior_outfit,  itm_khergit_elite_armor,  itm_hide_boots,  itm_splinted_leather_greaves,  itm_khergit_guard_helmet, itm_leather_gloves,   itm_khergit_sword_two_handed_a,  itm_lance, itm_tab_shield_small_round_b, itm_khergit_bow, itm_bodkin_arrows],  knight_attrib_1,wp(120),knight_skills_1, 0x0000000c350c418438ab85b75c61b8d300000000001d21530000000000000000, khergit_face_middle_2],
  ["knight_3_17", "Ulusamai Noyan", "Ulusamai", tf_hero, 0, reserved,  fac_kingdom_3, [itm_wwarhorsemaille1,  itm_leather_vest, itm_mongol_armor_heavy, itm_leather_boots, itm_mail_boots, itm_mongol_helmet_xg1, itm_leather_gloves,   itm_great_bardiche, itm_tab_shield_small_round_c, itm_lonely, itm_arrows],  knight_attrib_2,wp(150),knight_skills_2, 0x0000000c3c0821c647264ab6e68dc4d500000000001e42590000000000000000, khergit_face_old_2],
  ["knight_3_18", "Karaban Noyan", "Karaban", tf_hero, 0, reserved,  fac_kingdom_3, [itm_wgoldcata,   itm_nomad_vest, itm_khergit_elite_armor, itm_hide_boots, itm_splinted_greaves,  itm_mongol_helmet_xf, itm_scale_gauntlets,itm_mongol_pike_a,   itm_rhun_greatsword, itm_tab_shield_small_round_c, itm_lance,  itm_spak_bow7,itm_khergit_arrows, itm_arrows],   knight_attrib_3,wp(180),knight_skills_3|knows_trainer_4, 0x0000000c0810500347ae7acd0d3ad74a00000000001e289a0000000000000000, khergit_face_older_2],
  ["knight_3_19", "Akadan Noyan","Akadan", tf_hero, 0, reserved,  fac_kingdom_3, [itm_easterling_warhorse01,   itm_nomad_robe, itm_lamellar_armor_cloak, itm_leather_boots, itm_splinted_leather_greaves,  itm_mask_helmet1, itm_lamellar_gauntlets, itm_sword_khergit_4, itm_shortened_military_scythe, itm_tab_shield_small_round_c],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x0000000c1500510528f50d52d20b152300000000001d66db0000000000000000, khergit_face_older_2],
  ["knight_3_20", "Dundush Noyan","Dundush", tf_hero, 0, reserved,  fac_kingdom_3, [itm_warhorse_steppe, itm_nomad_robe, itm_khergit_elite_armor, itm_hide_boots, itm_mail_chausses, itm_mongol_helmet_xf, itm_scale_gauntlets, itm_khergit_sword_two_handed_a, itm_brass_shield, itm_lance, itm_khergit_bow, itm_barbed_arrows],  knight_attrib_5,wp(240),knight_skills_5, 0x0000000f7800620d66b76edd5cd5eb6e00000000001f691e0000000000000000, khergit_face_older_2],

  ["knight_4_1", "Jarl Aedin", "Aedin", tf_hero, 0, reserved,  fac_kingdom_4, [itm_rich_outfit,  itm_dejawolf_vikingbyrnie,   itm_woolen_hose,  itm_mail_boots,  itm_valsgarde_new, itm_mail_mittens, itm_great_axe,itm_pa_axe_04, itm_tab_shield_round_d,itm_sp_2hsw, itm_throwing_axes], knight_attrib_1,wp(130),knight_skills_1, 0x0000000c13002254340eb1d91159392d00000000001eb75a0000000000000000, nord_face_middle_2],
  ["knight_4_2", "Jarl Irya", "Irya", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_short_tunic,  itm_banded_armor, itm_blue_hose,  itm_splinted_greaves,  itm_maciejowski_helmet_new_grn, itm_scale_gauntlets, itm_vsword01,  itm_tab_shield_round_d, itm_throwing_axes],  knight_attrib_2,wp(160),knight_skills_2|knows_trainer_3, 0x0000000c1610218368e29744e9a5985b00000000001db2a10000000000000000, nord_face_old_2],
  ["knight_4_3", "Jarl Olaf", "Olaf", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse, itm_rich_outfit,  itm_heraldic_mail_with_tabard,   itm_nomad_boots,  itm_mail_chausses, itm_scale_gauntlets,   itm_nordic_warlord_helmet,   itm_great_axe,itm_ak_wlocznie_a, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_3,wp(190),knight_skills_3, 0x0000000c03040289245a314b744b30a400000000001eb2a90000000000000000, nord_face_older_2],
  ["knight_4_4", "Jarl Reamald", "Reamald", tf_hero, 0, reserved,  fac_kingdom_4, [itm_wlong16,   itm_leather_vest,   itm_banded_armor,   itm_woolen_hose,  itm_mail_boots, itm_scale_gauntlets,  itm_col1_crusaderbucket1, itm_fighting_pick,itm_mercy, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(210),knight_skills_4, 0x0000000c3f1001ca3d6955b26a8939a300000000001e39b60000000000000000, nord_face_older_2],
  ["knight_4_5", "Jarl Turya", "Turya", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_heraldic_mail_with_surcoat,   itm_leather_boots,  itm_splinted_leather_greaves,  itm_scale_gauntlets, itm_nordic_huscarl_helmet, itm_vsword02, itm_tab_shield_round_e, itm_throwing_axes, itm_throwing_axes], knight_attrib_5,wp(250),knight_skills_5, 0x0000000ff508330546dc4a59422d450c00000000001e51340000000000000000, nord_face_older_2],
  ["knight_4_6", "Jarl Gundur", "Gundur", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_nomad_robe,   itm_dejawolf_vikingbyrnie,  itm_nomad_boots,  itm_mail_chausses,   itm_maciejowski_helmet_new_b2, itm_mail_mittens,itm_sp_2hsw,   itm_war_axe, itm_tab_shield_round_d],   knight_attrib_1,wp(130),knight_skills_1, 0x00000005b00011813d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_middle_2],
  ["knight_4_7", "Jarl Harald", "Harald", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_arnor_reinf_jerkin,   itm_nomad_boots,  itm_mail_boots,  itm_valsgarde_new, itm_mail_mittens,   itm_sword_viking_3, itm_shortened_military_scythe,itm_ak_wlocznie_a,  itm_tab_shield_round_d],   knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x00000006690002873d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_old_2],
  ["knight_4_8", "Jarl Knudarr", "Knudarr", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_mail_and_plate,   itm_woolen_hose,  itm_mail_chausses,   itm_valsgarde_guards2, itm_scale_gauntlets, itm_war_axe,  itm_tab_shield_round_e, itm_throwing_axes],   knight_attrib_3,wp(190),knight_skills_3, 0x0000000f830051c53b026e4994ae272a00000000001db4e10000000000000000, nord_face_older_2],
  ["knight_4_9", "Jarl Haeda", "Haeda", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse, itm_nomad_robe,   itm_banded_armor_a_new1, itm_blue_hose,  itm_mail_boots,  itm_guard_helmet, itm_scale_gauntlets, itm_arrows, itm_long_bow,   itm_one_handed_battle_axe_c,  itm_tab_shield_round_e],  knight_attrib_4,wp(220),knight_skills_4|knows_trainer_5|knows_power_draw_4, 0x00000000080c54c1345bd21349b1b67300000000001c90c80000000000000000, nord_face_older_2],
  ["knight_4_10", "Jarl Turegor", "Turegor", tf_hero, 0, reserved,  fac_kingdom_4, [itm_scalecharger2w,   itm_courtly_outfit,   itm_coat_of_plates,   itm_nomad_boots,  itm_splinted_greaves, itm_scale_gauntlets,  itm_winged_great_helmet,itm_great_axe, itm_tab_shield_round_e],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_6, 0x000000084b0002063d9b6d4a92ada53500000000001cc1180000000000000000, nord_face_older_2],
  ["knight_4_11", "Jarl Logarson", "Logarson", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_banded_armor,   itm_woolen_hose,  itm_mail_boots,  itm_nordic_helmet,  itm_mail_mittens,  itm_great_bardiche,itm_pa_axe_06, itm_tab_shield_round_d], knight_attrib_1,wp(140),knight_skills_1, 0x000000002d100005471d4ae69ccacb1d00000000001dca550000000000000000, nord_face_middle_2],
  ["knight_4_12", "Jarl Aeric", "Aeric", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_short_tunic,  itm_dejawolf_vikingbyrnie, itm_blue_hose,  itm_splinted_greaves,  itm_nordic_huscarl_helmet,  itm_mail_mittens,  itm_one_handed_battle_axe_c,  itm_tab_shield_round_d],  knight_attrib_2,wp(200),knight_skills_2, 0x0000000b9500020824936cc51cb5bb2500000000001dd4d80000000000000000, nord_face_old_2],
  ["knight_4_13", "Jarl Faarn", "Faarn", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse, itm_rich_outfit,  itm_heraldic_mail_with_tabard,   itm_nomad_boots,  itm_mail_chausses, itm_scale_gauntlets,   itm_nordic_warlord_helmet,   itm_sorrow,itm_war_axe, itm_tab_shield_round_e],  knight_attrib_3,wp(250),knight_skills_3|knows_trainer_3, 0x0000000a300012c439233512e287391d00000000001db7200000000000000000, nord_face_older_2],
  ["knight_4_14", "Jarl Bulba", "Bulba", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_leather_vest,   itm_banded_armor,   itm_woolen_hose,  itm_mail_boots,  itm_maciejowski_helmet_newmod1, itm_scale_gauntlets, itm_fighting_pick, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(200),knight_skills_4, 0x0000000c0700414f2cb6aa36ea50a69d00000000001dc55c0000000000000000, nord_face_older_2],
  ["knight_4_15", "Jarl Rayeck", "Rayeck", tf_hero, 0, reserved,  fac_kingdom_4, [itm_platedw,   itm_leather_jacket,   itm_heraldic_mail_with_tabard,   itm_leather_boots, itm_scale_gauntlets,  itm_splinted_leather_greaves,  itm_nordic_huscarl_helmet, itm_shortened_military_scythe, itm_tab_shield_round_e], knight_attrib_5,wp(290),knight_skills_5|knows_trainer_6, 0x0000000d920801831715d1aa9221372300000000001ec6630000000000000000, nord_face_older_2],
  ["knight_4_16", "Jarl Dirigun", "Dirigun", tf_hero, 0, reserved,  fac_kingdom_4, [   itm_nomad_robe,   itm_banded_armor,  itm_nomad_boots,  itm_mail_chausses,   itm_nordic_huscarl_helmet, itm_mail_mittens,   itm_war_axe, itm_tab_shield_round_d, itm_throwing_axes],   knight_attrib_1,wp(120),knight_skills_1, 0x000000099700124239233512e287391d00000000001db7200000000000000000, nord_face_middle_2],
  ["knight_4_17", "Jarl Marayirr", "Marayirr", tf_hero, 0, reserved,  fac_kingdom_4, [  itm_fur_coat,   itm_banded_armor,   itm_nomad_boots,  itm_mail_boots,  itm_nordic_warlord_helmet, itm_mail_mittens,   itm_sword_viking_3,  itm_tab_shield_round_d, itm_throwing_axes],   knight_attrib_2,wp(150),knight_skills_2|knows_trainer_4, 0x0000000c2f0442036d232a2324b5b81400000000001e55630000000000000000, nord_face_old_2],
  ["knight_4_18", "Jarl Gearth", "Gearth", tf_hero, 0, reserved,  fac_kingdom_4, [ itm_rich_outfit,  itm_mail_and_plate,   itm_woolen_hose,  itm_mail_chausses,   itm_segmented_helmet, itm_scale_gauntlets, itm_sword_viking_3, itm_shortened_military_scythe,  itm_tab_shield_round_d],   knight_attrib_3,wp(180),knight_skills_3, 0x0000000c0d00118866e22e3d9735a72600000000001eacad0000000000000000, nord_face_older_2],
  ["knight_4_19", "Jarl Surdun", "Surdun", tf_hero, 0, reserved,  fac_kingdom_4, [itm_warhorse, itm_nomad_robe,   itm_banded_armor_a_new1, itm_blue_hose,  itm_mail_boots,  itm_guard_helmet, itm_scale_gauntlets,   itm_one_handed_battle_axe_c,itm_sp_2hsw,  itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x0000000c0308225124e26d4a6295965a00000000001d23e40000000000000000, nord_face_older_2],
  ["knight_4_20", "Jarl Gerlad", "Gerlad", tf_hero, 0, reserved,  fac_kingdom_4, [itm_charger_02,   itm_courtly_outfit,   itm_coat_of_plates,   itm_nomad_boots,  itm_splinted_greaves, itm_scale_gauntlets,  itm_winged_great_helmet,itm_great_axe, itm_tab_shield_round_e, itm_throwing_axes],  knight_attrib_5,wp(240),knight_skills_5, 0x0000000f630052813b6bb36de5d6eb7400000000001dd72c0000000000000000, nord_face_older_2],

  ["knight_5_1", "Count Matheas", "Matheas", tf_hero, 0, reserved,  fac_kingdom_5, [itm_barded2w,   itm_tabard,   itm_heraldic_mail_with_surcoat,       itm_leather_boots,    itm_steel_greaves,    itm_guard_helmet, itm_leather_gloves, itm_sp_2hsw,    itm_fighting_pick,   itm_tab_shield_heater_c],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000a1b0c00483adcbaa5ac9a34a200000000001ca2d40000000000000000, rhodok_face_middle_2],
  ["knight_5_2", "Count Gutlans", "Gutlans", tf_hero, 0, reserved,  fac_kingdom_5, [itm_platedw,    itm_red_gambeson,       itm_heraldic_mail_with_tabard,    itm_leather_boots,    itm_mail_boots,    itm_maciejowski_helmet_newmod1, itm_leather_gloves,     itm_mercy, itm_military_pick,  itm_sword_two_handed_a,   itm_tab_shield_heater_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000c390c659229136db45a75251300000000001f16930000000000000000, rhodok_face_old_2],
  ["knight_5_3", "Count Laruqen", "Laruqen", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger_plate_1,     itm_short_tunic,  itm_mail_and_plate,     itm_nomad_boots,      itm_splinted_leather_greaves,  itm_chapel_de_fer_mail3, itm_gauntlets, itm_shortened_military_scythe,  itm_tab_shield_heater_d,itm_spak_crsb01,itm_steel_bolts],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000c2f10415108b1aacba27558d300000000001d329c0000000000000000, rhodok_face_older_2],
  ["knight_5_4", "Count Raichs", "Raichs", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_grn2,     itm_leather_jacket,     itm_brigandine_red,       itm_woolen_hose,      itm_splinted_greaves,    itm_zitta_bascinet, itm_gauntlets, itm_bastard_sword_a,itm_ak_poleaxe,    itm_tab_shield_heater_d],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c3c005110345c59d56975ba1200000000001e24e40000000000000000, rhodok_face_older_2],
  ["knight_5_5", "Count Reland", "Reland", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_holy,     itm_rich_outfit,  itm_copy_plate_harness_01,     itm_leather_boots,    itm_mail_boots,    itm_great_helmet, itm_gauntlets, itm_shortened_military_scythe,  itm_tab_shield_heater_d,itm_spak_crsb01,itm_steel_bolts], knight_attrib_5,wp(250),knight_skills_5, 0x0000000c060400c454826e471092299a00000000001d952d0000000000000000, rhodok_face_older_2],
  ["knight_5_6", "Count Tarchias", "Tarchias", tf_hero, 0, reserved,  fac_kingdom_5, [itm_sumpter_horse,    itm_ragged_outfit,      itm_heraldic_mail_with_tabard,       itm_woolen_hose,      itm_splinted_greaves, itm_gauntlets,   itm_skullcap,     itm_sword_two_handed_b,itm_luc_two_handed_axe_2,   itm_tab_shield_heater_c],    knight_attrib_1,wp(130),knight_skills_1, 0x000000001100000648d24d36cd964b1d00000000001e2dac0000000000000000, rhodok_face_middle_2],
  ["knight_5_7", "Count Gharmall", "Gharmall", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_ylw2,     itm_coarse_tunic,       itm_heraldic_mail_with_surcoat,   itm_leather_boots,    itm_mail_chausses,  itm_gauntlets,      itm_sallet_a_open1,       itm_bastard_sword_a,    itm_tab_shield_heater_c],     knight_attrib_2,wp(160),knight_skills_2, 0x0000000c3a0455c443d46e4c8b91291a00000000001ca51b0000000000000000, rhodok_face_old_2],
  ["knight_5_8", "Count Talbar", "Talbar", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_holy, itm_courtly_outfit,     itm_platemail_harness_05,    itm_woolen_hose,      itm_mail_boots,    itm_nasal_helmet,  itm_gauntlets,      itm_military_pick, itm_sword_two_handed_b,  itm_tab_shield_heater_c],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x0000000c2c0844d42914d19b2369b4ea00000000001e331b0000000000000000, rhodok_face_older_2],
  ["knight_5_9", "Count Rimusk", "Rimusk", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse,     itm_leather_jacket,     itm_heraldic_platemail_01,   itm_leather_boots,    itm_steel_greaves2,       itm_montforthelm, itm_gauntlets,   itm_great_bardiche,itm_ak_poleaxe,   itm_tab_shield_heater_d],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x00000000420430c32331b5551c4724a100000000001e39a40000000000000000, rhodok_face_older_2],
  ["knight_5_10", "Count Falsevor", "Falsevor", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse,     itm_rich_outfit,  itm_coat_of_plates_g,     itm_blue_hose,  itm_mail_chausses,       itm_great_helmet, itm_gauntlets,       itm_bastard_sword_a,   itm_tab_shield_heater_d],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4, 0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000, rhodok_face_older_2],
  ["knight_5_11", "Count Etrosq", "Etrosq", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger_black,     itm_tabard,       itm_guesclin_banner,       itm_leather_boots,    itm_steel_greaves,    itm_maciejowski_helmet_newmod1,  itm_leather_gloves,    itm_fighting_pick,   itm_tab_shield_heater_c,itm_steel_bolts,itm_sniper_crossbow],     knight_attrib_1,wp(130),knight_skills_1, 0x0000000c170c14874752adb6eb3228d500000000001c955c0000000000000000, rhodok_face_middle_2],
  ["knight_5_12", "Count Kurnias", "Kurnias", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger_black,    itm_red_gambeson,       itm_heraldic_mail_with_tabard,    itm_leather_boots,    itm_mail_boots,    itm_sallet_a_open1,  itm_demi_gauntlets,      itm_military_pick,   itm_tab_shield_heater_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x0000000c080c13d056ec8da85e3126ed00000000001d4ce60000000000000000, rhodok_face_old_2],
  ["knight_5_13", "Count Tellrog", "Tellrog", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger2,     itm_short_tunic,  itm_guesclin,     itm_nomad_boots,      itm_splinted_leather_greaves,  itm_winged_great_helmet, itm_gauntlets,       itm_sword_two_handed_a,  itm_tab_shield_heater_d],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000cbf10100562a4954ae731588a00000000001d6b530000000000000000, rhodok_face_older_2],
  ["knight_5_14", "Count Tribidan", "Tribidan", tf_hero, 0, reserved,  fac_kingdom_5, [itm_hunter,     itm_leather_jacket,     itm_full_plate_armor_banner,       itm_woolen_hose,      itm_steel_greaves2,    itm_sallet_a_closed1, itm_gauntlets, itm_bastard_sword_a,    itm_tab_shield_heater_d],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c330805823baa77556c4e331a00000000001cb9110000000000000000, rhodok_face_older_2],
  ["knight_5_15", "Count Gerluchs", "Gerluchs", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_prp,     itm_rich_outfit,  itm_heraldic_platemail_02,     itm_leather_boots,    itm_mail_boots,    itm_great_helmet, itm_gauntlets,       itm_sword_two_handed_a,  itm_tab_shield_heater_d], knight_attrib_5,wp(250),knight_skills_5, 0x0000000d51000106370c4d4732b536de00000000001db9280000000000000000, rhodok_face_older_2],
  ["knight_5_16", "Count Fudreim", "Fudreim", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_sarranid,    itm_ragged_outfit,      itm_heraldic_mail_with_tabard,       itm_woolen_hose,      itm_splinted_greaves,    itm_guard_helmet, itm_leather_gloves,itm_ganquang_axe,     itm_fighting_pick,   itm_tab_shield_heater_c],    knight_attrib_1,wp(120),knight_skills_1, 0x0000000c06046151435b5122a37756a400000000001c46e50000000000000000, rhodok_face_middle_2],
  ["knight_5_17", "Count Nealcha", "Nealcha", tf_hero, 0, reserved,  fac_kingdom_5, [itm_barded2w,     itm_coarse_tunic,       itm_heraldic_mail_with_surcoat,   itm_leather_boots,    itm_mail_chausses,       itm_col1_crusaderbucket1,  itm_demi_gauntlets,      itm_bastard_sword_a,itm_jack_anduril,    itm_tab_shield_heater_c,itm_steel_bolts,itm_sniper_crossbow],     knight_attrib_2,wp(150),knight_skills_2, 0x0000000c081001d3465c89a6a452356300000000001cda550000000000000000, rhodok_face_old_2],
  ["knight_5_18", "Count Fraichin", "Fraichin", tf_hero, 0, reserved,  fac_kingdom_5, [itm_charger_steel, itm_courtly_outfit,     itm_swadian_lordly_plate_armor,    itm_woolen_hose,      itm_mail_boots,    itm_col1_gotlandbucket, itm_gauntlets,       itm_ganquang_pick,   itm_tab_shield_heater_d,itm_flintlock_pistol,itm_cartridges],    knight_attrib_3,wp(180),knight_skills_3, 0x0000000a3d0c13c3452aa967276dc95c00000000001dad350000000000000000, rhodok_face_older_2],
  ["knight_5_19", "Count Trimbau", "Trimbau", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse_sarranid,     itm_leather_jacket,     itm_brigandine_plate_heraldic,   itm_leather_boots,    itm_splinted_leather_greaves,       itm_kettle_hat, itm_gauntlets,   itm_fighting_pick,  itm_sword_two_handed_a, itm_tab_shield_heater_d],   knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x0000000038043194092ab4b2d9adb44c00000000001e072c0000000000000000, rhodok_face_older_2],
  ["knight_5_20", "Count Reichsin", "Reichsin", tf_hero, 0, reserved,  fac_kingdom_5, [itm_warhorse,     itm_rich_outfit,  itm_rhodok_honorguard_armor,     itm_blue_hose,  itm_mail_chausses,       itm_great_helmet, itm_gauntlets,       itm_sp_2hsw, itm_ganquang_pick,  itm_tab_shield_heater_d,itm_steel_bolts,itm_sniper_crossbow],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_6, 0x000000003600420515a865b45c64d64c00000000001d544b0000000000000000, rhodok_face_older_2],

  ["knight_6_1", "Emir Uqais", "Uqais", tf_hero, 0, reserved,  fac_kingdom_6, [itm_wgoldcata,   itm_mamluke_mail,          itm_sarranid_boots_c,    itm_mail_boots,    itm_sarranid_warrior_cap, itm_leather_gloves,    itm_rhun_greatfalchion, itm_sarranid_cavalry_sword,   itm_brass_shield],     knight_attrib_1,wp(130),knight_skills_1|knows_trainer_3, 0x0000000fa00ca084486195383349eae500000000001d16a30000000000000000],
  ["knight_6_2", "Emir Hamezan", "Hamezan", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_b,    itm_sarranid_elite_armor,       itm_sarranid_boots_c,    itm_mail_boots,    itm_sarranid_warrior_cap, itm_leather_gloves,   itm_lance, itm_pa_sword_07,  itm_military_pick,  itm_sword_two_handed_a,   itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_4, 0x0000000cf808d5d444cb68b92b8d3b1d00000000001dd71e0000000000000000],
  ["knight_6_3", "Emir Atis", "Atis", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger_y,     itm_mamluke_mail,       itm_nomad_boots,      itm_sarranid_warrior_cap,  itm_shortened_military_scythe, itm_lamellar_gauntlets,itm_jack_anduril,  itm_tab_shield_small_round_c],    knight_attrib_3,wp(190),knight_skills_3, 0x0000000f6208a28579723147247ad4e500000000001f14d40000000000000000],
  ["knight_6_4", "Emir Nuwas", "Nuwas", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger_x,     itm_sarranid_mail_shirt,            itm_sarranid_boots_c,          itm_sarranid_mail_coif,  itm_sarranid_cavalry_sword, itm_lamellar_gauntlets, itm_lance, itm_jack_glamdring,  itm_brass_shield1],    knight_attrib_4,wp(220),knight_skills_4, 0x0000000c7f08a285050caa7d285be51a00000000001d11010000000000000000],
  ["knight_6_5", "Emir Mundhalir", "Mundhalir", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger_x,     itm_sarranid_elite_cavalary_mod1,       itm_sarranid_boots_c,    itm_sarranid_veiled_helmet,  itm_shortened_military_scythe,itm_rhun_greatsword,  itm_tab_shield_small_round_c], knight_attrib_5,wp(250),knight_skills_5, 0x0000000faa08a003330175aae175da9c00000000001e02150000000000000000],
  ["knight_6_6", "Emir Ghanawa", "Ghanawa", tf_hero, 0, reserved,  fac_kingdom_6, [itm_arabian_horse_a,    itm_sarranid_elite_armor,            itm_sarranid_boots_c,      itm_splinted_greaves,    itm_sarranid_veiled_helmet, itm_lance,  itm_pa_sword_02,    itm_sarranid_cavalry_sword,   itm_tab_shield_small_round_c],    knight_attrib_1,wp(130),knight_skills_1, 0x0000000a8300d3834733294c89b128e200000000001e59510000000000000000],
  ["knight_6_7", "Emir Nuam", "Nuam", tf_hero, 0, reserved,  fac_kingdom_6, [itm_wwarhorsemaille3,     itm_sarranid_elite_cavalary_mod1,          itm_sarranid_boots_c,          itm_sarranid_mail_coif,       itm_sarranid_cavalry_sword,  itm_lamellar_gauntlets,  itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2, 0x0000000fbf10c34020504bbbda9135d500000000001f62380000000000000000],
  ["knight_6_8", "Emir Dhiyul", "Dhiyul", tf_hero, 0, reserved,  fac_kingdom_6, [itm_wlong22, itm_mamluke_mail,         itm_sarranid_boots_c,      itm_mail_boots,    itm_vaegir_mask,        itm_lance,itm_pa_sword_04,  itm_sarranid_cavalry_sword,  itm_brass_shield],    knight_attrib_3,wp(190),knight_skills_3|knows_trainer_3, 0x0000000ed004d003336dcd3ca2cacae300000000001f47640000000000000000],
  ["knight_6_9", "Emir Lakhem", "Lakhem", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_heavy_lamellar_armor,        itm_sarranid_boots_c,    itm_sarranid_royal_helmet, itm_lamellar_gauntlets, itm_pa_axe_01,  itm_lance, itm_tab_shield_small_round_c],   knight_attrib_4,wp(220),knight_skills_4|knows_trainer_6, 0x000000045e00d0c4549dd5ca6f4dd56500000000001e291b0000000000000000],
  ["knight_6_10", "Emir Ghulassen", "Ghulassen", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_arab_mail_plate_3,itm_arabian_robe_a,       itm_sarranid_boots_c,  itm_sarranid_boots_c,       itm_sarranid_helmet1, itm_lamellar_gauntlets,   itm_lance,itm_ak_poleaxe,     itm_sarranid_cavalry_sword,   itm_tab_shield_small_round_c],  knight_attrib_5,wp(250),knight_skills_5|knows_trainer_4, 0x00000003e604c1c66ce99256b4ad4b3300000000001d392c0000000000000000],
  ["knight_6_11", "Emir Azadun", "Azadun", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger_a,     itm_arab_mail_plate_3,              itm_sarranid_boots_c,    itm_sarranid_boots_c,    itm_sarranid_mail_coif,  itm_leather_gloves, itm_despair,   itm_fighting_pick, itm_mongol_spear_x,  itm_tab_shield_small_round_c],     knight_attrib_1,wp(130),knight_skills_1, 0x000000023f08c34726c28af8dc96e4da00000000001e541d0000000000000000],
  ["knight_6_12", "Emir Quryas", "Quryas", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger_a,    itm_mamluke_mail,           itm_sarranid_boots_c,    itm_mail_boots,    itm_sarranid_veiled_helmet, itm_lance,    itm_military_pick,itm_rhun_greatsword,   itm_tab_shield_small_round_c],     knight_attrib_2,wp(160),knight_skills_2|knows_trainer_5, 0x000000043510a084635b74ba5491a7a400000000001e46d60000000000000000],
  ["knight_6_13", "Emir Amdar", "Amdar", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger_x,     itm_sarranid_mail_shirt,       itm_sarranid_boots_c,      itm_sarranid_boots_c,  itm_sarranid_royal_helmet,   itm_lamellar_gauntlets, itm_mercy,    itm_sword_two_handed_a,  itm_brass_shield1],    knight_attrib_3,wp(190),knight_skills_3, 0x000000058010a1435b734d4ad94eba9400000000001eb8eb0000000000000000],
  ["knight_6_14", "Emir Hiwan", "Hiwan", tf_hero, 0, reserved,  fac_kingdom_6, [itm_jewlw,     itm_sarranid_elite_armor,       itm_sarranid_boots_c,      itm_sarranid_boots_c,    itm_sarranid_mail_coif, itm_lance,itm_luc_knightly_axe_two_handed,  itm_sarranid_cavalry_sword,    itm_tab_shield_small_round_c],    knight_attrib_4,wp(220),knight_skills_4, 0x000000058c0ca5c63a5b921ac22db8e200000000001cca530000000000000000],
  ["knight_6_15", "Emir Muhnir", "Muhnir", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger_x,     itm_arab_mail_plate_3,       itm_sarranid_boots_c,    itm_mail_boots,    itm_vaegir_mask,  itm_sword_two_handed_a,  itm_tab_shield_small_round_c,itm_flintlock_pistol,itm_cartridges], knight_attrib_5,wp(250),knight_skills_5, 0x000000035b0ca185369a6938cecde95600000000001f25210000000000000000],
  
  ["knight_6_16", "Emir Ayyam", "Ayyam", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger_y,    itm_mamluke_mail,             itm_sarranid_boots_c,      itm_sarranid_boots_c,    itm_sarranid_royal_helmet, itm_leather_gloves,  itm_lance,itm_ganquang_dart,    itm_fighting_pick,   itm_dec_steel_shield],    knight_attrib_1,wp(120),knight_skills_1, 0x000000017708a1c80a01e1c5eb51ffff00000000001f12d80000000000000000],
  ["knight_6_17", "Emir Raddoun", "Raddoun", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger_y,     itm_sarranid_elite_cavalary_mod1,          itm_sarranid_boots_c,    itm_sarranid_boots_c,       itm_sarranid_mail_coif,  itm_leather_gloves,      itm_sarranid_cavalry_sword,itm_great_long_bardiche,    itm_tab_shield_small_round_c],     knight_attrib_2,wp(150),knight_skills_2, 0x000000007f0462c32419f47a1aba8bcf00000000001e7e090000000000000000, rhodok_face_old_2],
  ["knight_6_18", "Emir Tilimsan", "Tilimsan", tf_hero, 0, reserved,  fac_kingdom_6, [itm_lamellar_charger_x,  itm_sarranid_elite_armor,     itm_sarranid_boots_c,      itm_mail_boots,    itm_sarranid_helmet1,  itm_lance,       itm_military_pick,   itm_tab_shield_small_round_c],    knight_attrib_3,wp(180),knight_skills_3, 0x000000017410a10070d975caac91aca500000000001c27530000000000000000],
  ["knight_6_19", "Emir Dhashwal", "Dhashwal", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_sarranid_mail_shirt,        itm_sarranid_boots_c,    itm_sarranid_boots_c,       itm_sarranid_mail_coif, itm_lamellar_gauntlets,   itm_sp_2hsw,  itm_sword_two_handed_a, itm_tab_shield_small_round_c,itm_flintlock_pistol,itm_cartridges],   knight_attrib_4,wp(210),knight_skills_4|knows_trainer_5, 0x000000048a08a18016ac36bc8b6e4a9900000000001dd45d0000000000000000],
  ["knight_6_20", "Emir Biliya", "Biliya", tf_hero, 0, reserved,  fac_kingdom_6, [itm_warhorse_sarranid,     itm_sarranid_cavalry_robe,       itm_sarranid_boots_c,  itm_sarranid_boots_c,       itm_sarranid_veiled_helmet,   itm_lance,      itm_sarranid_cavalry_sword,   itm_tab_shield_small_round_c],  knight_attrib_5,wp(240),knight_skills_5|knows_trainer_6, 0x00000006bd00d0c0281a899ac956b94b00000000001ec8910000000000000000],

  #kingdom7
  ["knight_7_1","Count Theodor", "Theodor",tf_hero, 0,0, fac_kingdom_7,[itm_jewlw,itm_rus_scale,itm_tagancha_helm_b,itm_rus_splint_greaves,itm_dorn_spearbearer_guant,itm_sp_2hsw,itm_tab_shield_kite_d,itm_jarid],
  knight_attrib_5,wp(350),knight_skills_5,0x0000000aad10251170e17e36db90bbbc00000000001d99300000000000000000],

  #zendar lord
  ["knight_8_1","Count Alexis", "Alexis",tf_hero, 0,0, fac_kingdom_8,[itm_tab_shield_kite_cav_b,itm_guard_helmet,itm_sword_medieval_d_long,itm_heraldic_mail_with_tabard,itm_mail_boots,itm_gauntlets,itm_warhorse_steppe],
  knight_attrib_4,wp(230),knight_skills_4,0x000000061e1032442d1d6c152455c86300000000001e45190000000000000000],
  ["knight_8_2","Count Framar", "Framar",tf_tall|tf_hero, 0,0, fac_kingdom_8,[itm_platemail_harness_05,itm_steel_boots_01,itm_leduc_helm,itm_henrysword,itm_steel_mittens,itm_charger_plate_1,itm_toumao],
  str_50|agi_50|int_25|cha_35|level(60),wp(400),knight_skills_5|knows_ironflesh_3|knows_power_strike_3,0x0000000b8010030a377971b92456472b00000000001db2ea0000000000000000],
  ["knight_8_3","Count Laris", "Laris",tf_hero, 0,0, fac_kingdom_8,[itm_dorn_knight_helmet_black_c,itm_riv_surcoat_b_cloak,itm_rivendellbow,itm_bow4_arr_spak,itm_rus_cav_boots_black,itm_dorn_spearbearer_guant,itm_jack_faramir,itm_sp_shr1,itm_wlong3],
  knight_attrib_4,wp(260),knight_skills_5,0x000000067f11114871f66988b978904e00000000001cb4b80000000000000000],
  ["knight_8_4","Count Aenar", "Aenar",tf_hero, 0,0, fac_kingdom_8,[itm_dorn_knight_helmet_black_c,itm_dorn_knight_armor_black,itm_dorn_spearbearer_boots,itm_jack_anduril,itm_rivendellbow,itm_bow4_arr_spak,itm_wplatedcharger7,itm_dorn_spearbearer_guant],
  knight_attrib_5,wp(285),knight_skills_4,0x0000000c3f09100533cb457c791090da00000000001c4b380000000000000000],
  ["knight_8_5","Count Griselda", "Griselda",tf_beautiful|tf_hero, 0,0, fac_kingdom_8,[itm_riv_foot_scale_b_cloak,itm_rus_cav_boots_black,itm_silver_lorien_round_shield,itm_pa_sword_02,itm_arrows_ghost,itm_war_bow_ghost_1,itm_ak_courser,itm_face_frame_a_1],
  knight_attrib_5,wp(320),knight_skills_4,0x00000003400c000e0000000000000e8300000000000000000000000000000000],
  
  ["kingdom_1_pretender",  "Lady Isolla of Suno",       "Isolla",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_1,[itm_charger,   itm_rich_outfit,  itm_blue_hose,      itm_iron_greaves,         itm_mail_shirt,      itm_sword_medieval_c_small,      itm_tab_shield_small_round_c,       itm_bascinet],          lord_attrib,wp(220),knight_skills_5, 0x00000000ef00000237dc71b90c31631200000000001e371b0000000000000000],
#claims pre-salic descent

  ["kingdom_2_pretender",  "Prince Valdym the Bastard", "Valdym",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_2,[itm_hunter,    itm_courtly_outfit,      itm_leather_boots,              itm_mail_chausses,              itm_lamellar_armor,       itm_military_pick,      itm_tab_shield_heater_b,      itm_flat_topped_helmet],    lord_attrib,wp(220),knight_skills_5, 0x00000000200412142452ed631b30365c00000000001c94e80000000000000000, vaegir_face_middle_2],
#had his patrimony falsified

  ["kingdom_3_pretender",  "Dustum Khan",               "Dustum",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_3,[itm_courser,   itm_nomad_robe,             itm_leather_boots,              itm_splinted_greaves,           itm_khergit_guard_armor,         itm_sword_khergit_2,              itm_tab_shield_small_round_c,       itm_segmented_helmet],      lord_attrib,wp(220),knight_skills_5, 0x000000065504310b30d556b51238f66100000000001c256d0000000000000000, khergit_face_middle_2],
#of the family

  ["kingdom_4_pretender",  "Lethwin Far-Seeker",   "Lethwin",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_4,[itm_hunter,    itm_tabard,    itm_leather_boots,              itm_mail_boots,                 itm_brigandine_red,           itm_sword_medieval_c,           itm_tab_shield_heater_cav_a,    itm_kettle_hat],            lord_attrib,wp(220),knight_skills_5, 0x00000004340c01841d89949529a6776a00000000001c910a0000000000000000, nord_face_young_2],
#dispossessed and wronged

  ["kingdom_5_pretender",  "Lord Kastor of Veluca",  "Kastor",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_nobleman_outfit,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_mail_hauberk,           itm_sword_medieval_c,         itm_tab_shield_heater_d,        itm_spiked_helmet],         lord_attrib,wp(220),knight_skills_5, 0x0000000bed1031051da9abc49ecce25e00000000001e98680000000000000000, rhodok_face_old_2],
#republican

  ["kingdom_6_pretender",  "Arwa the Pearled One",       "Arwa",  tf_hero|tf_beautiful|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_6,[itm_arabian_horse_b, itm_sarranid_mail_shirt, itm_sarranid_boots_c, itm_sarranid_cavalry_sword,      itm_tab_shield_small_round_c,itm_courtly_outfit],          lord_attrib,wp(220),knight_skills_5, 0x000000050b003004072d51c293a9a70b00000000001dd6a90000000000000000],

##  ["kingdom_1_lord_a", "Kingdom 1 Lord A", "Kingdom 1 Lord A", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_b", "Kingdom 1 Lord B", "Kingdom 1 Lord B", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_c", "Kingdom 1 Lord C", "Kingdom 1 Lord C", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_d", "Kingdom 1 Lord D", "Kingdom 1 Lord D", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_e", "Kingdom 1 Lord E", "Kingdom 1 Lord E", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_f", "Kingdom 1 Lord F", "Kingdom 1 Lord F", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_g", "Kingdom 1 Lord G", "Kingdom 1 Lord G", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_h", "Kingdom 1 Lord H", "Kingdom 1 Lord H", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_i", "Kingdom 1 Lord I", "Kingdom 1 Lord I", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_j", "Kingdom 1 Lord J", "Kingdom 1 Lord J", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_k", "Kingdom 1 Lord K", "Kingdom 1 Lord K", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_l", "Kingdom 1 Lord L", "Kingdom 1 Lord L", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_m", "Kingdom 1 Lord M", "Kingdom 1 Lord M", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_n", "Kingdom 1 Lord N", "Kingdom 1 Lord N", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],



#  ["town_1_ruler_a", "King Harlaus",  "King Harlaus",  tf_hero, scn_town_1_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010908101e36db44b75b6dd],
#  ["town_2_ruler_a", "Duke Taugard",  "Duke Taugard",  tf_hero, scn_town_2_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000310401e06db86375f6da],
#  ["town_3_ruler_a", "Count Grimar",  "Count Grimar",  tf_hero, scn_town_3_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004430301e46136eb75bc0a],
#  ["town_4_ruler_a", "Count Haxalye", "Count Haxalye", tf_hero, scn_town_4_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010918701e77136e905bc0e
#  ["town_5_ruler_a", "Count Belicha", "Count Belicha", tf_hero, scn_town_5_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000421c801e7713729c5b8ce],
#  ["town_6_ruler_a", "Count Nourbis", "Count Nourbis", tf_hero, scn_town_6_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c640501e371b72bcdb724],
#  ["town_7_ruler_a", "Count Rhudolg", "Count Rhudolg", tf_hero, scn_town_7_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c710201fa51b7286db721],
 
#  ["town_8_ruler_b", "King Yaroglek", "King_yaroglek", tf_hero, scn_town_8_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000128801f294ca6d66d555],
#  ["town_9_ruler_b", "Count Aolbrug", "Count_Aolbrug", tf_hero, scn_town_9_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004234401f26a271c8d38ea],
#  ["town_10_ruler_b","Count Rasevas", "Count_Rasevas", tf_hero, scn_town_10_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000001032c201f38e269372471c],
#  ["town_11_ruler_b","Count Leomir",  "Count_Leomir",  tf_hero, scn_town_11_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c538001f55148936d3895],
#  ["town_12_ruler_b","Count Haelbrad","Count_Haelbrad",tf_hero, scn_town_12_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000410c701f38598ac8aaaab],
#  ["town_13_ruler_b","Count Mira",    "Count_Mira",    tf_hero, scn_town_13_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004204401f390c515555594],
#  ["town_14_ruler_b","Count Camechaw","Count_Camechaw",tf_hero, scn_town_14_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

##  ["kingdom_2_lord_a", "Kingdom 2 Lord A", "Kingdom 2 Lord A", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_b", "Kingdom 2 Lord B", "Kingdom 2 Lord B", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_c", "Kingdom 2 Lord C", "Kingdom 2 Lord C", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_d", "Kingdom 2 Lord D", "Kingdom 2 Lord D", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_e", "Kingdom 2 Lord E", "Kingdom 2 Lord E", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_f", "Kingdom 2 Lord F", "Kingdom 2 Lord F", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_g", "Kingdom 2 Lord G", "Kingdom 2 Lord G", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_h", "Kingdom 2 Lord H", "Kingdom 2 Lord H", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_i", "Kingdom 2 Lord I", "Kingdom 2 Lord I", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_j", "Kingdom 2 Lord J", "Kingdom 2 Lord J", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_k", "Kingdom 2 Lord K", "Kingdom 2 Lord K", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_l", "Kingdom 2 Lord L", "Kingdom 2 Lord L", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_m", "Kingdom 2 Lord M", "Kingdom 2 Lord M", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_n", "Kingdom 2 Lord N", "Kingdom 2 Lord N", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],



#Royal family members

  ["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  #Swadian ladies - eight mothers, eight daughters, four sisters
  ["kingdom_1_lady_1","Lady Anna","Anna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [          itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_1_lady_2","Lady Nelda","Nelda",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001981050080000000000000f1100000000000000000000000000000000],
  ["knight_1_lady_3","Lady Bela","Bela",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["knight_1_lady_4","Lady Elina","Elina",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a70000060000000000000e3700000000000000000000000000000000],
  ["kingdom_l_lady_5","Lady Constanis","Constanis",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_6","Lady Vera","Vera",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_1_lady_7","Lady Auberina","Auberina",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_8","Lady Tibal","Tibal",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_1_lady_9","Lady Magar","Magar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_10","Lady Thedosa","Thedosa",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200f0000000000000edb00000000000000000000000000000000],
  ["kingdom_1_lady_11","Lady Melisar","Melisar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_12","Lady Irena","Irena",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f0450080000000000000f6b00000000000000000000000000000000],
  ["kingdom_l_lady_13","Lady Philenna","Philenna",tf_hero|tf_beautiful|tf_randomize_face|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_14","Lady Sonadel","Sonadel",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_1_lady_15","Lady Boadila","Boadila",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_1_lady_16","Lady Elys","Elys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_1_lady_17","Lady Johana","Johana",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_1_lady_18","Lady Bernatys","Bernatys",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_1_lady_19","Lady Enricata","Enricata",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_1_lady_20","Lady Gaeta","Gaeta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],
  
  #Vaegir ladies
  ["kingdom_2_lady_1","Lady Junitha","Junitha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_2","Lady Katia","Katia",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_3","Lady Seomis","Seomis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_4","Lady Drina","Drina",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_5","Lady Nesha","Nesha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_6","Lady Tabath","Tabath",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c20050000000000000f9300000000000000000000000000000000],
  ["kingdom_2_lady_7","Lady Pelaeka","Pelaeka",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_8","Lady Haris","Haris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_9","Lady Vayen","Vayen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_10","Lady Joaka","Joaka",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_11","Lady Tejina","Tejina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_12","Lady Olekseia","Olekseia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [      itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_2_lady_13","Lady Myntha","Myntha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_14","Lady Akilina","Akilina",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_15","Lady Sepana","Sepana",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_16","Lady Iarina","Iarina",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000850080000000000000f3500000000000000000000000000000000],
  ["kingdom_2_lady_17","Lady Sihavan","Sihavan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_2_lady_18","Lady Erenchina","Erenchina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_2_lady_19","Lady Tamar","Tamar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_2_lady_20","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],


  ["kingdom_3_lady_1","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_2","Lady Tuan","Tuan",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_3","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_4","Lady Ayasu","Ayasu",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c3003000000000000091c00000000000000000000000000000000],
  ["kingdom_3_lady_5","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_6","Lady Ruha","Ruha",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_7","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_8","Lady Kefra","Kefra",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_9","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_3_lady_10","Lady Dulua","Dulua",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002c08200d0000000000000f2e00000000000000000000000000000000],
  ["kingdom_3_lady_11","Lady Selik","Selik",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_3_lady_12","Lady Thalatha","Thalatha",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200d0000000000000f1c00000000000000000000000000000000],
  ["kingdom_3_lady_13","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_3_lady_14","Lady Nadha","Nadha",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_3_lady_15","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_3_lady_16","Lady Arjis","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_3_lady_17","Lady Atjahan", "Atjahan",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_3_lady_18","Lady Qutala","Qutala",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_3_lady_19","Lady Hindal","Hindal",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_3_lady_20","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  
  
  
  ["kingdom_4_lady_1","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_2","Lady Miar","Miar",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_4_lady_3","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_4","Lady Glunde","Glunde",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000080000000000000f8c00000000000000000000000000000000],
  ["kingdom_4_lady_5","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_6","Lady Bryn","Bryn",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000091000040000000000000f4a00000000000000000000000000000000],
  ["kingdom_4_lady_7","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_1","Lady Thera","Thera",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000000a0000000000000f9400000000000000000000000000000000],
  ["kingdom_4_lady_9","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_1","Lady Endegrid","Endegrid",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000610000c0000000000000f4b00000000000000000000000000000000],
  ["kingdom_4_lady_11","Lady Herjasa","Herjasa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2c_daughter","Lady Svipul","Svipul",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000101020030000000000000b6c00000000000000000000000000000000],
  ["knight_4_1b_wife","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_4_lady_14","Lady Kaeteli","Kaeteli",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1b_daughter","Lady Eilif","Eilif",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["knight_4_2b_daughter_2","Lady Gudrun","Gudrun",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_4_lady_17","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["knight_4_2c_wife_2","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["knight_4_1c_daughter","Lady Alfrun","Alfrun",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000400c000b69a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_4_lady_20","Lady Afrid","Afrid",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000400000010000000000000f9400000000000000000000000000000000],


  ["kingdom_5_lady_1","Lady Brina","Brina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_lady_2","Lady Aliena","Aliena",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_lady_3","Lady Aneth","Aneth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_4","Lady Reada","Reada",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_5_wife","Lady Saraten","Saraten",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_5_2b_wife_1","Lady Baotheia","Baotheia",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],
  ["kingdom_5_1c_daughter_1","Lady Eleandra","Eleandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_1","Lady Meraced","Meraced",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_1","Lady Adelisa","Adelisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_1","Lady Calantina","Calantina",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003008200e0000000000000ee300000000000000000000000000000000],
  ["kingdom_5_1c_daughter_2","Lady Forbesa","Forbesa",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_2c_daughter_2","Lady Claudora","Claudora",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a00000b0000000000000ff800000000000000000000000000000000],
  ["kingdom_5_1b_wife","Lady Anais","Anais",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2b_wife_2","Lady Miraeia","Miraeia",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_3","Lady Agasia","Agasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_16","Lady Geneiava","Geneiava",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_5_1c_wife_2","Lady Gwenael","Gwenael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_5_2c_wife_2","Lady Ysueth","Ysueth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_5_1c_daughter_4","Lady Ellian","Ellian",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000007900200d364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_5_lady_20","Lady Timethi","Timethi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000007a00000f4123dae69e8e48e200000000001e08db0000000000000000],
  
#Sarranid ladies
  ["kingdom_6_lady_1","Lady Rayma","Rayma",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,  itm_sarranid_head_cloth,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_6_lady_2","Lady Thanaikha","Thanaikha",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002808500b0000000000000e7d00000000000000000000000000000000],
  ["kingdom_6_lady_3","Lady Sulaha","Sulaha",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_6_lady_4","Lady Shatha","Shatha",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_6_lady_5","Lady Bawthan","Bawthan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_6","Lady Mahayl","Mahayl",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_6_lady_7","Lady Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_8","Lady Siyafan","Siyafan",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000110850100000000000000e4000000000000000000000000000000000],
  ["kingdom_6_lady_9","Lady Ifar","Ifar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_10","Lady Yasmin","Yasmin",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a0020030000000000000edb00000000000000000000000000000000],
  ["kingdom_6_lady_11","Lady Dula","Dula",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_12","Lady Ruwa","Ruwa",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_6_lady_13","Lady Luqa","Luqa",tf_hero|tf_randomize_face|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_14","Lady Zandina","Zandina",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_6_lady_15","Lady Lulya","Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_6_lady_16","Lady Zahara","Zahara",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b0850030000000000000f5a00000000000000000000000000000000],
  ["kingdom_6_lady_17","Lady Safiya","Safiya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_6_lady_18","Lady Khalisa","Khalisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_6_lady_19","Lady Janab","Janab",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_6_lady_20","Lady Sur","Sur",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

  ["kingdom_8_lady_1","Lady Dis","Dis",tf_hero|tf_beautiful|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000001000040000000000000ee600000000000000000000000000000000],
  ["kingdom_8_lady_2","Lady Rune","Rune",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000d400400025915aa226b4d975200000000001ea49e0000000000000000],


  
#  ["kingdom_11_lord_daughter","kingdom_11_lord_daughter","kingdom_11_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
#  ["kingdom_13_lord_daughter","kingdom_13_lord_daughter","kingdom_13_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
##  ["kingdom_1_lady_a","kingdom_1_lady_a","kingdom_1_lady_a",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
##  ["kingdom_1_lady_b","kingdom_1_lady_b","kingdom_1_lady_b",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
##  ["kingdom_2_lady_a","Kingdom 2 Lady a","Kingdom 2 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
##  ["kingdom_2_lady_b","Kingdom 2 Lady b","Kingdom 2 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
##  ["kingdom_3_lady_a","Kingdom 3 Lady a","Kingdom 3 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_3, [               itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
##
##  ["kingdom_3_lady_b","Kingdom 3 Lady b","Kingdom 3 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_3,  [                         itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
##  ["kingdom_4_lady_a","Kingdom 4 Lady a","Kingdom 4 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
##  ["kingdom_4_lady_b","Kingdom 4 Lady b","Kingdom 4 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,            itm_fighting_axe,       itm_leather_jerkin,         itm_leather_boots,          itm_straw_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_saddle_horse,       itm_arming_sword,       itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_nordic_sword,       itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_saddle_horse,       itm_falchion,           itm_light_leather,          itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_saddle_horse,       itm_sword,              itm_ragged_outfit,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_saddle_horse,      itm_scimitar,           itm_leather_jerkin,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_arming_sword,       itm_padded_leather,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_saddle_horse,      itm_nordic_sword,       itm_light_leather,          itm_leather_boots,          itm_woolen_hood],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_saddle_horse,      itm_sword,              itm_padded_leather,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_falchion,           itm_leather_jerkin,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_padded_leather,         itm_woolen_hose,            itm_fur_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_falchion,           itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_arming_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],

  
#Seneschals
  ["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_female, 0,reserved,  fac_neutral,[     itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_female, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_green_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_tunic,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_female, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[ itm_green_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_female, 0,reserved,  fac_neutral,[ itm_coarse_tunic,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_padded_cloth,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_green_tunic,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_female, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_female, 0,reserved,  fac_neutral,[ itm_padded_cloth,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_padded_cloth,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[ itm_red_tunic,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, man_face_older_2],

  ["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_female, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_female, 0,reserved,  fac_neutral,[itm_padded_cloth,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[itm_padded_cloth,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_female, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_female, 0,reserved,  fac_neutral,[itm_padded_cloth,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_female, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[itm_studded_leather_coat,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ragged_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_tabard,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_padded_cloth,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_nomad_vest,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face, 0,reserved,  fac_neutral,[itm_ragged_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_beautiful, 0,reserved,  fac_neutral,[itm_tabard,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],
  ["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant|tf_randomize_face|tf_female, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, man_face_middle_1, man_face_older_2],

#Arena Masters#seneschal end
  ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_nomad_armor,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_leather_jerkin,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_nomad_armor,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],



# Underground 

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_leather_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_apron,      itm_hide_boots          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[itm_red_gambeson,       itm_blue_hose           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_woolen_dress,       itm_woolen_hood         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##  
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_jacket,     itm_leather_boots       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_blue_dress,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[itm_blue_gambeson,     itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_woolen_dress,      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
  #arena_masters_end = zendar_armorer

  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,          itm_straw_hat       ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,        itm_hide_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_blue_hose       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_leather,       itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_beautiful|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_common_dress,         itm_sarranid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  
  ["zendar_armorer","Zendar_armorer","Zendar_armorer",tf_hero|tf_is_merchant, scn_zendar_center|entry(4),reserved,  fac_commoners,[itm_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000c7f10234548185fd52272c31b00000000001c35c60000000000000000],

# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,     itm_nomad_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,   itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_beautiful|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,     itm_wrapping_boots,itm_straw_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_blue,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  
  ["zendar_weaponsmith","Zendar_weaponsmith","Zendar_weaponsmith",tf_hero|tf_is_merchant, scn_zendar_center|entry(3),reserved,  fac_commoners,[itm_ragged_outfit,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fc0040452431d9163644f3b2200000000001dbaeb0000000000000000],

#Tavern keepers

  ["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_beautiful, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_leather_boots,      itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,      itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_beautiful, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_beautiful, scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_beautiful, scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_beautiful, scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_sarranid_dress_a,        itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe,       itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_sarranid_common_dress,        itm_sarranid_boots_a,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe_b,               itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  # ["town_23_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_23_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe_b,               itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["zendar_tavernkeeper","Zendar_tavernkeeper","Zendar_tavernkeeper",tf_hero|tf_female, scn_the_happy_boar|entry(1),reserved,  fac_commoners,[itm_red_dress,itm_blue_hose],def_attrib|level(5),wp(20),knows_common,0x00000001870800033b3231e3aa39b69100000000000e36990000000000000000],

#Goods Merchants

  ["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_nomad_armor,   itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_woolen_dress,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_sarranid_common_dress_b,  itm_sarranid_boots_a, itm_sarranid_felt_head_cloth_b  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_sarranid_dress_a,         itm_sarranid_boots_a,  itm_sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  
  ["zendar_merchant","Zendar_merchant","Zendar_merchant",tf_hero|tf_is_merchant|tf_beautiful, scn_zendar_merchant|entry(1),reserved,  fac_commoners,[itm_leather_jerkin,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,0x00000001bf0c000316526c9722922ad600000000001dc3040000000000000000],

  ["salt_mine_merchant","Barezan","Barezan",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_leather_apron, itm_leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6],

# Horse Merchants

  ["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_nomad_armor,          itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_dress,                itm_woolen_hose,    itm_woolen_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_woolen_hose],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_beautiful,  0, 0, fac_commoners,[itm_blue_dress,          itm_blue_hose,      itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_sarranid_boots_a],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe,      itm_sarranid_boots_a],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe_b,        itm_sarranid_boots_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_beautiful,  0, 0, fac_commoners,[itm_sarranid_common_dress_b,       itm_blue_hose,      itm_sarranid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  
  ["zendar_horse_merchant","Zendar_horse_merchant","Zendar_horse_merchant",tf_hero|tf_is_merchant, scn_zendar_center|entry(6),reserved,  fac_commoners,[itm_nomad_robe,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x00000001940c240e572466c32b8e354b00000000001dac610000000000000000],


#Town Mayors    #itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit
  ["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_gambeson,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_blue_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_fur_coat,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_rich_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_red_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_fur_coat,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,     itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,       itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,    itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_sarranid_boots_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_23_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_sarranid_boots_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],


#Village stores
  ["village_1_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_9_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_46_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_53_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_65_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_66_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_68_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_69_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_70_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_71_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_72_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_73_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_74_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_75_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_76_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_77_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_78_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_79_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_80_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_81_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_82_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_83_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_84_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_85_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_86_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_87_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_88_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_89_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_90_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_91_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_92_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_93_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_94_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_95_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_96_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_97_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_98_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_99_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_100_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_101_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_102_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_103_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_104_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_105_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_106_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_107_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_108_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_109_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_110_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
# Place extra merchants before this point
  ["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  #Used for player enterprises
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
  
# Chests
  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_salt,itm_lamellar_gauntlets,itm_kettle_hat],def_attrib|level(18),wp(60),knows_common, 0],
  #  [],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_arabian_armor_b,itm_splinted_greaves],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_boots,itm_arabian_sword_d],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_iron_staff,itm_vaegir_lamellar_helmet],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_4","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tab_shield_round_b,itm_lance],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_5","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_khergit_sword_two_handed_a,itm_sarranid_mail_coif],def_attrib|level(18),wp(60),knows_common, 0],

  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],  
  
# These are used as arrays in the scripts.
  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [itm_arrows,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_khergit_bow,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],


# Add Extra Quest NPCs below this point  
["store_target","{!}store_target","{!}store_target",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10|knows_looting_10,0],
["store_player","{!}store_player","{!}store_player",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10|knows_looting_10,0],
["player_chest","{!}player_chest","{!}player_chest",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_1|knows_looting_10,0],
["player_culture","{!}player_culture","{!}player_culture",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10|knows_looting_10,0],
["player_achievement","{!}player_achievement","{!}player_achievement",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10|knows_looting_10,0],
["player_magic","{!}player_magic","{!}player_magic",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10|knows_looting_10,0],

#manhunter contact start,end=alayen(needchange)
["manhunter_contact_1","manhunter_contact","manhunter_contact",tf_hero, 0, reserved,  fac_manhunters,
[itm_gauntlets,itm_teutonichelm_e,itm_surcoat_over_mail,itm_iron_greaves, itm_sword_medieval_d_long],
str_25|agi_8|int_7|cha_8|level(20),wp(100),knows_riding_1|knows_athletics_1|knows_power_strike_1,0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
["manhunter_contact_2","manhunter_contact","manhunter_contact",tf_hero, 0, reserved,  fac_manhunters,
[itm_gauntlets,itm_full_helm,itm_scale_armor,itm_iron_greaves, itm_long_axe_c],
str_25|agi_8|int_7|cha_8|level(20),wp(100),knows_riding_1|knows_athletics_1|knows_power_strike_1,0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
["manhunter_contact_3","manhunter_contact","manhunter_contact",tf_hero, 0, reserved,  fac_manhunters,
[itm_mail_mittens,itm_valsgarde_new,itm_cuir_bouilli,itm_mail_boots, itm_hafted_blade_b],
str_25|agi_8|int_7|cha_8|level(20),wp(100),knows_riding_1|knows_athletics_1|knows_power_strike_1,0x000000018b0001d3263ccbff161aecbf00000000001ec0380000000000000000],
["manhunter_contact_4","manhunter_contact","manhunter_contact",tf_hero, 0, reserved,  fac_manhunters,
[itm_lamellar_gauntlets,itm_mask_helmet1,itm_khergit_elite_armor,itm_khergit_leather_boots, itm_sword_khergit_4],
str_25|agi_8|int_7|cha_8|level(20),wp(100),knows_riding_1|knows_athletics_1|knows_power_strike_1,0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
["manhunter_contact_5","manhunter_contact","manhunter_contact",tf_hero, 0, reserved,  fac_manhunters,
[itm_lamellar_gauntlets,itm_dorn_immortal_helmet,itm_sarranid_elite_armor,itm_sarranid_boots_d, itm_sarranid_two_handed_mace_1],
str_25|agi_8|int_7|cha_8|level(20),wp(100),knows_riding_1|knows_athletics_1|knows_power_strike_1,0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],

# hero hero end=hareck
["wabbaer","Wabbaer","Wabbaer",tf_undead|tf_hero,0,0,fac_wabber,
[itm_ganquang_melee,itm_barbuta_b_2,itm_obsidianaxe,itm_sp_shr1,itm_ak_wlocznie_b,itm_twiligh_armor,itm_twilight_gloves,itm_twilight_boots,itm_ripper_chain], 
str_50 | agi_12 |level(45),wp(150),knows_athletics_1|knows_ironflesh_10|knows_power_strike_5|knows_riding_7|knows_shield_5,0x0000000180000000000000000000000000000000000000000000000000000000],
["onsved","onsved","onsved",tf_tall|tf_hero,0,0,fac_onsved,
[itm_bear_warrior_b,itm_horny_charger_plate,itm_valhelm_c,itm_black_greaves,itm_rhun_greataxe,itm_toumao,itm_rhun_greatsword], 
str_125 | agi_45 | int_12 | cha_12|level(60),wp(425),knows_athletics_10|knows_ironflesh_14|knows_power_strike_14|knows_riding_10|knows_shield_10|knows_power_throw_11,0x0000000b400c030923a357c76739baea00000000001edb320000000000000000],
["matheld","Matheld","Matheld",tf_female|tf_hero, 0, reserved,fac_ortlinde,
[itm_barf_helm,itm_woman,itm_mail_mittens,itm_mail_boots,itm_sword_viking_3,itm_heavy_throwing_axes,itm_tab_shield_round_e,itm_great_axe,itm_ak_wlocznie_a],
def_lord|level(50),wp(350),knows_ironflesh_9|knows_shield_10|knows_power_strike_10|knows_athletics_10|knows_power_throw_10,0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
["firentis","Firentis","Firentis",tf_hero, 0, reserved,  fac_spring_knight,
[itm_cloak_early_transitional_flower_magic,itm_steel_boots_01,itm_steel_gauntlets,itm_teutonichelm_flower,itm_wplatedcharger5,itm_caveirabastard_magic],
def_lord|level(48),wp(335),knows_athletics_9|knows_ironflesh_9|knows_power_strike_9|knows_riding_10,0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
["bunduk","Bunduk","Bunduk",tf_hero, 0, reserved,  fac_manhunters,
[itm_van_helsing_crossbow_01,itm_van_helsing_crossbow_bolt,itm_wisby_gauntlets_red,itm_early_transitional_white,itm_ganquang_pick,itm_steel_boots_01,itm_hounskull_bascinet_06,itm_tab_shield_pavise_d],
def_lord|level(49),wp(375),knows_athletics_9|knows_ironflesh_9|knows_power_strike_9,0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
["marcus","Marcus","Marcus",tf_hero, 0, reserved,  fac_gulfod_theocracy,
[itm_gothic_plate_black,itm_blackgauntlets,itm_sallet_b_closed1,itm_black_greaves,itm_wplatedcharger9,itm_pistol,itm_cartridges,itm_demon_sword,itm_steel_shield],
def_lord_1|level(50),wp(390),knows_athletics_10|knows_ironflesh_10|knows_power_strike_10|knows_riding_10|knows_horse_archery_9,0x00000009c000400513f276ab152e64e400000000001c94b00000000000000000],
["jerome","Jerome","Jerome",tf_hero, 0, reserved,  fac_outlaws,
[itm_throwing_spears,itm_platemail_harness_05,itm_tournament_helmb,itm_charger_plate_1,itm_newnarsil,itm_steel_boots_01,itm_steel_mittens,itm_steel_shield_heater,itm_ak_wlocznie_b],
def_lord_1|level(50),wp(350),knows_athletics_10|knows_ironflesh_10|knows_power_strike_10|knows_riding_10,0x000000039700439108a32472012da32100000000001d24c40000000000000000],
["ulf","Ulf","Ulf",tf_hero, 0, reserved,  fac_outlaws,
[itm_bear_warrior,itm_2kettle_hat_new,itm_beargauntlets,itm_iron_greaves,itm_doubleaxe_of,itm_throwing_spears,itm_throwing_spears,itm_heavy_throwing_axes],
def_lord|level(45),wp(350),knows_athletics_8|knows_ironflesh_8|knows_power_strike_8|knows_riding_8|knows_power_throw_8,0x000000018b0001d3263ccbff161aecbf00000000001ec0380000000000000000],
["giscard","Giscard","Giscard",tf_hero, 0, reserved,  fac_turumia,
[itm_heraldic_platemail_02,itm_hounskull_bascinet_06,itm_steel_shield_heater,itm_steel_boots_01,itm_steel_mittens,itm_black_lance_banner,itm_hope,itm_plate_charger_white],
def_lord_2|level(55),wp(380),knows_athletics_9|knows_ironflesh_10|knows_power_strike_9|knows_riding_9|knows_power_throw_8,0x0000000fc0010452481bb6c24b52568500000000001e9c650000000000000000],
["zandana","Zandana","Zandana",tf_hero|tf_beautiful, 0, reserved,  fac_ciambia,
[itm_armor_23_green_1,itm_steel_boots_01,itm_dorn_spearbearer_guant,itm_dorn_knight_helmet_black_a,itm_bow4_arr_spak,itm_lonely,itm_pa_sword_02,itm_dec_steel_shield,itm_exp_charger_w],
def_lord|level(45),wp(300),knows_athletics_10|knows_ironflesh_10|knows_power_strike_10|knows_riding_10|knows_power_draw_10|knows_horse_archery_9,0x00000001c010500b0000000000000e8b00000000000000000000000000000000],
["world_destoryer","Anruilonger","World Destoryer",tf_tall|tf_hero,0,0,fac_son_of_starka,
[itm_barbar_armor,itm_barbar_boots,itm_barbar_helm,itm_barbar_hand,itm_barbar_axe], 
str_155 | agi_125 | int_25 | cha_25|level(100),wp(555),knows_athletics_12|knows_ironflesh_15|knows_power_strike_15|knows_shield_12|knows_power_throw_11,0x00000006540002873f86a62a9cd5d36d00000000001db6a50000000000000000],
["female_adventurer_dis","Cristina","Cristina",tf_beautiful|tf_hero,0,0,fac_shameless_adventurer,
[itm_joan_black,itm_brienne_spurs_black,itm_sorrow,itm_dorn_spearbearer_guant,itm_platedw,itm_sub_shield_01,itm_tournament_helmb_black,itm_bow4_arr_spak,itm_rivendellbow], 
def_lord|level(50),wp(315),knows_athletics_9|knows_ironflesh_10|knows_power_strike_10|knows_shield_10|knows_power_throw_10|knows_power_draw_9|knows_riding_11|knows_horse_archery_6,0x00000001e71020100000000000000f4800000000000000000000000000000000],
["judge_the_highest","Carlos","Carlos",tf_hero,0,0,fac_witch_finder,
[itm_wp_armor,itm_molot_cherep_kluv,itm_plate_boots,itm_holy_holo,itm_gauntlets,itm_pa_sword_03_shield], 
str_50 | agi_45 | int_25 | cha_25|level(75),wp(400),knows_athletics_10|knows_ironflesh_13|knows_power_strike_13|knows_shield_10,0x0000000fe111100021c5aef4eb52c6d500000000001dc4d90000000000000000],
["occis","occis","occis",tf_demon|tf_hero,0,0,fac_roskel,
[itm_blackdemonheart,itm_ganquang_melee,itm_twilight_gloves,itm_twilight_boots,itm_dark_charger_c,itm_dark_lord_armor,itm_sub_shield_01,itm_charonscall,itm_demon_protection],
str_150 | agi_50|level(90),wp(450),knows_ironflesh_15|knows_power_strike_15|knows_riding_12|knows_athletics_12|knows_shield_12|knows_power_throw_12|knows_horse_archery_9,0x0000000000000007000000000000000000000000000000000000000000000000],
["propheta","propheta","propheta",tf_hero,0,0,fac_ymira,
[itm_wei_xiadi_sarranid_mamluk_armor,itm_dorn_knight_boots_gold,itm_dorn_guardsun_helmet,itm_lamellar_gauntlets,],
def_lord_2|level(60),wp(380),knows_ironflesh_12|knows_power_strike_12|knows_riding_12|knows_athletics_12|knows_shield_12|knows_power_throw_12|knows_horse_archery_9,0x0000000b8010a288712a924f29da4aad00000000001f9cfc0000000000000000],
["singleeye","singleeye","singleeye",tf_hero,0,0,fac_outlaws,
[itm_wei_xiadi_samurai_armor02,itm_mongol_helmet_xf,itm_black_greaves,itm_lamellar_gauntlets,],
def_lord_1|level(55),wp(350),knows_ironflesh_10|knows_power_strike_10|knows_riding_12|knows_athletics_12|knows_shield_12|knows_power_draw_10|knows_horse_archery_9,0x0000000b8010f38b525f7d372b6926dd00000000001e62fd0000000000000000],

#can hire from him
["constable_hareck","Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_leather_jacket,itm_leather_boots],def_attrib|level(5),wp(20),knows_common,0x00000001830c25844921a156dc48eb6b00000000000646920000000000000000],
["simon","Simon Forest Patrol leader","Simon",tf_hero,0,reserved,  fac_commoners,[itm_fighting_pick,itm_bastard_sword_b,itm_bodkin_arrows,itm_arrows,itm_long_bow,itm_brigandine_red,itm_bascinet_2,itm_splinted_leather_greaves,itm_leather_gloves],def_guard|level(25),wp(150),knows_power_draw_7,0x000000019f0800462f6409ecee92351b00000000001de1760000000000000000],

#Mercenary intermediary
["alayaya","Alayaya", "Mercenary intermediary",tf_hero|tf_beautiful, 0,0, fac_commoners,[itm_scimitar,itm_mamluke_mail, itm_sarranid_boots_d],def_knight|level(20),wp(100),knows_inventory_management_10,0x000000019e0850030000000000000e1700000000000000000000000000000000],
["malthar","Malthar", "Mercenary intermediary",tf_hero, 0,0, fac_commoners,[itm_scimitar,itm_lamellar_vest_khergit, itm_khergit_leather_boots],def_knight|level(20),wp(100),knows_inventory_management_10,0x00000009ff0c708852f04d16a454aae500000000001f147f0000000000000000],
["nymella","Nymella", "Mercenary intermediary",tf_hero|tf_beautiful, 0,0, fac_commoners,[itm_sword_of_war,itm_surcoat_over_mail, itm_splinted_greaves],def_knight|level(20),wp(100),knows_inventory_management_10,0x00000002400800060000000000000ee800000000000000000000000000000000],
["arys","Arys", "Mercenary intermediary",tf_hero, 0,0, fac_commoners,[itm_fighting_axe,itm_mail_long_surcoat_new_c3, itm_splinted_greaves],def_knight|level(20),wp(100),knows_inventory_management_10,0x000000019e0445942b94d2d51369477300000000001daaa40000000000000000],
["illifer","Illifer", "Mercenary intermediary",tf_hero, 0,0, fac_commoners|tf_tall,[itm_sword_medieval_d_long,itm_heraldic_mail_with_surcoat, itm_splinted_greaves],def_knight|level(20),wp(100),knows_inventory_management_10,0x00000001a50011117bffb385ffffffff00000000001e99670000000000000000],
["regis","Regis", "Mercenary intermediary",tf_hero, 0,0, fac_commoners,[itm_heraldic_platemail_02,itm_mackie_bastard, itm_lamellar_gauntlets,itm_splinted_greaves],def_knight_1|level(20),wp(100),knows_inventory_management_10,0x0000000d00080307452652845c96569900000000001ed4aa0000000000000000],

["deliver","Deliver","Deliver",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,#Mercenary intermediary End
   [itm_short_tunic, itm_linen_tunic,itm_fur_coat, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_arena_tunic_white, itm_leather_apron, itm_shirt, itm_arena_tunic_green, itm_arena_tunic_blue, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_guard|level(24),wp(160),knows_common,man_face_young_1, man_face_old_2],
["alexis","Count Alexis", "Alexis",tf_hero, 0,0, fac_kingdom_8,[itm_tab_shield_kite_cav_b,itm_guard_helmet,itm_sword_medieval_d_long,itm_heraldic_mail_with_tabard,itm_mail_boots,itm_gauntlets,itm_warhorse_steppe],
  knight_attrib_4,wp(230),knight_skills_4,0x000000061e1032442d1d6c152455c86300000000001e45190000000000000000],
# quest npc
#family
["father","father","father", tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_short_tunic, itm_linen_tunic,itm_fur_coat, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_arena_tunic_white, itm_leather_apron, itm_shirt, itm_arena_tunic_green, itm_arena_tunic_blue, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_farmer|level(5),wp(60),knows_athletics_3|knows_shield_2|knows_ironflesh_3,0x0000000e8000000136db6db6db6db6db00000000001db6db0000000000000000,0x0000000e8000700136db6db6db6db6db00000000001db6db0000000000000000],
["mother","mother","mother", tf_guarantee_boots|tf_guarantee_armor|tf_female,0,0,fac_commoners,
   [itm_knife,itm_hatchet,itm_club,itm_dress,itm_short_tunic, itm_linen_tunic,itm_fur_coat,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_farmer|level(5),wp(60),knows_athletics_3|knows_shield_2|knows_ironflesh_3,0x0000000ec104000f64d66a15216525a300000000001c66d40000000000000000,0x0000000ec104400f64d66a15216525a300000000001c66d40000000000000000],

["brother","brother", "brother",tf_hero, 0,0, fac_commoners,[itm_scimitar,itm_padded_cloth, itm_leather_boots],def_attrib|level(1),wp(30),knows_common,0x000000001204200137088db4e656aa6500000000001e99b30000000000000000],
["sister","sister", "sister",tf_hero|tf_beautiful, 0,0, fac_commoners,[itm_scimitar,itm_padded_cloth, itm_leather_boots],def_attrib|level(1),wp(30),knows_common,0x000000003f04000d0000000000000fc000000000000000000000000000000000],

["villager","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_farmer|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
["villager_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_farmer|level(4),wp(40),knows_common,refugee_face1,refugee_face2],

#scene2
["aerys","Aerys", "Aerys",tf_hero, 0,0, fac_commoners,[itm_rhun_greatsword,itm_bear_warrior,itm_beargauntlets,itm_bear_boots,itm_mongol_helmet_xb,itm_copy_bear],
knight_attrib_3,wp(200),knight_skills_3,0x00000000000400876cdcad3b98cb14da00000000001d48e30000000000000000],
["tallad","Tallad", "Tallad",tf_hero, 0,0, fac_commoners,[itm_wolf_helm1,itm_great_axe,itm_northmen_med_a1_pelt,itm_stark_hanter_boots,itm_beargauntlets,itm_hunter],
knight_attrib_4,wp(225),knight_skills_4,0x00000008001003524d2caf02f8b1472400000000001ec45d0000000000000000],
["elaena","Elaena", "Elaena",tf_hero|tf_beautiful, 0,0, fac_commoners,[itm_rhun_greatfalchion,itm_northmen_med_a3_cloak,itm_stark_hanter_boots,itm_beargauntlets,itm_mongol_helmet_xa1,itm_steppe_horse],
knight_attrib_4,wp(200),knight_skills_3,0x00000000001000100000000000000f7100000000000000000000000000000000],
#sea raider leader
["baldersvold","Baldersvold", "Baldersvold",tf_hero, 0,0, fac_commoners,[itm_rhodok_cuir_bouilli,itm_nordic_warlord_helmet,itm_mail_mittens,itm_mail_boots,itm_long_axe_c,itm_sword_viking_3,itm_tab_shield_round_e,itm_northerner_horse_hunter,itm_heavy_throwing_axes],
str_35|agi_35|int_35|cha_35|level(40),wp(255),knows_ironflesh_8|knows_power_strike_8|knows_athletics_8|knows_riding_8|knows_power_throw_8|knows_shield_8,0x0000000b00080280474ab33b3157cc2400000000001ecb8c0000000000000000],
#spring temple
["old_knight_gideon","Gideon","Gideon",tf_hero,0,0,fac_spring_knight,
   [itm_cloak_early_transitional_flower_magic,itm_steel_boots_01,itm_steel_gauntlets,itm_wplatedcharger5,itm_caveirabastard],
   def_knight_2|level(55),wp(350),knows_ironflesh_10|knows_power_strike_9|knows_riding_10|knows_athletics_10,0x0000000fc01013525b1456436c4da76e00000000001de6d40000000000000000],
#special npc start(for player)
["mikhail", "Mikhail Blackarrow", "Mikhail Blackarrow",tf_hero,0,reserved,fac_caprine,[itm_wolf_helm3,itm_elite_cavalary,itm_black_greaves,itm_beargauntlets,itm_rangerbow2,itm_bow3_arr_spak_1,itm_ak_miecz_mis,itm_bow3_arr_spak_1],
str_50|agi_50|int_45|cha_45|level(70),wp(380),knows_ironflesh_10|knows_power_strike_10|knows_athletics_10|knows_power_draw_12, 0x0000000c0f04324a2509d5d53944c6a300000000001d5b320000000000000000, vaegir_face_old_2],
["order_knight", "order_knight", "order_knight",tf_hero,0,reserved,fac_seven_god,[itm_dark_lord_armor2_g,itm_twilight_gloves_g,itm_twilighthelm_s_g,itm_twilight_boots_g],
str_75|agi_55|int_35|cha_35|level(75),wp(400),knows_ironflesh_14|knows_power_strike_12|knows_athletics_10|knows_riding_12|knows_shield_10, 0x0000000fc001119447738e24a299476300000000001eb51b0000000000000000],
["death_knight", "death_knight", "death_knight",tf_hero|tf_skeleton,0,reserved,fac_neutral,[itm_pickaxe_hand,itm_pickaxe_hand_sheild,itm_death_k,itm_twiligh_armor,itm_twilight_gloves,itm_twilight_boots,itm_demon_hood,itm_ganquang_melee,itm_ganquang_melee],
str_85|agi_85|int_45|cha_35|level(80),wp(475),knows_ironflesh_11|knows_power_strike_11|knows_athletics_11|knows_riding_12|knows_shield_11|knows_power_throw_12|knows_horse_archery_7,0x0000000800000000000000000000000000000000000000000000000000000000],
["hunger_knight", "hunger_knight", "hunger_knight",tf_hero|tf_giant,0,reserved,fac_neutral,[itm_hunger_k,itm_czarne_gauntlets,itm_spak_coat_of_plates_b,itm_czarne_platebut,itm_helm_b_crusher_b_02,itm_spak_iceaxe],
str_125|agi_50|int_55|cha_55|level(80),wp(400),knows_ironflesh_15|knows_power_strike_10|knows_athletics_6|knows_riding_8|knows_shield_10,0x0000000800000000000000000000000000000000000000000000000000000000],
["conquer_knight", "conquer_knight", "conquer_knight",tf_hero,0,reserved,fac_neutral,[itm_bb_war_bow,itm_bow3_arr_spak_1,itm_conquer_k,itm_spak_black_armor,itm_spak_black_boots,itm_spak_black_gauntlets,itm_crown_coif,itm_linhir_eket,itm_linhir_eket_sheild],
str_60|agi_60|int_40|cha_40|level(80),wp(430),knows_ironflesh_10|knows_power_strike_12|knows_athletics_10|knows_riding_12|knows_shield_10|knows_power_draw_12|knows_horse_archery_8,0x0000000fff0462877187fe492649225b00000000001f89380000000000000000],
["war_knight", "war_knight", "war_knight",tf_hero|tf_beautiful,0,reserved,fac_neutral,
[itm_war_k,itm_female_plate_boots_falcon,itm_female_plate_falcon,itm_female_plate_falcon_fist,itm_female_plate_falcon_hood,itm_ganquang_sword,itm_ganquang_sword_two_handed,itm_spikeshield_01,itm_gondor_tower_spear],
str_100|agi_55|int_25|cha_25|level(80),wp(425),knows_ironflesh_11|knows_power_strike_14|knows_athletics_10|knows_riding_9|knows_shield_10,0x00000008220c50080000000000000ec200000000000000000000000000000000],

#another special npc(for npc)
["vags","Vags","Vags",tf_hero|tf_tall,0,0,fac_son_of_starka,[itm_mail_boots,itm_barbar_body,itm_bear_warior_helm,itm_pa_axe_02],
str_75 | agi_55 | int_10 | cha_10|level(65),wp(400),knows_ironflesh_12|knows_power_strike_12|knows_athletics_12,0x00000007c010034b7e6c96c9638dc9a400000000001ec8f80000000000000000],
["feignes","Feignes","Feignes",tf_hero|tf_succubus,0,0,fac_ymira,[itm_xena_armor,itm_demon_horn_mod7,itm_twilight_gloves],
str_35 | agi_35 | int_35 | cha_35|level(55),wp(330),knows_ironflesh_6|knows_power_strike_6|knows_athletics_12|knows_reserved_6_12|knows_reserved_5_12,0x000000083f0c50050000000000000e0400000000000000000000000000000000],
["agnete","Agnete","Agnete",tf_hero|tf_succubus,0,0,fac_ymira,[itm_xena_armor,itm_demon_horn_mod7,itm_twilight_gloves],
str_35 | agi_35 | int_35 | cha_35|level(55),wp(330),knows_ironflesh_6|knows_power_strike_6|knows_athletics_12|knows_reserved_6_12|knows_reserved_5_12,0x000000082d0c500b0000000000000e0400000000000000000000000000000000],
["alfred","Alfred","Alfred",tf_hero|tf_tall,0,0,fac_turumia,[itm_heraldic_platemail_02,itm_steel_mittens,itm_steel_boots_01,itm_hounskull_bascinet_06,itm_charger,itm_lightedge_spak_black],
def_lord_1|level(50),wp(365),knows_ironflesh_10|knows_power_strike_10|knows_athletics_10|knows_riding_10,0x0000000cc0011140692574e8f48d6c8400000000001ccb5b0000000000000000],
["founds","Founds","Founds",tf_hero, 0, reserved,  fac_spring_knight,
[itm_early_transitional_banner,itm_steel_boots_01,itm_steel_gauntlets,itm_great_helmet_newflower,itm_wplatedcharger5,itm_caveirabastard,itm_bow3_spak,itm_new1,itm_new1],
def_knight_1|level(40),wp(275),knows_athletics_8|knows_ironflesh_8|knows_power_strike_8|knows_riding_8|knows_power_draw_8|knows_horse_archery_8,0x000000003f1001412a9425cb2576b9d300000000001d459d0000000000000000],
["coster","Coster","Coster",tf_hero, 0, reserved,  fac_gulfod_theocracy,
[itm_marmont_armor,itm_blackgauntlets,itm_sallet_b_closed1,itm_black_greaves,itm_wplatedcharger9,itm_spak_bow8,itm_fire_arrows,itm_steel_shield,itm_pa_maul_02],
def_knight_1|level(40),wp(300),knows_athletics_7|knows_ironflesh_8|knows_power_strike_8|knows_riding_8|knows_power_draw_7|knows_horse_archery_9,0x00000007070c419170a58dc4b951a49700000000001c95280000000000000000],
["eimyria","Eimyria","Eimyria",tf_beautiful|tf_hero, 0, reserved,fac_ortlinde,
[itm_barf_helm,itm_wei_xiadi_nord_cuir_bouilli,itm_mail_mittens,itm_mail_boots,itm_heavy_throwing_axes,itm_heavy_throwing_axes,itm_toumao,itm_flamberge],
def_knight_1|level(40),wp(285),knows_ironflesh_7|knows_power_strike_9|knows_athletics_8|knows_power_throw_10,0x00000000800000010000000000000f1100000000000000000000000000000000],
# ["eimyria","Eimyria","Eimyria",tf_beautiful|tf_hero, 0, reserved,fac_ortlinde,
# [itm_barf_helm,itm_wei_xiadi_nord_cuir_bouilli,itm_mail_mittens,itm_mail_boots,itm_heavy_throwing_axes,itm_heavy_throwing_axes,itm_toumao,itm_flamberge],
# def_knight_1|level(40),wp(285),knows_ironflesh_7|knows_power_strike_9|knows_athletics_8|knows_power_throw_10,0x00000000800000010000000000000f1100000000000000000000000000000000],
["moss","Moss","Moss",tf_hero|tf_tall, 0, reserved,  fac_ciambia,
[itm_armor_22,itm_rus_splint_greaves,itm_dorn_knight_helmet_black_a,itm_dec_steel_shield,itm_exp_warhorse_w,itm_luc_throwing_hammer,itm_luc_celtic_sword],
def_champion|level(30),wp(200),knows_athletics_6|knows_ironflesh_6|knows_power_strike_6|knows_riding_6|knows_power_throw_6|knows_horse_archery_4,0x00000000000ca01447d379493a71259300000000001d38ea0000000000000000],
["seth","Seth","Seth",tf_hero,0,0,fac_gulfod_theocracy,
   [itm_gothic_plate_silver,itm_pa_sword_03_shield,itm_dorn_knight_boots,itm_dorn_knight_gant,itm_holy_holo,itm_pa_maul_02,itm_plate_charger_white],
   def_lord_2|level(55),wp(360),knows_ironflesh_12|knows_shield_11|knows_power_strike_10|knows_athletics_10|knows_riding_10,0x0000000ca410414062d97211a69946aa00000000001ec4d00000000000000000],

#helpful npc(for npc)(guide/doctor/trainer/trader)
#guide
["random_npc_1_1","random_npc_1","random_npc_1",tf_hero,0,0,fac_commoners,
[itm_rhodok_honorguard_armor,itm_splinted_leather_greaves,itm_leather_gloves,itm_combed_morion,itm_sp_pikee],
str_21 | agi_25 | int_10 | cha_10|level(25),wp(140),knows_power_strike_5|knows_ironflesh_5|knows_athletics_5,bandit_face1, bandit_face2],
["random_npc_1_2","random_npc_1","random_npc_1",tf_hero,0,0,fac_commoners,
[itm_wei_xiadi_sarranid_mamluk_armor,itm_sarranid_boots_b,itm_vaeg_helmet8,itm_double_sword],
str_21 | agi_24 | int_10 | cha_10|level(25),wp(150),knows_power_strike_5|knows_ironflesh_5|knows_athletics_5,bandit_face1, bandit_face2],
#doctor
["random_npc_2_1","random_npc_1","random_npc_1",tf_hero,0,0,fac_commoners,
[itm_kettlehatfacebyrnie,itm_copy_armor_14,itm_rus_cav_boots,itm_luc_english_polehammer,itm_luc_throwing_hammer,itm_luc_throwing_hammer],
str_25 | agi_22 | int_18 | cha_10|level(30),wp(166),knows_power_strike_6|knows_ironflesh_6|knows_athletics_5|knows_power_throw_7,bandit_face1, bandit_face2],
#trainer
["random_npc_3_1","random_npc_1","random_npc_1",tf_hero,0,0,fac_commoners,
[itm_rhodok_knight_armor,itm_rus_splint_greaves,itm_lamellar_gauntlets,itm_pigface_klappvisor_open,itm_flamberge,itm_bb_arming_sword_long,itm_tab_shield_pavise_c],
str_27 | agi_27 | int_18 | cha_10|level(35),wp(200),knows_power_strike_7|knows_ironflesh_7|knows_athletics_7|knows_shield_5,bandit_face1, bandit_face2],
#trader
["random_npc_4_1","random_npc_1","random_npc_1",tf_hero,0,0,fac_commoners,
[itm_rhodok_padded_jack,itm_splinted_leather_greaves,itm_leather_gloves,itm_helmet_with_neckguard,itm_steel_bolts,itm_sniper_crossbow,itm_long_axe_b],
str_22 | agi_23 | int_10 | cha_15|level(27),wp(155),knows_power_strike_5|knows_ironflesh_5|knows_athletics_5,bandit_face1, bandit_face2],
# enemy 
# demon heresy
["garth","garth", "dark lord",tf_hero, 0,0, fac_commoners,[itm_sword_medieval_d_long,itm_heraldic_mail_with_surcoat, itm_splinted_greaves],
str_40|agi_40|int_35|cha_35|level(60),wp(300),knows_ironflesh_10|knows_power_strike_10|knows_power_throw_10|knows_athletics_10|knows_shield_10|knows_riding_10,0x0000000aff10049121238eb69e09b72f00000000001e14600000000000000000],
["lilith","beautiful lilith", "dark",tf_hero|tf_beautiful, 0,0, fac_commoners,[itm_sword_medieval_d_long,itm_heraldic_mail_with_surcoat, itm_splinted_greaves],
knight_attrib_4,wp(230),knight_skills_4,0x0000000aff10000a0000000000000f2f00000000000000000000000000000000],
["alester","old alester", "dark",tf_hero, 0,0, fac_commoners,[itm_sword_medieval_d_long,itm_heraldic_mail_with_surcoat, itm_splinted_greaves],
knight_attrib_5,wp(240),knight_skills_5,0x0000000fe40c400017db6f4f2133078600000000001d6a400000000000000000],
["zamin","old zamin", "dark",tf_hero|tf_female, 0,0, fac_commoners,[itm_sword_medieval_d_long,itm_heraldic_mail_with_surcoat, itm_splinted_greaves],
knight_attrib_5,wp(250),knight_skills_4,0x0000000fda0c100b77db8194e31fefff00000000001fec790000000000000000],
#Necromancer
["alendi","alendi", "ArchMage",tf_hero, 0,0, fac_necromancer,[itm_sword_medieval_d_long,itm_heraldic_mail_with_surcoat, itm_splinted_greaves],def_attrib|level(60),wp(300),knows_inventory_management_10,0x00000000240c200406e46c2506d1a69300000000001db8c00000000000000000],

["emperor_anor","King Vorian", "Vorian",tf_hero, 0,0, fac_kingdom_8,
   [itm_noblemanshirt,itm_rus_cav_boots_black,itm_elf_spear_2,itm_lorien_kite,itm_rivendellrewardarmour,itm_rivendellswordfighterhelmet,itm_leather_gauntlets_new,itm_pa_sword_02],
   knight_attrib_5,wp(300),knight_skills_5,0x0000000d00091111415292d55cb5a6ec00000000001db6790000000000000000],
#assassin leader
["masked_man","Masked man", "Masked man",tf_hero, 0,0, fac_commoners,
   [itm_blackleather_gloves,itm_blackleather_boots_a,itm_assassin_armor,itm_assassin_helmet,itm_assassin_helmet2,itm_luc_celtic_sword,itm_steel_shield,itm_ganquang_dart,itm_ganquang_dart],
   def_knight_1|level(38),wp(275),knows_ironflesh_7|knows_power_strike_10|knows_power_throw_9|knows_athletics_10|knows_shield_7,0x000000083f005005272c49c85a99e96d00000000001d36920000000000000000],
["varin","Varin", "Varin",tf_hero, 0,0, fac_commoners,
   [itm_blackleather_gloves,itm_blackleather_boots_a,itm_assassin_armor,itm_assassin_helmet,itm_assassin_helmet2,itm_luc_celtic_sword,itm_steel_shield,itm_ganquang_dart,itm_ganquang_dart],
   def_knight_1|level(38),wp(275),knows_ironflesh_7|knows_power_strike_10|knows_power_throw_9|knows_athletics_10|knows_shield_7,0x000000083f005005272c49c85a99e96d00000000001d36920000000000000000],
#new
["vorian_singer","Vorian the Singer", "Vorian",tf_hero, 0,0, fac_commoners,
   [itm_noblemanshirt,itm_rus_cav_boots,itm_lyre,itm_bastard_sword_b],
   knight_attrib_5,wp(275),knight_skills_5,0x0000000180091008175272d55cb5a6ec00000000001e361d0000000000000000],

#randomhero_start#askr hero
["askr_random_hero_1", "random_hero_1", "{!}random_hero_1", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_askr,
[], 
def_lord_2|level(50),wp(280),knight_skills_4, nord_face_younger_1, nord_face_older_2],
["askr_random_hero_2", "random_hero_2", "{!}random_hero_2", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_askr,
[], 
knight_attrib_4|level(43),wp(350),knight_skills_4, nord_face_younger_1, nord_face_older_2],
["askr_random_hero_3", "random_hero_3", "{!}random_hero_3", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_askr,
[], 
knight_attrib_4|level(42),wp(250),knight_skills_5, nord_face_younger_1, nord_face_older_2],
["askr_random_hero_4", "random_hero_4", "{!}random_hero_4", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_askr,
[], 
lord_attrib|level(50),wp(250),knight_skills_4, nord_face_younger_1, nord_face_older_2],
["askr_random_hero_5", "random_hero_5", "{!}random_hero_5", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_askr,
[], 
knight_attrib_5|level(40),wp(250),knight_skills_5, nord_face_younger_1, nord_face_older_2],
["askr_random_hero_6", "random_hero_6", "{!}random_hero_6", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_askr,
[], 
knight_attrib_4|level(45),wp(255),knight_skills_4, nord_face_younger_1, nord_face_older_2],
["askr_random_hero_7", "random_hero_7", "{!}random_hero_7", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_askr,
[], 
lord_attrib|level(54),wp(280),knight_skills_5, nord_face_younger_1, nord_face_older_2],
["askr_random_hero_8", "random_hero_8", "{!}random_hero_8", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_askr,
[], 
knight_attrib_5|level(40),wp(270),knight_skills_4, nord_face_younger_1, nord_face_older_2],
["askr_random_hero_9", "random_hero_9", "{!}random_hero_9", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_askr,
[], 
def_lord_2|level(40),wp(280),knight_skills_5, nord_face_younger_1, nord_face_older_2],
["askr_random_hero_10", "random_hero_10", "{!}random_hero_10", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_askr,
[], 
knight_attrib_5|level(40),wp(250),knight_skills_4, nord_face_younger_1, nord_face_older_2],
#dark hero
["dark_random_hero_1", "random_hero_1", "{!}random_hero_1", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_destroyer,
[], 
def_lord_1|level(40),wp(300),knight_skills_5, man_face_middle_1, mercenary_face_2],
["dark_random_hero_2", "random_hero_2", "{!}random_hero_2", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_destroyer,
[], 
def_lord_2|level(60),wp(350),knight_skills_4, man_face_middle_1, mercenary_face_2],
["dark_random_hero_3", "random_hero_3", "{!}random_hero_3", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_destroyer,
[], 
def_lord|level(40),wp(250),knight_skills_5, man_face_middle_1, mercenary_face_2],
["dark_random_hero_4", "random_hero_4", "{!}random_hero_4", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_destroyer,
[], 
def_lord_1|level(40),wp(250),knight_skills_4, man_face_middle_1, mercenary_face_2],
["dark_random_hero_5", "random_hero_5", "{!}random_hero_5", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_destroyer,
[], 
def_lord|level(40),wp(250),knight_skills_3, man_face_middle_1, mercenary_face_2],
["dark_random_hero_6", "random_hero_6", "{!}random_hero_6", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_destroyer,
[], 
def_lord_1|level(40),wp(250),knight_skills_4, man_face_middle_1, mercenary_face_2],
["dark_random_hero_7", "random_hero_7", "{!}random_hero_7", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_destroyer,
[], 
def_lord|level(44),wp(250),knight_skills_5, man_face_middle_1, mercenary_face_2],
["dark_random_hero_8", "random_hero_8", "{!}random_hero_8", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_destroyer,
[], 
def_lord_1|level(45),wp(250),knight_skills_4, man_face_middle_1, mercenary_face_2],
["dark_random_hero_9", "random_hero_9", "{!}random_hero_9", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_destroyer,
[], 
def_lord_1|level(40),wp(250),knight_skills_5, man_face_middle_1, mercenary_face_2],
["dark_random_hero_10", "random_hero_10", "{!}random_hero_10", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_destroyer,
[], 
knight_attrib_5|level(40),wp(250),knight_skills_4, man_face_middle_1, mercenary_face_2],
#robber_knight
["robber_random_hero_1", "random_hero_1", "{!}random_hero_1", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_outlaws,
[], 
def_lord_2|level(60),wp(380),knight_skills_5, man_face_middle_1, mercenary_face_2],
["robber_random_hero_2", "random_hero_2", "{!}random_hero_2", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_outlaws,
[], 
knight_attrib_4|level(40),wp(250),knight_skills_3, man_face_middle_1, mercenary_face_2],
["robber_random_hero_3", "random_hero_3", "{!}random_hero_3", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_outlaws,
[], 
knight_attrib_3|level(35),wp(250),knight_skills_4, man_face_middle_1, mercenary_face_2],
["robber_random_hero_4", "random_hero_4", "{!}random_hero_4", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_outlaws,
[], 
lord_attrib|level(45),wp(290),knight_skills_3, man_face_middle_1, mercenary_face_2],
["robber_random_hero_5", "random_hero_5", "{!}random_hero_5", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_outlaws,
[], 
knight_attrib_5|level(50),wp(300),knight_skills_4, man_face_middle_1, mercenary_face_2],
["robber_random_hero_6", "random_hero_6", "{!}random_hero_6", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_outlaws,
[], 
knight_attrib_4|level(42),wp(300),knight_skills_3, man_face_middle_1, mercenary_face_2],
["robber_random_hero_7", "random_hero_7", "{!}random_hero_7", tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, 0,reserved,  fac_outlaws,
[], 
knight_attrib_3|level(38),wp(200),knight_skills_2, man_face_middle_1, mercenary_face_2],
#singer anmi#randomhero_start
#dedal
["musican_male","Musican","Musican",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_short_tunic,itm_linen_tunic,itm_tabard,itm_woolen_hose,itm_blue_hose],def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
["musican_female","Musican","Musican",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_woolen_hose,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood],def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
["musicans_end","_","_",tf_inactive,0,0,0,[],0,0,0,0],
##############################for test
  # ["new_troop","new_troop","new_troop",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
  #  [itm_arena_armor_green,itm_arena_shield_green,itm_axe,itm_hide_boots],
  #  str_9|agi_9|level(5),wp(80),knows_common,mercenary_face_1, mercenary_face_2],#test

  #  ["npc17","Geoffrey","Geoffrey", tf_hero,scn_town_23_tavern|entry(1),reserved, fac_commoners,[itm_arena_armor_green,itm_hide_boots,itm_club],
  #  str_7|agi_7|int_11|cha_6|level(1),wp(40),knows_merchant_npc|
  #  knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
  #  0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  #  ["hareck","hareck","hareck",tf_hero,scn_town_23_tavern|entry(2),reserved,  fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x000000019808730b0af3ada6626d486a000000000011c70d0000000000000000],
################################for test

  ["testlady","testlady", "testlady",tf_hero|tf_beautiful, 0,0, fac_commoners,[itm_sword_medieval_d_long,itm_xena_boots,itm_xena_armor],
knight_attrib_5,wp(450),knight_skills_5,0x00000008000c30080000000000000f0e00000000000000000000000000000000],

  ["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_medieval_b, itm_throwing_daggers],
   def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1, man_face_old_2],
   
  ["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_8|level(15),wp(120),knows_common|knows_power_strike_2|knows_ironflesh_9,    bandit_face1, bandit_face2],

  ["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, #they look like belligerent drunks
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

  ["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

   
   
  ["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_viking_1,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1, man_face_older_2],
   
  ["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],

   ["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_robe, itm_black_hood, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,woman_face_1, woman_face_2],   
   ["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_rich_outfit, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],   
   
   
##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
##   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [itm_sword,itm_leather_jacket,itm_hide_boots, itm_saddle_horse, itm_leather_jacket, itm_leather_cap],
##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [itm_knife,itm_dagger,itm_hunting_crossbow,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
##   def_attrib|level(3),wp(45),knows_common,refugee_face1,refugee_face2],


  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_padded_cloth,itm_nomad_boots, itm_splinted_leather_greaves, itm_skullcap, itm_sword_medieval_b,  itm_crossbow, itm_bolts, itm_plate_covered_round_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
  ["swadian_crossbowman_multiplayer_ai","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_a,itm_tab_shield_heater_b,
    itm_leather_jerkin,itm_leather_armor,itm_ankle_boots,itm_footman_helmet],
   def_attrib|level(19),wp_melee(90)|wp_crossbow(100),knows_common|knows_ironflesh_4|knows_athletics_6|knows_shield_5|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer_ai","Swadian Infantry","Swadian Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_pike,itm_bastard_sword_a,itm_tab_shield_heater_c,
    itm_studded_leather_coat,itm_ankle_boots,itm_flat_topped_helmet],
   def_attrib|level(19),wp_melee(105),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_5|knows_athletics_4,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_lance,itm_bastard_sword_a,itm_tab_shield_heater_cav_a,
    itm_mail_with_surcoat,itm_hide_boots,itm_norman_helmet,itm_hunter],
   def_attrib|level(19),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer_ai","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_scimitar,itm_nomad_bow,
    itm_leather_vest,itm_nomad_boots,itm_spiked_helmet,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_4|knows_power_draw_5|knows_athletics_6|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer_ai","Vaegir Spearman","Vaegir Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_padded_leather,itm_nomad_boots,itm_spiked_helmet,itm_nomad_cap, itm_spear, itm_tab_shield_kite_b, itm_mace_1, itm_javelin],
   def_attrib|str_12|level(19),wp_melee(90),knows_ironflesh_4|knows_athletics_6|knows_power_throw_3|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer_ai","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_battle_axe,itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
     itm_studded_leather_coat,itm_lamellar_vest,itm_nomad_boots,itm_spiked_helmet,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_4|knows_ironflesh_4|knows_power_strike_4|knows_shield_3,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_dismounted_lancer_multiplayer_ai","Khergit Dismounted Lancer","Khergit Dismounted Lancer",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c],
   def_attrib|level(19),wp(100),knows_riding_4|knows_power_strike_1|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_1|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer_ai","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_khergit_bow,itm_khergit_arrows,itm_tab_shield_small_round_b,
    itm_khergit_cavalry_helmet,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_steppe_horse],
   def_attrib|level(19),wp(90)|wp_archery(100),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_horse_archery_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer_ai","Khergit Lancer","Khergit Lancers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_scale_gauntlets,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser],
   def_attrib|level(19),wp(100),knows_riding_7|knows_power_strike_2|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_1|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["nord_veteran_multiplayer_ai","Nord Footman","Nord Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
   [itm_sword_viking_2,itm_one_handed_battle_axe_b,itm_two_handed_axe,itm_tab_shield_round_d,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
   def_attrib|level(19),wp(130),knows_ironflesh_3|knows_power_strike_5|knows_power_throw_3|knows_athletics_5|knows_shield_3,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer_ai","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_two_handed_axe,itm_spear,itm_tab_shield_round_a,
    itm_skullcap,itm_nordic_archer_helmet,itm_leather_jerkin,itm_leather_boots,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,nord_face_young_1, nord_face_older_2],
  ["nord_archer_multiplayer_ai","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_two_handed_axe,itm_sword_viking_2,itm_short_bow,
    itm_leather_jerkin,itm_blue_tunic,itm_leather_boots,itm_nasal_helmet,itm_leather_cap],
   def_attrib|str_11|level(19),wp_melee(80)|wp_archery(110),knows_ironflesh_4|knows_power_strike_2|knows_shield_1|knows_power_draw_5|knows_athletics_6,nord_face_young_1, nord_face_old_2],
  ["rhodok_veteran_crossbowman_multiplayer_ai","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_pick,itm_club_with_spike_head,itm_maul,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts,
    itm_leather_cap,itm_padded_leather,itm_nomad_boots],
   def_attrib|level(19),wp_melee(100)|wp_crossbow(120),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_3|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_multiplayer_ai","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [itm_ashwood_pike,itm_war_spear,itm_pike,itm_club_with_spike_head,itm_sledgehammer,itm_tab_shield_pavise_c,itm_sword_medieval_a,
    itm_leather_cap,itm_byrnie,itm_ragged_outfit,itm_nomad_boots],
   def_attrib|level(19),wp(115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai","Rhodok Scout","Rhodok Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
   #TODO: Change weapons, copied from Nord Scout
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a,itm_light_lance,itm_skullcap,itm_aketon_green,
    itm_ragged_outfit,itm_nomad_boots,itm_ankle_boots,itm_saddle_horse],
   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,rhodok_face_young_1, rhodok_face_older_2],
  ["sarranid_infantry_multiplayer_ai","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
   [itm_sarranid_mail_shirt,itm_sarranid_horseman_helmet,itm_sarranid_boots_b,itm_sarranid_boots_c,itm_splinted_leather_greaves,itm_arabian_sword_b,itm_mace_3,itm_spear,itm_tab_shield_kite_c],
   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3,swadian_face_middle_1, swadian_face_old_2],
  ["sarranid_archer_multiplayer_ai","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_archers_vest,itm_sarranid_boots_b,itm_sarranid_helmet1,itm_turban,itm_desert_turban],
   def_attrib|level(19),wp_melee(90)|wp_archery(100),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_horseman_multiplayer_ai","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
    itm_sarranid_mail_shirt,itm_sarranid_boots_b,itm_sarranid_boots_c,itm_sarranid_horseman_helmet,itm_courser,itm_hunter],
   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

   
   
#Multiplayer troops (they must have the base items only, nothing else)
  ["swadian_crossbowman_multiplayer","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_b_small,itm_tab_shield_heater_a,itm_red_shirt,itm_ankle_boots],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wpe(90,60,180,90),knows_common_multiplayer|knows_ironflesh_2|knows_athletics_4|knows_shield_5|knows_power_strike_2|knows_riding_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_tab_shield_heater_a,itm_red_tunic,itm_ankle_boots],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wpex(105,130,110,40,60,110),knows_common_multiplayer|knows_ironflesh_5|knows_shield_4|knows_power_strike_4|knows_power_throw_2|knows_athletics_6|knows_riding_1,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_a,
    itm_red_tunic,itm_ankle_boots,itm_saddle_horse],
   str_14 | agi_16 |def_attrib_multiplayer|level(20),wp_melee(110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3|knows_shield_2|knows_power_throw_2|knows_power_strike_3|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],
#  ["swadian_mounted_crossbowman_multiplayer","Swadian Mounted Crossbowman","Swadian Mounted Crossbowmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
#   [itm_bolts,itm_light_crossbow,itm_tab_shield_heater_cav_a,itm_bastard_sword_a,
#    itm_red_shirt,itm_hide_boots,itm_saddle_horse],
#   def_attrib_multiplayer|level(20),wp_melee(100)|wp_crossbow(120),knows_common_multiplayer|knows_riding_4|knows_shield_3|knows_ironflesh_3|knows_horse_archery_2|knows_power_strike_3|knows_athletics_2|knows_shield_2,swadian_face_young_1, swadian_face_old_2],
  ["vaegir_archer_multiplayer","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_mace_1,itm_nomad_bow,
    itm_linen_tunic,itm_hide_boots],
   str_14 | agi_14 |def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_common_multiplayer|knows_ironflesh_2|knows_power_draw_7|knows_athletics_3|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spear, itm_tab_shield_kite_a, itm_mace_1,
    itm_linen_tunic,itm_hide_boots],
   str_15 | agi_15 |def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_common_multiplayer|knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_4|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
    itm_linen_tunic,itm_hide_boots,itm_saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_4|knows_power_strike_3|knows_shield_3|knows_power_throw_4|knows_horse_archery_1,vaegir_face_young_1, vaegir_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_nomad_bow,itm_arrows,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   str_15 | agi_18 |def_attrib_multiplayer|level(21),wpe(70,142,60,100),knows_common_multiplayer|knows_riding_2|knows_power_draw_5|knows_horse_archery_3|knows_athletics_3|knows_shield_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_infantry_multiplayer","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_spear,itm_tab_shield_small_round_a,
    itm_steppe_armor,itm_hide_boots,itm_leather_gloves],
   str_14 | agi_15 |def_attrib_multiplayer|level(19),wp(110),knows_common_multiplayer|knows_ironflesh_3|knows_power_throw_3|knows_shield_4|knows_power_strike_3|knows_athletics_6|knows_riding_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_lance,itm_tab_shield_small_round_a,
    itm_khergit_armor,itm_leather_steppe_cap_a,itm_hide_boots,itm_steppe_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(21),wp(115),knows_common_multiplayer|knows_riding_6|knows_ironflesh_3|knows_power_throw_3|knows_shield_4|knows_power_strike_3|knows_athletics_4,khergit_face_middle_1, khergit_face_older_2],
  ["nord_archer_multiplayer","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2_small,itm_short_bow,
    itm_blue_tunic,itm_leather_boots],
   str_15 | agi_14 |def_attrib_multiplayer|str_11|level(15),wpe(90,150,60,80),knows_common_multiplayer|knows_ironflesh_2|knows_power_strike_2|knows_shield_3|knows_power_draw_5|knows_athletics_3|knows_riding_1,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_multiplayer","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_a,itm_tab_shield_round_a,
    itm_blue_tunic,itm_leather_boots],
   str_17 | agi_15 |def_attrib_multiplayer|level(24),wpex(110,135,100,40,60,140),knows_common_multiplayer|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_sword_viking_1,itm_spear,itm_tab_shield_small_round_a,
    itm_blue_tunic,itm_leather_boots,itm_saddle_horse],
   str_16 | agi_15 |def_attrib_multiplayer|level(19),wp(105),knows_common_multiplayer|knows_riding_6|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_3|knows_power_throw_3|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
  ["rhodok_veteran_crossbowman_multiplayer","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_pavise_a,
    itm_tunic_with_green_cape,itm_ankle_boots],
   str_16 | agi_15 |def_attrib_multiplayer|level(20),wpe(100,60,180,90),knows_common_multiplayer|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_4|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sergeant_multiplayer","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_fighting_pick,itm_tab_shield_pavise_a,itm_spear,
    itm_green_tunic,itm_ankle_boots],
   str_16 | agi_14 |def_attrib_multiplayer|level(20),wpex(110,100,140,30,50,110),knows_common_multiplayer|knows_ironflesh_4|knows_shield_5|knows_power_strike_4|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sword_medieval_a,itm_tab_shield_heater_cav_a, itm_light_lance, 
    itm_green_tunic,itm_ankle_boots,itm_saddle_horse],
   str_15 | agi_15 |def_attrib_multiplayer|level(20),wp(100),knows_common_multiplayer|knows_riding_4|knows_ironflesh_3|knows_shield_3|knows_power_strike_3|knows_power_throw_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["sarranid_archer_multiplayer","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arrows,itm_arabian_sword_a,itm_nomad_bow,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b],
   str_15 | agi_16 |def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_common_multiplayer|knows_ironflesh_4|knows_power_draw_5|knows_athletics_3|knows_shield_2|knows_riding_1|knows_weapon_master_1,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_footman_multiplayer","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_bamboo_spear, itm_tab_shield_kite_a, itm_arabian_sword_a,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b],
   str_14 | agi_15 |def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_common_multiplayer|knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_4|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["sarranid_mamluke_multiplayer","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_a,
    itm_sarranid_cloth_robe, itm_sarranid_boots_b,itm_saddle_horse],
   str_15 | agi_14 |def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_common_multiplayer|knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2|knows_weapon_master_1,vaegir_face_young_1, vaegir_face_older_2],


   ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   
   #Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

  ["quick_battle_troop_1","Rodrigo de Braganca","Rodrigo de Braganca", tf_hero,0,0,fac_kingdom_1,
   [itm_double_sword, itm_ganquang_dart, itm_ganquang_dart,itm_tab_shield_round_d,
    itm_vaegir_spiked_helmet, itm_wei_xiadi_samurai_armor02, itm_west_arbalester_boots, itm_leather_gloves],
   str_27|agi_27|int_12|cha_12|level(35),wpex(189,153,248,35,32,180),knows_athletics_5|knows_shield_5|knows_weapon_master_3|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_6,0x0000000e240070cd598bb02b9556428c00000000001eabce0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_2","Usiatra","Usiatra", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_strong_bow, itm_barbed_arrows, itm_scimitar_b, itm_tab_shield_small_round_c, itm_courser,
    itm_heavy_lamellar_armor, itm_khergit_guard_boots,itm_khergit_cavalry_helmet],
   str_32|agi_21|int_12|cha_18|level(38),wpex(182,113,112,189,82,135),knows_horse_archery_5|knows_riding_5|knows_athletics_4|knows_shield_4|knows_weapon_master_4|knows_power_draw_7|knows_power_throw_1|knows_power_strike_5|knows_ironflesh_5,0x000000007f004000719b69422165b71300000000001d5d1d0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_3","Hegen","Hegen", tf_hero|tf_tall,0,0,fac_kingdom_1,
   [itm_great_lance, itm_sword_two_handed_a, itm_sword_medieval_d_long, itm_tab_shield_heater_c, itm_charger,
    itm_guard_helmet, itm_coat_of_plates, itm_gauntlets, itm_plate_boots],
   str_35|agi_26|int_15|cha_15|level(40),wpex(250,252,252,31,33,34),knows_riding_7|knows_athletics_7|knows_shield_5|knows_weapon_master_7|knows_power_strike_8|knows_ironflesh_9,0x000000018000324428db8a431491472400000000001e44a90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_4","Konrad","Konrad", tf_hero,0,0,fac_kingdom_1,
   [itm_sword_two_handed_a, itm_luc_flanged_mace_iron, itm_tab_shield_kite_d,
    itm_bascinet_3, itm_heraldic_mail_with_tunic, itm_mail_mittens, itm_mail_boots],
   str_28|agi_25|int_17|cha_17|level(34),wpex(180,210,150,30,50,90),knows_riding_2|knows_athletics_9|knows_shield_7|knows_weapon_master_5|knows_power_throw_3|knows_power_strike_7|knows_ironflesh_8,0x000000081700205434db6df4636db8e400000000001db6e30000000000000000, swadian_face_old_2],
  ["quick_battle_troop_5","Sverre","Sverre", tf_hero|tf_tall,0,0,fac_kingdom_1,
   [itm_2dblhead_ax, itm_vsword02, itm_heavy_throwing_axes, itm_tab_shield_round_e,
    itm_williamconqueror_helm, itm_williamconquer, itm_mail_mittens, itm_splinted_greaves],
   str_35|agi_35|int_15|cha_15|level(42),wpex(210,250,210,80,15,210),knows_riding_1|knows_athletics_9|knows_shield_7|knows_weapon_master_6|knows_power_draw_2|knows_power_throw_7|knows_power_strike_8|knows_ironflesh_10,0x000000048a00024723134e24cb51c91b00000000001dc6aa0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_6","Borislav","Borislav", tf_hero,0,0,fac_kingdom_1,
   [itm_ivorybow, itm_spak_bow8_arrow, itm_spak_bow8_arrow, itm_xeno_war_pick02,
    itm_vaegir_fur_helmet, itm_tribal_warrior_outfit, itm_leather_gloves, itm_leather_boots],
   str_22|agi_27|int_18|cha_11|level(28),wpex(70,70,170,180,15,170),knows_horse_archery_2|knows_riding_2|knows_athletics_7|knows_weapon_master_5|knows_power_draw_6|knows_power_throw_3|knows_power_strike_5|knows_ironflesh_5,0x000000089e00444415136e36e34dc8e400000000001d46d90000000000000000, swadian_face_old_2],
  ["quick_battle_troop_7","Stavros","Stavros", tf_hero,0,0,fac_kingdom_1,
   [itm_spak_crsb02_new, itm_steel_bolts, itm_sword_medieval_c_long, itm_tab_shield_pavise_d,
    itm_flattop_helmet_new_grn, itm_armor_23_green, itm_leather_gloves, itm_rus_splint_greaves],
   str_22|agi_25|int_15|cha_12|level(31),wpex(170,70,70,30,180,80),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_7|knows_weapon_master_5|knows_power_throw_2|knows_power_strike_6|knows_ironflesh_6,0x0000000e1400659226e34dcaa46e36db00000000001e391b0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_8","Gamara","Gamara", tf_hero|tf_female,0,0,fac_kingdom_1,
   [itm_throwing_spears, itm_throwing_spears, itm_bb_sword_long, itm_plate_covered_round_shield,
    itm_sarranid_mail_coif_black, itm_assassin_armor, itm_leather_gloves, itm_sarranid_boots_c],
   str_22|agi_25|int_13|cha_15|level(28),wpex(175,40,100,85,15,180),knows_horse_archery_2|knows_riding_2|knows_athletics_9|knows_shield_5|knows_weapon_master_5|knows_power_draw_2|knows_power_throw_8|knows_power_strike_9|knows_ironflesh_5,0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_9","Aethrod","Aethrod", tf_hero,0,0,fac_kingdom_1,
   [itm_war_bow, itm_barbed_arrows, itm_barbed_arrows, itm_sword_khergit_4,
    itm_mail_boots, itm_vaegir_elite_armor,itm_vaegir_war_helmet],
   str_30|agi_27|int_13|cha_16|level(36),wpex(232,133,112,189,82,115),knows_horse_archery_2|knows_riding_2|knows_athletics_9|knows_shield_2|knows_weapon_master_4|knows_power_draw_8|knows_power_throw_3|knows_power_strike_7|knows_ironflesh_7,0x000000000000210536db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2],
  ["quick_battle_troop_10","Zaira","Zaira", tf_hero|tf_beautiful,0,0,fac_kingdom_1,
   [itm_sarranid_cavalry_sword, itm_strong_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_lamellar_charger_y,
    itm_sarranid_royal_helmet, itm_sarranid_elite_round_spaulders, itm_sarranid_boots_d],
   str_25|agi_32|int_15|cha_15|level(28),wpex(166,19,23,199,41,26),knows_horse_archery_7|knows_riding_8|knows_weapon_master_2|knows_power_draw_6|knows_power_throw_1|knows_power_strike_6|knows_ironflesh_5,0x0000000502003001471a6a24dc6594cb00000000001da4840000000000000000, swadian_face_old_2],
  ["quick_battle_troop_11","Argo Sendnar","Argo Sendnar", tf_hero,0,0,fac_kingdom_1,
   [itm_morningstar, itm_tab_shield_round_d, itm_heavy_lance, itm_3lamellar_charger,
    itm_leather_gloves, itm_mongol_helmet_xf, itm_rus_cav_boots, itm_rhodok_padded_jack],
   str_25|agi_22|int_17|cha_20|level(38),wpex(165,35,190,15,17,19),knows_riding_7|knows_athletics_5|knows_shield_6|knows_weapon_master_6|knows_power_strike_9|knows_ironflesh_7,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000, swadian_face_old_2],
  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_hunter, itm_saddle_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_tribal_warrior_outfit,itm_nomad_robe,itm_hide_boots,itm_tab_shield_small_round_a,itm_steppe_horse],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_2],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_leather_vest,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],
   
  ["swadian_merchant", "Merchant of Praven", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, [itm_sword_two_handed_a, itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["vaegir_merchant", "Merchant of Reyvadin", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_5, [itm_sword_two_handed_a, itm_nobleman_outfit, itm_woolen_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["nord_merchant", "Merchant of Sargoth", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, [itm_sword_two_handed_a, itm_leather_jerkin, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, [itm_sword_two_handed_a, itm_sarranid_cloth_robe, itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],       
  ["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],
 
  ["sea_raider_leader","Sea Raider Captain","Sea Raider Captains",tf_hero|tf_guarantee_all_wo_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_helmet,itm_nasal_helmet,itm_mail_shirt,itm_byrnie,itm_mail_hauberk,itm_leather_boots, itm_nomad_boots],
   def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],

  ["looter_leader","Robber","Looters",tf_hero,0,0,fac_outlaws,
   [itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],
   
  ["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],   
  
  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],   
   
  ["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],     

  ["swadian_crossbowman_multiplayer_coop_tier_1","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_hunting_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_heater_a,itm_arming_cap,itm_padded_cloth,itm_ankle_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_infantry_multiplayer_coop_tier_1","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_spiked_club,itm_tab_shield_heater_b,itm_felt_hat,itm_leather_apron,itm_wrapping_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_man_at_arms_multiplayer_coop_tier_1","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_light_lance,itm_sword_medieval_b_small,itm_tab_shield_heater_a,itm_leather_cap,itm_leather_gloves,itm_padded_cloth,itm_wrapping_boots,itm_warhorse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_archer_multiplayer_coop_tier_1","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_arrows,itm_axe,itm_hunting_bow,itm_linen_tunic,itm_nomad_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_1","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_tab_shield_kite_a, itm_axe,itm_rawhide_coat,itm_hide_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_horseman_multiplayer_coop_tier_1","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_spear,itm_tab_shield_kite_cav_a,itm_linen_tunic,itm_hide_boots,itm_hunter],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_veteran_horse_archer_multiplayer_coop_tier_1","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_nomad_bow,itm_arrows,itm_steppe_armor,itm_hide_boots,itm_steppe_horse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_1","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_1,itm_tab_shield_small_round_a,itm_steppe_armor,itm_hide_boots,itm_leather_gloves],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_lancer_multiplayer_coop_tier_1","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_spear,itm_tab_shield_small_round_a,itm_steppe_armor,itm_steppe_cap,itm_hide_boots,itm_leather_gloves,itm_courser],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_archer_multiplayer_coop_tier_1","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2_small,itm_short_bow,itm_blue_tunic,itm_leather_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_veteran_multiplayer_coop_tier_1","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_1,itm_one_handed_war_axe_a,itm_tab_shield_round_a,itm_blue_tunic,itm_leather_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_1","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_war_spear,itm_tab_shield_small_round_a,itm_blue_tunic,itm_leather_boots,itm_saddle_horse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_veteran_crossbowman_multiplayer_coop_tier_1","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_pavise_a,itm_tunic_with_green_cape,itm_ankle_boots],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_sergeant_multiplayer_coop_tier_1","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_military_cleaver_b,itm_tab_shield_pavise_a,itm_darts,itm_green_tunic,itm_ankle_boots,itm_leather_cap],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_1","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_tab_shield_heater_cav_a, itm_light_lance, itm_green_tunic,itm_ankle_boots,itm_padded_coif,itm_saddle_horse],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_archer_multiplayer_coop_tier_1","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arrows,itm_sarranid_mace_1,itm_short_bow,itm_sarranid_cloth_robe, itm_sarranid_boots_b],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_footman_multiplayer_coop_tier_1","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_tab_shield_kite_a, itm_sarranid_axe_a,itm_sarranid_cloth_robe, itm_sarranid_boots_b],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_mamluke_multiplayer_coop_tier_1","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_lance,itm_tab_shield_small_round_a,itm_sarranid_cloth_robe, itm_sarranid_boots_b,itm_arabian_horse_a],
    level(4)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

  ["swadian_crossbowman_multiplayer_coop_tier_2","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_spiked_club,itm_crossbow,itm_bolts,itm_tab_shield_heater_b,itm_arming_cap,itm_red_gambeson,itm_ankle_boots],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_infantry_multiplayer_coop_tier_2","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b,itm_tab_shield_heater_c,itm_spear,itm_mail_coif,itm_leather_gloves,itm_mail_with_tunic_red,itm_ankle_boots],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_man_at_arms_multiplayer_coop_tier_2","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_b,itm_helmet_with_neckguard,itm_leather_gloves,itm_haubergeon,itm_leather_boots,itm_warhorse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_archer_multiplayer_coop_tier_2","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_axe,itm_nomad_bow,itm_leather_vest,itm_nomad_boots,itm_vaegir_fur_helmet],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_2","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_javelin,itm_scimitar,itm_tab_shield_kite_b,itm_leather_jerkin,itm_nomad_boots,itm_vaegir_lamellar_helmet,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_horseman_multiplayer_coop_tier_2","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_war_spear,itm_tab_shield_kite_cav_b,itm_javelin,itm_studded_leather_coat,itm_leather_gloves,itm_nomad_boots,itm_vaegir_lamellar_helmet,itm_hunter],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_veteran_horse_archer_multiplayer_coop_tier_2","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_khergit_bow,itm_barbed_arrows,itm_steppe_armor,itm_leather_steppe_cap_a,itm_nomad_boots,itm_steppe_horse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_2","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_2,itm_tab_shield_small_round_b,itm_javelin,itm_tribal_warrior_outfit,itm_nomad_boots,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_lancer_multiplayer_coop_tier_2","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_war_spear,itm_tab_shield_small_round_b,itm_javelin,itm_tribal_warrior_outfit,itm_leather_steppe_cap_b,itm_nomad_boots,itm_courser],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_archer_multiplayer_coop_tier_2","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_arrows,itm_sword_viking_2,itm_long_bow,itm_leather_jerkin,itm_leather_boots,itm_nordic_archer_helmet],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_veteran_multiplayer_coop_tier_2","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_a,itm_tab_shield_round_b,itm_throwing_axes,itm_leather_jerkin,itm_leather_boots,itm_nordic_footman_helmet,itm_leather_gloves],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_2","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_javelin,itm_lance,itm_tab_shield_small_round_a,itm_leather_jerkin,itm_leather_boots,itm_leather_gloves,itm_nordic_footman_helmet,itm_saddle_horse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_veteran_crossbowman_multiplayer_coop_tier_2","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_heavy_crossbow,itm_bolts,itm_club_with_spike_head,itm_tab_shield_pavise_b,itm_leather_armor,itm_leather_boots,itm_leather_gloves,itm_leather_cap],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_sergeant_multiplayer_coop_tier_2","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_military_cleaver_b,itm_tab_shield_pavise_b,itm_war_darts,itm_padded_cloth,itm_leather_boots,itm_leather_gloves,itm_footman_helmet],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_2","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_tab_shield_heater_cav_b, itm_heavy_lance,itm_javelin,itm_padded_cloth,itm_leather_boots,itm_leather_gloves,itm_footman_helmet,itm_saddle_horse],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_archer_multiplayer_coop_tier_2","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_barbed_arrows,itm_sarranid_mace_1,itm_nomad_bow,itm_archers_vest,itm_desert_turban,itm_leather_gloves,itm_sarranid_boots_b],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_footman_multiplayer_coop_tier_2","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_tab_shield_kite_b, itm_sarranid_axe_b,itm_javelin,itm_archers_vest,itm_sarranid_warrior_cap,itm_leather_gloves,itm_sarranid_boots_b],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_mamluke_multiplayer_coop_tier_2","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_tab_shield_small_round_b,itm_javelin,itm_archers_vest, itm_sarranid_warrior_cap,itm_leather_gloves,itm_sarranid_boots_b,itm_arabian_horse_a],
    level(5)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

  ["swadian_crossbowman_multiplayer_coop_tier_3","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b,itm_heavy_crossbow,itm_steel_bolts,itm_tab_shield_heater_c,itm_segmented_helmet,itm_leather_jerkin,itm_leather_boots],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_infantry_multiplayer_coop_tier_3","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bastard_sword_a,itm_awlpike,itm_tab_shield_heater_c,itm_bascinet,itm_mail_mittens,itm_mail_with_surcoat,itm_mail_chausses],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_man_at_arms_multiplayer_coop_tier_3","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_heavy_lance,itm_bastard_sword_b,itm_tab_shield_heater_cav_a,itm_flat_topped_helmet,itm_mail_mittens,itm_mail_with_surcoat,itm_mail_chausses,itm_warhorse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_archer_multiplayer_coop_tier_3","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_scimitar_b,itm_strong_bow,itm_leather_jerkin,itm_splinted_leather_greaves,itm_vaegir_spiked_helmet,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_3","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_scimitar_b, itm_tab_shield_kite_b,itm_javelin,itm_lamellar_armor,itm_splinted_leather_greaves,itm_vaegir_lamellar_helmet,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_horseman_multiplayer_coop_tier_3","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_heavy_lance,itm_tab_shield_kite_cav_b, itm_javelin,itm_lamellar_armor,itm_splinted_leather_greaves,itm_vaegir_lamellar_helmet,itm_hunter,itm_mail_mittens],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_veteran_horse_archer_multiplayer_coop_tier_3","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_khergit_3,itm_strong_bow,itm_khergit_arrows,itm_tribal_warrior_outfit,itm_leather_steppe_cap_c,itm_khergit_leather_boots,itm_steppe_horse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_3","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_hafted_blade_a,itm_javelin,itm_leather_steppe_cap_c,itm_lamellar_armor,itm_splinted_leather_greaves,itm_mail_mittens],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_lancer_multiplayer_coop_tier_3","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_heavy_lance,itm_tab_shield_small_round_a,itm_lamellar_armor,itm_leather_steppe_cap_c,itm_splinted_leather_greaves,itm_courser],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_archer_multiplayer_coop_tier_3","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_barbed_arrows,itm_sword_viking_3,itm_long_bow,itm_leather_jerkin,itm_leather_boots,itm_nordic_veteran_archer_helmet,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_veteran_multiplayer_coop_tier_3","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_b,itm_tab_shield_round_d,itm_heavy_throwing_axes,itm_mail_shirt,itm_splinted_leather_greaves,itm_nordic_huscarl_helmet],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_3","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_throwing_spears,itm_heavy_lance,itm_tab_shield_small_round_b,itm_mail_shirt,itm_splinted_leather_greaves,itm_nordic_fighter_helmet,itm_saddle_horse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_veteran_crossbowman_multiplayer_coop_tier_3","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sniper_crossbow,itm_steel_bolts,itm_military_cleaver_c,itm_tab_shield_pavise_c,itm_padded_cloth,itm_leather_boots,itm_footman_helmet,itm_leather_gloves],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_sergeant_multiplayer_coop_tier_3","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_tab_shield_pavise_c,itm_military_cleaver_c,itm_javelin,itm_ragged_outfit,itm_splinted_greaves,itm_kettle_hat,itm_mail_mittens],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_3","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_javelin,itm_tab_shield_heater_cav_b, itm_heavy_lance, itm_ragged_outfit,itm_splinted_greaves,itm_bascinet_2,itm_mail_mittens,itm_saddle_horse],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_archer_multiplayer_coop_tier_3","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_khergit_arrows,itm_sarranid_mace_1,itm_nomad_bow,itm_archers_vest,itm_sarranid_mail_coif,itm_leather_gloves,itm_sarranid_boots_c],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_footman_multiplayer_coop_tier_3","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_jarid, itm_tab_shield_kite_c, itm_sarranid_axe_b,itm_sarranid_mail_shirt,itm_sarranid_mail_coif,itm_mail_mittens,itm_sarranid_boots_c],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_mamluke_multiplayer_coop_tier_3","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_heavy_lance,itm_tab_shield_small_round_b,itm_jarid,itm_sarranid_cavalry_robe,itm_sarranid_horseman_helmet,itm_mail_mittens,itm_sarranid_boots_c,itm_arabian_horse_a],
    level(6)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

  ["swadian_crossbowman_multiplayer_coop_tier_4","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b,itm_sniper_crossbow,itm_steel_bolts,itm_tab_shield_heater_c,itm_helmet_with_neckguard,itm_leather_gloves,itm_haubergeon,itm_mail_chausses],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_infantry_multiplayer_coop_tier_4","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bastard_sword_b,itm_awlpike_long,itm_tab_shield_heater_d,itm_guard_helmet,itm_gauntlets,itm_coat_of_plates,itm_iron_greaves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["swadian_man_at_arms_multiplayer_coop_tier_4","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_great_lance,itm_morningstar,itm_tab_shield_heater_cav_b,itm_great_helmet,itm_gauntlets,itm_coat_of_plates_red,itm_plate_boots,itm_warhorse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_archer_multiplayer_coop_tier_4","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_barbed_arrows,itm_bardiche,itm_war_bow,itm_lamellar_vest,itm_splinted_leather_greaves,itm_vaegir_lamellar_helmet,itm_leather_gloves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_spearman_multiplayer_coop_tier_4","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_bardiche,itm_javelin,itm_vaegir_elite_armor,itm_splinted_greaves,itm_vaegir_war_helmet,itm_mail_mittens],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["vaegir_horseman_multiplayer_coop_tier_4","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_heavy_lance,itm_tab_shield_kite_cav_b,itm_javelin,itm_vaegir_elite_armor,itm_splinted_greaves,itm_hunter,itm_vaegir_war_helmet,itm_scale_gauntlets],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_veteran_horse_archer_multiplayer_coop_tier_4","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_hafted_blade_b,itm_strong_bow,itm_khergit_arrows,itm_lamellar_vest_khergit,itm_khergit_guard_helmet,itm_splinted_leather_greaves,itm_steppe_horse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_infantry_multiplayer_coop_tier_4","Khergit Infantry","Khergit Infantries",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_hafted_blade_b,itm_tab_shield_small_round_a,itm_jarid,itm_khergit_elite_armor,itm_khergit_guard_boots,itm_khergit_war_helmet,itm_lamellar_gauntlets],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["khergit_lancer_multiplayer_coop_tier_4","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_great_lance,itm_tab_shield_small_round_c,itm_khergit_elite_armor,itm_khergit_war_helmet,itm_khergit_guard_boots,itm_lamellar_gauntlets,itm_courser],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_archer_multiplayer_coop_tier_4","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_khergit_arrows,itm_sword_viking_3,itm_long_bow,itm_byrnie,itm_splinted_leather_greaves,itm_nordic_footman_helmet,itm_leather_gloves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_veteran_multiplayer_coop_tier_4","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_great_axe,itm_tab_shield_round_e,itm_heavy_throwing_axes,itm_banded_armor,itm_mail_boots,itm_nordic_warlord_helmet],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["nord_scout_multiplayer_coop_tier_4","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_throwing_spears,itm_great_lance,itm_tab_shield_small_round_c,itm_mail_hauberk,itm_splinted_leather_greaves,itm_nordic_huscarl_helmet,itm_saddle_horse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_veteran_crossbowman_multiplayer_coop_tier_4","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sniper_crossbow,itm_steel_bolts,itm_sledgehammer,itm_tab_shield_pavise_d,itm_mail_with_tunic_green,itm_kettle_hat,itm_splinted_greaves,itm_leather_gloves],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_sergeant_multiplayer_coop_tier_4","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_two_handed_cleaver,itm_tab_shield_pavise_d,itm_javelin,itm_surcoat_over_mail,itm_iron_greaves,itm_gauntlets,itm_full_helm,],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["rhodok_horseman_multiplayer_coop_tier_4","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_javelin,itm_tab_shield_heater_cav_b, itm_great_lance, itm_surcoat_over_mail,itm_iron_greaves,itm_gauntlets,itm_full_helm,itm_saddle_horse],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_archer_multiplayer_coop_tier_4","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_khergit_arrows,itm_sarranid_two_handed_mace_1,itm_strong_bow,itm_sarranid_mail_shirt,itm_sarranid_mail_coif,itm_leather_gloves,itm_sarranid_boots_d],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_footman_multiplayer_coop_tier_4","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_bamboo_spear, itm_tab_shield_kite_c, itm_arabian_sword_a,itm_sarranid_elite_armor,itm_sarranid_veiled_helmet,itm_scale_gauntlets, itm_sarranid_boots_d],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],
  ["sarranid_mamluke_multiplayer_coop_tier_4","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_c,itm_mamluke_mail,itm_sarranid_veiled_helmet,itm_scale_gauntlets, itm_sarranid_boots_d,itm_arabian_horse_a],
    level(7)|str_20, wp(300), knows_power_draw_10|knows_power_throw_10|knows_riding_10, 0, 0],

   ["coop_faction_troop_templates_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   #tier 1
  ["npc1_1","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_armor,itm_nomad_boots,itm_knife, itm_courser],
   str_16|agi_17|int_6|cha_30|level(25),wpex(250,80,140,160,90,250),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_ironflesh_1|knows_power_strike_7|knows_pathfinding_3|knows_athletics_5|knows_tracking_1|knows_riding_6|knows_power_throw_7|knows_power_draw_5, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2_1","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_linen_tunic,itm_hide_boots,itm_club, itm_saddle_horse],
   str_14|agi_17|int_6|cha_30|level(25),wpex(240,130,170,150,170,90),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_5|knows_first_aid_1|knows_leadership_1|knows_riding_4|knows_power_strike_7|knows_power_draw_3|knows_power_throw_3,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3_1","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_dress,itm_woolen_hose,itm_knife, itm_hunter],
   str_24|agi_13|int_6|cha_30|level(25),wpex(190,80,240,180,180,80),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_6|knows_riding_8|knows_power_strike_5|knows_power_draw_3|knows_power_throw_3,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4_1","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_jerkin,itm_nomad_boots, itm_sword_medieval_a, itm_hunter],
   str_20|agi_13|int_6|cha_30|level(25),wpex(210,230,200,90,100,95),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_2|knows_power_strike_9|knows_riding_8|knows_athletics_7|knows_power_throw_3|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2|knows_power_draw_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5_1","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_vest,itm_nomad_boots, itm_sword_khergit_1, itm_steppe_horse],
   str_18|agi_13|int_6|cha_30|level(25),wpex(160,80,130,250,50,230),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_riding_7|knows_horse_archery_9|knows_power_draw_8|knows_leadership_2|knows_weapon_master_1|knows_power_strike_5|knows_power_throw_8|knows_athletics_5,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6_1","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_a, itm_sumpter_horse],
   str_20|agi_19|int_6|cha_30|level(25),wpex(240,210,180,90,100,80),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_riding_7|knows_weapon_master_2|knows_athletics_8|knows_trainer_1|knows_leadership_1|knows_power_strike_7|knows_power_draw_2|knows_power_throw_3,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7_1","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_ragged_outfit,itm_wrapping_boots, itm_hunting_bow, itm_arrows, itm_quarter_staff, itm_arabian_horse_b],
   str_16|agi_13|int_6|cha_30|level(25),wpex(90,80,230,280,110,130),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_tracking_2|knows_athletics_8|knows_spotting_1|knows_pathfinding_1|knows_power_draw_10|knows_riding_4|knows_power_strike_6|knows_power_throw_5,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8_1","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tribal_warrior_outfit,itm_nomad_boots, itm_sword_viking_1, itm_courser],
   str_18|agi_15|int_6|cha_30|level(25),wpex(190,250,80,120,80,250),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_3|knows_athletics_10|knows_leadership_3|knows_tactics_1|knows_riding_4|knows_power_strike_10|knows_power_draw_2|knows_power_throw_8,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9_1","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_tabard,itm_nomad_boots, itm_sword_medieval_b_small, itm_courser],
   str_22|agi_19|int_6|cha_30|level(25),wpex(80,230,130,220,70,160),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_1|knows_riding_4|knows_athletics_6|knows_leadership_1|knows_tactics_1|knows_power_strike_4|knows_power_draw_7|knows_power_throw_5,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10_1","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_padded_leather,itm_nomad_boots, itm_crossbow, itm_bolts, itm_pickaxe, itm_saddle_horse],
   str_24|agi_19|int_6|cha_30|level(25),wpex(170,80,80,160,290,150),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2|knows_riding_4|knows_power_strike_5|knows_power_draw_5|knows_power_throw_5|knows_athletics_7,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11_1","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_leather_apron, itm_falchion, itm_wrapping_boots, itm_sumpter_horse],
   str_16|agi_17|int_6|cha_30|level(25),wpex(140,230,130,80,210,170),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5|knows_riding_4|knows_power_strike_5|knows_power_draw_2|knows_power_throw_7|knows_athletics_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12_1","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_disguise,itm_nomad_boots, itm_staff, itm_sumpter_horse],
   str_16|agi_17|int_6|cha_30|level(25),wpex(120,110,290,80,110,120),   knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_ironflesh_1|knows_power_strike_7|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3|knows_riding_4|knows_power_draw_2|knows_power_throw_3|knows_athletics_7,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13_1","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nomad_robe,itm_nomad_boots, itm_scimitar, itm_courser],
   str_14|agi_17|int_6|cha_30|level(25),wpex(250,80,140,210,110,140),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_riding_9|knows_leadership_2|knows_athletics_5|knows_ironflesh_2|knows_power_strike_6|knows_weapon_master_1|knows_power_draw_7|knows_power_throw_4,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14_1","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_nobleman_outfit,itm_nomad_boots, itm_sword_medieval_b_small, itm_courser],
   str_18|agi_19|int_6|cha_30|level(25),wpex(280,170,170,170,170,180),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1|knows_riding_7|knows_power_strike_7|knows_power_draw_6|knows_power_throw_6|knows_athletics_8,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15_1","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_rich_outfit,itm_nomad_boots, itm_sword_medieval_b_small, itm_hunter],
   str_18|agi_13|int_6|cha_30|level(25),wpex(190,290,130,210,90,90),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1|knows_riding_6|knows_power_strike_7|knows_power_draw_7|knows_power_throw_3|knows_athletics_5,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16_1","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_peasant_dress,itm_nomad_boots, itm_dagger, itm_throwing_knives, itm_saddle_horse],
   str_14|agi_17|int_6|cha_30|level(25),wpex(260,10,100,160,30,300),knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10|
   knows_power_throw_10|knows_athletics_10|knows_power_strike_8|knows_riding_4|knows_power_draw_5,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],
   
    #tier 2
  ["npc1_2","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_leather_steppe_cap_c,itm_leather_gloves,itm_nomad_robe,itm_hide_boots,itm_sword_medieval_b_small, itm_courser],
   str_16|agi_17|int_12|cha_7|level(14),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2_2","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_nasal_helmet,itm_padded_leather,itm_leather_boots,itm_mace_2,itm_tab_shield_small_round_a, itm_saddle_horse],
   str_14|agi_17|int_11|cha_6|level(14),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3_2","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_head_wrappings,itm_leather_jerkin,itm_wrapping_boots,itm_sword_medieval_b_small, itm_hunter],
   str_24|agi_13|int_11|cha_6|level(14),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4_2","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_kettle_hat,itm_leather_gloves,itm_studded_leather_coat,itm_leather_boots,itm_sword_medieval_c,itm_tab_shield_heater_c, itm_hunter],
   str_20|agi_13|int_13|cha_10|level(27),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5_2","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_khergit_2, itm_tab_shield_small_round_b, itm_leather_steppe_cap_b, itm_tribal_warrior_outfit, itm_khergit_leather_boots, itm_steppe_horse],
   str_18|agi_13|int_12|cha_7|level(23),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6_2","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bastard_sword_a, itm_mail_coif, itm_mail_with_tunic_red, itm_ankle_boots, itm_sumpter_horse],
   str_20|agi_19|int_10|cha_5|level(25),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7_2","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_voulge, itm_short_bow, itm_barbed_arrows, itm_nordic_fighter_helmet, itm_leather_gloves, itm_studded_leather_coat, itm_leather_boots, itm_arabian_horse_b],
   str_16|agi_13|int_10|cha_6|level(17),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8_2","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_2, itm_nordic_helmet, itm_byrnie, itm_leather_boots, itm_courser],
   str_18|agi_15|int_9|cha_10|level(26),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9_2","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_c, itm_vaegir_fur_cap, itm_leather_vest, itm_nomad_boots, itm_courser],
   str_22|agi_19|int_7|cha_8|level(17),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10_2","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_military_sickle_a, itm_heavy_crossbow, itm_bolts, itm_mail_coif, itm_leather_gloves, itm_aketon_green, itm_leather_boots, itm_saddle_horse],
   str_24|agi_19|int_9|cha_11|level(27),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11_2","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sarranid_axe_a, itm_arming_cap, itm_leather_gloves, itm_padded_cloth, itm_ankle_boots, itm_sumpter_horse],
   str_16|agi_17|int_10|cha_10|level(26),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12_2","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_iron_staff, itm_padded_coif, itm_leather_gloves, itm_pilgrim_disguise, itm_leather_boots, itm_sumpter_horse],
   str_16|agi_17|int_13|cha_7|level(20),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13_2","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar, itm_tab_shield_small_round_b, itm_sarranid_warrior_cap, itm_sarranid_leather_armor, itm_sarranid_boots_b, itm_courser],
   str_14|agi_17|int_12|cha_8|level(19),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14_2","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_b, itm_tab_shield_heater_c, itm_mail_coif, itm_studded_leather_coat, itm_leather_boots, itm_courser],
   str_18|agi_19|int_11|cha_8|level(23),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15_2","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_axe, itm_helmet_with_neckguard, itm_leather_gloves, itm_red_gambeson, itm_leather_boots, itm_hunter],
   str_18|agi_13|int_12|cha_8|level(25),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16_2","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_2_small, itm_light_throwing_axes, itm_helmet_with_neckguard, itm_leather_gloves, itm_leather_jerkin, itm_ankle_boots, itm_saddle_horse],
   str_14|agi_17|int_8|cha_7|level(17),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],

  #tier 3
  ["npc1_3","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_war_helmet,itm_lamellar_gauntlets,itm_lamellar_vest_khergit,itm_khergit_leather_boots,itm_sword_medieval_c_small, itm_courser],
   str_16|agi_17|int_12|cha_7|level(14),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2_3","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_nordic_veteran_archer_helmet,itm_leather_gloves,itm_byrnie,itm_leather_boots,itm_mace_3,itm_tab_shield_small_round_b, itm_saddle_horse],
   str_14|agi_17|int_11|cha_6|level(14),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3_3","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_skullcap,itm_leather_gloves,itm_mail_shirt,itm_wrapping_boots,itm_sword_medieval_c_small, itm_hunter],
   str_24|agi_13|int_11|cha_6|level(14),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4_3","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bascinet_2,itm_leather_gloves,itm_surcoat_over_mail,itm_mail_chausses,itm_sword_medieval_c_long,itm_tab_shield_heater_c, itm_hunter],
   str_20|agi_13|int_13|cha_10|level(27),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5_3","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar, itm_tab_shield_small_round_c, itm_khergit_cavalry_helmet, itm_leather_gloves, itm_lamellar_vest, itm_khergit_leather_boots, itm_steppe_horse],
   str_18|agi_13|int_12|cha_7|level(23),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6_3","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bastard_sword_b, itm_flat_topped_helmet, itm_mail_mittens, itm_haubergeon, itm_mail_chausses, itm_sumpter_horse],
   str_20|agi_19|int_10|cha_5|level(25),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7_3","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_bardiche, itm_strong_bow, itm_barbed_arrows, itm_nordic_helmet, itm_leather_gloves, itm_mail_hauberk, itm_splinted_leather_greaves, itm_arabian_horse_b],
   str_16|agi_13|int_10|cha_6|level(17),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8_3","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_battle_axe, itm_nordic_huscarl_helmet, itm_leather_gloves, itm_mail_hauberk, itm_mail_chausses, itm_courser],
   str_18|agi_15|int_9|cha_10|level(26),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9_3","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_c_long, itm_vaegir_lamellar_helmet, itm_leather_gloves, itm_lamellar_vest, itm_leather_boots, itm_courser],
   str_22|agi_19|int_7|cha_8|level(17),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10_3","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_military_pick, itm_heavy_crossbow, itm_steel_bolts, itm_kettle_hat, itm_leather_gloves, itm_mail_with_tunic_green, itm_leather_boots, itm_saddle_horse],
   str_24|agi_19|int_9|cha_11|level(27),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11_3","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sarranid_axe_b, itm_arming_cap, itm_leather_gloves, itm_mail_with_surcoat, itm_mail_chausses, itm_sumpter_horse],
   str_16|agi_17|int_10|cha_10|level(26),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12_3","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_iron_staff, itm_mail_coif, itm_mail_mittens, itm_pilgrim_disguise, itm_mail_chausses, itm_sumpter_horse],
   str_16|agi_17|int_13|cha_7|level(20),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13_3","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar, itm_tab_shield_small_round_c, itm_sarranid_mail_coif, itm_arabian_armor_b, itm_sarranid_boots_c, itm_courser],
   str_14|agi_17|int_12|cha_8|level(19),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14_3","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_c, itm_tab_shield_heater_c, itm_bascinet_2, itm_leather_gloves, itm_surcoat_over_mail, itm_mail_chausses, itm_courser],
   str_18|agi_19|int_11|cha_8|level(23),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15_3","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_axe_b, itm_guard_helmet, itm_mail_mittens, itm_haubergeon, itm_mail_chausses, itm_hunter],
   str_18|agi_13|int_12|cha_8|level(25),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16_3","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_2_small, itm_throwing_axes, itm_vaegir_fur_helmet, itm_leather_gloves, itm_lamellar_vest, itm_leather_boots, itm_saddle_horse],
   str_14|agi_17|int_8|cha_7|level(17),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],

   #tier 4
  ["npc1_4","Borcha","Borcha",tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_khergit_guard_helmet,itm_lamellar_gauntlets,itm_khergit_guard_armor,itm_khergit_guard_boots,itm_sword_viking_3_small, itm_courser],
   str_16|agi_17|int_12|cha_7|level(14),wp(60),knows_tracker_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_3|knows_athletics_2|knows_tracking_1|knows_riding_2, #skills 2/3 player at that level
   0x00000004bf086143259d061a9046e23500000000001db52c0000000000000000],
  ["npc2_4","Marnid","Marnid", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_nordic_helmet,itm_mail_mittens,itm_mail_hauberk,itm_mail_chausses,itm_mace_4,itm_tab_shield_small_round_c, itm_saddle_horse],
   str_14|agi_17|int_11|cha_6|level(14),wp(40),knows_merchant_npc|
   knows_trade_2|knows_weapon_master_1|knows_ironflesh_1|knows_wound_treatment_1|knows_athletics_2|knows_first_aid_1|knows_leadership_1,
   0x000000019d004001570b893712c8d28d00000000001dc8990000000000000000],
  ["npc3_4","Ymira","Ymira",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_guard_helmet,itm_gauntlets,itm_plate_armor,itm_plate_boots,itm_sword_viking_3_small, itm_hunter],
   str_24|agi_13|int_11|cha_6|level(14),wp(20),knows_merchant_npc|
   knows_wound_treatment_1|knows_trade_1|knows_first_aid_3|knows_surgery_1|knows_athletics_1|knows_riding_1,
   0x0000000083040001583b6db8dec5925b00000000001d80980000000000000000],
  ["npc4_4","Rolf","Rolf",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_full_helm,itm_scale_gauntlets,itm_heraldic_mail_with_tabard,itm_iron_greaves,itm_sword_medieval_d_long,itm_tab_shield_heater_d, itm_hunter],
   str_20|agi_13|int_13|cha_10|level(27),wp(110),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2,
   0x000000057f1074002c75c6a8a58ad72e00000000001e1a890000000000000000],
  ["npc5_4","Baheshtur","Baheshtur",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar_b, itm_tab_shield_small_round_c, itm_khergit_guard_helmet, itm_scale_gauntlets, itm_lamellar_armor, itm_iron_greaves, itm_steppe_horse],
   str_18|agi_13|int_12|cha_7|level(23),wp(90),knows_warrior_npc|
   knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1,
   0x000000088910318b5c6f972328324a6200000000001cd3310000000000000000],
  ["npc6_4","Firentis","Firentis",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_two_handed_b, itm_bascinet, itm_gauntlets, itm_cuir_bouilli, itm_plate_boots, itm_sumpter_horse],
   str_20|agi_19|int_10|cha_5|level(25),wp(105),knows_warrior_npc|
   knows_riding_2|knows_weapon_master_2|knows_power_strike_2|knows_athletics_3|knows_trainer_1|knows_leadership_1,
  0x00000002050052036a1895d0748f3ca30000000000000f0b0000000000000000],
  ["npc7_4","Deshavi","Deshavi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_great_long_bardiche, itm_war_bow, itm_khergit_arrows, itm_nordic_huscarl_helmet, itm_scale_gauntlets, itm_heraldic_mail_with_tabard, itm_iron_greaves, itm_arabian_horse_b],
   str_16|agi_13|int_10|cha_6|level(17),wp(80),knows_tracker_npc|
   knows_tracking_2|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2,
   0x00000001fc08400533a15297634d44f400000000001e02db0000000000000000],
  ["npc8_4","Matheld","Matheld",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_great_axe, itm_nordic_warlord_helmet, itm_mail_mittens, itm_banded_armor, itm_mail_chausses, itm_courser],
   str_18|agi_15|int_9|cha_10|level(26),wp(90),knows_warrior_npc|
   knows_weapon_master_3|knows_power_strike_2|knows_athletics_2|knows_leadership_3|knows_tactics_1,
   0x00000005800c000637db8314e331e76e00000000001c46db0000000000000000],
  ["npc9_4","Alayen","Alayen",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_bastard_sword_b, itm_vaegir_war_helmet, itm_lamellar_gauntlets, itm_banded_armor, itm_iron_greaves, itm_courser],
   str_22|agi_19|int_7|cha_8|level(17),wp(100),knows_warrior_npc|
   knows_weapon_master_1|knows_riding_1|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_1,
   0x000000030100300f499d5b391b6db8d300000000001dc2e10000000000000000],
  ["npc10_4","Bunduk","Bunduk",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_military_pick, itm_sniper_crossbow, itm_steel_bolts, itm_full_helm, itm_mail_mittens, itm_surcoat_over_mail, itm_splinted_leather_greaves, itm_saddle_horse],
   str_24|agi_19|int_9|cha_11|level(27),wp(105),knows_warrior_npc|
   knows_weapon_master_3|knows_tactics_1|knows_leadership_1|knows_ironflesh_3|knows_trainer_2|knows_first_aid_2,
   0x0000000a3f081006572c91c71c8d46cb00000000001e468a0000000000000000],
  ["npc11_4","Katrin","Katrin",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sarranid_two_handed_axe_a, itm_great_helmet, itm_gauntlets, itm_brigandine_red, itm_plate_boots, itm_sumpter_horse],
   str_16|agi_17|int_10|cha_10|level(26),wp(70),knows_merchant_npc|
   knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5,
   0x0000000d7f0400035915aa226b4d975200000000001ea49e0000000000000000],
  ["npc12_4","Jeremus","Jeremus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_iron_staff, itm_kettle_hat, itm_gauntlets, itm_surcoat_over_mail, itm_plate_boots, itm_sumpter_horse],
   str_16|agi_17|int_13|cha_7|level(20),wp(30),   knows_merchant_npc|
   knows_ironflesh_1|knows_power_strike_1|knows_surgery_4|knows_wound_treatment_3|knows_first_aid_3,
   0x000000078000500e4f8ba62a9cd5d36d00000000001e36250000000000000000],
  ["npc13_4","Nizar","Nizar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_scimitar_b, itm_tab_shield_small_round_c, itm_sarranid_veiled_helmet, itm_scale_gauntlets, itm_mamluke_mail, itm_sarranid_boots_d, itm_courser],
   str_14|agi_17|int_12|cha_8|level(19),wp(80),knows_warrior_npc|
   knows_riding_2|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1,
   0x00000004bf0475c85f4e9592de4e574c00000000001e369c0000000000000000],
  ["npc14_4","Lezalit","Lezalit",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_medieval_d_long, itm_tab_shield_heater_d, itm_great_helmet, itm_gauntlets, itm_heraldic_mail_with_surcoat, itm_plate_boots, itm_courser],
   str_18|agi_19|int_11|cha_8|level(23),wp(100),knows_warrior_npc|
   knows_trainer_4|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1,
   0x00000001a410259144d5d1d6eb55e96a00000000001db0db0000000000000000],
  ["npc15_4","Artimenner","Artimenner",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_axe_c, itm_full_helm, itm_scale_gauntlets, itm_heraldic_mail_with_surcoat, itm_iron_greaves, itm_hunter],
   str_18|agi_13|int_12|cha_8|level(25),wp(80),knows_warrior_npc|
   knows_tactics_2|knows_engineer_4|knows_trade_3|knows_tracking_1|knows_spotting_1,
   0x0000000f2e1021862b4b9123594eab5300000000001d55360000000000000000],
  ["npc16_4","Klethi","Klethi",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_viking_3_small, itm_heavy_throwing_axes, itm_vaegir_lamellar_helmet, itm_lamellar_gauntlets, itm_lamellar_armor, itm_khergit_guard_boots, itm_saddle_horse],
   str_14|agi_17|int_8|cha_7|level(17),wp(80),knows_tracker_npc|
   knows_power_throw_3|knows_athletics_2|knows_power_strike_1,
   0x00000000000c100739ce9c805d2f381300000000001cc7ad0000000000000000],

   ["coop_companion_equipment_ui_0","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_ui_0_f","{!}multiplayer_end","{!}multiplayer_end", tf_female, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_ui_1","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_ui_1_f","{!}multiplayer_end","{!}multiplayer_end", tf_female, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],
   ["coop_companion_equipment_sets_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

]


#Troop upgrade declarations

upgrade(troops,"farmer", "watchman")
# upgrade(troops,"townsman","watchman")
upgrade2(troops,"watchman","caravan_guard","mercenary_crossbowman")
upgrade(troops,"mercenary_crossbowman","mercenary_crossbowman_1")
upgrade(troops,"mercenary_crossbowman_1","mercenary_crossbowman_2")
upgrade2(troops,"caravan_guard","mercenary_swordsman","mercenary_horseman")
upgrade(troops,"mercenary_swordsman","hired_blade")
upgrade(troops,"mercenary_horseman","mercenary_cavalry")

upgrade(troops,"mercenary_noleman","mercenary_squire")
upgrade(troops,"mercenary_squire","mercenary_knight")

upgrade2(troops,"female_noleman","female_noleman_archer","female_noleman_sword")
upgrade(troops,"female_noleman_archer","female_noleman_archer_e")
upgrade(troops,"female_noleman_archer_e","female_noleman_archer_f")

upgrade(troops,"female_noleman_sword","female_noleman_sword_e")
upgrade(troops,"female_noleman_sword_e","female_noleman_knight")

upgrade(troops,"swadian_recruit","swadian_militia")

upgrade2(troops,"swadian_militia","swadian_footman","swadian_skirmisher")
upgrade2(troops,"swadian_footman","swadian_man_at_arms","swadian_infantry")
upgrade(troops,"swadian_infantry","swadian_sergeant")
upgrade(troops,"swadian_skirmisher","swadian_crossbowman")

upgrade(troops,"swadian_crossbowman","swadian_sharpshooter")

upgrade(troops,"swadian_man_at_arms","swadian_knight")

upgrade(troops,"swadian_nobleman","swadian_squire")
upgrade(troops,"swadian_squire","swadian_knight_n")

upgrade(troops,"vaegir_recruit","vaegir_footman")
upgrade2(troops,"vaegir_footman","vaegir_veteran","vaegir_skirmisher")

upgrade(troops,"vaegir_skirmisher","vaegir_archer")

upgrade(troops,"vaegir_archer","vaegir_marksman")

upgrade2(troops,"vaegir_veteran","vaegir_horseman","vaegir_infantry")

upgrade(troops,"vaegir_infantry","vaegir_guard")
upgrade(troops,"vaegir_horseman","vaegir_knight")

upgrade(troops,"vaegir_nobleman","vaegir_noble_warrior")
upgrade2(troops,"vaegir_noble_warrior","vaegir_holy_warrior","vaegir_noble_knight")

upgrade(troops,"khergit_tribesman","khergit_skirmisher")
upgrade(troops,"khergit_skirmisher","khergit_horseman")
upgrade2(troops,"khergit_horseman","khergit_veteran_horseman","khergit_horse_archer")
upgrade(troops,"khergit_veteran_horseman","khergit_lancer")
upgrade(troops,"khergit_horse_archer","khergit_veteran_horse_archer")

upgrade(troops,"khergit_nobleman","khergit_nobleman_warrior")
upgrade2(troops,"khergit_nobleman_warrior","khergit_nobleman_horse_archer","khergit_nobleman_knight")

upgrade2(troops,"nord_recruit","nord_footman","nord_huntsman")
upgrade(troops,"nord_footman","nord_trained_footman")
upgrade(troops,"nord_trained_footman","nord_warrior")
upgrade(troops,"nord_warrior","nord_veteran")
upgrade(troops,"nord_veteran","nord_champion")
upgrade2(troops,"nord_huntsman","nord_archer","nord_archer_1")
upgrade(troops,"nord_archer_1","nord_archer_2")
upgrade(troops,"nord_archer","nord_veteran_archer")

upgrade(troops,"nord_nobleman","nord_nobleman_warrior")
upgrade(troops,"nord_nobleman_warrior","nord_nobleman_champion_horse")

upgrade2(troops,"rhodok_tribesman","rhodok_spearman","rhodok_crossbowman")
upgrade(troops,"rhodok_spearman","rhodok_trained_spearman")
upgrade2(troops,"rhodok_trained_spearman","rhodok_veteran_spearman","rhodok_trained_horseman")
upgrade(troops,"rhodok_trained_horseman","rhodok_trained_horseman_1")
upgrade(troops,"rhodok_veteran_spearman","rhodok_sergeant")

upgrade(troops,"rhodok_crossbowman","rhodok_trained_crossbowman")
upgrade(troops,"rhodok_trained_crossbowman","rhodok_veteran_crossbowman") #new 1.126
upgrade(troops,"rhodok_veteran_crossbowman","rhodok_sharpshooter")

upgrade(troops,"rhodok_nobleman","rhodok_squire")
upgrade2(troops,"rhodok_squire","rhodok_knight","rhodok_walk_knight")

upgrade(troops,"sarranid_recruit","sarranid_footman")

upgrade2(troops,"sarranid_footman","sarranid_veteran_footman","sarranid_skirmisher")
upgrade2(troops,"sarranid_veteran_footman","sarranid_horseman","sarranid_infantry")
upgrade(troops,"sarranid_infantry","sarranid_guard")
upgrade(troops,"sarranid_skirmisher","sarranid_archer")

upgrade2(troops,"sarranid_archer","sarranid_master_archer","sarranid_master_archerwithhorse")

upgrade(troops,"sarranid_horseman","sarranid_mamluke")

upgrade(troops,"sarranid_nobleman","sarranid_nobleman_warrior")
upgrade2(troops,"sarranid_nobleman_warrior","sarranid_nobleman_knight","sarranid_nobleman_knight_archor")

upgrade(troops,"calradic_recruit","calradic_footman")
upgrade2(troops,"calradic_footman","calradic_trained_footman","calradic_skirmisher")
upgrade2(troops,"calradic_trained_footman","calradic_heavy_infantry","calradic_horseman")

upgrade(troops,"calradic_horseman","calradic_cavalry")

upgrade(troops,"calradic_heavy_infantry","calradic_legionary")
upgrade(troops,"calradic_skirmisher","calradic_archer")
upgrade(troops,"calradic_archer","calradic_veteran_archer")

upgrade2(troops,"calradic_nobleman","calradic_nobleman_warrior","calradic_nobleman_archer")
upgrade(troops,"calradic_nobleman_warrior","calradic_knight")
upgrade(troops,"calradic_nobleman_archer","calradic_roaly_archer")

upgrade(troops,"askr_recruit","askr_hunter")
upgrade2(troops,"askr_hunter","askr_axeman","askr_skirmisher")
upgrade(troops,"askr_skirmisher","askr_archer")
upgrade(troops,"askr_archer","askr_veteran_archer")

upgrade(troops,"askr_axeman","askr_warrior")
upgrade(troops,"askr_warrior","askr_guard")
upgrade(troops,"askr_guard","askr_champion")

upgrade(troops,"askr_nobleman","askr_nobleman_warrior")
upgrade(troops,"askr_nobleman_warrior","askr_nobleman_knight")
#
upgrade(troops,"gulfod_citizen","gulfod_militia")
upgrade2(troops,"gulfod_militia","gulfod_footman","gulfod_militia_skirmisher")
upgrade(troops,"gulfod_footman","gulfod_soldier")
upgrade(troops,"gulfod_soldier","gulfod_heavy_soldier")

upgrade(troops,"gulfod_militia_skirmisher","gulfod_musketeer")
upgrade2(troops,"gulfod_musketeer","gulfod_veteran_musketeer","gulfod_musketeer_cavalry")

upgrade2(troops,"gulfod_nobleman","gulfod_nobleman_warrior","gulfod_nobleman_warrior1")
upgrade(troops,"gulfod_nobleman_warrior","gulfod_nobleman_knight")
upgrade(troops,"gulfod_nobleman_warrior1","gulfod_nobleman_knight1")
#
upgrade2(troops,"coleta_citizen","coleta_militia","coleta_crossbowman")
upgrade(troops,"coleta_militia","coleta_swordman")
upgrade(troops,"coleta_swordman","coleta_skilled_swordman")
upgrade(troops,"coleta_skilled_swordman","coleta_swordmaster")

upgrade(troops,"coleta_crossbowman","coleta_engineer")
upgrade(troops,"coleta_engineer","coleta_trained_engineer")
upgrade(troops,"coleta_trained_engineer","coleta_veteran_engineer")
upgrade(troops,"coleta_veteran_engineer","coleta_engineer_master")
upgrade2(troops,"coleta_engineer_master","coleta_royal_engineer","coleta_royal_mechanic")
#
upgrade(troops,"ciambia_slave","ciambia_slave_soldier")
upgrade2(troops,"ciambia_slave_soldier","ciambia_slave_soldier_1","ciambia_slave_skirmisher")
upgrade(troops,"ciambia_slave_soldier_1","ciambia_slave_soldier_2")
upgrade2(troops,"ciambia_slave_soldier_2","ciambia_slave_warrior","ciambia_gladiatus")
upgrade(troops,"ciambia_slave_warrior","ciambia_trained_soldier")
upgrade(troops,"ciambia_trained_soldier","ciambia_guard")

upgrade(troops,"ciambia_gladiatus","ciambia_veteran_gladiatus")
upgrade(troops,"ciambia_veteran_gladiatus","ciambia_gladiatus_champion")

upgrade(troops,"ciambia_slave_skirmisher","ciambia_archer")

upgrade2(troops,"ciambia_nobleman","ciambia_nobleman_hunter","ciambia_nobleman_watcher")
#
upgrade(troops,"turumia_recruit","turumia_militia")
upgrade(troops,"turumia_militia","turumia_soldier")
upgrade(troops,"turumia_soldier","turumia_trained_soldier")
upgrade(troops,"turumia_trained_soldier","turumia_cavalry")
upgrade(troops,"turumia_cavalry","turumia_elite_cavalry")
upgrade(troops,"turumia_elite_cavalry","turumia_man_at_arm")

upgrade(troops,"turumia_nobleman","turumia_squire")
upgrade(troops,"turumia_squire","turumia_knight")
upgrade2(troops,"turumia_knight","turumia_conquer_knight","turumia_guard_knight")
#
# upgrade(troops,"anar_lower","anar_footman")
# upgrade2(troops,"anar_footman","anar_soilder","anar_archer")
# upgrade(troops,"anar_soilder","anar_veteran_soilder")
# upgrade(troops,"anar_archer","anar_veteran_archer")

upgrade2(troops,"anar_nobleman","anar_silver_rider","anar_ranger")
upgrade(troops,"anar_silver_rider","anar_silver_knight")

upgrade(troops,"anar_ranger","anar_shadow_walker")
upgrade(troops,"anar_shadow_walker","anar_shadow_walker_master")

upgrade2(troops,"anar_fnobleman","anar_fnobleman_sword","anar_fnobleman_archer")
upgrade(troops,"anar_fnobleman_archer","anar_fnobleman_archer_e")
upgrade(troops,"anar_fnobleman_sword","anar_fnobleman_sword_e")

upgrade(troops,"anar_archer_knight","anar_archer_knight_e")
#
upgrade(troops,"looter","bandit")
upgrade(troops,"bandit","brigand")
upgrade(troops,"brigand","brigand_0")
upgrade(troops,"brigand_0","brigand_1")
upgrade(troops,"brigand_1","brigand_2")

upgrade(troops,"flooter","fbandit")
upgrade(troops,"fbandit","fbrigand")
upgrade(troops,"fbrigand","fbrigand_leader")
#new tree connections
upgrade(troops,"mountain_bandit","mountain_bandit_1")
upgrade(troops,"mountain_bandit_1","mountain_bandit_2")
upgrade(troops,"forest_bandit","forest_bandit_1")
upgrade(troops,"forest_bandit_1","forest_bandit_2")
upgrade(troops,"steppe_bandit","steppe_bandit_1")
upgrade(troops,"steppe_bandit_1","steppe_bandit_2")
upgrade(troops,"taiga_bandit","taiga_bandit_1")
upgrade(troops,"taiga_bandit_1","taiga_bandit_2")
upgrade(troops,"sea_raider","sea_raider_1")
upgrade(troops,"sea_raider_1","sea_raider_2")
upgrade(troops,"desert_bandit","desert_bandit_1")
upgrade(troops,"desert_bandit_1","desert_bandit_2")
upgrade(troops,"outlaw_squire","outlaw_knight")
upgrade(troops,"outlaw_knight","black_knight_1")
upgrade(troops,"brotherhood_member","brotherhood_marksman")
upgrade(troops,"black_khergit_horseman","black_khergit_horseman_leader")
upgrade(troops,"mafia4_member","mafia4_warrior")
upgrade(troops,"shadow_member","shadow_warrior")
upgrade(troops,"bloodlion_recuirt","bloodlion_member")
upgrade(troops,"bloodlion_member","bloodlion_killer")
upgrade(troops,"bloodlion_killer","bloodlion_capo")
#new tree connections ended
upgrade(troops,"manhunt_squire","manhunt_knight")
upgrade(troops,"manhunt_knight","manhunt_knight_b")

upgrade2(troops,"volunteer","city_guard","city_patroller")
upgrade(troops,"city_guard","city_guard_veteran")
upgrade(troops,"city_guard_veteran","city_elite_guard")
upgrade(troops,"city_elite_guard","city_guard_captain")

upgrade2(troops,"city_patroller","city_patroller_veteran","manhunter_0")

upgrade(troops,"city_patroller_veteran","constable")
upgrade(troops,"manhunter_0","manhunter")
upgrade(troops,"manhunter","manhunter_elite")

#upgrade(troops,"forest_bandit","mercenary_crossbowman")
# upgrade(troops,"slave_driver_0","slave_driver")

upgrade(troops,"slave_driver","slave_hunter")
upgrade(troops,"slave_hunter","slave_crusher")
upgrade(troops,"slave_crusher","slaver_chief")

upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")

upgrade2(troops,"fighter_woman","sword_sister","woman_crossbow")
upgrade(troops,"woman_crossbow","woman_crossbow_elite")
upgrade(troops,"sword_sister","war_sister")
upgrade2(troops,"war_sister","war_sister_elite","war_sister_horse")
upgrade(troops,"war_sister_horse","war_sister_knight")
# upgrade(troops,"refugee","follower_woman")
upgrade(troops,"peasant_woman","follower_woman")
#wabber
upgrade(troops,"pilgrim_of_wabbaer","wabbaer_follower")
upgrade(troops,"wabbaer_follower","wabbaer_worshiper")
upgrade(troops,"wabbaer_worshiper","wabbaer_grace_receiver")
#caprine
upgrade(troops,"caprine_hunter","caprine_senior_hunter")
upgrade(troops,"caprine_senior_hunter","caprine_archer")
upgrade(troops,"caprine_archer","caprine_marksman")
upgrade(troops,"caprine_marksman","caprine_wild_hunt_warrior")
upgrade(troops,"caprine_wild_hunt_warrior","caprine_wild_hunt_champion")
#
upgrade(troops,"khanjat_recruit","khanjat_horseman")
upgrade(troops,"khanjat_horseman","khanjat_warrior")
upgrade(troops,"khanjat_warrior","khanjat_champion")

upgrade(troops,"khanjat_guard_0","khanjat_guard")
upgrade(troops,"khanjat_guard","khanjat_guard_b")
#
upgrade(troops,"depravity_member","depravity_guard")
upgrade(troops,"depravity_member_f","depravity_guard_f")

upgrade(troops,"magic_apprentice","wizard")
upgrade(troops,"wizard","wizard_e")

upgrade(troops,"dark_apprentice","darkwizard")
upgrade(troops,"darkwizard","darkwizard_e")
#valkyrie
upgrade(troops,"nord_female","nord_female_hunter")
upgrade(troops,"nord_female_hunter","nord_female_warrior")
upgrade(troops,"nord_female_warrior","nord_war_sister")
upgrade(troops,"nord_war_sister","nord_valkyrie")
#springknight
upgrade(troops,"spring_pilgrim","spring_warrior")
upgrade(troops,"spring_warrior","spring_squire")
upgrade(troops,"spring_squire","spring_knight")
upgrade(troops,"spring_knight","spring_lake_guard")
#demonhunter
upgrade(troops,"demonhunterapprentice","demonhunter")
upgrade(troops,"demonhunter","demonhunterveteran")
upgrade(troops,"demonhunterveteran","demonhuntermaster")
#dragonknight
upgrade(troops,"dragonretinue","dragoncavalry")
upgrade(troops,"dragoncavalry","dragonknight")
upgrade(troops,"dragonknight","dragonknightleader")
#sevengod
upgrade(troops,"sevengod_pilgrim","sevengod_monk")
upgrade(troops,"sevengod_monk","sevengod_priest")
upgrade(troops,"sevengod_priest","sevengod_warrior")
upgrade2(troops,"sevengod_warrior","sevengod_elite_warrior","sevengod_knight")
upgrade(troops,"sevengod_elite_warrior","sevengod_elite_guard")
upgrade(troops,"sevengod_knight","sevengod_holy_knight")

upgrade(troops,"witch_hunter","witch_hunter_e")
upgrade(troops,"sevengod_pilgrim_a","sevengod_zealot")
#worshiper
upgrade(troops,"dark_pilgrim","dark_monk")
upgrade(troops,"dark_monk","dark_follower")
upgrade2(troops,"dark_follower","dark_warrior","dark_worshiper")
upgrade(troops,"dark_warrior","dark_elite_warrior")
upgrade2(troops,"dark_elite_warrior","dark_champion_warrior","dark_champion_warrior_1")
upgrade(troops,"dark_worshiper","dark_knight")
upgrade(troops,"dark_knight","dark_knight_champion")

upgrade(troops,"degenerate_nobleman","degenerate_squire")
upgrade(troops,"degenerate_squire","black_knight")
#demon
upgrade2(troops,"demon_slave","demon_warrior","demon_knight")
upgrade(troops,"demon_warrior","demon_high_warrior")
upgrade(troops,"demon_high_warrior","demon_lord")
upgrade(troops,"demon_knight","demon_elite_knight")
upgrade(troops,"demon_elite_knight","demon_lord")
upgrade(troops,"roskel_champion","roskel_champion_e")