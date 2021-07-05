def sum_with_0(index, summation, arr, n, subset_list):
    if index == n:
        if summation == 0:
            print(subset_list)
            return 1
        else:
            return 0

    if visit[index][summation + array_size]:
        if dp[index][summation + array_size] != 0:
            print(subset_list)
        return dp[index][summation + array_size]

    visit[index][summation + array_size] = 1

    subset_list.append(arr[index])
    temp1 = sum_with_0(index + 1, summation + arr[index], arr, n, subset_list)
    subset_list.remove(arr[index])
    temp2 = sum_with_0(index + 1, summation, arr, n, subset_list)
    dp[index][summation + array_size] = temp1 + temp2

    return dp[index][summation + array_size]


# Driver Code
if __name__ == "__main__":
    A = [2, 3, -5, -8, 6, -1]
    length = len(A)
    maximum_sum = 0
    for i in range(length):
        if A[i] < 0:
            maximum_sum -= A[i]
        else:
            maximum_sum += A[i]
    array_size = (maximum_sum // 2)

    dp = [[0 for i in range(maximum_sum)] for j in range(length)]
    visit = [[0 for i in range(maximum_sum)] for j in range(length)]

    sum_with_0(0, 0, A, length, [])
    for i in range(array_size):
        for j in range(maximum_sum):
            print(dp[i][j], end=" ")
        print()
