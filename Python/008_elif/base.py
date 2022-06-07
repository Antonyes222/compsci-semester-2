num1 = int(input("Please enter a number. "))
op = input("Please enter an operation. ")
num2 = int(input("Please enter a second number. "))
answer = 0
if op == "+":
    answer = num1+num2
elif op == "-":
    answer = num1-num2
elif op == "*":
    answer = num1*num2
elif op == "/":
    answer = num1/num2
print(str(num1)+str(op)+str(num2)+"="+str(answer))