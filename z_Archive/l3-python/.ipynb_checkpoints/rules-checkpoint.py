""" rules.py
    States the rules and contains an execution function that can execute all the rules for ass4
    """

from state import Predicate

#######################################
# any variables declared here will be treated as scenario parameters
PERFORMANCE_GOOD = 0.25
PERFORMANCE_SUFFICIENT = 0.5
PERFORMANCE_INSUFFICIENT = 0.75
LOW_CHANCE_THRESHOLD = 0.33
MEDIUM_CHANCE_THRESHOLD = 0.66
step_size = 0.1


#######################################
# create any functions here


def set_expectation_about_others(states, t):
    """
        set the expectation about others based on training and the emotion regulation ability

        training : [[agent], value]
        expectation_about_others : [[agent], value]
    """

    previous_state = states[t - 1]
    new_predicates = []

    for predicate in previous_state.get_predicate("training"):
        agent = predicate.agents[0]
        training = (predicate.value == 'true')
        for expectation_about_others in previous_state.get_predicate_by_agent("expectation_about_others", agent):
            expectation_value = expectation_about_others.value
            if training and expectation_value <= 0.9:
                expectation_about_others = expectation_value + 0.1
            else:
                expectation_about_others = expectation_value
            #print("New expectation_about_others:", expectation_about_others)
            new_predicates.append(Predicate([agent], expectation_about_others))
    states[t].add_predicate_to_state("expectation_about_others", new_predicates)


def set_emotion_regulation_ability(states, t):
    """
        set the emotion regulation ability based on training and the current ability

        training : [[agent], value]
        emotion_regulation_ability : [[agent], value]
    """

    previous_state = states[t - 1]
    new_predicates = []

    for predicate in previous_state.get_predicate("training"):
        agent = predicate.agents[0]
        training = (predicate.value == 'true')
        for emotion_regulation_ability in previous_state.get_predicate_by_agent("emotion_regulation_ability", agent):
            ability_value = emotion_regulation_ability.value
            if training and 0 < ability_value <= 0.9:
                regulation_ability = ability_value + 0.1
            else:
                regulation_ability = ability_value
            new_predicates.append(Predicate([agent], regulation_ability))
    states[t].add_predicate_to_state("emotion_regulation_ability", new_predicates)


def set_social_activities_enjoyed(states, t):
    """
        set the social activities enjoyed based on the number of activities

        amount_of_activities : [[agent], value]
        social_activities_enjoyed : [[agent], value]
    """

    previous_state = states[t - 1]
    new_predicates = []

    for predicate in previous_state.get_predicate("amount_of_activities"):
        agent = predicate.agents[0]
        amount = predicate.value
        activities_enjoyed = (1 - (amount * 0.2 * 0.9))
        new_predicates.append(Predicate([agent], activities_enjoyed))
    states[t].add_predicate_to_state("social_activities_enjoyed", new_predicates)


def set_feeling_of_loneliness(states, t):
    """
        set the feeling of loneliness of an agent based on the level of vulnerability, emotion regulation ability,
        expectation about others and social activities enjoyed

        level_of_vulnerability : [[agent], value]
        emotion_regulation_ability : [[agent], value]
        expectation_about_others : [[agent], value]
        social_activities_enjoyed : [[agent], value]
        feeling_of_loneliness : [[agent], value]
    """

    previous_state = states[t - 1]
    new_predicates = []

    for predicate in previous_state.get_predicate("feeling_of_loneliness"):
        agent = predicate.agents[0]
        vulnerability_level = -1
        regulation_ability = -1
        expectation_others = -1
        activities_enjoyed = -1
        for vulnerability_level in previous_state.get_predicate_by_agent("level_of_vulnerability", agent):
            vulnerability_level = vulnerability_level.value
        for regulation_ability in previous_state.get_predicate_by_agent("emotion_regulation_ability", agent):
            regulation_ability = regulation_ability.value
        for expectation_others in previous_state.get_predicate_by_agent("expectation_about_others", agent):
            expectation_others = expectation_others.value
        for activities_enjoyed in previous_state.get_predicate_by_agent("social_activities_enjoyed", agent):
            activities_enjoyed = activities_enjoyed.value
        level_of_loneliness = (vulnerability_level + (1-regulation_ability) + (1-expectation_others) + activities_enjoyed) / 4
        new_predicates.append(Predicate([agent], level_of_loneliness))
    states[t].add_predicate_to_state("feeling_of_loneliness", new_predicates)


