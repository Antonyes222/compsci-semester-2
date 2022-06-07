import random
Count = int(input("How many random numbers do you need? "))
listt = []
for x in range(0,Count):
    listt.append(random.randrange(1,10))
for x in range(0,Count-1):
    print(listt[x],end=", ")
print(listt[Count-1])