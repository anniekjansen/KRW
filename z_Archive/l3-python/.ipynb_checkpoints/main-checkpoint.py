""" main.py
    Everything except the State and StateMachine, used for running the simulation
    """
from state_machine import StateMachine
import rules
from visualization import run_visualization


###### ass4 ######
MAX_T = 50
scenario1 = "scenario_false.txt"
scenario2 = "scenario_true.txt"
StateMachine1 = StateMachine(scenario1, MAX_T, rules.rules)
StateMachine2 = StateMachine(scenario2, MAX_T, rules.rules)

StateMachine1.run()
StateMachine2.run()

# for i in range(MAX_T):
#     if "level_of_vulnerability" in StateMachine.states[i].predicates:
#         # print(StateMachine.states[i].predicates["assessment"].value)
#         print(StateMachine.states[i].predicates["level_of_vulnerability"])

#run_visualization(StateMachine, 'line', ["expectation_about_others", "agent_happy"], None)
#run_visualization(StateMachine, 'line', ["emotion_regulation_ability", "agent_happy"], None)


run_visualization(StateMachine1, 'line', ["feeling_of_loneliness", "agent_happy"], None)
run_visualization(StateMachine1, 'bar', [
    ("training", 'agent_happy', "true"),
    ("performance_at_work", 'agent_happy', 'good'),
    ("chance_of_cardiovascular_diseases", 'agent_happy', 'low'),
    ("level_of_alcoholism", 'agent_happy', 'low'),
    ("belief_chance_of_cardiovascular_diseases", 'agent_happy', 'low'),
    ("desire_feeling_of_loneliness", 'agent_happy', "True"),
    ("assessment_feeling_of_loneliness", 'agent_happy', True),
    ("belief_feeling_of_loneliness", "agent_happy", True)], 50)
run_visualization(StateMachine2, 'bar', [
    ("training", 'agent_happy', "true"),
    ("performance_at_work", 'agent_happy', 'good'),
    ("chance_of_cardiovascular_diseases", 'agent_happy', 'low'),
    ("level_of_alcoholism", 'agent_happy', 'low'),
    ("belief_chance_of_cardiovascular_diseases", 'agent_happy', 'low'),
    ("desire_feeling_of_loneliness", 'agent_happy', "True"),
    ("assessment_feeling_of_loneliness", 'agent_happy', True),
    ("belief_feeling_of_loneliness", "agent_happy", False)], 50)