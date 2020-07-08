# Start Program
"""
Program: new_employee.py
Author: Paul Thairu
Last date modified: 07/07/2020

Write a program that creates two derived classes, SalariedEmployee and HourlyEmployee.
SalariedEmployee with members start_date and salary and methods give_raise()
that updates salary and display() that returns a string.
HourlyEmployee has hourly_pay, start_date, method give_raise() that updates salary and
display() that returns a string.

"""
from datetime import date

# declaring Employee class
class Employee:
    # Declaring name variable
    def __init__(self, name):
        self.name = name

    # Function that displays employee name
    def display(self):
        print("Employee Name: " + self.name)

# Salaried employee derived class
class SalariedEmployee(Employee):
    # Function to declare variables
    def __init__(self, name, start_date, salary):
        Employee.__init__(self, name)  # name variable inherited from Employee class
        self.start_date = start_date  # declaring start date variable
        self.salary = salary  # declaring salary variable

    # Function that raises employee salary
    def give_raise(self, increment):
        self.salary = self.salary + increment  # incrementing employee salary

    # Function that display salary employee information
    def display(self):
        Employee.display(self)
        print("Employee start Date: " + self.start_date + " Salary: $", self.salary)

# Hourly employee derived class
class HourlyEmployee(Employee):
    # Function to declare variables
    def __init__(self, name, start_date, hourly_pay):
        Employee.__init__(self, name)  # name variable inherited from Employee class
        self.start_date = start_date  # declaring start date variable
        self.hourly_pay = hourly_pay  # declaring hourly pay variable

    # Function that raises employee hourly pay
    def give_raise(self, hourly_increment):
        self.hourly_pay = self.hourly_pay + hourly_increment

    # Function that display salary employee information
    def display(self):
        Employee.display(self)
        print("Employee start date: " + self.start_date + " Hourly pay: $", float(self.hourly_pay))

# creating Employee1 object and assigning values
Employee1 = SalariedEmployee('Paul Thairu', str(date.today()), 45000)
Employee1.display()
print("****** New salary after employee have been given a raise *******")
# Incrementing Employee1 object salary by $ 5000
Employee1.give_raise(5000.00)
# Displaying Employee1 new salary
Employee1.display()
print("---------------------------------------------------")
# creating Employee2 object and assigning values
Employee2 = HourlyEmployee('Beth Maina', str(date.today()), 10)
Employee2.display()
print("******* New hourly pay after employee have been given a raise ******")
# Incrementing Employee2 hourly pay with $ 2
Employee2.give_raise(2.00)
# Displaying Employee2 new hourly pay
Employee2.display()

del Employee1
del Employee2

# End program

