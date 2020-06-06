import time
import random
import sys


def print_time(message_to_print):
    print(message_to_print)
    time.sleep(2)


weapons = ["pistol", "sword", "magic knife", "pepper spray"]


enemies = ["Blair witch", "troll", "orc", "big foot"]


florest = ["one", "two"]


fight = ['1', '2']


def intro():
    print_time("You are in a big forest.")
    print_time("And arriving at a small clearing\n"
               "you are faced with an old hut.")
    print_time("You know that in the forest there are many dangers\n"
               "but you need a place to rest.")
    print_time("After thinking for a moment\n"
               "you realize that there are two possibilities.")
    print_time("(1) The first possibility is to continue traveling for some\n"
               "kilometers to the nearest village.")
    print_time("(2) The second possibility is to enter the old hut for\n"
               "rest and leave the next morning.")
    choice_way()


def house_route():
    print_time("You go into the old hut and come across a creature:\n"
               f"{random.choice(enemies)}.")
    print_time("You have two choices:")
    print_time("(1) You run away and go back to the forest.")
    print_time("(2) You struggle with one\n"
               f"{random.choice(weapons)} that you carry around your waist.")
    fight_choice()


def fight_choice():
    response = input("Please enter 1 or 2.\n")
    if response == "1":
        print_time("When you encounter the enemy, you decide to flee and\n"
                   "running back to the forest towards the village.")
        print_time("End of the game for you who are not an adventurer\n"
                   "and you weren't even aware of the forest.:(")
    else:
        if f'{random.choice(fight)}' == '1':
            print_time("You are faced with the enemy.")
            print_time("You fight with your available weapon.")
            print_time("You defeat the enemy and win.")
            print_time("Congratulations you won the game!:)")
        else:
            print_time("You fight with the enemy,\n"
                       "but your weapon is not very effective against him.")
            print_time("Your enemy has a powerful magic sword\n"
                       "and defeated you.")
    play_again()


def florest_route():
    if f'{random.choice(florest)}' == "one":
        print_time("Despite being tired you decide to follow\n"
                   "a few more kilometers until you reach the village.")
        print_time("You make that decision based on the news\n"
                   "that you learned about a witch inhabits the forest.")
        print_time("Did you learn about the forest before\n"
                   "to enter it, so you won the game! :)")
    elif f'{random.choice(florest)}' == "two":
        print_time("You return to the forest and head towards the village.")
        print_time("But you fall into a big bear trap and\n"
                   "you end up seriously injured and you die.")
        print_time("Game over! :(")
    play_again()


def play_again():
    print_time("Would you like to play again?")
    response = input("y or n?\n")
    if "y" in response:
        play_adventure_game()
    elif "n" in response:
        print_time("OK, have a nice week!")
        sys.exit()
    else:
        print_time("Sorry this isn't the answer.")
        play_again()


def choice_way():
    way = input("Please enter 1 or 2.\n")
    if way == '1':
        florest_route()
    elif way == '2':
        house_route()
    else:
        choice_way()


def play_adventure_game():
    items = []
    intro()
    choice_way()


play_adventure_game()
