import time
import random

ENEMY_LIST = ["Beast", "dinosaur", "huged spieder"]
CHOOSE_MAGIC_LIST = ["fire", "run", "super"]


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("Welcome to the game.")
    print_pause("Now you at a cross road.")
    print_pause("To your right is a green road")
    print_pause("To your left is a black road")
    print_pause("We have a gift for you, it's courage. We hope the courage magic always with you")
    print_pause("Place choose a road you like, each road has different situation that you will meet. Good luck!")


def green_road(items):
    choose_enemy = random.choice(ENEMY_LIST)
    print_pause("You walk on the road, flowers in both side are very beautiful. It's seems like a good beginning.")
    print_pause(f"But suddenly a {choose_enemy} appeared in front.")
    print_pause(f"{choose_enemy} attacks you!")
    choose_act(items, choose_enemy)


def black_road(items):
    choose_magic = random.choice(CHOOSE_MAGIC_LIST)
    if "fire" in items and "run" in items and "super" in items:
        print_pause("You've been here before, and have all magic you need.")
        print_pause("Go to adventure, fairy said")
        print_pause("You at the cross_road.")
        choose_road(items)
    if "fire" in items or "run" in items or "super" in items:
        print_pause("You still worry about your journey. Don't worry, I have a gift for you, she said.")
        print_pause(f"It's a {choose_magic} magic!")
        print_pause("You walk back out to the cross_road.")
        items.append(choose_magic)
        choose_road(items)
    else:
        print_pause("You walk on the road, you walk very slowly, because you think it's must something around here.")
        print_pause("You see someone in front of you. Oh she's a fairy, she is so beautiful.")
        print_pause("Oh, how a brave adventurer. I have a gift for you, she said.")
        print_pause(f"It's a {choose_magic} magic!")
        print_pause("You walk back out to the cross_road.")
        items.append(choose_magic)
        choose_road(items)


def fight(items, enemy):
    if "fire" in items or "super" in items:
        print_pause(f"As the {enemy} moves to attack, you use the magic.")
        print_pause(f"The {enemy} runs away!")
        print_pause(f"You win the {enemy}. You are victorious!")
    else:
        print_pause("You do your best...")
        print_pause(f"but your magic is no enough for the {enemy}. You have been defeated!")
        print_pause("GAME OVER")
    again_game(items)


def cross_road(items, enemy):
    if "run" in items:
        print_pause("You run back at a cross Road, you are safe now. ")
        choose_road(items)
    else:
        print_pause(f"You don't have run magic, you can't run away. {enemy} attack you.")
        print_pause("You have been defeated!")
        print_pause("GAME OVER")
    again_game(items)


def choose_road(items):
    print_pause("Place choose a road?(Please enter 1 or 2.)")
    place = input("1. Go to green Road.\n"
                  "2. Go to black Road.\n")
    if place == '1':
        green_road(items)
    elif place == '2':
        black_road(items)
    else:
        print_pause("Please enter 1 or 2")
        choose_road(items)


def choose_act(items, enemy):
    print_pause("Would you like to?(Please enter 1 or 2.)")
    act = input("1. fight\n"
                "2. run away\n")
    if act == '1':
        fight(items, enemy)
    elif act == '2':
        cross_road(items, enemy)
    else:
        print_pause("Please enter 1 or 2")
        choose_act(items)


def again_game(items):
    response = input("Would you like to play again?(y/n)").lower()
    if response == "y":
        play_game()
    elif response == "n":
        print_pause("Thank you for your play")
    else:
        print_pause("Please enter y or n")
        again_game(items)


def play_game():
    items = list()
    intro()
    choose_road(items)


play_game()