def set_performance_level(states, t):
    """
        set the level of performance at work of an agent based on the behaviour level

        feeling_of_loneliness : [[agent], value]
        performance_at_work : [[agent], performance]
    """

    previous_state = states[t - 1]
    new_predicates = []
    if previous_state.check_predicate("feeling_of_loneliness"):
        for predicate in previous_state.get_predicate("feeling_of_loneliness"):
            agent = predicate.agents[0]
            performance_level = convert_performance_level(1-predicate.value)
            new_predicates.append(Predicate([agent], performance_level))
        states[t].add_predicate_to_state("performance_at_work", new_predicates)


def convert_performance_level(value):
    """
        obtain the performance level based on the behaviour level of the agent and thresholds
    """
    if value >= PERFORMANCE_GOOD:
        return "good"
    elif PERFORMANCE_GOOD > value >= PERFORMANCE_SUFFICIENT:
        return "sufficient"
    elif PERFORMANCE_SUFFICIENT > value >= PERFORMANCE_INSUFFICIENT:
        return "insufficient"
    else:
        return "bad"


def set_chance_cardio_disease(states, t):
    """
        set the chance of cardiovascular diseases of an agent based on the physical level

        feeling_of_loneliness : [[agent], value]
        chance_of_cardiovascular_diseases : [[agent], chance]
    """

    previous_state = states[t - 1]
    new_predicates = []
    if previous_state.check_predicate("feeling_of_loneliness"):
        for predicate in previous_state.get_predicate("feeling_of_loneliness"):
            agent = predicate.agents[0]
            feeling_of_loneliness = predicate.value
            #print("Cardio_risk based on: ", feeling_of_loneliness)
            chance = convert_chance_cardio_disease(feeling_of_loneliness)
            #print("chance", chance)
            new_predicates.append(Predicate([agent], chance))
        states[t].add_predicate_to_state("chance_of_cardiovascular_diseases", new_predicates)


def convert_chance_cardio_disease(value):
    """
        obtain the performance level based on the thresholds
    """
    if value <= LOW_CHANCE_THRESHOLD:
        return "low"
    elif LOW_CHANCE_THRESHOLD < value <= MEDIUM_CHANCE_THRESHOLD:
        return "medium"
    else:
        return "high"


def set_alcoholism_level(states, t):
    """
        set the level of alcoholism of an agent based on the physical level and level of behaviour

        feeling_of_loneliness : [[agent], value]
        level_of_alcoholism : [[agent], level]
    """
    previous_state = states[t - 1]

    new_predicates = []
    if previous_state.check_predicate("feeling_of_loneliness"):
        for predicate in previous_state.get_predicate("feeling_of_loneliness"):
            agent = predicate.agents[0]
            feeling_of_loneliness = predicate.value
            alcoholism_level = convert_alcoholism_level(feeling_of_loneliness)
            new_predicates.append(Predicate([agent], alcoholism_level))
    states[t].add_predicate_to_state("level_of_alcoholism", new_predicates)


def convert_alcoholism_level(alcoholism_level):
    """
        obtain the performance level based on the behaviour level of the agent and thresholds
    """
    if alcoholism_level <= LOW_CHANCE_THRESHOLD:
        return "low"
    elif LOW_CHANCE_THRESHOLD < alcoholism_level <= MEDIUM_CHANCE_THRESHOLD:
        return "medium"
    else:
        return "high"
    
    
# Start here with the rules about observations

def observe_alcoholism_level(states, t):
    """
        set the observation of the level of alcoholism of an agent based on the level of alcoholism of an agent

        level_of_alcoholism : [[agent], level]
        observed : {level_of_alcoholism : [[agent], level]}
    """
    previous_state = states[t - 1]
    new_predicates = []

    if previous_state.check_predicate("level_of_alcoholism"):
        for predicate in previous_state.get_predicate("level_of_alcoholism"):
            agent = predicate.agents[0]
            alcoholism_level = predicate.value
            new_predicates.append(Predicate([agent], alcoholism_level))
    states[t].add_nested_predicate_to_state("observed", "level_of_alcoholism", new_predicates)


