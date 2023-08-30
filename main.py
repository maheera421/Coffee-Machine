import data

print(data.logo)

proceed = "Yes"
while proceed == "Yes":
    print("--------------------------------------------------")
    func = input('If you want to place an order, type "order"\n'
                 'If you want the resource report, type "report"\n'
                 'If you want to turn off the machine, type "off": ')
    print("--------------------------------------------------")

    if func == "report":
        print(f'Water = {data.resources["water"]}ml')
        print(f'Milk = {data.resources["milk"]}ml')
        print(f'Coffee = {data.resources["coffee"]}g')

    elif func == "off":
        break

    elif func == "order":
        # checking for resources
        if data.resources["water"] <= 0 or data.resources["milk"] <= 0 or data.resources["coffee"] <= 0:
            print(f"Sorry, the machine does not have sufficient resources to make your {order}.")
            continue

        # order placement
        order = input("What would you like?\n"
                      "Espresso for $1.50\n"
                      "Latte for $2.50\n"
                      "Cappuccino for $3.00: ")

        # money conversion into cents
        print("\nPlease insert coins.")
        quarters = int(input("How many quarters?: "))
        quarters *= 25
        dimes = int(input("How many dimes?: "))
        dimes *= 10
        nickles = int(input("How many nickles?: "))
        nickles *= 5
        pennies = int(input("How many pennies?: "))

        total_cents = quarters + dimes + nickles + pennies
        total_dollars= total_cents / 100

        # transaction processing
        if order == "espresso":
            change = total_dollars - data.MENU["espresso"]["cost"]
            Change = round(change, 2)

            if Change > 0.00:
                print(f"\nHere is ${Change} in change.")
                print(f"Here is your {order}☕. Enjoy!")

                # deduction from resources
                data.resources["water"] = data.resources["water"] - data.MENU["espresso"]["ingredients"]["water"]
                # resources["milk"] = resources["milk"] - MENU["espresso"]["ingredients"]["milk"]
                data.resources["coffee"] = data.resources["coffee"] - data.MENU["espresso"]["ingredients"]["coffee"]
            elif Change < 0.00:
                print("Sorry, that's not enough money. Money refunded.")

        elif order == "latte":
            change = total_dollars - data.MENU["latte"]["cost"]
            Change = round(change, 2)

            if Change > 0.00:
                print(f"\nHere is ${Change} in change.")
                print(f"Here is your {order}☕. Enjoy!")

                #deduction from resources
                data.resources["water"] = data.resources["water"] - data.MENU["latte"]["ingredients"]["water"]
                data.resources["milk"] = data.resources["milk"] - data.MENU["latte"]["ingredients"]["milk"]
                data.resources["coffee"] = data.resources["coffee"] - data.MENU["latte"]["ingredients"]["coffee"]
            elif Change < 0.00:
                print("Sorry, that's not enough money. Money refunded.")

        elif order == "cappuccino":
            change = total_dollars - data.MENU["cappuccino"]["cost"]
            Change = round(change, 2)

            if Change > 0.00:
                print(f"\nHere is ${Change} in change.")
                print(f"Here is your {order}☕. Enjoy!")

                #deduction from resources
                data.resources["water"] = data.resources["water"] - data.MENU["cappuccino"]["ingredients"]["water"]
                data.resources["milk"] = data.resources["milk"] - data.MENU["cappuccino"]["ingredients"]["milk"]
                data.resources["coffee"] = data.resources["coffee"] - data.MENU["cappuccino"]["ingredients"]["coffee"]
            elif Change < 0.00:
                print("Sorry, that's not enough money. Money refunded.")

        continue

