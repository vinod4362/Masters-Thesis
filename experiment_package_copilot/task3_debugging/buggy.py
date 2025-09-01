# Buggy Fibonacci with supposed memoization
_cache = {}

def fib(n):
    # Input validation
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in _cache:
        return _cache[n]
    value = fib(n-1) + fib(n-2)
    _cache[n] = value
    return value
