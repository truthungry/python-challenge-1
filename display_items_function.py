
# Function to display menu items in a category
def display_items(category_items):
    if isinstance(category_items, dict):
        for item, price in category_items.items():
            if isinstance(price, dict):
                print(f"  {item}:")
                for sub_item, sub_price in price.items():
                    print(f"    {sub_item} - ${sub_price:.2f}")
            else:
                print(f"  {item} - ${price:.2f}")
    else:
        print("  No items available in this category.")
