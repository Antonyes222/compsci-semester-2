name = input("Put in your first and last name : ")
leng = len(name)
space = 0
for x in range(0,leng):
    print(name[leng-x-1:leng-x])
    if name[x-1:x] == " ":
        space = x
print(name[space:leng]+" "+name[0:space])
    