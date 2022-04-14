from state import Predicate
from memory import *

#######################################
# Parameters
TAKEN_VOLUME_B1 = 16
TAKEN_VOLUME_B2 = 20



######################################
#Support Functions

#######################################
#Functions that formalize the rules for concepts

def inspection_tour(states, t):
    pass


def observe_bin(states, t):

    previous_state = states[t - 1]
    new_predicates = []
    
    for predicate in previous_state.get_predicate("inspection_tour"):
        uri = predicate.agents[0]
        inspection_bool = predicate.value
        new_predicates.append(Predicate([uri], inspection_bool))
    
    states[t].add_predicate_to_state("observe_bin", new_predicates)

def observe_object(states, t):
    previous_state = states[t - 1]
    new_predicates = []
    
    for predicate in previous_state.get_predicate("inspection_tour"):
        uri = predicate.agents[0]
        inspection_bool = predicate.value
        new_predicates.append(Predicate([uri], inspection_bool))
    
    states[t].add_predicate_to_state("observe_object", new_predicates)

def belief_object_position(states, t):
    previous_state = states[t - 1]
    new_predicates = []
    
    for predicate in previous_state.get_predicate("observe_object"):
        uri = get_uri_obj()
        print(uri)
        if predicate.value == "true":
            coords = get_coords_obj()
            new_predicates.append(Predicate([uri], coords))
        else: 
            new_predicates.append(Predicate([uri], "none"))           

    states[t].add_predicate_to_state("belief_object_position", new_predicates)

# def belief_object_dimension(states, t):
#     previous_state = states[t - 1]
#     new_predicates = []
    
#     for predicate in previous_state.get_predicate("inspection_tour"):
#         uri = predicate.agents[0]
#         coords = get_coords_obj()
#         new_predicates.append(Predicate([uri], coords))

#     states[t].add_predicate_to_state("belief_object_dimension", new_predicates)


# def belief_specialized_bin_1_position(states, t):

# def belief_specialized_bin_2_position(states, t):

# def belief_all_in_bin_position(states, t):

# def belief_specialized_bin_1_volume(states, t):

# def belief_specialized_bin_2_volume(states, t):

# def decision_process(states, t):

# def belief_chosen_bin(states, t):

# def go_to_object_place(states, t):

# def pick_object(states, t):

# def go_to_chosen_bin(states, t):

# def robot_trash_object(states, t):





###############################
# any functions that actually need to be executed in the simulation must be put in this list
rules = [observe_bin, observe_object, belief_object_position]