# add other required observations.....
# ...
def observe_chance_of_cardiovascular_diseases_level(states, t):

    previous_state = states[t - 1]
    new_predicates = []

    if previous_state.check_predicate("chance_of_cardiovascular_diseases"):
        for predicate in previous_state.get_predicate("chance_of_cardiovascular_diseases"):
            agent = predicate.agents[0]
            chance_of_cardiovascular_diseases_level = predicate.value
            new_predicates.append(Predicate([agent], chance_of_cardiovascular_diseases_level))
    states[t].add_nested_predicate_to_state("observed", "chance_of_cardiovascular_diseases", new_predicates)
    
# All observations are translated to beliefs via the following rule

def observe_to_belief(states, t):
    """
        set observations to beliefs

        observed : {observations ...}
        belief : {beliefs ...}
    """
    previous_state = states[t - 1]
    observations = previous_state.retrieve_observations()
    if observations:
        for predicate in observations.keys():
            new_predicates = []
            for single_predicate in observations[predicate]:
                agent = single_predicate.agents[0]
                observation = single_predicate.value
                new_predicates.append(Predicate([agent], observation))
            states[t].add_nested_predicate_to_state("belief", predicate, new_predicates)

# Complete / adapt the rules to generate new beliefs from existing beliefs and an assessment

def belief_feeling_of_loneliness(states, t):
    """
        set the belief of the feeling of loneliness of an agent based on the belief of the level of alcoholism and the
        chance of cardiovascular of an agent

        belief : {chance_of_cardiovascular_diseases : [[agent], chance],}
                  level_of_alcoholism : [[agent], level]}
        belief : {feeling_of_loneliness : [[agent], bool]}
    """
    previous_state = states[t - 1]
    beliefs = previous_state.retrieve_beliefs()
    if beliefs:
        new_predicates = []
        for predicate in beliefs["level_of_alcoholism"]:
            agent = predicate.agents[0]
            belief_alcoholism = predicate.value
            belief_cardiovascular_diseases = -1
            for cardiovascular_diseases in previous_state.get_nested_predicate_by_name("belief", "cardiovascular_diseases", agent):
                belief_cardiovascular_diseases = cardiovascular_diseases.value
            belief_feeling = False
            if (belief_alcoholism == "high" and belief_cardiovascular_diseases == "medium") or (
                    belief_cardiovascular_diseases == "high" and belief_alcoholism == "medium"):
                belief_feeling = True
            new_predicates.append(Predicate([agent], belief_feeling))
        states[t].add_nested_predicate_to_state("belief", "feeling_of_loneliness", new_predicates)


def assessment_feeling_of_loneliness(states, t):

    """
        set the assessment of the feeling of loneliness of an agent based on the belief of the feeling of loneliness and
        the desire of the feeling of loneliness

        belief : {feeling_of_loneliness : [[agent], bool]}
        desire : {feeling_of_loneliness : [[agent], bool]}
        assessment : {feeling_of_loneliness : [[agent], bool]}
    """
    previous_state = states[t - 1]
    beliefs = previous_state.retrieve_beliefs()
    if beliefs:
        new_predicates = []
        if previous_state.check_belief_in_beliefs("feeling_of_loneliness"):
            for predicate in beliefs["feeling_of_loneliness"]:
                agent = predicate.agents[0]
                belief_feeling_of_loneliness = predicate.value
                desire_feeling_of_loneliness = -2
#########################


                for desire in previous_state.get_nested_predicate_by_name("desire", "feeling_of_loneliness", agent):
                    desire_feeling_of_loneliness = desire.value

                if desire_feeling_of_loneliness == "False":
                    desire_feeling_of_loneliness = False
                else:
                    desire_feeling_of_loneliness = True

                if desire_feeling_of_loneliness is True and belief_feeling_of_loneliness is True or desire_feeling_of_loneliness is False and belief_feeling_of_loneliness is False:

                    assessment_feeling = True
                else:

                    assessment_feeling = False

                new_predicates.append(Predicate([agent], assessment_feeling))

###########################
            states[t].add_nested_predicate_to_state("assessment", "feeling_of_loneliness", new_predicates)


###############################
# any functions that actually need to be executed in the simulation must be put in this list
rules = [set_expectation_about_others, set_emotion_regulation_ability,
         set_social_activities_enjoyed, set_feeling_of_loneliness, set_performance_level, 
         set_chance_cardio_disease, set_alcoholism_level,
         observe_alcoholism_level,observe_chance_of_cardiovascular_diseases_level, observe_to_belief,
         belief_feeling_of_loneliness, assessment_feeling_of_loneliness]