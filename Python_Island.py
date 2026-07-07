# Python_Island is a simple text-based adventure game where the player explores an island, 
# encounters challenges, and makes choices that affect the outcome of the game. 

# Q1 the code is meant to introduce the player.
coins = 0  # Initialize the coin variable to keep track of the player's coins
def introduction():
    print("\nWelcome to Python Island!\n")

def get_player_name():
    user_name = input("What is your name, adventurer? ")
    print(f"Hello, {user_name}! Your adventure begins now.")
    global coins
    coins += 5
    print(f" Congratulations! 5 coins have been added to your chest.\n")
    return user_name


# Q2 the code is meant to get the user's age.
def get_player_age():
    user_age = int(input("How old are you, adventurer? "))
    print(f"Interesting, {player_name}. You are {user_age} years old.")
    global coins
    coins += 5
    print(f" Congratulations! 5 coins have been added to your chest.\n")
    return user_age


# Q3 the code is meant to create a pirate name for the user.
def create_pirate_name():
    user_favourite_color = input("What is your favorite color, adventurer? ")
    user_favourite_animal = input("What is your favorite animal, adventurer? ")
    pirate_name = f"{player_name} {user_favourite_color} {user_favourite_animal}"
    print(f"Welcome aboard, {pirate_name}, explorer of Python Island!")
    global coins
    coins += 5
    print(f" Congratulations! 5 coins have been added to your chest.\n")
    return pirate_name


# Q4 the code is meant to calculate the total coins collected by the user.
def calculate_total_coins():
    temp_coin= int(input("How many coins have you collected so far? ")) # Coins from introduction, age, and pirate name
    if temp_coin < 15 or temp_coin > 15:
        print("Please enter a valid number of coins (15).")
        return calculate_total_coins()  # Recursively ask for input until valid
    print(f" Congratulations! You just added another 5 coins to your chest.")
    global coins
    coins += 5  # Add the coins earned from previous actions
    print(f"Great job {pirate_name}, you have collected a total of {coins} coins so far!\n")
    return coins


# adding function for the congratulation message after the entire adventure
def congratulate_player(coins_earned):
    total_earned = coins_earned
    print("Congratulations! You have successfully completed this part of your adventure.")
    print(f"You have earned {coins_earned} coins for all your efforts.\n")
    print(f"Your total coins are now: {total_earned}\n")  # Adding coins for the congratulation message
    return total_earned

# Q5 the code is meant to ask how many member are in the user's crew and to share the total coins among them.
def share_coins_among_crew(total_coins):
    crew_members = int(input(f"How many members are in your crew, {pirate_name}? "))
    if crew_members > 0:
        coins_per_member = total_coins // crew_members
        print(f"Each member of your crew will receive {coins_per_member} coins.")
        print(f" Congratulations! 5 more coins have been added to your chest.")
        global coins
        coins = total_coins + 5

    else:
        print("You must have at least one crew member to share the coins.")
    return crew_members


# Q6 the code is meant to ask to validate the sharing of coins among the crew members.
def validate_coin_sharing():
    confirmation = input(f"\nDid each member of your crew receive at least 15 coins? (yes/no) ")
    if confirmation.lower() == "yes":
        print("Great! Your crew is happy and well-rewarded.\n")
    else:
        print("Oh no! you need more coins to encourage your crew.\n")

    global coins
    coins += 5

introduction()

player_name = get_player_name()

player_age = get_player_age()

pirate_name = create_pirate_name()

temp_coins = calculate_total_coins()

crew_members = share_coins_among_crew(temp_coins)

validate_coin_sharing()

congratulate_player(coins)
