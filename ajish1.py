def Task():
    num1=int(input("Enter first number:"));
    num2=int(input("Enter second number:"));
    if num1 and num2 % 2==0:
        a=num1+num2
        print(a,'is even')
        return a
    else:
        a=num1*num2
        print(a,'is odd')
        return a