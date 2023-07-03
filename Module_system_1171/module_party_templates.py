from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,5,10),(trp_watchman,5,10),(trp_lost_knight,0,5)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Looters",icon_axeman|carries_goods(8)|pf_show_faction,0,fac_outlaws,bandit_personality,[(trp_looter,3,45)]),
# Ryan END
  ("manhunters","Manhunters",icon_gray_knight|pf_show_faction,0,fac_manhunters,soldier_personality,[(trp_manhunter,9,40),(trp_manhunter_elite,3,23)]),
  ("manhunt_knight","Manhunters",icon_gray_knight|pf_show_faction,0,fac_manhunters,soldier_personality,[(trp_manhunt_knight,1,10),(trp_manhunt_squire,3,25)]),
  ("woman_knight","woman_knight",icon_gray_knight|pf_show_faction,0,fac_manhunters,soldier_personality,[(trp_war_sister_knight,1,10),(trp_war_sister_horse,5,25),(trp_war_sister_elite,5,25),(trp_woman_crossbow_elite,5,25),(trp_sword_sister,5,25),(trp_woman_crossbow,5,25)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ("steppe_bandits","Steppe Bandits",icon_khergit|carries_goods(2)|pf_show_faction,0,fac_outlaws,bandit_personality,[(trp_steppe_bandit,4,58),(trp_steppe_bandit_1,2,10),(trp_steppe_bandit_2,1,5)]),
  ("taiga_bandits","Tundra Bandits",icon_axeman|carries_goods(2)|pf_show_faction,0,fac_outlaws,bandit_personality,[(trp_taiga_bandit,4,58),(trp_taiga_bandit_1,2,10),(trp_taiga_bandit_2,1,5)]),
  ("desert_bandits","Desert Bandits",icon_vaegir_knight|carries_goods(2)|pf_show_faction,0,fac_outlaws,bandit_personality,[(trp_desert_bandit,4,58),(trp_desert_bandit_1,2,10),(trp_desert_bandit_2,1,5)]),
  ("forest_bandits","Forest Bandits",icon_axeman|carries_goods(2)|pf_show_faction,0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,4,52),(trp_forest_bandit_1,2,10),(trp_forest_bandit_2,1,5)]),
  ("mountain_bandits","Mountain Bandits",icon_axeman|carries_goods(2)|pf_show_faction,0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit,4,60),(trp_mountain_bandit_1,2,10),(trp_mountain_bandit_2,1,5)]),
  ("sea_raiders","Sea Raiders",icon_axeman|carries_goods(2)|pf_show_faction,0,fac_outlaws,bandit_personality,[(trp_sea_raider,5,50),(trp_sea_raider_1,2,10),(trp_sea_raider_2,1,5)]),

  ("deserters","Deserters",icon_vaegir_knight|carries_goods(3)|pf_show_faction,0,fac_deserters,bandit_personality,[]),
  ("outlaw_knight","Outlaw Knights",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_outlaws,bandit_personality,[(trp_outlaw_knight,1,10),(trp_outlaw_squire,3,25),(trp_volunteer,0,5,pmf_is_prisoner)]),
  ("lootergroup","Outlaw Knights",icon_axeman|carries_goods(5)|pf_show_faction,0,fac_outlaws,bandit_personality,[(trp_looter,10,15),(trp_bandit,10,15),(trp_brigand,5,10),(trp_brigand_0,5,10),(trp_brigand_1,5,10),(trp_brigand_2,1,5)]),

#new template
#random
  ("wild_hunt_hunter","wild_hunt_hunter",icon_axeman|pf_show_faction,0,fac_caprine,bandit_personality,[(trp_caprine_wild_hunt_warrior,75,150)]),
  ("wild_hunt_prey","wild_hunt_prey",icon_gray_knight|pf_show_faction,0,fac_caprine_prey,bandit_personality,[(trp_caprine_dead_wild_hunt_warrior,55,105)]),
