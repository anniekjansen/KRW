from state_machine import StateMachine
import rules
from visualization import run_visualization


###### INPUT VALUES ######
MAX_T = 50
scenario = "scenario.txt"
StateMachine1 = StateMachine(scenario, MAX_T, rules.rules)

StateMachine1.run()

run_visualization(StateMachine1, 'bar', [("inspection_tour", "URIR", "true" ), ("observe_bin", "URIR", "true"), ("observe_object", "URIR", "true"), ("belief_object_position", "URIO", "none")], MAX_T)

# run_visualization(StateMachine1, 'bar', [
#     ("training", 'agent_happy', "true"),
#     ("performance_at_work", 'agent_happy', 'good'),
#     ("chance_of_cardiovascular_diseases", 'agent_happy', 'low'),
#     ("level_of_alcoholism", 'agent_happy', 'low'),
#     ("belief_chance_of_cardiovascular_diseases", 'agent_happy', 'low'),
#     ("desire_feeling_of_loneliness", 'agent_happy', "True"),
#     ("assessment_feeling_of_loneliness", 'agent_happy', True),
#     ("belief_feeling_of_loneliness", "agent_happy", True)], 50)
