
import random
import math

def add(a,b) : return a+b
def subtract(a,b) : return a-b
def multiply(a,b) : return a*b
def divide(a,b) : return a/b
def power(a,b) : return pow(a,b)
def factorial(n): return math.factorial(n)
def sq_root(n): return math.sqrt(n)

def scientific_calculator():
    
    while True:
        functions = {
        "1" : ("Sin" , lambda angle: math.sin(angle)),
        "2" : ("Cos" , lambda angle: math.cos(angle)),
        "3" : ("Tan" , lambda angle: math.tan(angle)),
        "0" : ("Exit" ,  None)
        }

        print("====SCIENTIFIC CALCULATOR====")
        for key in functions :
            print(f"{key} : {functions[key][0]}")
        
        choice1 = input("\nEnter your choice : ")

        if choice1 == "0":
            print("\nExiting scientific calculator... \nThankyou!")
            exit()
        elif choice1 in functions:
            angle = float(input("Enter the angle : "))
            angle = math.radians(angle)
            result2 = functions[choice1][1](angle)
            print(f"Result : {result2}")
            x = input("\nWant to go back to home screen ? (y/n): ")
            if x.lower() == "y":
                home()
            elif x.lower() == "n":
                print("Thankyou for using scientific calculator...!")
                exit()
            else:
                print("Please enetr valid choice !")
                exit()
                


def home(): 
    while True:
        operations = {
    "1" : ["Add" , lambda : add(float(input("a : ")) , float(input("b : ")))],
    "2" : ["subtract" ,  lambda : subtract(float(input("a : ")) , float(input("b : ")))],
    "3" : ["Multiply" , lambda : multiply(float(input("a : ")) , float(input("b : ")))],
    "4" : ["Divide" , lambda : divide(float(input("a : ")) , float(input("b : ")))],
    "5" : ["Power" , lambda : power(float(input("a : ")) , float(input("b : ")))],
    "6" : ["Factorial" , lambda : factorial(int(input("n : ")))],
    "7" : ["Root" , lambda : sq_root(float(input("n : ")))],
    "8": ["Scientific Calculator", lambda: scientific_calculator()],
    "0" : ["Exit" , lambda : None]
        }

    
        print("==== WELCOME BACK! ====")
        
        for keys in operations:
                print(f"{keys}.{operations[keys][0]}")
        choice = input("\nSelect your choice : ")

        if choice == "0":
            print("\nExiting calculator... \nThankyou!")
            exit()
        
        elif choice in operations:
                result = operations[choice][1]()
                if result is not None:
                    print(f"Result: {result}\n")

        else:
                print("Please enter a valid choice...")
                

        z = input("\nWant to go back to home screen ? (y/n): ")
        if z.lower() == "y":
            home()
        elif z.lower() == "n":
            print("Thankyou for using  calculator...!")
            exit()
        else:
            print("Please enetr valid choice !")
            exit()

        
        

home()
