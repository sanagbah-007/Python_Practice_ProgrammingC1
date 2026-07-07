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

#Q7 the code is meant to run a number gussing game where the user guesses
# a secret number in this case the secret number is 7. The user has 3 attempts to guess the number correctly.
def number_guessing_game(secret_number=7, attempts=3):
    secret_number = 7
    attempts = 3
    print(f"\nLet's play a number guessing game {pirate_name}!\n")
    print(f"\nYou have {attempts} attempts to guess the secret number between 1 and 10.\n")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            print("\nCongratulations! You've guessed the secret number!")
            global coins
            coins += 10  # Reward for guessing correctly
            print(f"\n You have earned 10 more coins! Your total coins are now: {coins}\n")
            return True
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

    print("Sorry, you've used all your attempts. The secret number was 7.")
    return False


# Q8 the code is meant to ask the user for word then it will
# repeat the word 5 times.
def repeat_word():
    word = input("Please enter a word to repeat: ")
    print(f"\nRepeating the word '{word}' 5 times:")
    for i in range(5):
        print(word)
    global coins
    coins += 10  # Reward for repeating the word
    print(f"\n Congratulations! 10 more coins have been added to your chest. Your total coins are now: {coins}\n")
    return word

# Q9 the code is meant to display the total a list of items 
# the user has collected during the adventure.
def display_collected_items(items=None):
    if items is None:
        items = ["Sword", "Compass", "Map", "Key", "Lantern"]
    print("\nHere are the items you have collected during your adventure:")
    for item in items:
        print(f"- {item}")

# Q10 the  code is meant ot list the total number of items in the 
# list of items the user has collected during the adventure.
def list_collected_items(items=None):
    if items is None:
        items = ["Sword", "Compass", "Map", "Key", "Lantern"]
    print(f"\nYou have collected a total of {len(items)} items during your adventure:")
    for item in items:
        print(f"- {item}")

# Q11 the code is meant to know whether the user is above or below 18 years old.
# and dcide wether they can continue the adventure or not.
def check_age_eligibility(age):
    if age < 18:
        print(f"\nSorry, {player_name}, you must be at least 18 years old to continue the adventure.")
        print("You can still explore the island, but some challenges may be restricted.\n")
    else:
        print(f"\nGreat! You are eligible to continue the adventure, {player_name}.\n") 

# Q12 the code is meant to display the toal number of coins 
# the user has collected during the adventure and convert 60% of the total coins
# into sliver coins and 40% into gold coins.
def convert_coins(total_coins):
    silver_coins = int(total_coins * 0.6)
    gold_coins = int(total_coins * 0.4)
    print(f"\n This is an appraisal of your coins:")
    print(f"- Silver Coins: {silver_coins}")
    print(f"- Gold Coins: {gold_coins}\n")


introduction()

player_name = get_player_name()

player_age = get_player_age()

pirate_name = create_pirate_name()

temp_coins = calculate_total_coins()

crew_members = share_coins_among_crew(temp_coins)

validate_coin_sharing()

congratulate_player(coins)

guessing_game_result = number_guessing_game()

repeat_word_result = repeat_word()

display_collected_items()

list_collected_items()

check_age_eligibility(player_age)

convert_coins(coins)
