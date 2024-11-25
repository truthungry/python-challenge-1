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

# This list will be used to store the customer's order in dictionary format
order_list = []

# Function to display menu items in a category; 
#   # Utilized examples on Python.org and stack overflow to help determine how to better organize this function  
def print_items(menu_items):
    if isinstance(menu_items, dict):
        for item, price in menu_items.items():
            if isinstance(price, dict):
                print(f"  {item}:")
                for sub_item, sub_price in price.items():
                    print(f"    {sub_item} - ${sub_price:.2f}")
            else:
                print(f"  {item} - ${price:.2f}")
    else:
        print("  No items available in this category.")
                                                                                                                                                                                                                                                    
# Function to calculate the total cost of the order by taking the item price and multiply by quantity
def calculate_total(order_list):
    total = 0
    for order in order_list:
        total += order["price"] * order["quantity"]
    return total

# Function to start the order process
def take_order():
    print("\nWelcome to Donshe's Food Truck!")
    while True:
        # Display Categories
        print("\nMenu Categories:")
        for index, category in enumerate(menu.keys(), start=1):
            print(f"{index}. {category}")

        # Get category choice from customer and validate input
        menu_selection = input("\nEnter a category number (or type 'exit' to quit): ").strip()
        if menu_selection.lower() == "exit":
            break
        if not menu_selection.isdigit() or int(menu_selection) not in range(1, len(menu) + 1):
            print("Invalid selection. Please choose a category number.")
            continue
        
        category = list(menu.keys())[int(menu_selection) - 1]
        print(f"\nYou selected: {category}\n")
        print_items(menu[category])

        # Get item choice from customer and validate input
        item_choice = input("\nEnter the name of the item you'd like to order (or type 'back' to choose another category): ").strip()
        if item_choice.lower() == "back":
            continue
        if item_choice not in menu[category]:
            print("Invalid item selection. Please choose an item from the menu.")
            continue

        # Handle sub-menu items (pizza types, soda sizes, etc.)
        item_price = menu[category][item_choice]
        if isinstance(item_price, dict):
            print("\nAvailable options:")
            for option, price in item_price.items():
                print(f"  {option} - ${price:.2f}")

            sub_choice = input("Choose an option: ").strip()
            if sub_choice not in item_price:
                print("Invalid option. Returning to menu selection.")
                continue
            item_price = item_price[sub_choice]
            item_choice += f" ({sub_choice})"

        # Get quantity
        while True:
            quantity_input = input(f"How many of '{item_choice}' would you like to order? ").strip()
            if not quantity_input.isdigit() or int(quantity_input) <= 0:
                print("Invalid quantity. Please enter a positive number.")
                continue
            quantity = int(quantity_input)
            break

        # Append this order to order list
        order = {
            "item_name": item_choice,
            "price": item_price,
            "quantity": quantity
        }
        order_list.append(order)
        print(f"Added {quantity} x '{item_choice}' to your order.")

        # Continue ordering?
        continue_ordering = input("\nWould you like to order from another category? (yes/no): ").strip().lower()
        if continue_ordering not in ["yes", "y"]:
            break

    # Print receipt
    print("\nYour Order:")
    print(f"{'Item Name':<30} {'Price':<10} {'Quantity':<10} {'Total':<10}")
    print("-" * 60)
    for order in order_list:
        total_price = order["price"] * order["quantity"]
        print(f"{order['item_name']:<30} ${order['price']:<9.2f} {order['quantity']:<10} ${total_price:<9.2f}")
    print("-" * 60)
    print(f"{'Grand Total':<30} {'':<10} {'':<10} ${calculate_total(order_list):<9.2f}")
    
    print("\nThank you for visiting Donshe's Food Truck!")

# Call the function to take the order
take_order()
