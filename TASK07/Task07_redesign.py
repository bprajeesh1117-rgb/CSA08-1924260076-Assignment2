
# TASK 7: Performance Bottleneck and Redesign
import time
import statistics


# Original implementation: repeated string concatenation
def original_version(items):
    result = ""

    for item in items:
        result += item + "\n"

    return result


# Redesigned implementation: join()
def redesigned_version(items):
    return "\n".join(items) + "\n"


# Measure execution time over multiple runs
def benchmark(function, items, repetitions=5):
    timings = []
    result = None

    for _ in range(repetitions):
        start = time.perf_counter()
        result = function(items)
        elapsed = time.perf_counter() - start
        timings.append(elapsed)

    return result, timings, statistics.mean(timings)


def main():
    sizes = [1000, 10000, 200000]

    for size in sizes:
        items = [f"Record {i}: Value {i % 100}" for i in range(size)]

        original_result, original_times, original_avg = benchmark(
            original_version, items
        )

        redesigned_result, redesigned_times, redesigned_avg = benchmark(
            redesigned_version, items
        )

        print("\n" + "=" * 45)
        print("Number of records:", size)
        print("Outputs match:", original_result == redesigned_result)

        print("\nOriginal version timings:")
        print([round(t, 6) for t in original_times])
        print("Original average:", round(original_avg, 6), "seconds")

        print("\nRedesigned version timings:")
        print([round(t, 6) for t in redesigned_times])
        print("Redesigned average:", round(redesigned_avg, 6), "seconds")

        if redesigned_avg > 0:
            speedup = original_avg / redesigned_avg
            print("Speedup ratio:", round(speedup, 2), "x")

        print("Output length:", len(original_result))


if __name__ == "__main__":
    main()
