## Module 2 Python Challenge
## By Sheila Mathews

# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
quantity = int()

# Create an empty list. This list will later store a customer's order in dictionary format, as follows:
order_list = []

# Start the ordering process
def take_order():
    print("\nWelcome to Donshe's Food Truck!")
    while True:
        # Display Categories
        print("\nMenu Categories:")
        for index, category in enumerate(menu, start=1):
            print(f"{index}. {category}")

        # Ask the customer for their category chaoice
        menu_selection = input("Which menu item number would you like to order? (or type 'exit' to quit): ").strip()

        # Exit condition
        if menu_selection.lower() == "exit":
            print("Thank you for visiting! Goodbye.")
            break

        # Check if the chosen category is a number
        if not menu_selection.isdigit() or int(menu_selection) not in range(1, len(menu) + 1):
            print("Invalid selection. Please choose from the categoty number.")
            continue

        # Get the selected category
        category_index = int(menu_selection) - 1
        selected_category = list(menu.keys())[category_index]

        print(f"\nYou selected: {selected_category}")
        print("\nHere are the items available in this category:\n")

        # Display items in the selected category
        for item, price in menu[selected_category].items():
            print(f"{item}: ${price}")

        # Ask for item selection
        item_selection = input("\nWhich item would you like to order? (or type exit to return to categories): ")
    
        if item_selection.lower() == "exit":
            continue
        
        # Validate item selection
        if item_selection not in menu[selected_category]:
           print("Invalid item. Please choose an item from the list.")
           continue

        # Ask for quantity
        while True:
            quantity = input(f"How many of '{item_selection}' would you like to order? ")
            try:
                quantity = int(quantity)
            except quantity.isnotdigit():
                print("Invalid input. Defaulting quantity to 1.")
            quantity = 1
            break
        
        # Add to order list
        order = {
            "item_name": item_selection,    
            "price": menu[selected_category][item_selection],
            "quantity": quantity
        }
        order_list.append(order)
        return(f"Added {quantity} '{item_selection}' to your order. \n")
        

    continue_ordering = input("\nWould you like to order from another category? (yes/no): ").strip().lower()
    if continue_ordering != 'y' or "yes":
        print("\nThank you for your order! Have a great day!")
        

price = "Price".strip()
price = price.replace(".", "")

# Call the functon to take the order
take_order ()


total = quantity * price 
print(f"Total: ${total}")

# Print receipt
print(f"{'Item name':<25}| {'Price':<8}| {'Quantity':<8}")
print("-" * 45) 