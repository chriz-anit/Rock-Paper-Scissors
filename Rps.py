from dis import dis
import random

def game():
    user = input("\nr - rock\np - paper\ns - scissors\nEnter your choice:")
    computer = random.choice(['r','p','s'])

    print('\nYOUR CHOICE:',end=" ",flush=True)
    disp_choice(user)
    print('\nMY CHOICE:',end=" ",flush=True)
    disp_choice(computer)

    if user == computer:
        print('\nITS A TIE')

    elif win(user,computer):
        print('\nYOU WON!!')
    else:
        print('\nYOU LOST!')

def disp_choice(choice):
    if  choice == 'r':
        print("Rock")
    elif choice == 'p':
        print("Paper")
    else:
        print("Scissors")

def win(u,c):
    #true if player wins
    if((u=='r' and c=='s') or (u=='p' and c=='r') or (u=='s' and c=='p')):
        return True

game()