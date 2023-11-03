import numpy as np

# 收益矩阵1为实际收益矩阵，收益矩阵2用于计算agent变更策略后的收益
payoff_matrix = np.array([[4, 1], [5, 2]])
payoff_matrix2 = np.array([[5, 2], [4, 1]])

# 主体数量和组数,100位同学，两两一组
num_agents = 100
num_groups = int(num_agents / 2)

# 策略A全力以赴，策略B摸鱼
strategies = ['A', 'B']

# 初始化每个主体的策略
agent_strategies = np.array(['A'] * 50 + ['B'] * 50)
# print(agent_strategies)

for _ in range(16):
    count_A = np.count_nonzero(agent_strategies == 'A')
    count_B = np.count_nonzero(agent_strategies == 'B')
    print(count_A,count_B)
    np.random.shuffle(agent_strategies)  # 随机打乱
    for i in range(num_groups):
        agent1_index = i * 2
        agent2_index = i * 2 + 1

        agent1_strategy = agent_strategies[agent1_index]
        agent2_strategy = agent_strategies[agent2_index]
        # 计算收益
        agent1_payoff = payoff_matrix[strategies.index(agent1_strategy),
        strategies.index(agent2_strategy)]
        agent2_payoff = payoff_matrix[strategies.index(agent2_strategy),
        strategies.index(agent1_strategy)]
        # 计算如果改变策略的收益
        agent1_payoff_2 = payoff_matrix2[strategies.index(agent1_strategy),
        strategies.index(agent2_strategy)]
        agent2_payoff_2 = payoff_matrix2[strategies.index(agent2_strategy),
        strategies.index(agent1_strategy)]

        if agent1_payoff < agent1_payoff_2:
        # 根据50%概率改变策略
           if np.random.random() < 0.5:
               if agent1_strategy == 'A':
                   agent1_strategy = 'B'
           else:
               agent1_strategy = 'A'

        if agent2_payoff < agent2_payoff_2:
        # 根据50%概率改变策略
           if np.random.random() < 0.5:
               if agent2_strategy == 'A':
                  agent2_strategy = 'B'
           else:
               agent2_strategy = 'A'

    # 更新主体的策略
        agent_strategies[agent1_index] = agent1_strategy
        agent_strategies[agent2_index] = agent2_strategy








