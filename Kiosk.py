'''
Ibrahim
(Input)
Get name
get main
get side
get drink
get payment method
get cash then get money
Process
figure out sub total
figure out tax
figure out total
Output
detailed receipt
list of ordered items
sub total
total
tax
If credit, charged amount
If cash then change
'''
# Set all constants we will be using for this program
TAXRATE = 0.07
# input
# Get name
name = input("Please enter your first name: ")
# Display the main menu and get customer choice(we will make this into a function later)
print("Please select your MAIN item from the list below by entering a number and pressing return")
print ("1 - Chicken Sandwich ($6.00)")
print ("2 - Large Fries ($5.00)")
print ("3 - Water ($3.00)")
main = input()
sideCost = 0
mainCost = 0
drinkCost = 0
if main == "1":
    mainCost = 6.00
    Order = "Chicken Sandwich ($6.00)"
elif main == "2":
    sideCost = 5.00
    Order = "Large Fries ($5.00)"
elif main == "3":
    drinkCost = 3.00
    Order = "Water ($3.00)"
else:
    print("you entered a wrong choice. Try again")
    exit
# you need to do the same thing for the side menu and drinks here
# Calculate subtotal and print it
subTotal = mainCost + sideCost + drinkCost
tax = subTotal * TAXRATE
total = subTotal + tax
print("Your subTotal is: ", subTotal)
print ("your tax is: ", tax)
print ("Your total is: ", total)
# Find out if customer wants to pay by Cash or Credit
# modify to accept both captial and lower case C and R
print("We accept both Cash and Credit. Will you pay by Cash or Credit? ")
print ("C - Cash")
print ("R - Credit")
payMethod = input()
if payMethod == "C":
    cashPaid = int(input("Enter the amount you will pay. Eg. 10, 15.27, 20, etc.: "))
    change = cashPaid - total
    if change < 0:
        print("What's going on? You didn't pay enough! We will talk later. Bye for now.")
    elif change >= 0:
        print("here is your change : $", change)
elif payMethod == "R":
# format this nicely. numbers to be 2 digits
    print("You ordered ", Order)
else:
    print("You ordered ", Order)
    print ("your credit card has been charged with this amount: ", total)