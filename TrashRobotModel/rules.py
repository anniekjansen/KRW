from state import Predicate
from queries import *

#######################################
# Parameters
TAKEN_VOLUME_B1 = 0.3
TAKEN_VOLUME_B2 = 1

#######################################
#Functions that formalize the rules for concepts
counter1=0
counter2=0
counter3=0

def inspection_tour(states, t):
    pass


def observe_bin(states, t):
    global counter2
    previous_state = states[t - 1]
    new_predicates = []

    for predicate in previous_state.get_predicate("inspection_tour"):
        uri = predicate.agents[0]
        inspection_bool = predicate.value
        if inspection_bool=="true":
            counter2+=1
        if counter2==0:
            new_predicates.append(Predicate([uri], inspection_bool))
        else:
            new_predicates.append(Predicate([uri], "true"))

    states[t].add_predicate_to_state("observe_bin", new_predicates)

def observe_object(states, t):
    global counter3
    previous_state = states[t - 1]
    new_predicates = []

    for predicate in previous_state.get_predicate("inspection_tour"):
        uri = predicate.agents[0]
        inspection_bool = predicate.value
        if inspection_bool == "true":
            counter3 += 1
        if counter3 == 0:
            new_predicates.append(Predicate([uri], inspection_bool))
        else:
            new_predicates.append(Predicate([uri], "true"))

    states[t].add_predicate_to_state("observe_object", new_predicates)

def belief_object_position(states, t):
    previous_state = states[t - 1]
    new_predicates = []

    for predicate in previous_state.get_predicate("observe_object"):
        uri = get_uri_obj()
        if predicate.value == "true":
            coords = get_coords_obj()
            new_predicates.append(Predicate([uri], coords))
        else:
            new_predicates.append(Predicate([uri], "none"))

    states[t].add_predicate_to_state("belief_object_position", new_predicates)

def belief_object_dimension(states, t):
    previous_state = states[t - 1]
    new_predicates = []

    for predicate in previous_state.get_predicate("observe_object"):
        uri = get_uri_obj()
        if predicate.value == "true":
            coords = get_volume_obj()
            new_predicates.append(Predicate([uri], coords))
        else:
            new_predicates.append(Predicate([uri], "none"))

    states[t].add_predicate_to_state("belief_object_dimension", new_predicates)


def belief_specialized_bin_1_position(states, t):
    previous_state = states[t - 1]
    new_predicates = []

    for predicate in previous_state.get_predicate("observe_bin"):
        uri = get_uri_b1()
        if predicate.value == "true":
            coords = get_coords_bin_1()
            new_predicates.append(Predicate([uri], coords))
        else:
            new_predicates.append(Predicate([uri], "none"))

    states[t].add_predicate_to_state("belief_specialized_bin_1_position", new_predicates)

def belief_specialized_bin_2_position(states, t):
    previous_state = states[t - 1]
    new_predicates = []

    for predicate in previous_state.get_predicate("observe_bin"):
        uri = get_uri_b2()
        if predicate.value == "true":
            coords = get_coords_bin_2()
            new_predicates.append(Predicate([uri], coords))
        else:
            new_predicates.append(Predicate([uri], "none"))

    states[t].add_predicate_to_state("belief_specialized_bin_2_position", new_predicates)

def belief_all_in_bin_position(states, t):
    previous_state = states[t - 1]
    new_predicates = []

    for predicate in previous_state.get_predicate("observe_bin"):
        uri = get_uri_ba()
        if predicate.value == "true":
            coords = get_coords_bin_a()
            new_predicates.append(Predicate([uri], coords))
        else:
            new_predicates.append(Predicate([uri], "none"))

    states[t].add_predicate_to_state("belief_all_in_bin_position", new_predicates)

def belief_specialized_bin_1_volume(states, t):
    previous_state = states[t - 1]
    new_predicates = []

    for predicate in previous_state.get_predicate("observe_bin"):
        uri = get_uri_b1()
        if predicate.value == "true":
            vol = get_volume_bin_1()
            new_predicates.append(Predicate([uri], vol))
        else:
            new_predicates.append(Predicate([uri], "none"))

    states[t].add_predicate_to_state("belief_specialized_bin_1_volume", new_predicates)


def belief_specialized_bin_2_volume(states, t):
    previous_state = states[t - 1]
    new_predicates = []

    for predicate in previous_state.get_predicate("observe_bin"):
        uri = get_uri_b2()
        if predicate.value == "true":
            vol = get_volume_bin_2()
            new_predicates.append(Predicate([uri], vol))
        else:
            new_predicates.append(Predicate([uri], "none"))

    states[t].add_predicate_to_state("belief_specialized_bin_2_volume", new_predicates)

def decision_process(states, t):
    previous_state = states[t - 1]
    new_predicates = []
    uri=get_uri_robot()
    for bin in previous_state.get_predicate("observe_bin"):
        bin_value=bin.value
        for object in previous_state.get_predicate("observe_object"):
            object_value=bin.value
            if object_value=="true" and bin_value=="true":
                dec_value=object_value
            else:
                dec_value = object_value
            new_predicates.append(Predicate([uri], dec_value))
    states[t].add_predicate_to_state("decision_process", new_predicates)

