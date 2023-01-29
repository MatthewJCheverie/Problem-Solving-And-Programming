PizzaPrice=input("Please enter the price of a pizza: ")
FryPrice=input("Please enter the price of fries: ")
AmountOfPizzas=input("Please enter the number of pizzas ordered ")
AmountOfFries=input("PLease enter the number of fries ordered: ")
PizzeriaDiscount=input("Please enter the discount for pizza del mat: ")
CostOfOrder= (float(FryPrice)*int(float(AmountOfFries))) + (float(PizzaPrice)*int(float(AmountOfPizzas)))
CostAfterDiscount= CostOfOrder*(1-float(PizzeriaDiscount)/100)
 
print("\nThe total cost of your order before discount is ${CostOfOrder:.2f}"\
    .format(CostOfOrder=float(CostOfOrder)), 
    "\nThe total cost of order after discount is ${CostAfterDiscount:.2f}"\
    .format(CostAfterDiscount=float(CostAfterDiscount)))
