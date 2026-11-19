robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}
while True:
    player_choice = input("What would you like to do:"
                          "\nA: View All Settings"
                          "\nB: Look Up a setting value"
                          "\nC: Change a Setting"
                          "\nD: Add a Setting"
                          "\nE: Exit"
                          "\n").strip().lower()
    if player_choice == "a":
        for key, value in robot.items():
            print(f"{key.capitalize()} : {value}")
    elif player_choice == "b":
        while True:
            key = input("What specific setting do you want to see?"
                        "\n")
            if robot.get(key) != None:
                print(f"The value of {key} is {robot.get(key)}")
            else:
                print("This setting does not exist")
            break
    elif player_choice == "c":
        while True:
            key = input("What specific setting value do you want to change?"
                        "\n").strip().lower()

            if robot.get(key) == None:
                print("This setting does not exist")
            else:
                change = input("What would you like to replace its value with?"
                      "\n")
                while True:
                    response = input("Is this value an "
                                   "\nA: Integer"
                                   "\nB: Float"
                                   "\nC: String"
                                   "\n").strip().lower()
                    if response == "a":
                        try:
                            change = int(change)
                            break
                        except ValueError:
                            print("That isn't a valid integer.")
                    elif response == "b":
                        try:
                            change = float(change)
                            break
                        except ValueError:
                            print("That isn't a valid integer.")
                    elif response == "c":
                        change = str(change)
                        break
                    else:
                        print("Invalid input, try again.")
                robot[key] = change
                print("Change has been made.")
            break

    elif player_choice == "d":
        inp = input("What is setting you would like to add?"
                    "\n").lower().strip()
        if inp in robot:
            print("Value already exists!")
        else:
            robot[inp] = ""
            print("Setting has been added.")
    elif player_choice == "e":
        break
