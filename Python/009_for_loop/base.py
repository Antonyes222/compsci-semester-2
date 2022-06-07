length = int(input("What is the length of the line? "))
Crab = input("Do you want the line 'Vertical' or 'Horizontal'? ")
if Crab == "Horizontal":
    for x in range(0,length):
        print("X",end="")
elif Crab == "Vertical":
    for x in range(0,length):
        print("X")
else:
    print("Something went wrong ")
