class FirstClass:
  def setdata(self, value):
    self.data = value
  def display(self):
    print(self.data)

class SecondClass(FirstClass):
  def display(self):
    print('Actual value = "{}"'.format(self.data))

z = SecondClass()
z.setdata(42)
z.display()