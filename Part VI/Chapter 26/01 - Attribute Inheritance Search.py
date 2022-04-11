class C3:
  w = 30
  z = 31

class C2:
  x = 20
  z = 21

class C1(C2, C3):
  x = 10
  y = 11
  def __init__(self, name):
    self.name = name

I1 = C1("Adam")
I2 = C1("Ewa")

print(I1.name)
print(I1.x)
print(I1.y)
print(I2.z)
print(I2.w)