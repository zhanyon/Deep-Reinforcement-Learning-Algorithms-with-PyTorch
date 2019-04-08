from Agents.Policy_Gradient_Agents.PPO_Agent import PPO_Agent
from Trainer import Trainer
from Utilities.Data_Structures.Config import Config
from Agents.DQN_Agents.DDQN_Agent import DDQN_Agent
from Agents.DQN_Agents.DDQN_With_Prioritised_Experience_Replay import DDQN_With_Prioritised_Experience_Replay
from Agents.DQN_Agents.DQN_Agent import DQN_Agent
from Agents.DQN_Agents.DQN_Agent_With_Fixed_Q_Targets import DQN_Agent_With_Fixed_Q_Targets
from Environments.Open_AI_Gym_Environments.Cart_Pole_Environment import Cart_Pole_Environment
from Agents.Policy_Gradient_Agents.REINFORCE_Agent import REINFORCE_Agent
from Agents.Stochastic_Policy_Search_Agents.Genetic_Agent import Genetic_Agent
from Agents.Stochastic_Policy_Search_Agents.Hill_Climbing_Agent import Hill_Climbing_Agent
from Utilities.Utility_Functions import run_games_for_agents

config = Config()
config.seed = 1
config.environment = Cart_Pole_Environment()
config.num_episodes_to_run = 450
config.file_to_save_data_results = "Data_and_Graphs/Cart_Pole_Results_Data.pkl"
config.file_to_save_results_graph = "Data_and_Graphs/Cart_Pole_Results_Graph.png"
config.show_solution_score = False
config.visualise_individual_results = False
config.visualise_overall_agent_results = True
config.standard_deviation_results = 1.0
config.runs_per_agent = 3
config.use_GPU = False
config.overwrite_existing_results_file = False
config.randomise_random_seed = True
config.save_model = False


config.hyperparameters = {
    "DQN_Agents": {
        "learning_rate": 0.005,
        "batch_size": 128,
        "buffer_size": 40000,
        "epsilon": 1.0,
        "epsilon_decay_rate_denominator": 3,
        "discount_rate": 0.99,
        "tau": 0.1,
        "alpha_prioritised_replay": 0.6,
        "beta_prioritised_replay": 0.1,
        "incremental_td_error": 1e-8,
        "update_every_n_steps": 3,
        "nn_layers": 2,
        "nn_start_units": 30,
        "nn_unit_decay": 0.5,
        "final_layer_activation": None,
        "batch_norm": False,
        "gradient_clipping_norm": 5
    },
    "Stochastic_Policy_Search_Agents": {
        "policy_network_type": "Linear",
        "noise_scale_start": 1e-2,
        "noise_scale_min": 1e-3,
        "noise_scale_max": 2.0,
        "noise_scale_growth_factor": 2.0,
        "stochastic_action_decision": False,
        "num_policies": 10,
        "episodes_per_policy": 1,
        "num_policies_to_keep": 5
    },
    "Policy_Gradient_Agents": {
        "learning_rate": 0.05,
        "nn_layers": 2,
        "nn_start_units": 20,
        "nn_unit_decay": 1.0,
        "final_layer_activation": "SOFTMAX",
        "learning_iterations_per_round": 10,
        "discount_rate": 0.99,
        "batch_norm": False,
        "clip_epsilon": 0.1,
        "episodes_per_learning_round": 3,
        "normalise_rewards": True,
        "gradient_clipping_norm": 5,
        "mu": 0.0, #only required for continuous action games
        "theta": 0.0, #only required for continuous action games
        "sigma": 0.0, #only required for continuous action games
        "noise_decay_denominator": 1 #only required for continuous action games
    }
}

if __name__ == "__main__":

    AGENTS = [PPO_Agent, DQN_Agent, DQN_Agent_With_Fixed_Q_Targets, DDQN_With_Prioritised_Experience_Replay,  DDQN_Agent]
             # Genetic_Agent, Hill_Climbing_Agent, DQN_Agent_With_Fixed_Q_Targets ]
    import os
    print(os.getcwd())
    print(os.listdir(os.getcwd()))
    import pickle

    with open(config.file_to_save_data_results, 'rb') as f:
        z = pickle.load(f)
        print(z.keys())

    trainer = Trainer(config, AGENTS)
    trainer.visualise_preexisting_results(config.file_to_save_results_graph)
    # trainer.run_games_for_agents()



