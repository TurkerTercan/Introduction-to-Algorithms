import time
import random


def rearrange(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
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


def insertion_sort(array, low, high):
    for index in range(low + 1, high):
        current = array[index]
        position = index - 1
        while position >= 1 and current <= array[position]:
            array[position + 1] = array[position]
            position = position - 1
        array[position + 1] = current


def hybrid_quick_sort(array, start, end, threshold):
    if start >= end:
        return
    if start - end < threshold:
        insertion_sort(array, start, end)
    else:
        pivot = rearrange(array, start, end)
        quick_sort(array, start, pivot - 1)
        quick_sort(array, pivot + 1, end)


if __name__ == '__main__':
    arr = [1] * 1000
    for i in range(0, 1000):
        arr[i] = random.randint(0, 9)
    start_time = time.time()
    hybrid_quick_sort(arr, 0, len(arr) - 1, 10)
    end_time = time.time()
    print("Hybrid QuickSort running time = ", (end_time - start_time), "\n")
