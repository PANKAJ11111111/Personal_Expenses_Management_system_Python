import os
import expense_class as e
import datetime
import pickle
from colorama import Fore, Back, Style

login_user = None


def getmonth(num):

    if num == '01':
        return 'January'
    elif num == '02':
        return 'February'
    elif num == '03':
        return 'March'
    elif num == '04':
        return 'April'
    elif num == '05':
        return 'May'
    elif num == '06':
        return 'June'
    elif num == '07':
        return 'July'
    elif num == '08':
        return 'August'
    elif num == '09':
        return 'September'
    elif num == '10':
        return 'October'
    elif num == '11':
        return 'November'
    else:
        return 'December'


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



def view_expence(login_user):
    os.system('cls')
    print()
    print(" Personal Expenses Managment System  ".center(100,"="))
    print()

    print()
    print("Hy {} Let’s see where your money has gone!".format(login_user.user_name))
    print("Select a view option to get started..")
    print("----------------------------------------------------")
    print()

    print("===== View Expenses =====")
    print()
    print("1. View All Expenses")
    print("2. View by Month")
    print("3. View by Year")
    print("4. Back to Main Menu")
    print()
    ch = int(input("Enter your choice (1-4): "))

    if ch == 1:
        user_folder = os.getcwd()
        user_folder = os.path.join(user_folder,'userdatabase',login_user.user_email.lower())

        all_expense_file = os.listdir(user_folder)

        os.system('cls')
        print()
        print(" Personal Expenses Managment System  ".center(100,"="))
        print()

        print()
        print("Hy {} Let’s see where your money has gone!".format(login_user.user_name))
        print("----------------------------------------------------")
        print()

        
        print()
        print("===== All Expenses =====")
        print()
        
        for i in range(len(all_expense_file)):
        
            month_file = os.path.join(user_folder,all_expense_file[i])
            month_sep = all_expense_file[i].split('_')
            month = month_sep[2]
            month_str = getmonth(month)
            year = month_sep[3].split('.')

            print("-".center(100,'-'))
            print("\033[31mMonth: {} {}\033[0m".format(month_str,year[0]).center(100,' '))
            print("-".center(100,'-'))
            
            
            current_open_file = open(month_file,'rb')
       
            try:
              
              i = 1
              total =0
              print()
              for _ in range(1000):
                  
                  current_e = pickle.load(current_open_file)
                  print("\033[31m{}.\033[0m \033[31mAmount:\033[0m {}, \033[31mCategory:\033[0m {}, \033[31mDate:\033[0m {}, \033[31mDescription:\033[0m {}".format( i ,current_e.e_amount, current_e.e_type, current_e.e_date, current_e.e_des))
                  i= i+1
                  total+=current_e.e_amount
                  print()
                  

            except EOFError:
                print("\033[31mTotal Expenses: \033[0m {}".format(total))
                monthint = int(month)-1
                
                if(total > login_user.monthly_buget[monthint]):
                   print("Budget: {}".format(login_user.monthly_buget[monthint]))
                   print("Warning: {}".format(login_user.user_name))
                   print("Your expenses for {} have exceeded the budget Limit..".format(month_str))   
                else:
                   print("Budget: {}".format(login_user.monthly_buget[monthint]))
                   print("Message: {}".format(login_user.user_name))
                   print("Your expenses for {} have Under the budget Limit..".format(month_str))
                    
                print()
                continue

        print()
        print("-----------------------------------------------------------")
        print()
        print(" ✔️  View Expenses successfully!  ✔️".center(100," "))
        c = int(input("For <- Back Press 1: "))

        if c == 1:
         os.system('cls')
         menushow(login_user)
         return
        else:
              print()
              os.system('cls')
              print(" Personal Expenses Managment System  ".center(100,"="))
              print()
              print("Thank you {} for using Personal Expense Tracker. ✨ Goodbye! ✨".center(100," ").format(login_user.user_name))
              print()
              print("Soory! You Enter Invalid Option 😵 😵 .")
              print("Log out .....")
              print()
              print()
    
    elif ch == 2:
        print()
        m = input("Enter Month & Year (MM-YYYY): ")
        l = m.split('-')
        print()

        mstring = getmonth(l[0])
        user_folder = os.getcwd()
        user_folder = os.path.join(user_folder,'userdatabase',login_user.user_email.lower())
        Monthpath = 'expense_of_'+l[0]+'_'+l[1]+'.txt'
        Monthpath = os.path.join(user_folder,Monthpath)
        
        if(os.path.isfile(Monthpath)):
            
            os.system('cls')
            print()
            print(" Personal Expenses Managment System  ".center(100,"="))
            print()

            print()
            print("Hy {} Let’s see where your money has gone!".format(login_user.user_name))
            print("----------------------------------------------------")
            print()

        
            print()
            print("===== All Expenses Of \033[31m{}\033[0m =====".format(mstring))
            print()
            print("-".center(100,'-'))
            
            try:
             current_open_file = open(Monthpath,'rb')
             i = 1
             total =0
             print()
             for _ in range(1000):
                  
              current_e = pickle.load(current_open_file)
              print("\033[31m{}.\033[0m \033[31mAmount:\033[0m {}, \033[31mCategory:\033[0m {}, \033[31mDate:\033[0m {}, \033[31mDescription:\033[0m {}".format( i ,current_e.e_amount, current_e.e_type, current_e.e_date, current_e.e_des))
              i= i+1
              total+=current_e.e_amount
              print()
                  

            except EOFError:
                print("\033[31mTotal Expenses: \033[0m {}".format(total))
                monthint = int(l[0])
                if(total > login_user.monthly_buget[monthint]):
                   print("Budget: {}".format(login_user.monthly_buget[monthint]))
                   print("Warning: {}".format(login_user.user_name))
                   print("Your expenses for {} have exceeded the budget Limit..".format(mstring))   
                else:
                   print("Budget: {}".format(login_user.monthly_buget[monthint]))
                   print("Message: {}".format(login_user.user_name))
                   print("Your expenses for {} have Under the budget Limit..".format(mstring))
                print()
                print("----------------------------------------------------")
                print()
                print(" ✔️  View Expenses successfully!  ✔️".center(100," "))
                c = int(input("For <- Back Press 1: "))

                if c == 1:
                 os.system('cls')
                 menushow(login_user)
                 return
                else:
                 print()
                 os.system('cls')
                 print(" Personal Expenses Managment System  ".center(100,"="))
                 print()
                 print("Thank you {} for using Personal Expense Tracker. ✨ Goodbye! ✨".center(100," ").   format(login_user.user_name))
                 print()
                 print("Soory! You Enter Invalid Option 😵 😵 .")
                 print("Log out .....")
                 print()
                 print()

        else:
            os.system('cls')
            print("There Was No Data For Given Month ❌ Try Again...")
            menushow(login_user)
            

    elif ch == 3:
        print()
        m = input("Enter Year (YYYY): ")
        print()
        user_folder = os.getcwd()
        user_folder = os.path.join(user_folder,'userdatabase',login_user.user_email.lower())
        os.system('cls')
        print()
        print(" Personal Expenses Managment System  ".center(100,"="))
        print()

        print()
        print("Hy {} Let’s see where your money has gone!".format(login_user.user_name))
        print("----------------------------------------------------")
        print()

        
        print()
        print("===== All Expenses Of {} =====".format(m))
        print()
        count = 0
        for j in range(1,13):
           ms = ''
           Monthpath = ''
           if(j == 10 or j == 11 or j == 12):
            Monthpath = 'expense_of_'+str(j)+'_'+m+'.txt'
            Monthpath = os.path.join(user_folder,Monthpath)
            ms = str(j)
           else:
             Monthpath = 'expense_of_0'+str(j)+'_'+m+'.txt'
             Monthpath = os.path.join(user_folder,Monthpath)
             ms = '0'+str(j) 

           if(os.path.isfile(Monthpath)):
            print("-".center(100,'-'))
            ms = getmonth(ms)
            print("\033[31mMonth: {} {}\033[0m".format(ms,m).center(100,' '))
            print("-".center(100,'-'))
            
           
            try:
             current_open_file = open(Monthpath,'rb')
             i = 1
             total =0
             print()
             for _ in range(1000):
                  
              current_e = pickle.load(current_open_file)
              print("\033[31m{}.\033[0m \033[31mAmount:\033[0m {}, \033[31mCategory:\033[0m {}, \033[31mDate:\033[0m {}, \033[31mDescription:\033[0m {}".format( i ,current_e.e_amount, current_e.e_type, current_e.e_date, current_e.e_des))
              i= i+1
              total+=current_e.e_amount
              print()
                  

            except EOFError:
                print("\033[31mTotal Expenses: \033[0m {}".format(total))
                if(total > login_user.monthly_buget[j-1]):
                   print("Budget: {}".format(login_user.monthly_buget[j-1]))
                   print("Warning: {}".format(login_user.user_name))
                   print("Your expenses for {} have exceeded the budget Limit..".format(ms))   
                else:
                   print("Budget: {}".format(login_user.monthly_buget[j-1]))
                   print("Message: {}".format(login_user.user_name))
                   print("Your expenses for {} have Under the budget Limit..".format(ms))
                print()
                print()

            
               
           else:
              count +=1

           
        if(count == 12):
            os.system('cls')
            print("There Was No Data For Given Year ❌ Try Again...")
            menushow(login_user)
            return

        else: 
            print()
            print("-----------------------------------------------------------")
            print()
            print(" ✔️  View Expenses successfully!  ✔️".center(100," "))
            c = int(input("For <- Back Press 1: "))

            if c == 1:
              os.system('cls')
              menushow(login_user)

            else:
              print()
              os.system('cls')
              print(" Personal Expenses Managment System  ".center(100,"="))
              print()
              print("Thank you {} for using Personal Expense Tracker. ✨ Goodbye! ✨".center(100," ").format(login_user.user_name))
              print()
              print("Soory! You Enter Invalid Option 😵 😵 .")
              print("Log out .....")
              print()
              print()

        
    
    elif ch == 4:
       os.system('cls')
       menushow(login_user)
       return
    
    else:
        os.system('cls')
        print()
        print("Soory! You Enter Invalid Option 😵 😵 .")
        menushow(login_user)
        return


