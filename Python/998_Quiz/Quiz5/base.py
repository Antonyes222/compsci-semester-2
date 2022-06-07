num = input("What is your favorite number? : ")
age = int(input("what is your age? "))
st = 0
ct = 0
num2 = 0
for x in range(0,len(num)):
    for i in range(0,10):
        if num[x:x+1]==str(i):
            st = x
            break

for x in range(st,len(num)):
    for i in range(0,10):
        if num[x:x+1]==str(i):
            num2 = int(num[st:x])
    
print(num2*age)