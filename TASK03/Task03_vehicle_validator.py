
# TASK 3: Vehicle Registration Number Validator

def normalise(text):
    text = text.strip()
    text = text.replace(" ", "")
    text = text.replace("-", "")
    text = text.upper()
    return text


def is_valid(reg):
    if len(reg) != 9 and len(reg) != 10:
        return False

    if not reg[0:2].isalpha():
        return False

    if not reg[2:4].isdigit():
        return False

    series_length = len(reg) - 8

    if not reg[4:4 + series_length].isalpha():
        return False

    if not reg[-4:].isdigit():
        return False

    return True


def format_receipt(reg):
    series_length = len(reg) - 8

    state = reg[:2]
    district = reg[2:4]
    series = reg[4:4 + series_length]
    number = reg[-4:]

    return state + " " + district + " " + series + " " + number


vehicles = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "MH 12 XYZ 4567",
    "DL 08 C 1234"
]

for raw in vehicles:
    reg = normalise(raw)

    if is_valid(reg):
        print(raw, "->", reg, "VALID")
        print("Receipt:", format_receipt(reg))
    else:
        print(raw, "->", reg, "INVALID")
