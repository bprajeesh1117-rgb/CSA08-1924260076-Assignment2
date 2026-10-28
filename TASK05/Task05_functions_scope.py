
# TASK 5: Functions and Scope

# 1. Demonstrating the mutable default argument bug
def add_item_bug(item, items=[]):
    items.append(item)
    return items


print("MUTABLE DEFAULT ARGUMENT BUG")
print(add_item_bug("Apple"))
print(add_item_bug("Banana"))
print(add_item_bug("Orange"))


# 2. Correct solution using None
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


print("\nCORRECT SOLUTION")
print(add_item("Apple"))
print(add_item("Banana"))
print(add_item("Orange"))


# 3. Positional, keyword and default arguments
def customer_details(name, age=18, city="Chennai"):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


print("\nCUSTOMER DETAILS")
customer_details("Arun")
customer_details("Priya", 20)
customer_details(name="Kumar", age=21, city="Madurai")


# 4. Returning multiple values
def calculate_bill(amount):
    gst = amount * 0.18
    total = amount + gst
    return total, gst


print("\nBILL CALCULATION")
total, gst = calculate_bill(1000)
print("GST:", gst)
print("Total bill:", total)


# 5. Local and global scope
message = "Global message"


def show_scope():
    message = "Local message"
    print("Inside function:", message)


print("\nVARIABLE SCOPE")
show_scope()
print("Outside function:", message)


# 6. Demonstrating nonlocal
def outer_function():
    count = 0

    def inner_function():
        nonlocal count
        count += 1

    inner_function()
    inner_function()
    print("Count after inner calls:", count)


outer_function()


# 7. Test three independent customers
print("\nTHREE CUSTOMER TESTS")
customers = [
    ("Arun", 1000),
    ("Priya", 2500),
    ("Kumar", 500)
]

for name, amount in customers:
    total, gst = calculate_bill(amount)
    print(name, "| Amount:", amount, "| GST:", round(gst, 2),
          "| Total:", round(total, 2))
