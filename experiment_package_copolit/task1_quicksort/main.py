#!/usr/bin/env python3
from typing import List

def quicksort(nums: List[int]) -> List[int]:
    # Handle edge cases: empty or single element
    if len(nums) <= 1:
        return nums.copy()
    arr = nums.copy()  # Do not modify input
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
        pi = _partition(arr, low, high)
        _quicksort(arr, low, pi - 1)
        _quicksort(arr, pi + 1, high)

def main():
    try:
        line = input().strip()
        if not line:
            print("".strip())
            return
        nums = list(map(int, line.split()))
        sorted_nums = quicksort(nums)
        print(" ".join(map(str, sorted_nums)))
    except Exception as e:
        # Basic robustness: avoid crashing on invalid input
        print("ERROR")

if __name__ == "__main__":
    main()
