import random
import os

def num_check(x):
    if x == 'letters':
        try:
            ret = int(input(f"How many letters would you like in your password? "))
            return ret
        except:
            print("Enter Integer value.\n")
            ret = num_check('letters')
            return ret
    elif x == 'symbols':
        try:
            ret = int(input(f"How many symbols would you like? "))
            return ret
        except:
            print("Enter Integer value.\n")
            ret = num_check('symbols')
            return ret
    else:
        try:
            ret = int(input(f"How many numbers would you like? "))
            return ret
        except:
            print("Enter Integer value.\n")
            ret = num_check('numbers')
            return ret

def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    print("Welcome to the PyPassword Generator!")
    nr_letters = num_check('letters')
    nr_symbols = num_check('symbols')
    nr_numbers = num_check('numbers')
    password = [random.choice(letters) for i in range(nr_letters)]
    password += [random.choice(symbols) for i in range(nr_symbols)]
    password += [random.choice(numbers) for i in range(nr_numbers)]
    lenp = len(password)
    for i in range(lenp):
        rand1, rand2 = random.randint(0,lenp-1), random.randint(0,lenp-1)
        password[rand1], password[rand2] = password[rand2], password[rand1]
    print(f"\nYour password: {''.join(password)}\n")
    start_program()

def start_program():
    inp = input("Generate another password (y/n): ").lower().strip()
    if inp == 'y':
        os.system('cls')
        gen_password()
    elif inp != 'n':
        start_program()

gen_password()