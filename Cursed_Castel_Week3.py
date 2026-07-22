# The Cursed Castle of Pytheria is an adventure game where the player navigates through a castle, 
# facing challenges and making choices that affect the outcome of the game. 

# This is a introduction function that welcomes the player to the game
# Asks for the player's name.                                
def introduction():
    print("\nYou were transported against your will, but you must survive!")
    print("Welcome to the Cursed Castle of Pytheria!")
    print ("You are on your own")



# Challenge 1: The player must choose a path in the castle.
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
def fight_skeletons(number_of_skeletons, weapon):
    try:
        number_of_skeletons = int(input("\nEnter the number of skeletons to fight: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    for i in range(number_of_skeletons):
        print(f"\nFighting skeleton {i + 1} with your {weapon}...")
        print("You defeated the skeleton!\n")
    print(f"You have defeated all {number_of_skeletons} skeletons!\n")


introduction()

chose_level()

chose_weapon()

treasure_chest()

fight_skeletons()