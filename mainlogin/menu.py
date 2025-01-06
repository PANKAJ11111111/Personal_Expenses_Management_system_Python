import os
import expense_class as e
import datetime
import pickle

login_user = None

def add_expenses(login_user):
    os.system('cls')
    print()
    print(" Personal Expenses Managment System  ".center(100,"="))
    print()

    print()
    print("Hy {} its Time to log your latest spending! ❤️".format(login_user.user_name))
    print("Enter the details to keep your budget updated...")
    print("----------------------------------------------------")
    print()

    user_folder = os.getcwd()
    user_folder = os.path.join(user_folder,'userdatabase',login_user.user_email.lower())
    
    expens = e.expense()
    
    date_e = expens.e_date
    date_e = date_e.split('-')
    file_month = 'expense_of_' + date_e[1] + "_" + date_e[2]+'.txt'

    month_file = os.path.join(user_folder, file_month)
    
    if(os.path.isfile(month_file)):
        file = open(month_file,'ab')
        pickle.dump(expens,file)
        file.close()
        print()
        print(" ✔️  Expense added successfully!  ✔️".center(100," "))
        c = int(input("For <- Back Press 1: "))

        if c == 1:
            os.system('cls')
            menushow(login_user)
        else:
            print()
            print("Soory! You Enter Invalid Option 😵 😵 .")
            print("Log out .....")
            print()
        print()
    
    else:

        file = open(month_file,'ab')
        pickle.dump(expens,file)
        file.close()
        print()
        print("Expense added successfully!".center(100," "))
        c = int(input("For <- Back Press 1: "))

        if c == 1:
            os.system('cls')
            menushow(login_user)
        else:
            print()
            print("Soory! You Enter Invalid Option 😵 😵 .")
            print("Log out .....")
            print()
        print()
        

    
def logoutcode(login_user):
    os.system('cls')
    print()
    print(" Personal Expenses Managment System  ".center(100,"="))
    print()
    print("Thank you {} for using Personal Expense Tracker. ✨ Goodbye! ✨".center(100," ").format(login_user.user_name))
    print()
    print("Log Out.....")
    print()
    print()

   


def menushow(user):
    login_user = user
    print()
    print(" Hello {} 💫 Welocome To Personal Expenses Managment System  ".center(100,"=").format(login_user.user_name))
    print()
    print("Hello {}! It's always a pleasure to assist you. ❤️".format(login_user.user_name)) 
    print("Let’s get started on keeping your finances organized and stress-free")
    print()
    print()

    print("===== Expense Tracker Menu =====")
    print()
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit/Delete Expense")
    print("4. Set Monthly Budget")
    print("5. Export Data:")
    print("6. Logout")
    user_choise = int(input("Enter your choice (1-6): "))

    if user_choise == 1:
        add_expenses(login_user)
    
    elif user_choise == 2:
        print("code for view expenses")

    elif user_choise == 3:
        print("code for edit/delete expenses")
    
    elif user_choise == 4:
        print("code for Set Monthly Buget")
    
    elif user_choise == 5:
        print("code for export data.")
    
    elif user_choise == 6:
        logoutcode(login_user)
    
    else:
        os.system('cls')
        print("You Enter Invalid Option! ❌ Try Again...")
        menushow(login_user)


