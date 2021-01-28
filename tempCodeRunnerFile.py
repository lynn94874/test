for i in range(5000):
    id = np.random.choice(6, 1, replace=False)
    if id == 0 or id == 1:
       num += 1
    poss_history.append((i + 1, 1.00 * num / (i + 1))) 