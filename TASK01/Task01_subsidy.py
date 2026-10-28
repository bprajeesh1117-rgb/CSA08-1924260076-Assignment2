
# Q1: Electricity Subsidy Eligibility

def separate_ifs(units, ration_card, elderly):
    if units <= 100:
        print("Full subsidy")

    if 101 <= units <= 200 and ration_card:
        print("Partial subsidy")

    if 101 <= units <= 200 and not ration_card:
        print("No subsidy")

    if units > 200 and elderly:
        print("Special elderly subsidy")

    if units > 200 and not elderly:
        print("No subsidy")


def chained_decision(units, ration_card, elderly):
    if units <= 100:
        return "Full subsidy"

    elif 101 <= units <= 200 and ration_card:
        return "Partial subsidy"

    elif 101 <= units <= 200 and not ration_card:
        return "No subsidy"

    elif units > 200 and elderly:
        return "Special elderly subsidy"

    else:
        return "No subsidy"


# Test eight households
households = [
    (100, False, False),
    (101, True, False),
    (101, False, False),
    (200, True, False),
    (200, False, False),
    (201, False, False),
    (201, False, True),
    (80, True, True)
]

print("SEPARATE IF STATEMENTS")
for units, card, elderly in households:
    print("Units:", units)
    separate_ifs(units, card, elderly)
    print()

print("IF-ELIF-ELSE")
for units, card, elderly in households:
    print("Units:", units,
          "->", chained_decision(units, card, elderly))
