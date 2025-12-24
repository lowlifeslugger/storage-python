def calculator():
    while 1:
        num1 = input("enter number : ")
        try:
            num1 = float(num1)
        except ValueError:
            print("valid number!")
            
        sym = input("enter a symbol\n + , - , X , /\n ----: ").lower()
        
        num2 = input("enter number : ")
        try:
            num2 = float(num2)
        except ValueError:
            print("valid number!")
        
        if sym == "+":
            print(num1+num2)
            
        elif sym == "-":
            print(num1-num2)
            
        elif sym == "*" or sym == "x":
            print(num1*num2)
            
        elif sym == "/":
            if num2 == 0:
                print("invalid syntax")
            else:
                print(num1/num2)
        else:
            print("enter valid symbol")

calculator()