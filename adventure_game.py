# Import necessary modules
import time
import random


# Function for printing and pausing for a few seconds
def print_and_delay(message_to_print):
    print(message_to_print)
    time.sleep(2)


# Function for game introduction
def game_intro(enemy):
    print_and_delay("You woke up in the scorching desert one afternoon,")
    print_and_delay("with endless sand dunes stretching out in all "
                    "directions.")
    print_and_delay(f"Rumors have it that a menacing {enemy} is "
                    "lurking somewhere in this barren wasteland.")
    print_and_delay("Before you stands a lonely desert shack.")
    print_and_delay("To your right, a dark and ominous cave entrance beckons.")
    print_and_delay("In your hand, you hold a very inefficient "
                    "and rusty dagger.\n")


# Function to validate user input
def validate_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if response == option1:
            break
        elif response == option2:
            break
        else:
            print_and_delay("Invalid input, please provide a valid response")
    return response


# Function for player to enter the house
def enter_shack(enemy, weapons_list, weapon):
    print_and_delay("You approach the lonely shack cautiously.")
    print_and_delay(f"As you raised your hand to knock, the door swings open, "
                    f"revealing a fearsome {enemy}.")
    print_and_delay(f"OMG!!! this shack belongs to the {enemy}!")
    print_and_delay(f"The {enemy} attacks you!")
    if weapons_list not in weapon:
        print_and_delay("You feel unprepared with just your rusty dagger.")
        print_and_delay("Having just a rusty dagger")
        flee_or_fight(enemy, weapons_list, weapon)
    else:
        flee_or_fight(enemy, weapons_list, weapon)


# Function for user to enter the cave
def enter_tunnel(enemy, weapons_list, weapon):
    print_and_delay("You venture into the ominous cave.")
    if weapons_list not in weapon:
        print_and_delay("Inside, you find an assortment of weapons.")
        print_and_delay(f"You took the {weapons_list}!\n"
                        f"You swap your rusty dagger for the {weapons_list}.")
        weapon.append(weapons_list)
    else:
        print_and_delay("You already have an impressive weapon "
                        "in your inventory\n"
                        "You are good to go")
    print_and_delay("You return to the desert, armed and ready.\n")
    shack_or_tunnel(enemy, weapons_list, weapon)


# Function loop for house or cave selection
def shack_or_tunnel(enemy, weapons_list, weapon):
    print_and_delay("Enter 1 to knock on the shack's door.")
    print_and_delay("Enter 2 to venture into the mysterious cave.")
    response = validate_input("What would you like to do?\n"
                              "(Please enter 1 or 2.)\n", "1", "2")
    if response == "1":
        enter_shack(enemy, weapons_list, weapon)
    elif response == "2":
        enter_tunnel(enemy, weapons_list, weapon)


# Function for user to fight with or without weapon
def fight(enemy, weapons_list, weapon):
    if weapons_list in weapon:
        print_and_delay(f"You attack the {enemy} with your {weapons_list}.")
        print_and_delay(f"The battle is fierce, but your {weapons_list} "
                        "prevails!")
        print_and_delay("You have vanquished the enemy and saved the desert.\n"
                        "You are victorious!\n")
        restart()

    else:
        print_and_delay(f"The {enemy} strikes you, "
                        "dealing massive damage to you")
        print_and_delay(f"but your rusty dagger is no match for the {enemy}.")
        print_and_delay("You have been defeated!\n")
        restart()


# Function for user to flee with or without weapon
def flee(enemy, weapons_list, weapon):
    print_and_delay("Running back into the desert")
    print_and_delay("You weren't followed")
    if weapons_list in weapon:
        print_and_delay(f"With your {weapons_list} I am confident "
                        f"you can conquer the {enemy}\n")
    else:
        print_and_delay("You are lucky to not have attacked unprepared")
        print_and_delay("But you need to find a new weapon")
        print_and_delay("How about you check in the cave "
                        "to see what's in store for you?\n")
    shack_or_tunnel(enemy, weapons_list, weapon)


# Function loop for fight or flee
def flee_or_fight(enemy, weapons_list, weapon):
    response = validate_input("Would you like to (1) fight "
                              "or (2) flee?\n", "1", "2")
    if response == "1":
        fight(enemy, weapons_list, weapon)
    elif response == "2":
        flee(enemy, weapons_list, weapon)


# Function for user to replay or quit game
def restart():
    restart = validate_input("Would you like to restart? "
                             "(y/n)\n", "y", "n")
    if restart == "y":
        print_and_delay("Excellent! Restarting the game ...\n")
        start_game()
    elif restart == "n":
        print_and_delay("Whew! that was fun, OH! wow it was just a dream.")
        print_and_delay("See you soon on the desert or who knows where "
                        "your dreams will take you next ...")


# Game start function
def start_game():
    enemy = random.choice(["sandstorm", "giant scorpion", "desert bandit",
                           "mummy", "vulture"])
    weapons_list = random.choice(["old revolver", "ancient scimitar",
                                  "loaded crossbow", "magic staff",
                                  "sword of ogoroth"])
    weapon = []
    game_intro(enemy)
    shack_or_tunnel(enemy, weapons_list, weapon)


# Game function call
start_game()
