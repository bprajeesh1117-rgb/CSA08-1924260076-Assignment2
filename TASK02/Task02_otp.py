
# Q2: OTP Verification

correct_otp = "1234"


# Method 1: Using while loop
def verify_while():
    attempts = 0

    while attempts < 3:
        otp = input("Enter OTP: ")

        if otp == "":
            print("Blank entry does not count")
            continue

        attempts += 1

        if otp == correct_otp:
            print("OTP verified successfully")
            break

        print("Wrong OTP")

    else:
        print("Account locked for 30 minutes")


# Method 2: Using for loop
def verify_for():
    attempts = 0

    for i in range(3):
        otp = input("Enter OTP: ")

        if otp == "":
            print("Blank entry does not count")
            attempts -= 1
            continue

        attempts += 1

        if otp == correct_otp:
            print("OTP verified successfully")
            break

        print("Wrong OTP")

    else:
        print("Account locked for 30 minutes")


# pass demonstration
def placeholder():
    pass


print("1. While loop")
print("2. For loop")

choice = input("Choose method: ")

if choice == "1":
    verify_while()
elif choice == "2":
    verify_for()
else:
    print("Invalid choice")
