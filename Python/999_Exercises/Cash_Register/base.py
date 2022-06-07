LItem = v
LPrice = []
total = 0
Count = int(input("How many items are you buying? "))
for x in range(0,Count):
    Item = input("What item are you buying? ")
    Cost = float(input("What is the price of the item? "))
    LItem.append(Item)
    LPrice.append(Cost)
    total = total+Cost
print("Total Price: $"+str(total))
for x in range(0,Count):
    print(LItem[x],end=": $")
    print(str(LPrice[x]))
print("Thank you for purchasing! Have a good day!")