def belief_chosen_bin(states, t):
    global TAKEN_VOLUME_B1, TAKEN_VOLUME_B2
    previous_state = states[t - 1]
    new_predicates = []
    uri_r = get_uri_robot()
    for decision in previous_state.get_predicate("decision_process"):
        for obdim in previous_state.get_predicate("belief_object_dimension"):
            for obpos in previous_state.get_predicate("belief_object_position"):
                for b1v in previous_state.get_predicate("belief_specialized_bin_1_volume"):
                    for b2v in previous_state.get_predicate("belief_specialized_bin_2_volume"):
                        for b1p in previous_state.get_predicate("belief_specialized_bin_1_position"):
                            for b2p in previous_state.get_predicate("belief_specialized_bin_2_position"):
                                for bap in previous_state.get_predicate("belief_all_in_bin_position"):
                                    #print(decision.value, obdim.value, obpos.value, b1v.value, b2v.value, b1p.value, b2p.value, bap.value)
                                    if decision.value=="false" or obdim.value=="none" or obpos.value=="none" or b1v.value=="none" or b2v.value=="none" or b1p.value=="none" or b2p.value=="none"or bap.value=="none":
                                        new_predicates.append(Predicate([uri_r], "none"))
                                        print(1)
                                    elif (bap.value[0]-obpos.value[0])**2+(bap.value[1]-obpos.value[1])**2<(b1p.value[0]-obpos.value[0])**2+(b1p.value[1]-obpos.value[1])**2 and (bap.value[0]-obpos.value[0])**2+(bap.value[1]-obpos.value[1])**2<(b2p.value[0]-obpos.value[0])**2+(b2p.value[1]-obpos.value[1])**2:
                                        chosen = get_uri_ba()
                                        new_predicates.append(Predicate([uri_r], chosen))
                                        print(2)
                                    elif obdim.value>(abs(TAKEN_VOLUME_B1-b1v.value)) and obdim.value>(abs(TAKEN_VOLUME_B2-b2v.value)):
                                        chosen=get_uri_ba()
                                        new_predicates.append(Predicate([uri_r], chosen))
                                        print(3)
                                    elif obdim.value > (abs(TAKEN_VOLUME_B1 - b1v.value)) and obdim.value < (abs(TAKEN_VOLUME_B2 - b2v.value)):
                                        chosen = get_uri_b2()
                                        new_predicates.append(Predicate([uri_r], chosen))
                                        print(4)
                                    elif obdim.value < (abs(TAKEN_VOLUME_B1 - b1v.value)) and obdim.value > (abs(TAKEN_VOLUME_B2 - b2v.value)):
                                        chosen = get_uri_b1()
                                        new_predicates.append(Predicate([uri_r], chosen))
                                        print(5)
                                    elif obdim.value <= (abs(TAKEN_VOLUME_B1 - b1v.value)) and obdim.value <= (abs(TAKEN_VOLUME_B2 - b2v.value)):
                                        if (bap.value[0]-obpos.value[0])**2+(bap.value[1]-obpos.value[1])**2<(b1p.value[0]-obpos.value[0])**2+(b1p.value[1]-obpos.value[1])**2 and (bap.value[0]-obpos.value[0])**2+(bap.value[1]-obpos.value[1])**2<(b2p.value[0]-obpos.value[0])**2+(b2p.value[1]-obpos.value[1])**2:
                                            chosen = get_uri_ba()
                                            new_predicates.append(Predicate([uri_r], chosen))
                                            print(6)
                                        elif (b1p.value[0]-obpos.value[0])**2+(b1p.value[1]-obpos.value[1])**2<(b2p.value[0]-obpos.value[0])**2+(b2p.value[1]-obpos.value[1])**2:
                                            chosen = get_uri_b1()
                                            new_predicates.append(Predicate([uri_r], chosen))
                                            print(7)
                                        else:
                                            chosen = get_uri_b2()
                                            new_predicates.append(Predicate([uri_r], chosen))
                                            print(8)

    states[t].add_predicate_to_state("belief_chosen_bin", new_predicates)


def go_to_object_place(states, t):
    global counter1
    previous_state = states[t - 1]
    new_predicates = []
    for predicate in previous_state.get_predicate("belief_chosen_bin"):
        uri = get_uri_robot()
        if predicate.value=="none" or counter1!=0:
            new_predicates.append(Predicate([uri], "false"))
        else:
            new_predicates.append(Predicate([uri], "true"))
            counter1+=1
    states[t].add_predicate_to_state("go_to_object_place", new_predicates)
    counter=0

def pick_object(states, t):
    previous_state = states[t - 1]
    new_predicates = []
    for predicate in previous_state.get_predicate("go_to_object_place"):
        uri = get_uri_robot()
        if predicate.value == "false":
            new_predicates.append(Predicate([uri], "false"))
        else:
            new_predicates.append(Predicate([uri], "true"))
    states[t].add_predicate_to_state("pick_object", new_predicates)

def go_to_chosen_bin(states, t):
    previous_state = states[t - 1]
    new_predicates = []
    for predicate in previous_state.get_predicate("pick_object"):
        uri = get_uri_robot()
        if predicate.value == "false":
            new_predicates.append(Predicate([uri], "false"))
        else:
            new_predicates.append(Predicate([uri], "true"))
    states[t].add_predicate_to_state("go_to_chosen_bin", new_predicates)

def robot_trash_object(states, t):
    previous_state = states[t - 1]
    new_predicates = []
    for predicate in previous_state.get_predicate("go_to_chosen_bin"):
        uri = get_uri_robot()
        if predicate.value == "false":
            new_predicates.append(Predicate([uri], "false"))
        else:
            new_predicates.append(Predicate([uri], "true"))
    states[t].add_predicate_to_state("robot_trash_object", new_predicates)





###############################
# any functions that actually need to be executed in the simulation must be put in this list
rules = [observe_bin, observe_object, belief_object_position, belief_object_dimension,belief_specialized_bin_1_position,
         belief_specialized_bin_2_position, belief_all_in_bin_position, belief_specialized_bin_1_volume,
         belief_specialized_bin_2_volume, decision_process, belief_chosen_bin,go_to_object_place, pick_object, go_to_chosen_bin,
         robot_trash_object]