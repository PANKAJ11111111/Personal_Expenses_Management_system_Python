import os

login_user = None

    
def logoutcode(login_user):
    os.system('cls')
    print()
    print(" Personal Expenses Managment System  ".center(100,"="))
    print()
    print("Thank you {} for using Personal Expense Tracker. ✨ Goodbye! ✨".center(100," ").format(login_user.user_name))
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
        print("code for add expenses")
    
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


