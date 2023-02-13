numberOfPizzasOrdered = int(input("How many pizzas would you like to order"))
pizzaCost = 10
orderCost = numberOfPizzasOrdered * pizzaCost
miniPartyDiscount = .1 * orderCost
partyDiscount = .2 * orderCost



if (numberOfPizzasOrdered < 1):
    print("You came her conversation or you going to order a pizza...")
    print("Total cost is ", orderCost)
else:
    if (numberOfPizzasOrdered == 1):
        print("Just one pizza doesnt qualify for discount")
        print("Total cost is", orderCost)

    else:
        if (numberOfPizzasOrdered > 1 and (numberOfPizzasOrdered <= 5)):
            print("You qualified for the mini party discount")
            print("Total cost is", (orderCost - miniPartyDiscount))

        elif (numberOfPizzasOrdered > 5): 
            print("You qualified for the party discount")
            print("Total cost is", (orderCost - partyDiscount))

        
