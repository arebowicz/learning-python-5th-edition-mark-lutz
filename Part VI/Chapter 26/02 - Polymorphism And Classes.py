class Employee:
  def __init__(self, hoursWorked):
    self.hoursWorked = hoursWorked
    self.salary = 0
  def computeSalary(self):
    self.salary = self.hoursWorked * 20
  def printSalary(self):
    print("Salary: {}".format(self.salary))
  def giveRaise(self, payRise):
    self.salary += payRise

class Programmer(Employee):
  def computeSalary(self):
      self.salary = self.hoursWorked * 50

olgierd = Employee(160)
konrad = Programmer(160)

company = [olgierd, konrad]
for emp in company:
  emp.computeSalary()
  emp.printSalary()