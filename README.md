# Coffee Machine


# ☕ How the Machine Works:

1. The machine starts with a welcome message and enters a loop where users can interact with it.

2. Users can perform three main functions:
   - **Order**: Users can place an order for coffee by selecting from the available options (Espresso, Latte, Cappuccino). They are prompted to insert coins (quarters, dimes, nickels, and pennies) to pay for their order.

   - **Report**: Users can check the current resource levels (water, milk, coffee) in the machine.

   - **Off**: Users can choose to turn off the machine, which breaks the loop and exits the program.

3. When placing an order:
   - The code checks if there are sufficient resources (water, milk, coffee) to fulfill the order. If not, it informs the user that the machine cannot make the requested coffee.

   - If there are sufficient resources, the code calculates the total cost based on the selected coffee type and the coins inserted by the user.

   - It then checks if the user has inserted enough money. If not, it refunds the money and informs the user.

   - If the user has inserted enough money, it calculates the change, deducts the required resources, and dispenses the coffee.

# 🛠️ Code Specifications:

- `data.resources`: This dictionary holds the current resource levels (water, milk, coffee) in the machine.

- `data.MENU`: This dictionary defines the menu of available coffee types, including their costs and required ingredients.

- The code handles user input and validates orders and payments.

# 🌍 Real-World Use:

This code simulates the operation of a basic coffee machine. It could serve as a starting point for building a real coffee vending machine or a coffee shop point-of-sale system with additional features. This code can be adapted for use in a cafe or coffee shop as a point-of-sale system. It could track orders, manage inventory, and handle payments.



