import os
import user_class as p
import pickle
import datetime

# here main login of code prasent



def register():
    os.system('cls') 
    print(" Hello Welocome To Personal Expenses Managment System Registration ".center(100,"="))
    print()

    user1 = p.user()
    print()
   
    # Construct the file path
    base_dir = os.path.dirname(__file__)  # Directory of the current script
    
    file_path = os.path.join(base_dir, '..', 'userdatabase', 'userdata.txt')
    print(file_path)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    file = open(file_path,'wb')

    pickle.dump(user1,file)
    file.close()
    print('Registration successful!')
    print('Now Login..')

    os.system('cls')
    print("Login Now...")
    intro()


def login():
    print("code for Login ")


def exit():
    print()
    print("Thank you for using Personal Expense Tracker. Goodbye!".center(100," "))
    print()


def intro():
    print()
    # welcome greet
    print(" Hello Welocome To Personal Expenses Managment System ".center(100,"="))
    print()

     # option

    print('1. Register ')
    print('2. Login ')
    print('3. Exit')

    #userchoise variable store user choise
    userchoise = int(input('Enter Your Choise (1/2/3): '))

    if(userchoise == 1):
       register()

    elif(userchoise == 2):
      login()

    elif(userchoise == 3):
      exit()

    else:
     print()
     print("Soory! You Enter Invalid Option.")
     print()

   

intro()



    