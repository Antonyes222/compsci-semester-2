

WORDLIST = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        WORDLIST.append(l)
import random
f.close()

WORD = WORDLIST[random.randrange(12972)]
print("WORDLE but pain.")
for x in range(0,6):
    attempt = input("Attempt"+str(x)+":")
    if attempt == WORD:
        print("You won! Good Job!")
        break
    else:
        print("Incorrect.")
    if(x==5):
        print("Sorry, you lost.")

print("The word was : "+WORD)
