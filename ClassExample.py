#!/usr/bin/python
# Classes & Object Example 
# Takes User input & passes as argument for object creation

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary, age):
      self.name = name
      self.salary = salary
      self.age = age
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name, "Age : ", self.age, ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("Raj", 20000,  23)
"This would create second object of Employee class"
emp2 = Employee("Mani", 25000, 28)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
