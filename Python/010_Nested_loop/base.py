Symbol = input("What Symbol is the box? ")
W = int(input("What is the width of your box? "))
L = int(input("What is the length of your box? "))
for x in range(0,L):
    print("")
    for x in range(0,W):
        print(Symbol,end="")