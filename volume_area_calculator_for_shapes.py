import math
while True:
    response = input("circle (1)\n square/rectangle (2)\n triangle(3)\n response : ")
    
    
    if response == "1":
        while True:
            r1 = input("enter radius of circle : ")
            try:
                r1 = float(r1)
                print(f"perimeter of circle -> {2*3.14*(r1)} \n area of circle -> {3.14*pow((r1),2)}\n\n")
                break
            except ValueError:
                print("try again\n\n")
                
                
    elif response == "2":
        while True:
            r2 = input("enter length of 2 sided figure : ")
            r3 = input("enter breadth of 2 sided figure : ")
            try:
                r2 = float(r2)
                r3 = float(r3)
                print(f"area of figure -> {r2*r3}\n perimeter of figure -> {2*(r2+r3)}\n\n")
                break
            except ValueError:
                print("try again\n\n")
                
                
    elif response == "3":
        while True:
            r4 = input("enter triangle base : ")
            r5 = input("enter triangle height : ")
            try:
                r4 = float(r4)
                r5 = float(r5)
                print(f"area of triangle -> {r4*r5*0.5}\n\n")
                break
                
                
            except ValueError:
                print("try again\n\n")
    else:
        print("try again\n\n")
        
        
    try:
        response = float(response)
        
    except ValueError:
        print("try again\n\n")