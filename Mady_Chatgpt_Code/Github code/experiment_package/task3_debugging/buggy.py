# Fixed Fibonacci with memoization (O(n))
_cache = {0: 0, 1: 1}

def fib(n):
    """
    Return the nth Fibonacci number for n >= 0.

    Examples:
      fib(0) = 0
      fib(1) = 1
      fib(10) = 55
      fib(30) = 832040
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    if n in _cache:
        return _cache[n]

    # Fill iteratively from the largest cached index up to n
    start = max(_cache) + 1
    for i in range(start, n + 1):
        _cache[i] = _cache[i - 1] + _cache[i - 2]
    return _cache[n]


# Optional: tiny CLI so you can "add the data" (enter n) and get fib(n)
if __name__ == "__main__":
    try:
        raw = input("Enter n (non-negative integer): ").strip()
        n = int(raw)
        print(fib(n))
    except Exception as e:
        print(f"ERROR: {e}")
