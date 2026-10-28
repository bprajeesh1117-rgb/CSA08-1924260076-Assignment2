"""Q5: Function parameters, mutable defaults, returns, and scope."""

def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order


def calculate_total_and_gst(amount, gst_rate=0.05):
    gst = amount * gst_rate
    return amount + gst, gst


def scope_demo():
    global global_counter
    global_counter += 1
    local_message = "I exist only inside scope_demo"

    def inner():
        nonlocal local_message
        local_message = "Changed by the inner function"
        return local_message

    print("nonlocal:", inner())
    print("local:", local_message)


global_counter = 0


def main():
    print("Buggy calls:")
    print(add_item_buggy("Tea"), add_item_buggy("Vada"))
    print("Correct calls:")
    print(add_item("Tea"), add_item("Vada"))
    print("Buggy defaults:", add_item_buggy.__defaults__)
    total, gst = calculate_total_and_gst(200, gst_rate=0.05)
    print(f"Total including GST: Rs {total:.2f}; GST: Rs {gst:.2f}")
    scope_demo()
    print("global_counter:", global_counter)


if __name__ == "__main__":
    main()
