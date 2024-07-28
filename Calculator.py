import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return (a * b)

def div(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b

def take_input(x):
    try:
        return float(input(f"Enter Operand {x}: "))
    except:
        print("Enter integer or decimal value.\n")
        take_input(x)

def operate(a, b):
    operations = {
        "+" : add,
        "-" : sub,
        "*" : mult,
        "/" : div
    }
    for i in operations:
        print(i)
    while True:
        oper = input("Choose Operation: ")
        if oper in operations:
            return [oper, operations[oper](a, b)]

def calculator(x = None):
    if x == None:
        print("\n",logo)
        a = take_input(1)
    else:
        a = x
        print()
    b = take_input(2)
    oper = operate(a, b)
    print(f"{a} {oper[0]} {b} = {oper[1]}\n")
    if oper[1] == "Cannot divide by zero.":
        inp = input("Start new calculation(y), to close(n): ")
        if inp == 'y':
            calculator()
    else:
        print(f"Continue calculations with {oper[1]} (y)\nstart new calculation (n)\nAny key to close application")
        inp = input("\nYour Choice: ")
        if inp == 'y':
            calculator(oper[1])
        elif inp == 'n':
            os.system('cls')
            calculator()

calculator()
    
    

    
    