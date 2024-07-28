from random import choice
from os import system

def print_logo():
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

def get_card():
    return choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def score(arr):
    return sum(arr)

def user_cards(user, comp):
    scr, newl = score(user), user[:]
    print(f"        Your Cards: {newl}, Current score: {scr}")
    print(f"        Computer's 1st card: {comp}\n")
    inp = input("Draw Card (y), pass (n): ").lower()
    if inp == 'y':
        newl.append(get_card())
        if newl[-1] == 11 and score(newl) > 21:
            newl[-1] = 1
        elif score(newl) > 21:
            print(f"        Your final hand: {newl}, Final score: {score(newl)}")
            return score(newl)
        user_cards(newl, comp)
    elif inp == 'n':
        print(f"        Your final hand: {newl}, Final score: {scr}")
        if len(newl) == 2 and score(newl) == 21:
            return 0
    else:
        user_cards(newl, comp)
    return score(newl)

def comp_cards(comp):
    newl = comp[:]
    if len(newl) == 2 and score(newl) == 21:
        return 0 
    else:
        while score(newl) < 17:
            newl.append(get_card())
            if newl[-1] == 11 and score(newl) > 21:
                newl[-1] = 1
    print(f"        Computer's final hand: {newl}, Final score: {score(newl)}\n")
    return score(newl)        

def comp_bj_check(comp):
    if len(comp) == 2 and score(comp) == 21:
        return 0
    return 1

def print_score(user_score, comp_score):
    if comp_score > 21 and user_score <= 21:
        print(f"        Computer went over. You WIN!!! 🤑\n")
    else:
        if user_score > comp_score:
            print(f"        Hurrayy!!! You WIN!!! 🥳🤑\n")
        elif comp_score > user_score:
            print(f"        You LOST!!! 😢\n")
        else:
            print(f"        It's a DRAW!!! 😐☹️\n")

def deal_cards():
    print_logo()
    user, comp = [get_card(), get_card()], [get_card(), get_card()]
    if user[-1] == 11 and score(user) > 21:
        user[-1] = 1
    if comp[-1] == 11 and score(comp) > 21:
        comp[-1] = 1
    user_score = user_cards(user, comp[0])
    if user_score > 21:
        print(f"        Computer's final hand: {comp}, Final score: {score(comp)}")
        print(f"        You went over. You LOSE!!! 😭")
        if not comp_bj_check(comp):
            print(f"        It's a BLACKJACK for Computer!!!")
    elif user_score == 0:
        print(f"        Computer's final hand: {comp}, Final score: {score(comp)}")
        if not comp_bj_check(comp):
            print(f"        It's a BLACKJACK for Computer!!! You LOSE!!! 😢😭")
        else:
            print(f"        It' a BlackJack! You WIN!!! 🥳🥳🥳")
    else:
        comp_score = comp_cards(comp)
        print_score(user_score, comp_score)
    play_blackjack()

def play_blackjack():
    inp = input(f"Play BlackJack (y/n): ").lower()
    if inp == 'y':
        system('cls')
        deal_cards()
    elif inp != 'n':
        play_blackjack()
    
play_blackjack()


