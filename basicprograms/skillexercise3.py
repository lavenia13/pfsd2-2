# Ex-3-1
class MyClass:
    class_variable = 33
    def __init__(self):
        self.instance_variable = 116
    def method(self):
        local_variable = 108
        print("Namespace inside method:", locals())
# Creating an instance of MyClass
obj = MyClass()
# Displaying namespaces
print("Namespace of the class:", MyClass.__dict__)
print("Namespace of the instance:", obj.__dict__)
# Calling a method to show its local namespace
obj.method()
# Ex-3-2
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    def add_student_class(self, student_class):
        self.student_class = student_class
# Creating an instance of the Student class
student = Student(1, 'SriRam')
# Displaying the attributes and their values before removal
print("Attributes and values before removal:")
print(student.__dict__)
# Adding a new attribute student_class
student.add_student_class('Class 10')
# Displaying the attributes and their values after adding student_class
print("\nAttributes and values after adding student_class:")
print(student.__dict__)
# Removing the student_name attribute
delattr(student, 'student_name')
# Displaying the attributes and their values after removing student_name
print("\nAttributes and values after removing student_name:")
print(student.__dict__)



#Ex-3-3
class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of Rs.{amount} successful.")
        self.display()

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of Rs.{amount} successful.")
            self.display()
        else:
            print("Insufficient funds for withdrawal.")

    def bankFees(self):
        fees = self.balance * 0.05
        self.balance -= fees
        print(f"Bank fees of 5% applied. Remaining balance: Rs{self.balance}")
        self.display()
    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Holder Name: {self.name}")
        print(f"Balance: Rs.{self.balance}")
# Example usage:
account = BankAccount(123456, "John Doe", 2000)
account.display()

account.deposit(500)
account.withdrawal(200)
account.bankFees()

