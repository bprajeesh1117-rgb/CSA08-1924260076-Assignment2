"""Q3: Vehicle registration number normaliser and validator."""

def normalise(text):
    """'tn 09 ab 1234' -> 'TN09AB1234'."""
    return text.strip().replace(" ", "").replace("-", "").upper()


def is_valid(reg):
    """Valid: 2 letters, 2 digits, 1-2 letters, 4 digits."""
    if len(reg) not in (9, 10):
        return False
    if not reg[0:2].isalpha() or not reg[2:4].isdigit():
        return False
    series_length = len(reg) - 8
    if not reg[4:4 + series_length].isalpha():
        return False
    if not reg[-4:].isdigit():
        return False
    return True


def format_receipt(reg):
    if not is_valid(reg):
        raise ValueError("Cannot format an invalid registration number.")
    series_length = len(reg) - 8
    return f"{reg[:2]} {reg[2:4]} {reg[4:4 + series_length]} {reg[-4:]}"


def main():
    samples = [
        "tn 09 ab 1234",
        "KA-01-M-0007",
        "TN9AB1234",
        "TN 22 1234 AB",
        "mh 12 xyz 4567",
        "DL 8 C 1234",
    ]
    for raw in samples:
        reg = normalise(raw)
        status = "valid" if is_valid(reg) else "INVALID"
        receipt = f" | receipt: {format_receipt(reg)}" if is_valid(reg) else ""
        print(f"{raw:18} -> {reg:11} {status}{receipt}")


if __name__ == "__main__":
    main()
