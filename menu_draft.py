 
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
from pprint import pprint

# Create an empty list. This list will later store a customer's order in dictionary format, as follows:
[
  {
    "Item number": str,
    "Price": float,
    "Quantity": int
  },
]

print()

# Start the ordering process
def take_order():
    print("\nWelcome to Donshe's Food Truck!")
    while True:
        # Display Categories
        print("\nMenu Categories:")
        for index, category in enumerate(menu, start=1):
            print(f"{index},{category}")

        # Ask the customer for their category chaoice
        category_choice = input("From which category would you like to order? (or type 'exit' to quit): ").strip()

        # Exit condition
        if category_choice.lower() == "exit":
            print("Thank you for visiting! Goodbye.")
            break

        # Check if the chosen category is valid
        if category_choice in menu:
            # Display the submenus of the chosen category
            print(f"\nItems in {category_choice}:")# \n{', '.join(menu[category_choice])}")
            for item in menu[category_choice]:
                print(f"- {item}")
        # Check if the chosen item is valid
        item_choice = input(f"Which item would you like to order from {category_choice}?").strip()

        if item_choice in menu[category_choice]:
            #Check if the item has a sub-menu
             if menu[category_choice][item_choice]:
                print(f"\nSub-menu for {item_choice}:")
                for sub_item in menu[category_choice][item_choice]:
                    print(f"- {sub_item}")

                sub_item_choice = input(f"Which menu item of {item_choice} would you like? ").strip()

                if sub_item_choice in menu[category_choice][item_choice]:
                    # Display the submenus of the chosen category
#                    print(f"Items in {category_choice}: {' , '.join(menu[category_choice[item_choice]])}")
                    print(f"Great choice! You ordered {sub_item_choice} {item_choice} from {category_choice}.")
                else:
                    print("Invalid category. Please choose from the available categories.")

        # Ask if the customer wants to continue ordering
        continue_ordering = input("\nWould you like to order from another category? (yes/no): ").strip().lower()
        if continue_ordering != "yes":
            print("Thank you for your order! Have a great day!")
            break

# Call the functon to take the order
take_order ()

