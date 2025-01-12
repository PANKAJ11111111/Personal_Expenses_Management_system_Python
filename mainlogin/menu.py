import os
import expense_class as e
import datetime
import pickle
from colorama import Fore, Back, Style
from Mail_handler.mail import send_email_with_attachment


# for get month name logic
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


# logic for add expence
def add_expenses(login_user):
    os.system('cls')
    print()
    print("💫 Welocome To Personal Expenses Managment System ".center(100,"="))
    print()

    print()
    print("Hy \033[31m{}\033[0m  its Time to log your latest spending! ❤️".format(login_user.user_name))
    print("Enter the details to keep your budget updated...")
    print()
    print("\033[31m----------------------------------------------------\033[0m")
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
            os.system('cls')
            print("Soory! You Enter Invalid Option 😵 😵 .")
            menushow(login_user)
            return
            
            
        print()


#login for view wzpense
def view_expence(login_user):
    os.system('cls')
    print()
    print("💫 Welocome To Personal Expenses Managment System ".center(100,"="))
    print()

    print()
    print("Hy \033[31m{}\033[0m  Let’s see where your money has gone!".format(login_user.user_name))
    print("Select a view option to get started..")
    print()
    print("\033[31m----------------------------------------------------\033[0m")
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
        print(" 💫 Welocome To Personal Expenses Managment System ".center(100,"="))
        print()

        print()
        print("Hy \033[31m{}\033[0m  Let’s see where your money has gone!".format(login_user.user_name))
        print()
        print("\033[31m----------------------------------------------------\033[0m")
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
                current_open_file.close()
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
        print("\033[31m-----------------------------------------------------------\033[0m")
        print()
        print(" ✔️  View Expenses successfully!  ✔️".center(100," "))
        c = int(input("For <- Back Press 1: "))

        if c == 1:
         os.system('cls')
         menushow(login_user)
         return
        else:
         os.system('cls')
         print("Soory! You Enter Invalid Option ❌ ❌.")
         menushow(login_user)
         return
    
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
            print("💫 Welocome To Personal Expenses Managment System ".center(100,"="))
            print()

            print()
            print("Hy \033[31m{}\033[0m Let’s see where your money has gone!".format(login_user.user_name))
            print()
            print("\033[31m----------------------------------------------------\033[0m")
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
                if(total > login_user.monthly_buget[monthint-1]):
                   print("Budget: {}".format(login_user.monthly_buget[monthint-1]))
                   print("Warning: {}".format(login_user.user_name))
                   print("Your expenses for {} have exceeded the budget Limit..".format(mstring))   
                else:
                   print("Budget: {}".format(login_user.monthly_buget[monthint-1]))
                   print("Message: {}".format(login_user.user_name))
                   print("Your expenses for {} have Under the budget Limit..".format(mstring))
                print()
                print("\033[31m----------------------------------------------------\033[0m")
                print()
                current_open_file.close()
                print(" ✔️  View Expenses successfully!  ✔️".center(100," "))
                c = int(input("For <- Back Press 1: "))

                if c == 1:
                 os.system('cls')
                 menushow(login_user)
                 return
                
                else:
                 os.system('cls')
                 print("Soory! You Enter Invalid Option ❌ ❌.")
                 menushow(login_user)
                 return

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
        print(" 💫 Welocome To Personal Expenses Managment System  ".center(100,"="))
        print()

        print()
        print("Hy \033[31m{}\033[0m Let’s see where your money has gone!".format(login_user.user_name))
        print()
        print("\033[31m----------------------------------------------------\033[0m")
        print()

        
        print()
        print("===== All Expenses Of \033[31m{}\033[0m =====".format(m))
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
                current_open_file.close()
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
            print("\033[31m-----------------------------------------------------------\033[0m")
            print()
            print(" ✔️  View Expenses successfully!  ✔️".center(100," "))
            c = int(input("For <- Back Press 1: "))

            if c == 1:
              os.system('cls')
              menushow(login_user)

            else:
              os.system('cls')
              print("Soory! You Enter Invalid Option ❌ ❌.")
              menushow(login_user)
              return
        
    
    elif ch == 4:
       os.system('cls')
       menushow(login_user)
       return
    
    else:
        os.system('cls')
        print()
        print("Soory! You Enter Invalid Option ❌ ❌ .")
        menushow(login_user)
        return


