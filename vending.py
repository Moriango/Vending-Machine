import os
sodas = ["Pepsi", "Cherry Coke Zero", "Mountain Dew", "Sprite"]
chips = ["Lays", "Fritos", "Doritos", "Hot Cheetos"]
candy = ["Snickers", "Gum", "Payday", "Eminems"]

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    choice = input("What would you like out of our vending machinge?\n> ")
    try:
        if choice.lower() in {'soda', 'sodas', 'pop'}:
            item = sodas.pop()
        elif choice.lower() in {'chips', 'chip', 'lays', 'snacks'}:
            item = chips.pop()
        elif choice.lower() == 'candy':
            item = candy.pop()
        else:
            print("Sorry, I didn't understand that.")
            continue
    except IndexError:
        clearScreen()
        print("Sorry, we are all out of {}".format(choice))
    else:
        clearScreen()
        print("Thank you for choosing {} section, here are your {}".format(choice, item))
