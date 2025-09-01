import random
from experiment_package.task1_quicksort.main import quicksort

def test_basic():
    assert quicksort([3,1,4,1,5,9]) == [1,1,3,4,5,9]

def test_empty():
    assert quicksort([]) == []

def test_duplicates():
    assert quicksort([5,5,5,1,1]) == [1,1,5,5,5]

def test_negatives():
    assert quicksort([-3, -1, -2, 0]) == [-3,-2,-1,0]

def test_random():
    for _ in range(20):
        arr = [random.randint(-100,100) for _ in range(50)]
        assert quicksort(arr[:]) == sorted(arr)
