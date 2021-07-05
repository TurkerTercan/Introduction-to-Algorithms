def rearrange(array, start, end):
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
        else:
            break
    arr[start], arr[high] = arr[high], array[start]
    return high


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = rearrange(array, start, end)
    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, end)


def binary_search(sorted_array, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if sorted_array[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(sorted_array, low, mid - 1, target)
        else:
            return binary_search(sorted_array, mid + 1, high, target)
    else:
        return -1


def pair_search(array, target):
    n = len(array)
    quick_sort(array, 0, n - 1)
    for i in range(n):
        index = binary_search(array, i + 1, n - 1, target / array[i])
        if index != -1:
            print("(", array[i], ",", array[index], ")")


if __name__ == '__main__':
    arr = [1, 2, 3, 6, 5, 4]
    pair_search(arr, 6)
