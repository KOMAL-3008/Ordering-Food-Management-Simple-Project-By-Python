print("*****WELCOME TO KOMAL'S BURGER RESTAURANT*****")
print("*****HERE IS THE RESTAURANT MENU*****")
print("1. VEG BURGER-----Rs.50")
print("2. VEG CHEESE BURGER-----Rs.65")
print("3. VEG TANDOORI BURGER-----Rs70")
print("4. VEG PANEER BURGER-----RS80")
print("5. Bill Please")
print("6. Exit")

total_amount = 0

while True:
  choice = int(input("What would you like to Choose (Option 1,2,3,4,5,6):= "))
  if choice == 1:
    quantity = int(input("Enter the quantity:= "))
    total_amount += 30 * quantity
  elif choice == 2:
    quantity = int(input("Enter the quantity:= "))
    total_amount += 35 * quantity
  elif choice == 3:
    quantity = int(input("Enter the quantity:= "))
    total_amount += 50 * quantity
  elif choice == 4:
    quantity = int(input("Enter the quantity:= "))
    total_amount += 40 * quantity
  elif choice == 5:
    print("TOTAL AMOUNT TO BE PAID:", total_amount)
    paid_amount = int(input("Input Money Recieve: "))
    change = paid_amount - total_amount
    print("Change:", change)
    print("*****THANK YOU, #ENJOY_THE_MEAL!!!*****")
    break
  elif choice == 6:
    print("Thank You!!")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 6.")