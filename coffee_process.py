def make_again():
    choice = input("Do you want to play again? (yes/no): ").strip().lower()
    if choice == 'yes':
        introduction()
    elif choice == 'no':
        print("Thank you for playing! \t BREW BREW UNTIL NEXT TIME!")
    else:
        print("Invalid choice. Please try again.")
        make_again()

def add_milk_sugar():
    print("You've decided to add milk and sugar! Great!")
    print("Add milk and sugar to your taste. You can also add a pinch of cinnamon or cardamom for extra flavor.")
    print("Enjoy your coffee!")
    make_again()

def hot_coffee():
    print("You've decided to make a hot coffee! Good choice!")
    print("Start by grinding fresh coffee beans to a medium-coarse consistency.")
    print("Add hot water (just below boiling) to the grounds, and let it steep for a few minutes.")
    print("Pour the freshly brewed coffee into your favorite mug and SIP IT;) YAYA")
    print("Would you like to add milk and sugar?")
    choice = input("Enter 'yes' or 'no' ").strip().lower()
    if choice == 'yes':
        add_milk_sugar()
    elif choice == 'no':
        print("Enjoy your coffee!")
        make_again()
    else:
        print("Invalid choice. Please enter again:(")
        hot_coffee()

def add_sugar():
    print("You've decided to add sugar! Great, even I like it sweet! ;)")
    print("Add sugar to your taste. You can also add a pinch of cinnamon or cardamom for extra flavor.")
    print("Enjoy your coffee!")
    print("Have a great day")
    make_again()

def cold_coffee():
    print("You've decided to make a cold coffee! Good choice!")
    print("Start by brewing a strong cup of coffee and let it cool down.")
    print("Add milk, sugar, and ice to the coffee.")
    print("Blend it well and pour it into a glass. You can also add a scoop of vanilla for better taste")
    print("Also would you like to add more sugar?")
    choice = input("Enter 'yes' or 'no' ").strip().lower()
    if choice == 'yes':
        add_sugar()
    elif choice == 'no':
        print("Enjoy your coffee!")
        make_again()
    else:
        print("Invalid choice. Please enter again:(")
        cold_coffee()

def myself():
    print("You've decided to make it yourself! Good choice!")
    print("You have the following ingredients: coffee beans, milk, sugar, and water.")
    print("What would you like to make?")
    choice = input("Enter 'hot' or 'cold' ").strip().lower()
    if choice == 'hot':
        hot_coffee()
    elif choice == 'cold':
        cold_coffee()
    else:
        print("Invalid choice. Please enter again:(")
        myself()

def go_to_cafe():
    print("You've decided to go to a cafe! Good choice!")
    print("You can try different types of coffee and enjoy the ambiance.")
    print("Have a great day")
    make_again()

def introduction():
    print("Welcome to Arpita's Kitchen!")
    print("Adventure in life is good; consistency in coffee even better. So let's get started!")
    print("Do you want to make it yourself or go to a cafe?")
    choice = input("Enter 'myself' or 'cafe' ").strip().lower()
    if choice == 'myself':
        myself()
    elif choice == 'cafe':
        go_to_cafe()
    else:
        print("Invalid choice. Please enter again:(")
        introduction()

if __name__ == "__main__":
    introduction()