def delete_expence(login_user):
    os.system('cls')
    print()
    print(" Personal Expenses Managment System  ".center(100,"="))
    print()

    print()
    print("Hy {} Ready to manage your expenses?".format(login_user.user_name))
    print("Let's help you clean up your records..")
    print("----------------------------------------------------")
    print()

    d = input("Please enter the date of the expense you want to Delete (DD-MM-YYYY): ")
    print()
    date = d.split('-')
    file_name = 'expense_of_'+date[1]+'_'+date[2]+'.txt'

    user_folder = os.getcwd()
    user_folder = os.path.join(user_folder,'userdatabase',login_user.user_email.lower())
    user_folder = os.path.join(user_folder,file_name)

    if(os.path.isfile(user_folder)):
       
       ex = open(user_folder,'rb')

       allexpense =[]

       try:
          for _ in range(100):
              l = pickle.load(ex)
              allexpense.append(l)

       except EOFError:
          ex.close()
        
       
       length = len(allexpense)

       filter_e = []
       for i in range(0,length):
          if(allexpense[i].e_date == d):
             filter_e.append(allexpense[i])
             
          
          else:
             continue
          
       allexpense = [expense for expense in allexpense if expense.e_date != d]   
          
       l_f = len(filter_e)

       print("-".center(100,'-'))
       print("  \033[31mExpenses on {}\033[0m".format(d).center(100,' '))
       print("-".center(100,'-'))

       print()

       if(l_f == 0):
        
        print()
        print("No ❌ expenses found for the specified date. ")
        print("Please check the date and try again. ")
        print()
        print("----------------------------------------------------")
        print()
        c = int(input("For <- Back Press 1: "))

        if c == 1:
         os.system('cls')
         menushow(login_user)
         return
       
       
        else:
         print()
         os.system('cls')
         print(" Personal Expenses Managment System  ".center(100,"="))
         print()
         print("Thank you {} for using Personal Expense Tracker. ✨ Goodbye! ✨".center(100," ").format(login_user.user_name))
         print()
         print("Soory! You Enter Invalid Option 😵 😵 .")
         print("Log out .....")
         print()
         print()

       
       else:
          
          for l in range(0,l_f):
            print("\033[31m{}.\033[0m \033[31mAmount:\033[0m {}, \033[31mCategory:\033[0m {}, \033[31mDate:\033[0m {}, \033[31mDescription:\033[0m {}".format( l+1 ,filter_e[l].e_amount, filter_e[l].e_type, filter_e[l].e_date, filter_e[l].e_des))
            print()
       
       print()
       print("----------------------------------------------------------")
       print()
       ch = int(input("Enter the S.No of the expense you want to delete: "))

       if(ch-1 < l_f):
          print()
          print("Deleting the expense...")
          del filter_e[ch-1]
          
       else:
          os.system('cls')
          print("Soory! You Enter Invalid Option 😵 😵 .")
          menushow(login_user)
          return
       
       allexpense = allexpense+filter_e

       new_l = len(allexpense)
       
       if(new_l == 0):
          os.remove(user_folder)
          return

       
       ex = open(user_folder,'wb')
      

       

       for i in range(0,new_l):
          e = allexpense[i]
          pickle.dump(e,ex)
       
   

       print()
       print("  ✅ Expense deleted successfully! ".center(100," "))
       c = int(input("For <- Back Press 1: "))

       if c == 1:
         os.system('cls')
         menushow(login_user)
         return
       
       
       else:
         print()
         os.system('cls')
         print(" Personal Expenses Managment System  ".center(100,"="))
         print()
         print("Thank you {} for using Personal Expense Tracker. ✨ Goodbye! ✨".center(100," ").format(login_user.user_name))
         print()
         print("Soory! You Enter Invalid Option 😵 😵 .")
         print("Log out .....")
         print()
         print()




        
    else:
       os.system('cls')
       print("No ❌ expenses found for the specified date. ")
       print("Please check the date and try again. ")
       menushow(login_user)
       return
    
    
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
    print("3. Delete Expense")
    print("4. Set Monthly Budget")
    print("5. Export Data")
    print("6. Logout")
    print()
    user_choise = int(input("Enter your choice (1-6): "))

    if user_choise == 1:
        add_expenses(login_user)
    
    elif user_choise == 2:
        view_expence(login_user)

    elif user_choise == 3:
        delete_expence(login_user)
    
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


