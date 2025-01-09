class expense:

    def __init__(self):
        self.e_amount = float(input("🔹Enter expense amount: "))
        self.e_type = input("🔹Enter category (e.g., Food, Travel, Bills): ")
        self.e_date = input("🔹Enter date (DD-MM-YYYY): ")
        self.e_des = input("🔹Enter description: ")
    
    def showexpens(self):
        print(self.e_amount)