import random
restaurant = ["TacoBell","BurgerKing","Dominos"]
TacoBell = ["Taco","Chalupa","BajaBlast"]
BurgerKing = ["Burger","ChickenNuggets","Fries"]
Dominos = ["CheesePizza","PepperoniPizza","Coke"]

for x in range(3):
    print(restaurant[x],end=(", "))

inp1 = input("What restaurant would you like to go?")
if inp1 == "TacoBell":
    for x in range(3):
        print(TacoBell[x],end=", ")
    print("You chose Tacobell! I reccomend the "+TacoBell[random.randrange(3)])
elif inp1 == "BurgerKing":
    for x in range(3):
        print(BurgerKing[x],end=", ")
    print("You chose BurgerKing! I reccomend the "+BurgerKing[random.randrange(3)])
elif inp1 == "Dominos":
    for x in range(3):
        print(Dominos[x],end=", ")
    print("You chose Dominos! I reccomend the "+Dominos[random.randrange(3)])