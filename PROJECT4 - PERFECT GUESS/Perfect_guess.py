import random


def game():
    number = random.randint(1,100)
    guess = int(input("\nGuess any number  between 1 and 100 🤔: "))

    count = 1
    while True :
        if guess not in range(1,101):
            print("\nInvalid input ! Please enter a valid number...❗")
            continue
        elif guess > number :
            guess = int(input("⬇️  Too High ! , Lower number please... "))
            count += 1
        elif guess < number :
            guess = int(input("⬆️  Too Low ! , Higher number please... "))
            count += 1
        elif guess == number :
            print(f"\nHuraay...!🎉\nYou guessed the correct number ({number})...!✅")
            print(f"You have used {count} guesses👍")
            
            try:
                
                open("Score.txt" , "a").close()
                open("Prev_score.txt" , "a").close()

                with (
                    open("Score.txt" , "r+") as f1 , 
                    open("Prev_score.txt" , "w") as f2
                ):
                
                        data1 = f1.read()
                        if data1!="":
                            if int(data1)>count:
                                f1.seek(0)
                                f1.write(str(count))
                                f1.truncate()
                            else:
                                f2.write(str(count))
                        elif data1 =="":
                            f1.write(str(count))
            except FileNotFoundError as f:
                print("Please first make a text file named 'Score.txt'! for saving your Best score")
            try:
                if data1 !="":
                    print(f"Your best score 🔥: {data1}")
            except NameError as n:
                print("Make sure the text files are accesible for opening succesfully !")

            choice()       

def choice():
    ch = input("\nDo you want to play again ? (y/n) :")
    if ch.lower() == "y":
        game()
    elif ch.lower() == "n":
        b = input("\nGo back to the menu ? (y/n) : ")
        if b.lower() == "y":
            menu()
        elif b.lower() == "n":
            print("Exiting the Game...\nThanks for playing !")
            exit()
        else :
                print("Invalid input ! , Please enter a valid input")
                choice()
    else :
        print("Invalid input ! , Please enter a valid input")
        choice()

def file():
    
    open("Prev_score.txt" , "a").close()
    
    with open("Prev_score.txt" , "r") as f:
        data = f.read()
        if data !="":
            print(f"\nYour previous score : {data}")
            b = input("\nGo back to the menu ? (y/n) : ")
            if b.lower() == "y":
                menu()
            elif b.lower() == "n":
                print("Exiting the Game...\nThankyou !")
                exit()
            else :
                print("Invalid input ! , Please enter a valid input")
        elif data == "" :
            print("No previous score found !")
            b = input("Go back to the menu ? (y/n) : ")
            if b.lower() == "y":
                menu()
            elif b.lower() == "n":
                print("Exiting the Game...\nThankyou !")
                exit()
            else :
                print("Invalid input ! , Please enter a valid input")

        


def menu():
    dic = {
        1 : "Start the game",
        2 : "View Your Previous score",
        3 : "Exit the game"
    }

    print("\n===A PERFECT GUESS====")
    for i in dic:
        print (f"\n{i} : {dic[i]}")
    choose1 = int(input("\nPlease enter your choice : "))
    if choose1 == 1 :
        game()
    elif choose1 == 2 :
        file()
    elif choose1 == 3 :
        print("\nExiting the game...\nThanks for playing !")
        exit()
    else :
        print("Invalid choice ! Please enter a valid choice...")
        b = input("\nGo back to the menu ? (y/n) : ")
        if b.lower() == "y":
            menu()
        elif b.lower() == "n":
            print("Exiting the Game...")
            exit()
        else :
                print("Invalid input ! , Please enter a valid input")
        



menu()