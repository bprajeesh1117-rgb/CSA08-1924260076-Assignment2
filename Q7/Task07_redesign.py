"""Q7: Diagnose string-building bottleneck and validate a join-based redesign."""
import time
import statistics


def original(parts):
    result = ""
    for item in parts:
        result += item + ";"
    return result


def redesigned(parts):
    return "".join(item + ";" for item in parts)


def measure(function, data, repeats=3):
    times = []
    output = None
    for _ in range(repeats):
        start = time.perf_counter()
        output = function(data)
        times.append(time.perf_counter() - start)
    return output, times, statistics.mean(times)


def main():
    sizes = (1_000, 10_000, 50_000)
    print("Q7 evidence: original repeated += versus join redesign")
    for size in sizes:
        data = [f"Call{i}:Rs{i % 100}" for i in range(size)]
        old_text, old_times, old_avg = measure(original, data)
        new_text, new_times, new_avg = measure(redesigned, data)
        print(f"\nInput lines: {size}")
        print(f"Outputs identical: {old_text == new_text}")
        print(f"Original times: {[round(t, 6) for t in old_times]}, average={old_avg:.6f}s")
        print(f"Redesigned times: {[round(t, 6) for t in new_times]}, average={new_avg:.6f}s")
        if new_avg > 0:
            print(f"Average speedup (old/new): {old_avg / new_avg:.2f}x")


if __name__ == "__main__":
    main()
