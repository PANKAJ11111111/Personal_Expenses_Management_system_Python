class user:
    #attributes of user
    user_name = "None"
    user_email = "None"
    user_password = "none"
    monthly_buget = []
    
    def __init__(self):
        
        self.user_name = input("Enter Your Name = ")
        self.user_email =input("Enter Your Email =  ")
        self.user_password = input("Enter Your Password = ")
        self.user_salary = int(input("Enter Your Salary = "))
        self.user_Target = int(input("Enter Your Monthly Expenses Target =  "))
        self.user_mobile = int(input("Enter Your Contect Number = "))
        self.monthly_buget = [self.user_Target] * 12
    
    def ShowUserDetail(self):
        print("User Name = ", self.user_name)
        print("User Email = ", self.user_email)
        print("User Salary = ", self.user_salary)
        print("User Contect No. = ", self.user_mobile)
        print("User Monthly Expenses Target = ", self.user_Target)
        print("target = ",self.monthly_buget)

        