
# TASK 4: Compare String Building Methods

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
    return "".join(f"{part};" for part in parts)


def measure(function, items):
    times = []

    for i in range(3):
        start = time.perf_counter()
        result = function(items)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

    average = statistics.mean(times)
    return result, times, average


def main():
    sizes = [1000, 10000, 200000]

    for size in sizes:
        items = [f"Item{i}:Rs{i % 50}" for i in range(size)]

        a, plus_times, plus_avg = measure(build_plus, items)
        b, join_times, join_avg = measure(build_join, items)
        c, f_times, f_avg = measure(build_fstring, items)

        print("\nNumber of lines:", size)
        print("Same output:", a == b == c)

        print("Plus times:", plus_times)
        print("Plus average:", round(plus_avg, 6), "seconds")

        print("Join times:", join_times)
        print("Join average:", round(join_avg, 6), "seconds")

        print("F-string times:", f_times)
        print("F-string average:", round(f_avg, 6), "seconds")


if __name__ == "__main__":
    main()
