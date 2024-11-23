#                        Module 2 Challenge: Python Challenge 1

### Design an interactive ordering system for a food truck menu. 
##  This program outlines the steps to manage and validate user inputs, then store the customer's orders and prints a formattedd receipt.
 and prints a receipt with the total price of all items ordered.
    Fix:
        * Enumerate line 89, the selected_category list - Format
        * Same list, when user chooses an item with a sub-menu, like Tea > Green...It is this sub-menu that has the pricing attached, but when I type anything but 'tea' I get an error, so I need to check that validation...but choosing tea, doesn't give the user the choice to choose from the sub-menu, so it just prints 'Tea and asks how many...
        * When user has finished ordering, and trying to print the receipt, it gives a typeError related to item_name, a string, needs to be an integer
        * 
Done - After the sub-menu is printed, prompt the customer to enter their selection from the menu, saving it as a variable menu_selection.

Use input validation to check if the customer input menu_selection is a number. If it isn't, print an error message. If it is a number, convert the input to an integer and use it to check if it is in the keys of menu_items.

If the user input is not in the menu_items keys, print an error. Otherwise, perform the following actions:

Get the item name from the menu_items dictionary and store it as a variable.

Ask the customer for the quantity of the menu item, using the item name variable in the question, and let them know that the quantity will default to 1 if their input is invalid. Save their answer as a variable called quantity.

Check that the customer input is a number. If it isn't, set the quantity to the value 1. If it is a number, convert the variable to an integer.

Append the customer's order to the order list in dictionary format with the following keys: "Item name", "Price", and "Quantity. You will need this information to print the receipt at the end of the order. The price should be found in the menu_items dictionary.

Inside the continuous while loop that prompts the customer if they would like to keep ordering, write a match:case statement that checks for y or n (upper or lowercase), and includes a default option if neither letter is entered by the customer. The following actions should be performed for each case:

y: Set the place_order variable to True and break from the continuous while loop.

n: Set the place_order variable to False, print "Thank you for your order", and break from the continuous while loop.

Default: Tell the customer to try again because they didn't type a valid input.

Order Receipt
Create a for loop to loop through the order list.

Inside the loop, save the value of each key as their own variable: item_name, price, and quantity.

Calculate the number of empty spaces that should be added to the display so that the receipt uses the following format:

Item name                 | Price  | Quantity
--------------------------|--------|----------
Apple                     | $0.49  | 1
Tea - Thai iced           | $3.99  | 2
Fried banana              | $4.49  | 3
Create the space strings as their own variables using string multiplication.

Print the line for the receipt using the format in Step 8.

Upon exiting the for loop, use list comprehension and sum() to calculate the total price of the order and display it to the customer. Make sure you multiply the price by the quantity in your list comprehension.

Hints and Considerations
Consider what you've learned so far. You’ve learned how to store content in variables, lists, and dictionaries. You’ve learned how to iterate through data structures, and you’ve learned how to debug along the way. Using all that you've learned, try to break down your tasks into discrete mini-objectives.
