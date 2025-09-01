#!/usr/bin/env python3
from typing import List

def quicksort(nums: List[int]) -> List[int]:
    # Perform in-place quicksort
    arr = nums[:]  # copy to avoid mutating input
    if len(arr) <= 1:
        return arr
    _quicksort(arr, 0, len(arr) - 1)
    return arr

def _partition(arr, low, high):
    # Lomuto partition scheme
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def _quicksort(arr, low, high):
    if low < high:
        p = _partition(arr, low, high)
        _quicksort(arr, low, p - 1)
        _quicksort(arr, p + 1, high)

def main():
    try:
        line = input().strip()
        if not line:
            print("")
            return
        nums = list(map(int, line.split()))
        sorted_nums = quicksort(nums)
        print(" ".join(map(str, sorted_nums)))
    except Exception:
        print("ERROR")

if __name__ == "__main__":
    main()
