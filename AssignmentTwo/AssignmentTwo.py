CustomerOrder=input("Hello what would you like to order today: ")
OrderPrice=input("The cost of a " + CustomerOrder + " is: ")    
print("Your total is ${OrderPrice:.2f}".format(OrderPrice=float(OrderPrice)) + " for a " + CustomerOrder)