#hero army
  ("quest_party","quest_party",icon_axeman|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("random_party","random_party",icon_vaegir_knight|carries_goods(3)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("hero_army","hero_army",icon_army|pf_show_faction,0,fac_commoners,soldier_personality,[]),
  ("random_hero_army","random_hero_army",icon_army|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#mafia dontchangeorder
  ("mafia1","mafia1",icon_khergit,0,fac_mafia1|pf_show_faction,bandit_personality,[(trp_black_khergit_horseman,10,30),(trp_black_khergit_horseman_leader,5,15)]),
  ("brotherhood","brotherhood",icon_axeman|pf_show_faction,0,fac_mafia2,bandit_personality,[(trp_brotherhood_member,10,30),(trp_brotherhood_marksman,5,15)]),
  ("mafia3","mafia3",icon_vaegir_knight|pf_show_faction,0,fac_mafia3,bandit_personality,[(trp_shadow_member,10,30),(trp_shadow_warrior,5,15)]),
  ("mafia4","mafia4",icon_axeman|pf_show_faction,0,fac_mafia4,bandit_personality,[(trp_mafia4_member,10,30),(trp_mafia4_warrior,5,15)]),
  ("mafia5","mafia5",icon_gray_knight|pf_show_faction,0,fac_mafia5,bandit_personality,[(trp_slave_driver,10,30),(trp_slave_hunter,5,15),(trp_slave_crusher,5,15),(trp_slaver_chief,1,5)]),
  ("mafia6","mafia6",icon_axeman|pf_show_faction,0,fac_mafia6,bandit_personality,[(trp_bloodlion_recuirt,10,30),(trp_bloodlion_member,5,15),(trp_bloodlion_killer,5,15),(trp_bloodlion_capo,1,5)]),
#mafia end
  ("wabber_group","wabber_group",icon_axeman|pf_show_faction,0,fac_wabber,bandit_personality,[(trp_phantom_of_wabbaer,1,5),(trp_wabbaer_grace_receiver,5,10),(trp_wabbaer_worshiper,7,12),(trp_wabbaer_follower,15,30),(trp_pilgrim_of_wabbaer,15,30)]),
  ("brotherhood_hunter","brotherhood_hunter",icon_gray_knight|pf_show_faction,0,fac_manhunters,soldier_personality,[(trp_swadian_horse_archer,15,30)]),

  ("nord_valkyrie","nord_valkyrie",icon_axeman|pf_show_faction,0,fac_ortlinde,soldier_personality,[(trp_nord_valkyrie,5,10)]),
  ("nord_valkyrie_hunter","nord_valkyrie_hunter",icon_axeman|pf_show_faction,0,fac_ortlinde,soldier_personality,[(trp_nord_valkyrie,1,5),(trp_nord_war_sister,3,8),(trp_nord_female_warrior,5,10),(trp_nord_female_hunter,5,10)]),
  ("spring_lake_guard","spring_lake_guard",icon_gray_knight|pf_show_faction,0,fac_spring_knight,soldier_personality,[(trp_spring_lake_guard,10,20)]),
  ("spring_knight","spring_knight",icon_gray_knight|pf_show_faction,0,fac_spring_knight,soldier_personality,[(trp_spring_knight,1,5),(trp_spring_squire,4,13),(trp_spring_warrior,7,21)]),
  #rebel nobleman
  ("swadian_shameless_adventurer","swadian_shameless_adventurer",icon_gray_knight|carries_goods(3)|pf_show_faction,0,fac_shameless_adventurer,bandit_personality,[(trp_swadian_knight_n,5,15),(trp_swadian_sword_master,5,15),(trp_swadian_horse_archer,5,15),(trp_swadian_squire,10,25),(trp_swadian_nobleman,10,25)]),
  ("vaegir_shameless_adventurer","vaegir_shameless_adventurer",icon_vaegir_knight|carries_goods(3)|pf_show_faction,0,fac_shameless_adventurer,bandit_personality,[(trp_vaegir_noble_knight,5,15),(trp_vaegir_snow_patroler,5,15),(trp_vaegir_snow_sister,5,15),(trp_vaegir_axe_warrior,5,15),(trp_vaegir_holy_warrior,5,15),(trp_vaegir_nobleman,10,25)]),
  ("khergit_shameless_adventurer","khergit_shameless_adventurer",icon_khergit|carries_goods(3)|pf_show_faction,0,fac_shameless_adventurer,bandit_personality,[(trp_khergit_nobleman_horse_archer,5,15),(trp_khergit_nobleman_knight,5,15),(trp_khergit_iron_knight,5,15),(trp_khergit_nobleman_warrior,10,25),(trp_khergit_nobleman,10,25)]),
  ("nord_shameless_adventurer","nord_shameless_adventurer",icon_gray_knight|carries_goods(3)|pf_show_faction,0,fac_shameless_adventurer,bandit_personality,[(trp_nord_nobleman_champion_horse,5,15),(trp_nord_axe_warrior,5,15),(trp_nord_fians,5,15),(trp_nord_nobleman_warrior,10,25),(trp_nord_nobleman,10,25)]),
  ("rhodok_shameless_adventurer","rhodok_shameless_adventurer",icon_gray_knight|carries_goods(3)|pf_show_faction,0,fac_shameless_adventurer,bandit_personality,[(trp_rhodok_knight,5,15),(trp_rhodok_walk_knight,5,15),(trp_rhodok_elite_knight,5,15),(trp_rhodok_shooter,5,15),(trp_rhodok_hunter,5,15),(trp_rhodok_nobleman,10,25)]),
  ("sarranid_shameless_adventurer","sarranid_shameless_adventurer",icon_gray_knight|carries_goods(3)|pf_show_faction,0,fac_shameless_adventurer,bandit_personality,[(trp_sarranid_nobleman_knight,5,15),(trp_sarranid_nobleman_knight_archor,5,15),(trp_sarranid_camel_warrior,5,15),(trp_sarranid_desert_archer,5,15),(trp_sarranid_ghazis_warrior,5,15),(trp_sarranid_nobleman,10,25)]),
  ("calradic_shameless_adventurer","calradic_shameless_adventurer",icon_gray_knight|carries_goods(3)|pf_show_faction,0,fac_shameless_adventurer,bandit_personality,[(trp_calradic_knight,5,15),(trp_calradic_roaly_archer,5,15),(trp_calradic_nobleman_archer,5,25),(trp_calradic_nobleman_warrior,5,25),(trp_calradic_veteran_archer,10,25),(trp_calradic_nobleman,10,25)]),
  ("regular_shameless_adventurer","regular_shameless_adventurer",icon_gray_knight|carries_goods(3)|pf_show_faction,0,fac_shameless_adventurer,bandit_personality,[(trp_mercenary_knight,5,15),(trp_lost_knight,5,15),(trp_mercenary_crossbowman_2,5,25),(trp_mercenary_cavalry,5,25),(trp_hired_blade,10,25),(trp_mercenary_noleman,10,25)]),
#adventurer#swadian=shameless end
  ("swadian_adventurer","swadian_adventurer",icon_gray_knight|pf_show_faction,0,fac_kingdom_1,soldier_personality,[(trp_swadian_knight_n,1,10),(trp_swadian_squire,5,25),(trp_swadian_knight,5,25),(trp_swadian_sharpshooter,5,25),(trp_swadian_sergeant,5,25),(trp_swadian_nobleman,5,25)]),
  ("vaegir_adventurer","vaegir_adventurer",icon_vaegir_knight|pf_show_faction,0,fac_kingdom_2,soldier_personality,[(trp_vaegir_noble_knight,1,10),(trp_vaegir_holy_warrior,1,10),(trp_vaegir_noble_warrior,5,25),(trp_vaegir_nobleman,5,25),(trp_vaegir_guard,5,25),(trp_vaegir_marksman,5,25)]),
  ("khergit_adventurer","khergit_adventurer",icon_khergit|pf_show_faction,0,fac_kingdom_3,soldier_personality,[(trp_khergit_nobleman_knight,1,10),(trp_khergit_nobleman_horse_archer,1,10),(trp_khergit_veteran_horse_archer,5,25),(trp_khergit_nobleman_warrior,5,25),(trp_khergit_nobleman,5,25),(trp_khergit_lancer,5,25)]),
  ("nord_adventurer","nord_adventurer",icon_gray_knight|pf_show_faction,0,fac_kingdom_4,soldier_personality,[(trp_nord_nobleman_champion_horse,1,10),(trp_nord_nobleman_warrior,5,25),(trp_nord_nobleman,5,25),(trp_nord_veteran_archer,5,25),(trp_nord_archer_2,5,25),(trp_nord_champion,5,25)]),
  ("rhodok_adventurer","rhodok_adventurer",icon_gray_knight|pf_show_faction,0,fac_kingdom_5,soldier_personality,[(trp_rhodok_knight,1,10),(trp_rhodok_walk_knight,1,12),(trp_rhodok_squire,5,25),(trp_rhodok_nobleman,5,25),(trp_rhodok_sharpshooter,5,25),(trp_rhodok_sergeant,5,25)]),
  ("sarranid_adventurer","sarranid_adventurer",icon_gray_knight|pf_show_faction,0,fac_kingdom_6,soldier_personality,[(trp_sarranid_nobleman_knight,1,10),(trp_sarranid_nobleman_knight_archor,1,10),(trp_sarranid_nobleman_warrior,5,25),(trp_sarranid_nobleman,5,25),(trp_sarranid_mamluke,5,25),(trp_sarranid_master_archer,5,25)]),
  ("calradic_adventurer","calradic_adventurer",icon_gray_knight|pf_show_faction,0,fac_kingdom_7,soldier_personality,[(trp_calradic_knight,1,10),(trp_calradic_roaly_archer,1,10),(trp_calradic_nobleman_warrior,5,25),(trp_calradic_nobleman_archer,5,25),(trp_calradic_veteran_archer,5,25),(trp_calradic_legionary,5,25)]),
#regular just seven one end=gulfod
  ("gulfod_army","gulfod_army",icon_gray_knight|pf_show_faction,0,fac_gulfod_theocracy,soldier_personality,[(trp_gulfod_nobleman_knight,1,10),(trp_gulfod_veteran_musketeer,5,25),(trp_gulfod_musketeer_cavalry,5,25),(trp_gulfod_heavy_soldier,5,25),(trp_gulfod_musketeer,5,25),(trp_gulfod_soldier,5,25)]),
  ("askr_army","askr_army",icon_gray_knight|pf_show_faction,0,fac_askr,soldier_personality,[(trp_askr_nobleman_knight,1,10),(trp_askr_nobleman_warrior,5,25),(trp_askr_champion,5,25),(trp_askr_veteran_archer,5,25),(trp_askr_guard,5,25),(trp_askr_archer,5,25)]),
#end
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),
  ("sea_raider_leader","sea raider groups",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,merchant_personality,[(trp_baldersvold,1,1),(trp_sea_raider_2,8,12),(trp_sea_raider_1,21,24),(trp_sea_raider,30,32)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),

# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
  ("patrol_party","patrol party",icon_gray_knight|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  ("guard_party","guard party",icon_gray_knight|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total
  # modding:less(12-24),med(8-16),high(6-12)
  ("reinforcements_for_all_center", "{!}reinforcements_for_all_center", 0, 0, fac_commoners, 0, [(trp_volunteer,10,25),(trp_city_guard,10,25),(trp_city_guard_veteran,10,25),(trp_city_elite_guard,10,25)]),

  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_recruit,5,10),(trp_swadian_militia,5,10),(trp_swadian_nobleman,2,4),(trp_swadian_flag_holder,1,2)]),
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,6),(trp_swadian_skirmisher,3,6),(trp_swadian_nobleman,2,4),(trp_swadian_flag_holder,1,2)]),
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,3,6),(trp_swadian_crossbowman,1,3),(trp_swadian_squire,2,4),(trp_swadian_flag_holder,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)

  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_recruit,5,10),(trp_vaegir_footman,5,10),(trp_vaegir_nobleman,2,4),(trp_vaegir_flag_holder,1,2)]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,2,4),(trp_vaegir_skirmisher,3,6),(trp_vaegir_footman,1,2),(trp_vaegir_nobleman,2,4),(trp_vaegir_flag_holder,1,2)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,3,5),(trp_vaegir_infantry,1,3),(trp_vaegir_noble_warrior,1,2),(trp_vaegir_noble_warrior,2,4),(trp_vaegir_flag_holder,1,2)]),

  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_tribesman,5,10),(trp_khergit_skirmisher,5,10),(trp_khergit_nobleman,2,4),(trp_khergit_flag_holder,1,2)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_horse_archer,3,6),(trp_khergit_skirmisher,1,2),(trp_khergit_nobleman,2,4),(trp_khergit_flag_holder,1,2)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horseman,3,6),(trp_khergit_veteran_horse_archer,1,3),(trp_khergit_nobleman_warrior,2,4),(trp_khergit_flag_holder,1,2)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_footman,5,10),(trp_nord_recruit,5,10),(trp_nord_nobleman,2,4),(trp_nord_flag_holder,1,2)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_huntsman,2,5),(trp_nord_archer,3,5),(trp_nord_archer_1,1,2),(trp_nord_nobleman,2,4),(trp_nord_flag_holder,1,2)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_warrior,3,6),(trp_nord_archer_2,1,2),(trp_nord_nobleman_warrior,2,4),(trp_nord_flag_holder,1,2)]),

  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_tribesman,5,10),(trp_rhodok_spearman,5,10),(trp_rhodok_nobleman,2,4),(trp_rhodok_flag_holder,1,2)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_crossbowman,3,6),(trp_rhodok_trained_crossbowman,2,4),(trp_rhodok_trained_horseman,1,2),(trp_rhodok_nobleman,2,4),(trp_rhodok_flag_holder,1,2)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_veteran_spearman,2,4),(trp_rhodok_veteran_crossbowman,2,4),(trp_rhodok_squire,2,4),(trp_rhodok_flag_holder,1,2)]), 

  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sarranid_recruit,5,10),(trp_sarranid_footman,5,10),(trp_sarranid_nobleman,2,4),(trp_sarranid_flag_holder,1,2)]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarranid_skirmisher,3,6),(trp_sarranid_veteran_footman,2,3),(trp_sarranid_footman,1,3),(trp_sarranid_nobleman,2,4),(trp_sarranid_flag_holder,1,2)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_horseman,4,8),(trp_sarranid_nobleman_warrior,2,4),(trp_sarranid_flag_holder,1,2)]),

  ("culture_7_reinforcements_a", "{!}culture_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_calradic_recruit,5,10),(trp_calradic_footman,5,10),(trp_calradic_nobleman,2,4)]),
  ("culture_7_reinforcements_b", "{!}culture_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_calradic_skirmisher,3,6),(trp_calradic_trained_footman,2,3),(trp_calradic_heavy_infantry,1,3),(trp_calradic_nobleman,2,4)]),
  ("culture_7_reinforcements_c", "{!}culture_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_calradic_horseman,4,8),(trp_calradic_nobleman_warrior,2,4)]),

  ("culture_8_reinforcements_a", "{!}culture_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_farmer,5,10),(trp_watchman,5,10),(trp_mercenary_noleman,2,4)]),
  ("culture_8_reinforcements_b", "{!}culture_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_mercenary_crossbowman,3,6),(trp_caravan_guard,2,3),(trp_mercenary_swordsman,1,3),(trp_mercenary_noleman,2,4)]),
  ("culture_8_reinforcements_c", "{!}culture_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_mercenary_horseman,2,4),(trp_mercenary_crossbowman_1,2,4),(trp_mercenary_squire,2,4)]),
  
  ("culture_9_reinforcements_a", "{!}culture_9_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_askr_recruit,5,10),(trp_askr_axeman,5,10),(trp_askr_nobleman,2,4)]),
  ("culture_9_reinforcements_b", "{!}culture_9_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_askr_hunter,3,6),(trp_askr_warrior,2,3),(trp_askr_guard,1,3),(trp_askr_nobleman,2,4)]),
  ("culture_9_reinforcements_c", "{!}culture_9_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_askr_archer,2,4),(trp_askr_guard,2,4),(trp_askr_nobleman_warrior,2,4)]),

  ("culture_10_reinforcements_a", "{!}culture_10_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_gulfod_citizen,5,10),(trp_gulfod_militia,5,10),(trp_gulfod_nobleman,2,4)]),
  ("culture_10_reinforcements_b", "{!}culture_10_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_gulfod_militia_skirmisher,3,6),(trp_gulfod_footman,2,3),(trp_gulfod_soldier,1,3),(trp_gulfod_nobleman,2,4)]),
  ("culture_10_reinforcements_c", "{!}culture_10_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_gulfod_musketeer,2,4),(trp_gulfod_soldier,2,4),(trp_gulfod_nobleman_warrior,1,2),(trp_gulfod_nobleman_warrior1,1,2)]),

  ("culture_11_reinforcements_a", "{!}culture_11_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_ciambia_slave,5,10),(trp_ciambia_slave_soldier,5,10),(trp_ciambia_slave_soldier_1,1,2),(trp_ciambia_nobleman,2,4)]),#have more
  ("culture_11_reinforcements_b", "{!}culture_11_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_ciambia_slave_skirmisher,3,6),(trp_ciambia_slave_soldier_2,2,3),(trp_ciambia_slave_warrior,1,3),(trp_ciambia_nobleman,2,4)]),
  ("culture_11_reinforcements_c", "{!}culture_11_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_ciambia_gladiatus,2,4),(trp_ciambia_archer,2,4),(trp_ciambia_nobleman_hunter,1,2),(trp_ciambia_nobleman_watcher,1,2)]),

  ("culture_12_reinforcements_a", "{!}culture_12_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_turumia_recruit,5,10),(trp_turumia_militia,5,10),(trp_turumia_nobleman,2,4)]),
  ("culture_12_reinforcements_b", "{!}culture_12_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_turumia_soldier,3,6),(trp_turumia_trained_soldier,3,6),(trp_turumia_nobleman,2,4)]),
  ("culture_12_reinforcements_c", "{!}culture_12_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_turumia_cavalry,2,4),(trp_turumia_trained_soldier,2,4),(trp_turumia_squire,2,4)]),

  ("culture_13_reinforcements_a", "{!}culture_13_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_dark_pilgrim,5,10),(trp_dark_monk,5,10),(trp_degenerate_nobleman,2,4)]),
  ("culture_13_reinforcements_b", "{!}culture_13_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_dark_follower,3,6),(trp_dark_warrior,3,6),(trp_degenerate_nobleman,2,4)]),
  ("culture_13_reinforcements_c", "{!}culture_13_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_dark_worshiper,2,4),(trp_dark_elite_warrior,2,4),(trp_degenerate_squire,2,4)]),

  ("culture_14_reinforcements_a", "{!}culture_14_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_pilgrim_of_wabbaer,5,10),(trp_wabbaer_follower,5,10),(trp_wabbaer_worshiper,2,4)]),
  ("culture_14_reinforcements_b", "{!}culture_14_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_wabbaer_follower,3,6),(trp_wabbaer_worshiper,3,6),(trp_phantom_of_wabbaer,1,2)]),
  ("culture_14_reinforcements_c", "{!}culture_14_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_wabbaer_worshiper,3,6),(trp_wabbaer_grace_receiver,2,4),(trp_phantom_of_wabbaer,1,2)]),

  ("culture_15_reinforcements_a", "{!}culture_15_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_farmer,5,10),(trp_watchman,5,10),(trp_anar_nobleman,1,2),(trp_anar_fnobleman,1,2)]),
  ("culture_15_reinforcements_b", "{!}culture_15_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_mercenary_crossbowman,2,4),(trp_caravan_guard,1,2),(trp_mercenary_swordsman,2,4),(trp_anar_fnobleman,1,2),(trp_anar_nobleman,1,2)]),
  ("culture_15_reinforcements_c", "{!}culture_15_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_mercenary_horseman,2,4),(trp_mercenary_crossbowman_1,2,4),(trp_anar_fnobleman_sword,1,2),(trp_anar_ranger,1,2)]),

  ("kingdom_1_personal_reinforcements", "{!}kingdom_1_personal_reinforcements", 0, 0, fac_commoners, 0, [(trp_swadian_knight_n,3,6)]),#kingdom1
  ("kingdom_2_personal_reinforcements", "{!}kingdom_2_personal_reinforcements", 0, 0, fac_commoners, 0, [(trp_vaegir_holy_warrior,3,6)]),#kingdom2
  ("kingdom_3_personal_reinforcements", "{!}kingdom_3_personal_reinforcements", 0, 0, fac_commoners, 0, [(trp_khergit_nobleman_horse_archer,3,6)]),#kingdom3
  ("kingdom_4_personal_reinforcements", "{!}kingdom_4_personal_reinforcements", 0, 0, fac_commoners, 0, [(trp_nord_nobleman_champion_horse,3,6)]),#kingdom4
  ("kingdom_5_personal_reinforcements", "{!}kingdom_5_personal_reinforcements", 0, 0, fac_commoners, 0, [(trp_rhodok_knight,3,6)]),#kingdom5
  ("kingdom_6_personal_reinforcements", "{!}kingdom_6_personal_reinforcements", 0, 0, fac_commoners, 0, [(trp_sarranid_nobleman_knight_archor,3,6)]),#kingdom6
  ("kingdom_7_personal_reinforcements", "{!}kingdom_7_personal_reinforcements", 0, 0, fac_commoners, 0, [(trp_calradic_roaly_archer,3,6)]),#kingdom7
  ("kingdom_8_personal_reinforcements", "{!}kingdom_8_personal_reinforcements", 0, 0, fac_commoners, 0, [(trp_anar_shadow_walker_master,2,3)]),#kingdom8

  ("anar_f_personal_reinforcements_a", "{!}anar_f_personal_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_anar_sword_dancer2,1,1),(trp_anar_sword_dancer3,1,1)]),
  ("anar_f_personal_reinforcements_c", "{!}anar_f_personal_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_anar_sword_dancer,1,1),(trp_anar_sword_dancer1,1,1)]),#kingdoms_end
  ("anar_f_personal_reinforcements_b", "{!}anar_f_personal_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_anar_fnobleman_archer,1,2),(trp_anar_fnobleman_sword,1,2),(trp_anar_fnobleman,2,4)]),

  ("manhunter_personal_reinforcements_a", "{!}manhunter_personal_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_volunteer,6,10),(trp_city_guard,4,10),(trp_city_patroller,2,4)]),
  ("manhunter_personal_reinforcements_c", "{!}manhunter_personal_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_city_guard_veteran,3,6),(trp_manhunter_0,3,6),(trp_city_patroller_veteran,2,4)]),#manhunter
  ("manhunter_personal_reinforcements_b", "{!}manhunter_personal_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_city_elite_guard,2,4),(trp_manhunter,2,4),(trp_manhunt_squire,2,4)]),
  
##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,7),(trp_swadian_skirmisher,5,10),(trp_swadian_militia,11,26)]),
##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,5,10),(trp_swadian_infantry,5,10),(trp_swadian_crossbowman,3,8)]),
##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight,2,6),(trp_swadian_sergeant,2,5),(trp_swadian_sharpshooter,2,5)]),
##
##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,3,7),(trp_vaegir_skirmisher,5,10),(trp_vaegir_footman,11,26)]),
##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,4,9),(trp_vaegir_infantry,5,10),(trp_vaegir_archer,3,8)]),
##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_knight,3,7),(trp_vaegir_guard,2,5),(trp_vaegir_marksman,2,5)]),
##
##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,3,7),(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,11,26)]),
##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer,4,9),(trp_khergit_horse_archer,5,10),(trp_khergit_horseman,3,8)]),
##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,3,7),(trp_khergit_veteran_horse_archer,2,5),(trp_khergit_horse_archer,2,5)]),
##
##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_nord_footman,5,10),(trp_nord_recruit,11,26)]),
##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_veteran,4,9),(trp_nord_warrior,5,10),(trp_nord_footman,3,8)]),
##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,3),(trp_nord_veteran,2,5),(trp_nord_warrior,2,5)]),
##
##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,3,7),(trp_rhodok_crossbowman,5,10),(trp_rhodok_tribesman,11,26)]),
##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,9),(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,3,8)]),
##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,7),(trp_rhodok_veteran_spearman,2,5),(trp_rhodok_veteran_crossbowman,2,5)]),



  ("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58),(trp_steppe_bandit_1,10,30),(trp_steppe_bandit_2,5,10)]),
  ("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58),(trp_taiga_bandit_1,10,30),(trp_taiga_bandit_2,5,10)]),
  ("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58),(trp_desert_bandit_1,10,30),(trp_desert_bandit_2,5,10)]),
  ("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58),(trp_forest_bandit_1,10,30),(trp_forest_bandit_2,5,10)]),
  ("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58),(trp_mountain_bandit_1,10,30),(trp_mountain_bandit_2,5,10)]),
  ("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50),(trp_sea_raider_1,10,30),(trp_sea_raider_2,5,10)]),
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),

  #########################for test
  #  ("new_template","new_template",icon_peasant|pf_civilian,0,fac_outlaws,soldier_personality,[(trp_npc17,1,1),(trp_new_troop,3,12)]),
]
