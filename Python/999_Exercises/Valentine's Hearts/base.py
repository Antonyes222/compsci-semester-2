import random
import datetime
peoplelist = []
with open('People.txt') as f:
    for line in f:
        l = line.strip()
        peoplelist.append(l)
        
complimentlist = []
with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        complimentlist.append(l)
        
print(peoplelist[random.randrange(12)]+" "+complimentlist[random.randrange(6)])



x = datetime.datetime.now()

print()
print("The date and time are:")
print(str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " at " + str(x.hour))

while true:
    if x.hour == 8:
        print(peoplelist[random.randrange(12)]+" "+complimentlist[random.randrange(6)])
f.close()
