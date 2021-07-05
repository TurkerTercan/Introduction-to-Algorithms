counts = [0, 0]


def rearrange(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end
    while True:
        while low <= high and arr[high] >= pivot:
            high = high - 1
        while low <= high and arr[low] <= pivot:
            low = low + 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            counts[0] = counts[0] + 1
        else:
            break
    arr[start], arr[high] = arr[high], arr[start]
    counts[0] = counts[0] + 1
    return high


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = rearrange(array, start, end)
    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, end)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        position = i - 1
        while position >= 0 and current < arr[position]:
            arr[position + 1] = arr[position]
            counts[1] = counts[1] + 1
            position -= 1
        arr[position + 1] = current
        counts[1] = counts[1] + 1


if __name__ == '__main__':
    temp1 = [15, 12, 13, 14, 6, 10]
    temp2 = [15, 12, 13, 14, 6, 10]
    quick_sort(temp1, 0, 5)
    insertion_sort(temp2)
    print("QuickSort: \t\t ", counts[0], " ", temp1)
    print("InsertionSort: \t", counts[1], " ", temp2)
