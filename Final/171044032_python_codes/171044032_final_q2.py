# CSE 321 - Introduction to Algorithm
# Türker Tercan - 171044032
# Final Takehome Exam - Question 2
def rearrange(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high += -1
        while low <= high and array[low] <= pivot:
            low += 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = rearrange(array, start, end)
    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, end)


if __name__ == "__main__":
    arr = [15, 12, 13, 14, 6, 10, -2, 2]
    interval = [[1, 8], [2, 7], [3, 6], [4, 5], [8, 8], [2, 3], [5, 6]]
    quick_sort(arr, 0, len(arr) - 1)
    print("Minimum interval values: ", end="")
    for i in interval:
        print(arr[i[0] - 1], end=" ")
    print("\nSorted list:", arr)
