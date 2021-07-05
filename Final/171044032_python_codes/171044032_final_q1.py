# CSE 321 - Introduction to Algorithm
# Türker Tercan - 171044032
# Final Takehome Exam - Question 1
def palindrome_length_2(string, dp, index):
    if index < len(string) - 1:
        if string[index] == string[index + 1]:
            dp[index][index + 1] = True
        palindrome_length_2(string, dp, index + 1)


def inner_recursive(index, k, string, dp):
    if index < len(string) - k + 1:
        j = index + k - 1
        if dp[index + 1][j - 1] and string[index] == string[j]:
            dp[index][j] = True
        inner_recursive(index + 1, k, string, dp)


def outer_recursive(k, string, dp):
    if k == len(string) + 2:
        return
    index = 0
    inner_recursive(index, k, string, dp)
    outer_recursive(k + 1, string, dp)


def longest_palindrome(string):
    length = len(string)
    dp = []
    for j in range(length):
        dp.append([False for i in range(length)])

    for i in range(length):
        dp[i][i] = True

    index = 0
    palindrome_length_2(string, dp, index)

    k = 3
    outer_recursive(k, string, dp)

    start = 0
    max_palindrome = 1
    for i in range(length):
        count = 0
        for j in range(i + 1):
            if i + j + 1 >= length:
                break
            if not dp[i - j][i + j + 1]:
                break
            count += 2
        if count > max_palindrome:
            max_palindrome = count
            start = i - (max_palindrome // 2) + 1

    for i in range(length):
        count = 0
        for j in range(i + 1):
            if i + j >= length:
                break
            if not dp[i - j][i + j]:
                break
            count += 2
        if count > max_palindrome:
            max_palindrome = count - 1
            start = i - (max_palindrome // 2)

    print(string[start:(start + max_palindrome)])


if __name__ == '__main__':
    text = "bananaana"
    longest_palindrome(text)
