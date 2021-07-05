# CSE 321 - Introduction to Algorithm
# Türker Tercan - 171044032
# Final Takehome Exam - Question 5
def max_earning(miles, places, earnings, length, distance):
    dp_earning = [0] * (miles + 1)
    next_billboard_index = 0
    recursive_earning(1, miles, places, earnings, length, distance, dp_earning, next_billboard_index)
    print(dp_earning)
    return dp_earning[miles]


def recursive_earning(i, miles, places, earnings, length, distance, dp_earning, next_billboard_index):
    if i < 1 or i > miles:
        return
    if next_billboard_index < length:
        if places[next_billboard_index] != i:
            dp_earning[i] = dp_earning[i - 1]
        else:
            if i <= distance:
                dp_earning[i] = max(dp_earning[i - 1], earnings[next_billboard_index])
            else:
                dp_earning[i] = max(dp_earning[i - distance - 1] + earnings[next_billboard_index],
                                    dp_earning[i - 1])
            next_billboard_index += 1
    else:
        dp_earning[i] = dp_earning[i - 1]
    recursive_earning(i + 1, miles, places, earnings, length, distance, dp_earning, next_billboard_index)


if __name__ == "__main__":
    M = 15
    x = [2, 4, 5, 7, 10, 11]
    t = 4
    r = [10, 7, 12, 3, 5, 8]
    n = len(x)
    print(max_earning(M, x, r, n, t))
