def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    n = len(values)
    new_values = [0] * n
    n_actions = len(transitions[0])
    for s in range(n):
        for a in range(n_actions):
            val = rewards[s][a]
            for sp in range(n):
                val += gamma * values[sp] * transitions[s][a][sp]
            new_values[s] = max(new_values[s], val)
    return new_values
                