"""Q2: OTP verification using while and for loops."""

CORRECT_OTP = "4826"


def verify_while():
    attempts = 0
    while attempts < 3:
        entry = input("OTP (blank does not count): ").strip()
        if entry == "":
            print("Blank entry: try again; attempt not counted.")
            continue
        attempts += 1
        if entry == CORRECT_OTP:
            print("OTP accepted.")
            break
        print(f"Incorrect OTP. Attempts used: {attempts}/3")
    else:
        print("Account locked for 30 minutes.")
    # `pass` is a no-op; shown here as a placeholder for a future audit action.
    if attempts == 0:
        pass


def verify_for():
    for attempt in range(1, 4):
        entry = input("OTP (blank does not count): ").strip()
        if entry == "":
            print("Blank entry: try again; attempt not counted.")
            # A for-loop advances automatically, so continue would consume an iteration.
            # For exact blank-does-not-count behaviour, repeat this attempt with an inner loop.
            while entry == "":
                entry = input("Please enter OTP (blank still does not count): ").strip()
        if entry == CORRECT_OTP:
            print("OTP accepted.")
            break
        print(f"Incorrect OTP. Attempts used: {attempt}/3")
    else:
        print("Account locked for 30 minutes.")


def verify_with_security_question():
    """Illustration: 3 normal attempts, then 2 extra if security answer is correct."""
    attempts = 0
    max_attempts = 3
    security_ok = input("Security answer (demo: blue): ").strip().lower() == "blue"
    if security_ok:
        max_attempts += 2
    while attempts < max_attempts:
        entry = input("OTP: ").strip()
        if not entry:
            print("Blank entry does not count.")
            continue
        attempts += 1
        if entry == CORRECT_OTP:
            print("OTP accepted.")
            break
    else:
        print("Account locked for 30 minutes.")


if __name__ == "__main__":
    mode = input("Choose mode: 1=while, 2=for, 3=security extension: ").strip()
    if mode == "1":
        verify_while()
    elif mode == "2":
        verify_for()
    elif mode == "3":
        verify_with_security_question()
    else:
        print("Invalid mode.")
