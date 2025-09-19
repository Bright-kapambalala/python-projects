num1 = float(input("enter first value: "))
operator =str (input("enter operator: "))
num2 = float(input("enter second value: "))
if operator == '+':
    print (num1, "+", num2, "=",num1 + num2)
elif operator == '-':
    print (num1, "-", num2, "=",num1 - num2)
    
elif operator == '*':
    print (num1, "*", num2, "=",num1 * num2)
    
elif operator == '/':
 if num2 != 0:
    print (num1, "/", num2, "=",num1 /  num2)
elif operator == '%':
    print (num1, "%" , num2, "=",num1 % num2)
elif operator == '**':
    print (num1, "**", num2, "=",num1 ** num2)
else :
    print("syntax error!")
