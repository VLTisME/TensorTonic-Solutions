import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    """
    Returns: updated Q-table Q_new
    """
    best_future_value = float("-inf")
    best_future_action = 0
    for next_a in range(len(Q[0])):
        if Q[s_next][next_a] > best_future_value:
            best_future_value = Q[s_next][next_a]
            best_future_action = next_a
    Q[s][a] = Q[s][a] + alpha * (r + gamma * best_future_value - Q[s][a])
    return Q