# The Cursed Castle of Pytheria is an adventure game where the player navigates through a castle, 
# facing challenges and making choices that affect the outcome of the game. 

# This is a introduction function that welcomes the player to the game
# Asks for the player's name.                                
def introduction():
    print("\nYou were transported against your will, but you must survive!")
    print("Welcome to the Cursed Castle of Pytheria!")
    print ("You are on your own")



# Challenge 1, the player must choose a path in the castle.
# Create check_level(player_name, level). Use an if statement. If level >= 5, 
# print 'The gateopens!'; otherwise print 'You are not strong enough!'
def chose_level():
    try:
        # get player name and level
        player_name = input("\nEnter your name: ")
        level_str = input("Choose a level (number): ")
        level = int(level_str)
    except ValueError:
        print("Invalid level. Please enter a number.")
        return
    except Exception:
        print("An error occurred.")
        return

    # the nested function is here to check level as requested
    def check_level(player_name, level):
        if level >= 5:
            print('The gateopens!')
        else:
            print('You are not strong enough!')

    check_level(player_name, level)


# Challenge 2 is meant to provide a menu for the user to chose a weapon.
# choose_weapon(weapon). Use if/elif/else for sword, bow, staff and invalid weapon.
def chose_weapon():
    try:
        weapon = input("\nChoose a weapon (sword/bow/staff): ")
    except Exception:
        print("An error occurred reading the weapon.")
        return

    # validate and describe chosen weapon, then return it
    if weapon == 'sword':
        print('You swing the sword like a knight.\n')
    elif weapon == 'bow':
        print('You hold an arrow and take aim.\n')
    elif weapon == 'staff':
        print('You can open portals through your staff.\n')
    else:
        print('Invalid weapon.')
        return chose_weapon()

    return weapon


# Challenge 3 is meant to reward a user after they open 10 chests
# Use a for loop to open five treasure chests. Then create collect_gold(number_of_chests)
# where each chest gives 10 gold coins.
def treasure_chest():
    for i in range(5):
        print(f"\nOpening chest {i + 1}...")
    
    def collect_gold(number_of_chests):
        gold = number_of_chests * 10
        print(f"\nYou collected {gold} gold coins!\n")
    
    collect_gold(5)


# Challenge 4 the code is meant to Create fight_skeletons(number_of_skeletons).
# the user must input a number of skeletons to fight. 
# Use a for loop to defeat each skeletonw with the weapon they chose.
def fight_skeletons(number_of_skeletons = None, weapon = None):
    try:
        if number_of_skeletons is None:
            number_of_skeletons = int(input("\nEnter the number of skeletons to fight: "))
        if weapon is None:
            # get weapon by calling chose_weapon which returns the validated weapon
            weapon = chose_weapon()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    for i in range(number_of_skeletons):
        print(f"\nFighting skeletons {i + 1} with your {weapon}...")
        print("You defeated the skeleton!\n")
    print(f"You have defeated all {number_of_skeletons} skeletons!\n")


# Challenge 5 is meant to create drink_potions(number_of_potions, health). 
# Each potion restores 10 HP. Health cannot exceed 100.
def drink_potions(number_of_potions=None, health=None):
    if health is None:
        health = 50  # Ensure health does not exceed 100 at the start
    if number_of_potions is None:
        number_of_potions = (100 - health) // 10  # Calculate how many potions can be used to reach 100 HP

    print(f"\nYou have {number_of_potions} potions to drink from. Your current health is {health} HP.\n")
    for i in range(number_of_potions):
        if health < 100:
            health += 10
            if health > 100:
                health = 100
            print(f"\nYou drank potion {i + 1}. Your health is now {health} HP.\n")
        else:
            print("\nYour health is already full. You cannot drink more potions.\n")
            break
    return health


# Challenge 6 is meant to Create fight_guardian(guardian_health). 
# Use a while loop until the guardian reaches 0HP.
def fight_guardian(guardian_health=100):
    print(f"\nYou are facing the guardian with {guardian_health} HP at the final gate.")
    print("1 strike = -1 HP")
    while guardian_health > 0:
        try:
            damage = int(input("Enter the number of strikes you want to inflict on the guardian: "))

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if damage < 0:
            print("Damage cannot be negative. Try again.")
            continue

        guardian_health -= damage
        if guardian_health > 0:
            print(f"\nYou inflicted {damage} strikes. Guardian's health is now {guardian_health} HP.\n")
            print("The guardian is still alive! Redo!\n")
            return fight_guardian(guardian_health)
        elif guardian_health <= 0:
            print(f"\nYou inflicted {damage} strikes. Guardian's health is now {guardian_health} HP.\n")
            print("Congratulations! You have defeated the guardian!\n")
            break


# Challenge 7 is meant to ask the user to guess a secret number
# and give them hints if this high or low to open the final gate. 
# The user has 3 attempts to guess the number.
# Secret number is 7. Create unlock_door(guess) using if/elif/else.
def unlock_door(guess=None):
    print("\nYou need to guess the secret number to unlock the final door.")
    secret_number = 7
    attempts = 3

    for attempt in range(attempts):
        if guess is None:
            guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Congratulations! You have unlocked the door!")
            return True
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        guess = None

    print("You have run out of attempts. Try again.")
    return False
    

# The main functions to run the game
introduction()

chose_level()

chose_weapon()

treasure_chest()

fight_skeletons()

drink_potions()

fight_guardian()

unlock_door()