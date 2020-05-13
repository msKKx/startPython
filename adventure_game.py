import time
import random

pause_time = 2
one_two = "What would you like to do?\n(Please enter 1 or 2.)\n"
run_fight = "Would you like to (1) fight or (2) run away?"
yes_no = "Would you like to play again (y/n)"
input_error = "Your answer was not correct. Please try again."
creature = random.choice(
    ['pirate', 'gorgon', 'troll', 'dragon', 'wicked fairie'])
weapon = random.choice(['sword', 'dagger', 'knife', 'gun'])


def print_pause(string):
    # Prints a text with defined time.sleep delay
    print(string)
    time.sleep(pause_time)


def intro(creature, weapon):
    print_pause(
        "You find yourself standing in an open field, filled with grass "
        + "and yellow wildflowers.")
    print_pause("Rumor has it that a " + creature +
                " is somewhere around here, and has been "
                + "terrifying the nearby village.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty "
        + "(but not very effective) "+weapon+".\n")
    print_pause("Enter 1 to knock on the door of the house.\n")
    print_pause("Enter 2 to peer into the cave.\n")
    print_pause(one_two)


def house(creature, weapon):
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.\n")
    print_pause(
        "You are about to knock when the door opens "
        + "and out steps a " + creature + ".\n")
    print_pause("Eep! This is the " + creature + "'s house!\n")
    print_pause("The " + creature + " attacks you!\n")
    print_pause(
        "You feel a bit under-prepared for this, "
        + "what with only having a tiny "+weapon+".\n")
    print_pause(run_fight)


def cave(weapon):
    # Things that happen to the player goes in the cave
    print_pause("You peer catiously into the cave.\n")
    print_pause("It turns out to be only a very small cave")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old " +
                weapon+" and take the sword with you.")
    print_pause("You walk back out to the field.\n")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.\n")
    print_pause(one_two)


def field():
    # Things that happen to the player goes in the field
    print_pause(
        "You run back into the field. "
        + "Luickly, you don't seem to have been followed.\n")
    print_pause("Enter 1 to knock on the door of the house.\n")
    print_pause("Enter 2 to peer into the cave.\n")
    print_pause(one_two)


def fight(creature, weapon):
    # Things that happen when the player fights
    print_pause("You do your best ... \n")
    print_pause("but your "+weapon+" is no match for the "+creature+".\n")
    print_pause("You have been defeated!")
    print_pause(yes_no)


def play_again():
    # Play again function at the end of the game
    option = get_input_with_two_options("y", "n")
    if option == "y":
        print_pause("Excellent restarting the game...")
        game_start()
    elif option == "n":
        print_pause("Thanks for playing! See you next time")
    else:
        print_pause("Your answer was not correct. Please enter 'y' or 'n'")


def get_input_with_two_options(x, y):
    # solange der input nicht korrekt ist, frage nach input"
    option = input()
    while option != x and option != y:
        print_pause(input_error)
        option = input()
    return option


def house_path():
    house(creature, weapon)
    option = get_input_with_two_options("1", "2")
    if option == "1":
        fight(creature, weapon)
        play_again()
    elif option == "2":
        field_path()
    else:
        print_pause(input_error)


def cave_path():
    cave(weapon)
    option = get_input_with_two_options("1", "2")
    if option == "1":
        house_path()
    elif option == "2":
        cave_path()
    else:
        print_pause(input_error)


def field_path():
    field()
    option = get_input_with_two_options("1", "2")
    if option == "1":
        house_path()
    elif option == "2":
        cave_path()
    else:
        print_pause(input_error)


def game_start():
    intro(creature, weapon)
    option = get_input_with_two_options("1", "2")
    if option == "1":
        house_path()
    elif option == "2":
        cave_path()
    else:
        print_pause(input_error)


game_start()
# Start the Game
