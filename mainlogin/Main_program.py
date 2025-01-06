#import all essential module
import os
import user_class as p
import pickle
import datetime
import menu as m

# here main login of code prasent


# fuction for Registration
def register():
    os.system('cls') 
    print(" Hello Welocome To Personal Expenses Managment System Registration ".center(100,"="))
    print()
    
    # create user object
    user1 = p.user()
    print()
   
    # Construct the file path
    base_dir = os.path.dirname(__file__)  # Directory of the current script
    
    file_path = os.path.join(base_dir, '..', 'userdatabase', 'userdata.txt')

    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    file = open(file_path,'ab')

    pickle.dump(user1,file)

    file.close()
    
    os.system('cls')
    print('Registration successful!')
    print('Now Login..')

    newdire = os.path.join(base_dir,'..','userdatabase',user1.user_email.lower())
    
    os.makedirs(newdire)

    intro()


# fuction for Login user
def login():
    os.system('cls') 
    print()
    print(" Hello Welocome To Personal Expenses Managment System Login ".center(100,"="))
    print()
    useremail = input("Enter Your Register Mail = ")
    userpassword = input("Enter Your Password = ")
    base_dir = os.path.dirname(__file__)  # Directory of the current script
    
    file_path = os.path.join(base_dir, '..', 'userdatabase', 'userdata.txt')

    readfile = open(file_path, "rb")

    try:
    
     for _ in range(100):
        data1 = pickle.load(readfile)

        if(useremail.lower() == data1.user_email.lower()):
          if(userpassword == data1.user_password):
             print()
             os.system('cls')
             m.menushow(data1)
             break
          else:
             os.system('cls')
             print("You Enter Invalid Password! ❌ Try Again...")
             intro()
             
        
        
    except EOFError:
      os.system('cls')
      print("User Not Found In DataBase Register First.... 🌍 ")
      intro()

    finally:
      readfile.close()
       
       
    

# function for exit
def exit():
    print()
    print("Thank you for using Personal Expense Tracker. ✨ Goodbye! ✨".center(100," "))
    print()


# fuction to show welcome
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

    # login for handle choise
    if(userchoise == 1):
      register()

    elif(userchoise == 2):
      login()

    elif(userchoise == 3):
      exit()

    else:
     print()
     print("Soory! You Enter Invalid Option 😵 😵 .")
     print()
     intro()
     
     

   


# code exection start from here
os.system('cls')
intro()



    