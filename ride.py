print("Select your ride option:")
print("1. Bike")
print("2. Car")
# Take input of 1 or 2 from user
# Select your ride option
choice = int(input("Enter your choice (1 or 2): "))
# User entering option 1
if (choice == 1):  # Condition 1 outer if statement
    print("What type of bike?")
    print("1. Scooty\n")
    print("2. Scooter\n")
    # Condition for selecting bike type
    choice2 = int(input("Enter your choice (1 or 2): "))
    if choice2 == 1:  # Inner if ststement
        print("You have selected the Scooty")
    else:
        print("You have selected the Scooter")
# User entering option 2
elif (choice == 2):  # Condition 2 outer if statement
    print("What type of car?")
    print("1. Sedan\n")
    print("2. XUV\n")
    choice3 = int(input("Enter your choice (1 or 2): "))
    if choice3 == 1:  # Inner if statement
        print("You have selected the Sedan")
    else:
        print("You have selected the XUV")
else:
    # Outer else statement
    print("Wrong choice!")
