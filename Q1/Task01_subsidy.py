"""Q1: State electricity subsidy eligibility."""

def separate_ifs(units, ration_card, elderly_over_80):
    decisions = []
    # Demonstrates why overlapping independent rules can produce multiple results.
    if units <= 100:
        decisions.append("Full subsidy")
    if 101 <= units <= 200 and ration_card:
        decisions.append("Partial subsidy")
    if units > 200:
        decisions.append("No subsidy")
    if units > 200 and elderly_over_80:
        decisions.append("Special elderly subsidy")
    return decisions or ["No subsidy"]


def chained_decision(units, ration_card, elderly_over_80):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "Partial subsidy"
        else:
            return "No subsidy"
    elif units > 200:
        if elderly_over_80:
            return "Special elderly subsidy"
        else:
            return "No subsidy"


def main():
    households = [
        ("H1", 100, False, False),
        ("H2", 101, True, False),
        ("H3", 101, False, False),
        ("H4", 200, True, False),
        ("H5", 200, False, False),
        ("H6", 201, False, False),
        ("H7", 201, False, True),
        ("H8", 80, True, True),
    ]
    print("Household | Units | Separate-if results | Chained result")
    for name, units, card, elderly in households:
        print(f"{name:9} | {units:5} | {', '.join(separate_ifs(units, card, elderly))} | "
              f"{chained_decision(units, card, elderly)}")

if __name__ == "__main__":
    main()
