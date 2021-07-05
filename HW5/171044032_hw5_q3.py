def unbounded_knapsack():
    knapsack = [0 for i in range(capacity + 1)]
    subset = [[] for i in range(capacity + 1)]
    for i in range(capacity + 1):
        for j in range(len(value)):
            if weight[j] <= i:
                temp0 = knapsack[i]
                temp1 = knapsack[i - weight[j]] + value[j]
                if temp0 < temp1:
                    knapsack[i] = temp1
                    subset[i] = [[weight[j], value[j]], subset[i - weight[j]]]

    print(knapsack)
    print(subset[capacity])
    return knapsack[capacity]


if __name__ == '__main__':
    weight = [5, 4, 2]
    value = [10, 4, 3]
    capacity = 9

    unbounded = unbounded_knapsack()
    print(unbounded)
