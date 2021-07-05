# CSE 321 - Introduction to Algorithm
# Türker Tercan - 171044032
# Final Takehome Exam - Question 5
def merge(array, temp, left, mid, right):
    i = left
    j = mid
    k = left
    count = 0
    while i <= mid - 1 and j <= right:
        if array[i] <= array[j] * 2:
            temp[k] = array[i]
            k += 1
            i += 1
        else:
            count += mid - i
            temp[k] = array[j]
            k += 1
            j += 1

    while i <= mid - 1:
        temp[k] = array[i]
        k += 1
        i += 1
    while j <= right:
        if array[i - 1] > array[j] * 2:
            count -= 1
        temp[k] = array[j]
        k += 1
        j += 1
    for i in range(left, right + 1):
        array[i] = temp[i]
    return count


def merge_sort(array, temp, left, right):
    count = 0
    if right > left:
        mid = (right + left) // 2
        count = merge_sort(array, temp, left, mid)
        count += merge_sort(array, temp, mid + 1, right)
        count += merge(array, temp, left, mid + 1, right)
    return count


def count_of_inversions(array, length):
    temp = [0] * length
    return merge_sort(array, temp, 0, length - 1)


if __name__ == "__main__":
    arr = [128, 64, 1, 32, 2, 16, 4, 8]
    n = len(arr)
    print(count_of_inversions(arr, n))
