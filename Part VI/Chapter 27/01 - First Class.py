class FirstClass:
  def setdata(self, value):
    self.data = value
  def display(self):
    print(self.data)

x = FirstClass()
y = FirstClass()

x.setdata("Król Artur")
FirstClass.setdata(y, 3.14159)

x.display()
y.display()