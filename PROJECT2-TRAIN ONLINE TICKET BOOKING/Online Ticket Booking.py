import random
from datetime import datetime

def ticket():

    source = input("Enter your Boarding Point : ")
    destination = input("Enter your Destination : ")
    date_input = input("Enter the date of your journey (dd-mm-yyyy) : ")
    try:
        journey_date = datetime.strptime(date_input, "%d-%m-%Y")
    except ValueError:
        print("Please enter valid date !")
        return
    
    names = ["Rajdhani Express","Shatabdi Express","Duronto Express","Vande Bharat Express","Humsafar Express"]

    trains = {} 
    for i in range(1,6):
        train_info=(
            f"\nTrain no. : {random.randint(1000,5000)}",
            f"Name : {random.choice(names)}",
            f"From : {source} ",
            f"To : {destination}",
            f"Date of Journey : {date_input}",
            f"Departural time : {random.randint(0,24)}:{random.randint(0,59)}{random.choice(['AM','PM'])}",
            f"Arrival time : {random.randint(0,24)}:{random.randint(0,59)}{random.choice(['AM','PM'])}",
            random.randint(1,100)
            )
        trains[str(i)] = train_info
     
    
    print("====WELCOME TO INDIAN RAILWAYS ONLINE TICKET BOOKING====")
    
    for keys in trains:
        train = trains[keys]  #train is a tuple now
        print(f"\n{keys} :")
        for item in train[:-1]:
            print(item)
        print(f"Seats Available : {train[-1]}")
    
    choice = input("\nSelect your train : ")

    if choice in trains:
        passenger=int(input("Enter the Number of passengers : "))
 
        if trains[choice][-1]>= passenger:
            print("✅ Your ticket is booked successfully !")

            with open("Ticket.txt" , "w") as f:
                for item in trains[choice][:-1]:
                        f.write(item + "\n")
                f.write(f"Seats Booked : {passenger}")
        else:
            print("❌ Sorry ! Seats are not available !")
    else:
        print("Please select a valid choice !")

    x = input("Go back to the home screen ? (y/n) :")
    if x.lower() == 'y':
        home()
    else:
        print("Your Ticket is Booked !\nHave a safe Journey...!")





def check_ticket():
    open("Ticket.txt" , "a").close()
    with open("Ticket.txt") as f:
        data=f.read()
        if data =="":
            print("❌No ticket booked !")
            c = input("Go back to home screen ? (y/n) : ")
            if c.lower() == 'y':
                home()
            else:
                print("\nExiting the program...\nThankyou for using Indian Railways")

        else:
            print("\n====YOUR TICKET DETAILS====")
            print(data)
            print("\nHave a safe journey...!")
            z = input("Go back to the home screen ? (y/n) :")
            if z.lower() == 'y':
                 home()
            else:
                 print("Your Ticket is Booked !\nHave a safe Journey...!")




def home():
    content = {
        "1" : ("Online Ticket Booking" ,  lambda : ticket()),
        "2" : ("Check your Online Ticket" , lambda : check_ticket()),
        "3" : ("Contact us" , lambda :  contact()),
        "4" : ("Exit",None)
    }

    print("====WELCOME TO INDIAN RAILWAYS====")
    for keys in content:
     print(f"{keys} . {content[keys][0]}")

    choice2 = input("Please select your Choice : ")
    if choice2 in content:
        if choice2 == "4":
            print("\nExiting the program...\nThankyou for using Indian Railways")
        
        else:
            content[choice2][1]()
    else:
        print("❌Please select a valid choice !")

def contact():
    print("📞Contact No. : 9418352771")
    print("📩e-mail : anshtyagiansh0@gmail.com")
    print("\nThankyou for using Indian Railways Services !")
    c = input("Go back to home screen ? (y/n) : ")
    if c.lower() == 'y':
        home()
    else:
        print("\nExiting the program...\nThankyou for using Indian Railways")

    
home()