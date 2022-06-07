# minimum : smallest number
# maximum : biggest number
# average : the average.
MAX = 0
MIN = 0
x = 0
average = 0
mynumbers = [6,9,32,28,15,22,3,18]
total = 0
#Maximum
for x in range(0,len(mynumbers)-1):
    if mynumbers[x]>mynumbers[x+1]:
        MAX = mynumbers[x]
    elif mynumbers[x]<mynumbers[x+1]:
        MAX = mynumbers[x+1]
#Minimum 
for x in range(0,len(mynumbers)-1):
    if mynumbers[x]<mynumbers[x+1]:
        MIN = mynumbers[x]
    elif mynumbers[x]>mynumbers[x+1]:
        MIN = mynumbers[x+1]
#Average
for x in range(0,len(mynumbers)):
   total = total + mynumbers[x]
average = total/len(mynumbers)

print("Your average is : "+str(average))
print("Your maximum is : "+str(MAX))
print("Your minimum is : "+str(MIN))
