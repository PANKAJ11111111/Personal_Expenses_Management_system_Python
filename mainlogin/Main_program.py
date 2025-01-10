#import all essential module
import os
import user_class as p
import pickle
import datetime
import menu as m
from Mail_handler.welcome_mail import send_email

# here main login of code prasent


# fuction for Registration
import os
import pickle

def register():
    os.system('cls') 
    print(" Hello Welocome To Personal Expenses Managment System Registration ".center(100, "="))
    print()
    
    # Create user object
    user1 = p.user()
    print()

    # Base directory of the current script
    base_dir = os.path.dirname(__file__)  
    
    # Path to the main user database file
    file_path = os.path.join(base_dir, '..', 'userdatabase', 'userdata.txt')

    # Check if user-specific directory exists
    user_dir = os.path.join(base_dir, '..', 'userdatabase', user1.user_email.lower())

    # If the user directory already exists
    if os.path.isdir(user_dir):
        os.system('cls')
        print(f'{user1.user_name}, You are already registered. Please log in.')
        intro()  # Call the intro function for login or other options
        return  # Exit the register function
    
    # If the user directory doesn't exist
    try:
        
        sender_email = "pankajwork33@gmail.com"  # Your email
        sender_password = "rdox ymsq xvdu bhpz"  # Your email password or app password
        recipient_email = user1.user_email  # Recipient's email
        subject = "Personal Expense Managment System "
        body = """ Dear {},

Welcome to the Personal Expenses Management System! 🎉

We are thrilled to have you on board and excited to help you take control of your finances. With our system, you can easily track and manage your expenses, set monthly targets, and stay on top of your financial goals. 📊💸

Here's a quick look at what you can do:

Track your expenses by date, category, and description.
Set monthly financial targets and get reminders.
View detailed reports of your spending patterns.
Easily delete or modify your expenses as you need.
To get started, simply log in using your credentials and begin adding your expenses right away. If you need any assistance, feel free to reach out to us. We're always here to help!

Once again, welcome aboard, and we wish you the best in managing your personal finances with us. 🏆

Thank you for choosing us to assist you with your financial journey. 😊

Best regards,
The Personal Expenses Management Team
Pankaj Saratkar (Head)
""".format(user1.user_name)
        
       
        e = send_email(sender_email,sender_password,recipient_email,subject,body)
        
        if(e == False):
           os.system('cls')
           print("Invalid Mail Id...")
           print("Try Again...")
           intro()
           return


        # Ensure the directory for the main user database file exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Save the new user data to the main database
        with open(file_path, 'ab') as file:
            pickle.dump(user1, file)
        
        # Create the user's specific directory
        os.makedirs(user_dir, exist_ok=True)
        
        os.system('cls')     
        print('Registration successful!')
        print('Now log in...')
        intro()  # Proceed to the intro/login function

    except Exception as e:
        os.system('cls')
        print('An error occurred during registration:', str(e))



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
    print()

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



    