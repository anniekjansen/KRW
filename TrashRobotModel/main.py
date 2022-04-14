from state_machine import StateMachine
import rules
from visualization import run_visualization
from queries import *


###### INPUT VALUES ######
MAX_T = 50
scenario = "scenario.txt"
StateMachine1 = StateMachine(scenario, MAX_T, rules.rules)
####### HELPER VARIABLES ######
object_position=get_coords_obj()
object_dimension=get_volume_obj()
bin1_position=get_coords_bin_1()
bin2_position=get_coords_bin_2()
bina_position=get_coords_bin_a()
bin1_v=get_volume_bin_1()
bin2_v=get_volume_bin_2()
bin1=get_uri_b1()
bin2=get_uri_b2()
binA=get_uri_ba()

StateMachine1.run()
run_visualization(StateMachine1, 'bar', [("inspection_tour", "http://www.trashrobot.com/onto/VURobot", "true" )], 11)

run_visualization(StateMachine1, 'bar', [("inspection_tour", "http://www.trashrobot.com/onto/VURobot", "true" ), ("observe_bin", "http://www.trashrobot.com/onto/VURobot", "true"),
                                         ("observe_object", "http://www.trashrobot.com/onto/VURobot", "true"), ("belief_object_position", "http://www.trashrobot.com/onto/trashObject11", object_position),
                                         ("belief_object_dimension", "http://www.trashrobot.com/onto/trashObject11", object_dimension),
                                         ("belief_specialized_bin_1_position", "http://www.trashrobot.com/onto/trashbin2", bin1_position),
                                         ("belief_specialized_bin_2_position", "http://www.trashrobot.com/onto/trashbin8", bin2_position),
                                         ("belief_all_in_bin_position", "http://www.trashrobot.com/onto/trashbin3", bina_position),
                                         ("belief_specialized_bin_1_volume", "http://www.trashrobot.com/onto/trashbin2", bin1_v),
                                         ("belief_specialized_bin_2_volume", "http://www.trashrobot.com/onto/trashbin8", bin2_v),
                                         ("decision_process", "http://www.trashrobot.com/onto/VURobot", "true"),
                                         ("belief_chosen_bin", "http://www.trashrobot.com/onto/VURobot", bin2),
                                         ("go_to_object_place", "http://www.trashrobot.com/onto/VURobot", "true"),
                                         ("pick_object", "http://www.trashrobot.com/onto/VURobot", "true"),("go_to_chosen_bin", "http://www.trashrobot.com/onto/VURobot", "true"),
                                         ("robot_trash_object", "http://www.trashrobot.com/onto/VURobot", "true")], 11)


run_visualization(StateMachine1, 'bar', [ ("belief_chosen_bin", "http://www.trashrobot.com/onto/VURobot", bin1),
                                          ("belief_chosen_bin", "http://www.trashrobot.com/onto/VURobot", bin2),
                                          ("belief_chosen_bin", "http://www.trashrobot.com/onto/VURobot", binA)
                                          ], 11)


