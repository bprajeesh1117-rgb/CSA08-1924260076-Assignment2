"""Q4: Compare repeated +=, join(), and f-string line creation."""
import time
import statistics


def build_plus(parts):
    text = ""
    for part in parts:
        text += part + ";"
    return text


def build_join(parts):
    return "".join(part + ";" for part in parts)


def build_fstring(parts):
    # f-strings are useful for creating each line; join combines the lines efficiently.
    return "".join(f"{part};" for part in parts)


def time_function(function, items, repeats=3):
    samples = []
    for _ in range(repeats):
        start = time.perf_counter()
        result = function(items)
        samples.append(time.perf_counter() - start)
    return result, samples, statistics.mean(samples)


def main():
    for size in (1_000, 10_000, 200_000):
        items = [f"Item{i}:Rs{i % 50}" for i in range(size)]
        plus, plus_samples, plus_avg = time_function(build_plus, items)
        joined, join_samples, join_avg = time_function(build_join, items)
        ftext, f_samples, f_avg = time_function(build_fstring, items)
        print(f"\nLines: {size:,}; same output: {plus == joined == ftext}")
        print(f"+= samples: {[round(x, 6) for x in plus_samples]} average={plus_avg:.6f}s")
        print(f"join samples: {[round(x, 6) for x in join_samples]} average={join_avg:.6f}s")
        print(f"f-string+join samples: {[round(x, 6) for x in f_samples]} average={f_avg:.6f}s")


if __name__ == "__main__":
    main()
