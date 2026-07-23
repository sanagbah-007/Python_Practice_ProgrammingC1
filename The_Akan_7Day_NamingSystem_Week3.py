# The Akan naming system is based on the day of the week a child is born. 
# Each day has a corresponding name for both males and females.
# The following code defines a function that takes the day of the week as input 
# and returns the corresponding Akan name for both males and females.
# The goal is to create a simple program that can be used
#  to determine Akan names based on the day of 
# the week just from the input of the date of birth.

# The 1st function is meant to welcome the user and ask for their name and country.
def welcome_user():
    print("\nWelcome to the Akan Naming System!\n")
    global name, country
    name = input("Please enter your name: ")
    country = input("Please enter your country: ")
    print(f"\nHello {name} from {country}! Let's find out your Akan name based on your date of birth.\n")
    return name, country


# The 2nd function is meant to display a menu of the days of the week 
# and their corresponding Akan names for both males and females.
# and ask the user to input their gender and date of birth.
def display_days_and_names():
    days_of_week = {
        "Sunday": {"male": "Kwasi", "female": "Akosua"},
        "Monday": {"male": "Kwadwo", "female": "Adwoa"},
        "Tuesday": {"male": "Kwabena", "female": "Abena"},
        "Wednesday": {"male": "Kwaku", "female": "Akua"},
        "Thursday": {"male": "Yaw", "female": "Yaa"},
        "Friday": {"male": "Kofi", "female": "Afia"},
        "Saturday": {"male": "Kwame", "female": "Ama"}
    }
    print("\nHere are the Akan names for each day of the week.\n")
    for day, names in days_of_week.items():
        print("the Akan names for " + day + " are:")
        print(f"Male - {names['male']}, Female - {names['female']}")

    gender = input("\nPlease enter your gender (male/female): ").lower()
    if gender not in ["male", "female"]:
        print("Invalid gender. Please enter 'male' or 'female'.")
        return display_days_and_names()

    date_of_birth = input("\nPlease enter your date of birth (YYYY-MM-DD): ")
    try:
        year, month, day = map(int, date_of_birth.split('-'))
        import datetime
        birth_date = datetime.date(year, month, day)
        day_name = birth_date.strftime("%A")
        if day_name in days_of_week:
            akan_name = days_of_week[day_name][gender]
            print(f"\nYou were born on a {day_name}. Your Akan name is {akan_name}.")
        else:
            print("Could not determine Akan name for that date.")
    except ValueError:
        print("Invalid date. Please enter the date in YYYY-MM-DD format.")
        return display_days_and_names()

# This is meant to congratulate the user and add their Akan name to their name.
    print(f"\nCongratulations {name} of {country}! Your Akan name is {akan_name}.")
    print("Thank you for using the Akan Naming System!\n")


intro = welcome_user()

display_days_and_names()

