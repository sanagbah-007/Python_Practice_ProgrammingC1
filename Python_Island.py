# Python_Island is a simple text-based adventure game where the player explores an island, 
# encounters challenges, and makes choices that affect the outcome of the game. 

# Q1 the code is meant to introduce the player.
def introduction():
    print("Welcome to Python_Island!")
introduction()

def get_player_name():
    user_name = input("What is your name, adventurer? ")
    print(f"Hello, {user_name}! Your adventure begins now.")
    return user_name

player_name = get_player_name()

# Q2 the code is meant to get the user's age.
def get_player_age():
    user_age = int(input("How old are you, adventurer? "))
    print(f"Interesting, {player_name}. You are {user_age} years old.")
    return user_age

player_age = get_player_age()

# Q3 the code is meant to create a pirate name for the user.
def create_pirate_name():
    user_favourite_color = input("What is your favorite color, adventurer? ")
    user_favourite_animal = input("What is your favorite animal, adventurer? ")
    pirate_name = f"{player_name} {user_favourite_color} {user_favourite_animal}"
    print(f"Welcome aboard, {pirate_name}, explorer of Python_Island!")
    return pirate_name

pirate_name = create_pirate_name()