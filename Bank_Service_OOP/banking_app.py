#Banking System Using OOP

#Parent Class : User 
#Child Class : Bank 
#Stores details about the account balance 
# Stores details about the amount 
# Allows for deposits, withdraw, view_balance

#Parent Class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)

#Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender) 
        self.balance = 0
    
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account balance has been updated : £", self.balance)

if __name__ == "__main__":
    johan = Bank('Johan', 21, 'Male')
    print(johan.deposit(100))
    #johan.show_details()


    