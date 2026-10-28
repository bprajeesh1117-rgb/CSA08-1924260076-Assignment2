
# TASK 6: Recursion - Climbing Stairs
import time
from functools import lru_cache


# Method 1: Basic recursion
recursive_calls = 0

def stairs_recursive(n):
    global recursive_calls
    recursive_calls += 1

    if n <= 2:
        return n

    return stairs_recursive(n - 1) + stairs_recursive(n - 2)


# Method 2: Recursion with memoisation
@lru_cache(maxsize=None)
def stairs_memo(n):
    if n <= 2:
        return n

    return stairs_memo(n - 1) + stairs_memo(n - 2)


# Method 3: Iterative solution
def stairs_iterative(n):
    if n <= 2:
        return n

    first, second = 1, 2

    for step in range(3, n + 1):
        first, second = second, first + second

    return second


# Test small values
print("TESTING n = 1 TO 6")

for n in range(1, 7):
    print(
        "n =", n,
        "| Recursive:", stairs_recursive(n),
        "| Memoised:", stairs_memo(n),
        "| Iterative:", stairs_iterative(n)
    )


# Compare execution times
print("\nPERFORMANCE COMPARISON")

for n in [10, 20, 25, 30]:
    recursive_calls = 0

    start = time.perf_counter()
    answer1 = stairs_recursive(n)
    recursive_time = time.perf_counter() - start
    calls = recursive_calls

    stairs_memo.cache_clear()
    start = time.perf_counter()
    answer2 = stairs_memo(n)
    memo_time = time.perf_counter() - start

    start = time.perf_counter()
    answer3 = stairs_iterative(n)
    iterative_time = time.perf_counter() - start

    print("\nn =", n)
    print("Answer:", answer1)
    print("Recursive calls:", calls)
    print("Basic recursion time:", round(recursive_time, 6), "seconds")
    print("Memoisation time:", round(memo_time, 6), "seconds")
    print("Iterative time:", round(iterative_time, 6), "seconds")

    assert answer1 == answer2 == answer3


# Test a larger input without using slow basic recursion
print("\nLARGE INPUT TEST")
print("Ways for n = 100:", stairs_iterative(100))

try:
    print("Ways for n = 1000:", stairs_memo(1000))
except RecursionError:
    print("Memoised recursion reached Python's recursion limit.")
