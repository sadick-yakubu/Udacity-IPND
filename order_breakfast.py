import time


def print_pause(message):
    print(message)
    time.sleep(2)


def valid_input(message, option1, option2):
    while True:
        order = input(message).lower()
        if option1 in order:
            break
        elif option2 in order:
            break
        else:
            print_pause("Sorry, I don't understand")
    return order


def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.\n")


def get_order():
    order = valid_input("Please place your order. "
                        "Would you like waffles or pancakes?\n",
                        "waffles", "pancakes")
    if "waffles" in order:
        print_pause("Waffles it is!")
    elif "pancakes" in order:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")
    order_again()


def order_again():
    order = valid_input("Would you like to place another order? "
                        "Please say 'yes' or 'no'.\n",
                        "yes", "no")
    if "yes" in order:
        print_pause("Very good, I'm happy to take another order.\n")
        get_order()
       
    elif "no" in order:
        print("OK, goodbye!")


def order_breakfast():
    intro()
    get_order()


order_breakfast()
