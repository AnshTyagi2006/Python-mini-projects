'''
S: is for SNAKE
W: is for WATER
G: is for GUN
'''
import random
def game():
    you= input("Enter your choice ( S : SNAKE🐍 , W : WATER 💧, G : GUN 🔫): ")
    you=you.upper()
 
    l=["S" ,"W" ,"G"]
    computer=random.choice(l)

    if( you not in l):
        print("Invalid input , Please enter the following : S , W , G")
    elif ( computer=="S"):
        if you=="S":
            print(" Your Choice : SNAKE 🐍! \n My Choice : SNAKE 🐍! \n WE TIED ! 🫤")
        elif you=="W":
            print(" Your Choice : WATER 💧! \n My Choice : SNAKE �🐍! \n I WIN! 😎")
        elif you=="G":
            print(" Your Choice : GUN 🔫! \n My Choice : SNAKE 🐍! \n YOU WIN! 😏")

    elif ( computer=="W"):
        if you=="S":
            print(" Your Choice : SNAKE 🐍! \n My Choice : WATER 💧! \n YOU WIN ! 😏")
        elif you=="W":
            print(" Your Choice : WATER 💧! \n My Choice : WATER💧! \n WE TIED! 🫤")
        elif you=="G":
            print(" Your Choice : GUN 🔫! \n My Choice : WATER💧! \n I WIN! 😎")

    elif ( computer=="G"):
        if you=="S":
            print(" Your Choice : SNAKE 🐍! \n My Choice : GUN 🔫! \n I WIN ! 😎")
        elif you=="W":
            print(" Your Choice : WATER 💧! \n My Choice : GUN🔫! \n YOU WIN! 😏")
        elif you=="G":
            print(" Your Choice : GUN 🔫! \n  My Choice : GUN🔫! \n WE TIED! 🫤")

game()

while True:
    print(' Want to play again?..."y" for yes and "n" for No')
    choice=input("Want to play one more round?...")
    choice=choice.lower()
    if choice=="y":
        print("Let's play again!")
        game()

    elif choice=="n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input , Please enter the following : y , n")