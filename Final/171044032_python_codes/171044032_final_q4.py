# CSE 321 - Introduction to Algorithm
# Türker Tercan - 171044032
# Final Takehome Exam - Question 4
def minimize_maximum_assignments(assignments):
    n = len(assignments)
    m = len(assignments[0])
    if m < n:
        print("Job size must be greater or equal to Person size\n")
        return None
    rows = [True] * n
    columns = [True] * m
    total = 0
    links = []
    while rows != [False] * n and columns != [False] * m:
        x = 0
        y = 0
        max_val = 0
        for i in range(0, n):
            for j in range(0, m):
                if rows[i] and columns[j]:
                    max_val = assignments[i][j]
                    x = i
                    y = j
                    break

        for i in range(0, n):
            for j in range(0, m):
                if rows[i] and columns[j] and max_val < assignments[i][j]:
                    max_val = assignments[i][j]
                    x = i
                    y = j
        min_val = max_val
        min_x = x
        min_y = y
        for j in range(0, m):
            if rows[x] and columns[j] and min_val > assignments[x][j]:
                min_val = assignments[x][j]
                min_x = x
                min_y = j
        for i in range(0, n):
            if rows[i] and columns[y] and min_val > assignments[i][y]:
                min_val = assignments[i][y]
                min_x = i
                min_y = y
        total += min_val
        links.append([min_x, min_y, min_val])
        rows[min_x] = False
        columns[min_y] = False
    print("Maximum cost among the assignments is minimized cost is = ", total)
    return links


if __name__ == '__main__':
    persons = [
        [550, 210, 1250, 1235, 999],
        [186, 842, 982, 396, 453],
        [666, 245, 852, 367, 1750],
        [110, 962, 456, 385, 750],
        [975, 265, 310, 1125, 870]
    ]
    return_value = minimize_maximum_assignments(persons)
    print(return_value)
