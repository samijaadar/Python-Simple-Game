import random
def win(user,computer):
    if user==computer :return "Tie"
    elif (computer=='r' and user =='s') or (computer=='s' and user=='p') or (computer=='p' and user=='r'):
        return "Computer Win"
    else: return "You win"

def game():
    user=str(input("r for rock , s for scissors , p for paper \n"))
    computer=random.choice(['p','s','r'])
    winner=win(user,computer)
    print("\ncomputer : "+ computer +"\nuser :"+ user+"\n")
    return winner

print(game())