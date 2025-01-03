# here main login of code prasent

def register():
    print("here we implement code for registration")

def login():
    print("code for Login ")

def exit():
    print()
    print("Thank you for using Personal Expense Tracker. Goodbye!".center(100," "))
    print()

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
