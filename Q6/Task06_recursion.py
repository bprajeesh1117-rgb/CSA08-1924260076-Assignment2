"""Q6: Staircase ways using naive recursion, memoisation, and iteration."""
from functools import lru_cache
import sys
import time

calls = 0


def ways_naive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_iterative(n):
    if n <= 1:
        return 1
    previous, current = 1, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current


def main():
    print("Answers n=1..6:", [ways_iterative(n) for n in range(1, 7)])
    for n in (10, 20, 25, 30):
        calls = 0
        start = time.perf_counter()
        answer_naive = ways_naive(n)
        naive_time = time.perf_counter() - start
        naive_calls = calls
        calls = 0
        ways_memo.cache_clear()
        start = time.perf_counter()
        answer_memo = ways_memo(n)
        memo_time = time.perf_counter() - start
        memo_calls = calls
        print(f"n={n}: naive={answer_naive}; naive calls={naive_calls}; naive time={naive_time:.6f}s")
        print(f"  memo={answer_memo}; memo calls={memo_calls}; memo time={memo_time:.6f}s")

    print("Recursion limit:", sys.getrecursionlimit())
    try:
        ways_memo.cache_clear()
        print("Memoised n=1000:", ways_memo(1000))
    except RecursionError as error:
        print("RecursionError at n=1000:", error)
    print("Iterative n=1000:", ways_iterative(1000))


if __name__ == "__main__":
    main()
