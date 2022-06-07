num = 0
num2 = 0
total = 0
with open('moby.txt') as f:
    for line in f:
        num = 0
        num2 = num2 + 1
        sentence = line.strip()
        for x in range(0,len(sentence)):
            if sentence[x:x+5] == 'whale':
                num = num+1
                total = total+1
        if num != 0:
            print('sentence '+str(num2)+' ( '+line+' ) :'+str(num))
f.close()
print('total : '+str(total))