#logic for delete expence
def delete_expence(login_user):
    os.system('cls')
    print()
    print("💫 Welocome To Personal Expenses Managment System ".center(100,"="))
    print()

    print()
    print("Hy {} Ready to manage your expenses?".format(login_user.user_name))
    print("Let's help you clean up your records..")
    print()
    print("\033[31m----------------------------------------------------\033[0m")
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
        print("\033[31m----------------------------------------------------\033[0m")
        print()
        c = int(input("For <- Back Press 1: "))

        if c == 1:
         os.system('cls')
         menushow(login_user)
         return
       
       
        else:
         os.system('cls')
         print("Soory! You Enter Invalid Option ❌ ❌.")
         menushow(login_user)
         return

       
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
          ex.close()
          os.remove(user_folder)
          print()
          print("  ✅ Expense deleted successfully! ".center(100," "))
          c = int(input("For <- Back Press 1: "))


          if c == 1:
           os.system('cls')
           menushow(login_user)
           return
       
       
          else:
           os.system('cls')
           print("Soory! You Enter Invalid Option ❌ ❌.")
           menushow(login_user)
           return
          

       else:
        ex = open(user_folder,'wb')

        for i in range(0,new_l):
           e = allexpense[i]
           pickle.dump(e,ex)
       
   
        ex.close()
        print()
        print("  ✅ Expense deleted successfully! ".center(100," "))
        c = int(input("For <- Back Press 1: "))

        if c == 1:
          os.system('cls')
          menushow(login_user)
          return
       
       
        else:
          os.system('cls')
          print("Soory! You Enter Invalid Option ❌ ❌.")
          menushow(login_user)
          return



        
    else:
       os.system('cls')
       print("No ❌ expenses found for the specified date. ")
       print("Please check the date and try again. ")
       menushow(login_user)
       return
    

#logic for set monthly target
def set_monthly(login_user):
    print(" 💫 Welocome To Personal Expenses Managment System  ".center(100,"="))
    print()
    print("Hi \033[31m{}\033[0m 🎯 ".format(login_user.user_name))
    print("Managing your expenses is easier with a clear goal. Let's set your financial target! 🚀")
    print()
    print()
    print("\033[31m----------------------------------------------------\033[0m")

    print("Which month's target would you like to set/update? ")
    print()
    print("1.  January  ")
    print("2.  February ")
    print("3.  March ")
    print("4.  April ")
    print("5.  May ")
    print("6.  June ")
    print("7.  July")
    print("8.  August ")
    print("9.  September ")
    print("10. October ")
    print("11. November ")
    print("12. December ")
    print()

    ch = int(input("Enter the number for the month: "))
    print("----------------------------------------------------")
    print()

    mstr = ''

    if ch == 1 :
        mstr = 'January'
    elif ch == 2 :
        mstr = 'February'
    elif ch == 3 :
        mstr = 'March'
    elif ch == 4 :
        mstr = 'April'
    elif ch == 5 :
        mstr = 'May'
    elif ch == 6 :
        mstr = 'June'
    elif ch == 7 :
        mstr = 'July'
    elif ch == 8 :
        mstr = 'Augest'
    elif ch == 9 :
        mstr = 'September'
    elif ch == 10:
        mstr = 'October'
    elif ch == 11:
       mstr = 'November'
    elif ch == 12:
       mstr = 'December'
    else:
     os.system('cls')
     print("Soory! You Enter Invalid Option ❌ ❌.")
     menushow(login_user)
     return
      
       

    
    newv = int(input("Please enter your new target for {} : ".format(mstr)))

    login_user.monthly_buget[ch-1] = newv
    print()

    print("✨ Your monthly target for {} has been successfully updated to ₹ {}! 🌟 ".format(mstr,newv).center(100,' '))
    print()


    alluser = []

    userfile = os.getcwd()
    userfile = os.path.join(userfile,'userdatabase','userdata.txt')

    file = open(userfile,'rb')

    try:
       for _ in range(1000):
          user = pickle.load(file)
          alluser.append(user)

    except EOFError:
       file.close()

    alluser = [useri for useri in alluser if useri.user_email != login_user.user_email]
    alluser.append(login_user)

    file = open(userfile,'wb')

    for i in range(0,len(alluser)):
       useri = alluser[i]
       pickle.dump(useri,file)
       
    file.close()
    c = int(input("For <- Back Press 1: "))

    if c == 1:
      os.system('cls')
      menushow(login_user)
      return
       
       
    else:
     os.system('cls')
     print("Soory! You Enter Invalid Option ❌ ❌.")
     menushow(login_user)
     return


