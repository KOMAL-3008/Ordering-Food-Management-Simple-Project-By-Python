# Ordering-Food-Management-Simple-Project-By-Python

# Komal's Burger Restaurant Ordering System

## Description
This is a simple Python-based ordering system for a burger restaurant. The program allows customers to choose from various burger options, specify the quantity, and calculate the total amount for their order. The system also allows the customer to pay and calculates the change if the amount paid exceeds the total.

## Features
- Display a menu of burgers with prices.
- Let the user choose an item and specify the quantity.
- Calculate the total price of the order based on the selected items and quantities.
- Allow the customer to pay and provide the correct change.
- Handle invalid choices or insufficient payment gracefully.

## How It Works

### Menu:
The user is presented with the following options:
1. **Veg Burger** - Rs. 50
2. **Veg Cheese Burger** - Rs. 65
3. **Veg Tandoori Burger** - Rs. 70
4. **Veg Paneer Burger** - Rs. 80
5. **Request Bill** - View the total amount and proceed to payment.
6. **Exit** - Exit the program.

### Process:
1. The customer selects the burger and specifies the quantity.
2. The total cost is updated based on the selected items and quantities.
3. The customer can choose to view the bill and make the payment.
4. The system will display the total amount, prompt the customer to enter the money received, and calculate the change.
5. If the customer does not have enough money, the program will ask them to pay the full amount.

## Requirements
- Python 3.x (The program has been tested with Python 3.7 and above)

## How to Run the Code
1. Clone the repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the Python file is saved.
4. Run the following command:
   ```bash
   python burger_ordering_system.py

# Sample Output

*****WELCOME TO KOMAL'S BURGER RESTAURANT*****
*****HERE IS THE RESTAURANT MENU*****
1. VEG BURGER-----Rs.50
2. VEG CHEESE BURGER-----Rs.65
3. VEG TANDOORI BURGER-----Rs.70
4. VEG PANEER BURGER-----Rs.80
5. Bill Please
6. Exit
What would you like to Choose (Option 1,2,3,4,5,6): 1
Enter the quantity: 2
What would you like to Choose (Option 1,2,3,4,5,6): 3
Enter the quantity: 1
What would you like to Choose (Option 1,2,3,4,5,6): 5
TOTAL AMOUNT TO BE PAID: 170
Input Money Received: 200
Change: Rs. 30
*****THANK YOU, #ENJOY_THE_MEAL!!!*****

# Code Walkthrough

# Menu Display: The program first shows the menu options with prices for each burger.
# Order Selection: The user selects a burger from the menu by entering a number (1 to 4). The user is then asked to enter the quantity for the selected item.
# Total Calculation: The total amount is calculated based on the selected items and quantities.
# Bill and Payment: The user can choose to view the bill by selecting option 5. The program will display the total amount and prompt for payment. If the user has enough money, the change will be calculated.
# Exit: The user can exit the program at any time by selecting option 6