#logic for export data
def export_data(login_user):
   
   os.system('cls')
   print(" 💫 Welocome To Personal Expenses Managment System  ".center(100,"="))
   print()
   print("Hi \033[31m{}\033[0m! 📁  ".format(login_user.user_name))
   print("Let's help you save or share your expense data with ease. 📝")
   print()
   print()
   print("\033[31m----------------------------------------------------\033[0m")
   print()

   print("🔹 Select the data you wish to export: ")
   print()
   print("1. All Expenses  ")
   print("2. Expenses for a Specific Month ")
   print("3. Back")
   print()
   ch  = int(input("Enter your choice (1/2/3): "))
   print()

   if ch == 1:
        
        user_folder = os.getcwd()
        user_folder = os.path.join(user_folder,'userdatabase',login_user.user_email.lower())
        export_path = os.path.join(user_folder,'export.txt')
        all_expense_file = os.listdir(user_folder)
        export_file = open(export_path,'a')

        
        export_file.write(" Personal Expenses Managment System  ".center(100,"="))
        export_file.write('\n')

        export_file.write('\n')
        export_file.write('\n')
        export_file.write("Hy {} Let’s see where your money has gone!\n".format(login_user.user_name))
        export_file.write("----------------------------------------------------")
        export_file.write('\n')

        
        export_file.write('\n')
        export_file.write("===== All Expenses =====")
        export_file.write('\n')
        export_file.write('\n')
        
        for i in range(len(all_expense_file)):
        
            month_file = os.path.join(user_folder,all_expense_file[i])
            month_sep = all_expense_file[i].split('_')
            month = month_sep[2]
            month_str = getmonth(month)
            year = month_sep[3].split('.')

            export_file.write('-----------------------------------------------------------------------')
            export_file.write('\n')
            export_file.write('\n')
            export_file.write("Month: {} {} \n".format(month_str,year[0]).center(100,' '))

            export_file.write('\n')
            
            
            current_open_file = open(month_file,'rb')
       
            try:
              
              i = 1
              total =0
              export_file.write('\n')
              for _ in range(1000):
                  
                  current_e = pickle.load(current_open_file)
                  export_file.write('\n')
                  export_file.write("{}. Amount: {}, Category: {}, Date: {}, Description: {} \n".format( i ,current_e.e_amount, current_e.e_type, current_e.e_date, current_e.e_des))
                  i= i+1
                  total+=current_e.e_amount
                  export_file.write('\n')
                  

            except EOFError:
                current_open_file.close()
                export_file.write("Total Expenses:  {} \n".format(total))
                monthint = int(month)-1
                
                if(total > login_user.monthly_buget[monthint-1]):
                   export_file.write("Budget: {}\n".format(login_user.monthly_buget[monthint]))
                   export_file.write("Warning: {}\n".format(login_user.user_name))
                   export_file.write("Your expenses for {} have exceeded the budget Limit..\n".format(month_str))   
                else:
                   export_file.write("Budget: {}\n".format(login_user.monthly_buget[monthint]))
                   export_file.write("Message: {}\n".format(login_user.user_name))
                   export_file.write("Your expenses for {} have Under the budget Limit..\n".format(month_str))
                    
                export_file.write('\n')
                continue
         

        export_file.close()
        sender_email = "pankajwork33@gmail.com"  # Your email
        sender_password = "rdox ymsq xvdu bhpz"  # Your email password or app password
        recipient_email = login_user.user_email # Recipient's email
        subject = "Personal Expense Managment System Exported Data "
        body = """Dear {},

Your expense data has been successfully exported and is attached to this email.

File Name: {}

Keep this file safe for your records. For any questions, feel free to contact us.

Thank you,
Personal Expense Managment System Exported Data
Expense Management Team
Pankaj Saratkar """.format(login_user.user_name, 'export.txt', )
        
        file_add = os.getcwd()

        file_add = os.path.join(file_add,'userdatabase', login_user.user_email,'export.txt')
        print()
        print("----------------------------------------------------") 
        print()
        print("📂 Exporting your All data ...")

        send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, file_add)

        print()
        print("----------------------------------------------------") 
        print()
        print("📂 Exporting your All data ...")
        print("✔ Data exported successfully! 🎉  ")
        print("Your expenses have been Send On Your Register Mail Id....")
        os.remove(file_add)
        
        print()
        c = int(input("For <- Back Press 1: "))

        if c == 1:
         os.system('cls')
         menushow(login_user)
         return
       
       
        else:
         os.system('cls')
         print("Soory! You Enter Invalid Option ❌ ❌.")
         menushow(login_user)
         return




   elif ch == 2:
        print()
        m = input("Enter Month & Year (MM-YYYY): ")
        l = m.split('-')
        print()

        mstring = getmonth(l[0])
        user_folder = os.getcwd()
        export_path = os.path.join(user_folder,'userdatabase',login_user.user_email.lower(),'export.txt')
        export_file = open(export_path,'a')
        user_folder = os.path.join(user_folder,'userdatabase',login_user.user_email.lower())
        Monthpath = 'expense_of_'+l[0]+'_'+l[1]+'.txt'
        Monthpath = os.path.join(user_folder,Monthpath)

        
        if(os.path.isfile(Monthpath)):
            
            
            export_file.write(" Personal Expenses Managment System  ".center(100,"="))
            export_file.write('\n')

            export_file.write('\n')
            export_file.write("Hy {} Let’s see where your money has gone!\n".format(login_user.user_name))
            export_file.write("----------------------------------------------------")
            export_file.write('\n')

        
            export_file.write('\n')
            export_file.write("===== All Expenses Of {} =====".format(mstring))
            export_file.write('\n')
            export_file.write('\n')
            export_file.write("-".center(100,'-'))
            export_file.write('\n')
            
            try:
             current_open_file = open(Monthpath,'rb')
             i = 1
             total =0
             export_file.write('\n')
             for _ in range(1000):
                  
              current_e = pickle.load(current_open_file)
              export_file.write("{}. Amount: {}, Category: {}, Date: {}, Description: {} \n".format( i ,current_e.e_amount, current_e.e_type, current_e.e_date, current_e.e_des))
              i= i+1
              total+=current_e.e_amount
              export_file.write('\n')
                  

            except EOFError:
                export_file.write("Total Expenses: {}\n".format(total))
                monthint = int(l[0])
                if(total > login_user.monthly_buget[monthint-1]):
                   export_file.write("Budget: {}\n".format(login_user.monthly_buget[monthint-1]))
                   export_file.write("Warning: {}\n".format(login_user.user_name))
                   export_file.write("Your expenses for {} have exceeded the budget Limit..\n".format(mstring))   
                else:
                   export_file.write("Budget: {}\n".format(login_user.monthly_buget[monthint-1]))
                   export_file.write("Message: {}\n".format(login_user.user_name))
                   export_file.write("Your expenses for {} have Under the budget Limit..\n".format(mstring))

                export_file.close()
                sender_email = "pankajwork33@gmail.com"  # Your email
                sender_password = "rdox ymsq xvdu bhpz"  # Your email password or app password
                recipient_email = login_user.user_email # Recipient's email
                subject = "Personal Expense Managment System Exported Data "
                body = """Dear {},

Your expense data has been successfully exported and is attached to this email.

File Name: {}

Keep this file safe for your records. For any questions, feel free to contact us.

Thank you,
Personal Expense Managment System Exported Data
Expense Management Team
Pankaj Saratkar """.format(login_user.user_name, 'export.txt', )
        
                file_add = os.getcwd()
        
                file_add = os.path.join(file_add,'userdatabase', login_user.user_email,'export.txt')
                
                print()
                print("----------------------------------------------------") 
                print()
                print("📂 Exporting your All data ...")
                send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, file_add)

                print("✔ Data exported successfully! 🎉  ")
                print("Your expenses have been Send On Your Register Mail Id....")
                os.remove(file_add)
                print()
                c = int(input("For <- Back Press 1: "))

                if c == 1:
                  os.system('cls')
                  menushow(login_user)
                  return
       
       
                else:
                 os.system('cls')
                 print("Soory! You Enter Invalid Option ❌ ❌.")
                 menushow(login_user)
                 return
 

        else:
            export_file.close()
            os.remove(export_path)
            os.system('cls')
            print("There Was No Data For Given Month ❌ Try Again...")
            menushow(login_user)


            

   
   elif ch == 3:
      os.system('cls')
      menushow(login_user)
      return
   
   else:
     os.system('cls')
     print("Soory! You Enter Invalid Option ❌ ❌.")
     menushow(login_user)
     return


# logic for log out    
def logoutcode(login_user):

    os.system('cls')
    print()
    print(" 💫 Welocome To Personal Expenses Managment System  ".center(100,"="))
    print()
    print("Thank you {} for using Personal Expense Tracker. ✨ Goodbye! ✨".center(100," ").format(login_user.user_name))
    print()
    print("Log Out.....")
    print()
    print()


#main menu logic
def menushow(user):
    login_user = user
    print()
    print(" 💫 Welocome To Personal Expenses Managment System  ".center(100,"="))
    print()
    print("Hello \033[31m{}\033[0m! It's always a pleasure to assist you. ❤️".format(login_user.user_name)) 
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
        os.system('cls')
        set_monthly(login_user)
    
    elif user_choise == 5:
        export_data(login_user)
    
    elif user_choise == 6:
        logoutcode(login_user)
    
    else:
        os.system('cls')
        print("\033[31mYou Enter Invalid Option! ❌ Try Again...\033[0m")
        menushow(login_user)


