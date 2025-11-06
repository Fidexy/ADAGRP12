"""
   Sample code for ADA topic 4

   Date: 20-10-2022

   Following should be inside "Cmp_No.py"
"""

# Cmp_No representing complex numbers (a+bi), 
# where a and b are both floating-point numbers

class Cmp_No:

   # constructor for creating a complex number, default is zero
   def __init__(self, a=0, b=0):
      self.a = a
      self.b = b

   def input(self):           # input a complex number from keyboard
       a, b = input("(a+bi) a b = ").split()
       self.a = float(a)
       self.b = float(b)

   def mag2(self):            # square of magnitude
       return self.a * self.a + self.b * self.b

   def __str__(self):         # convert to str for display
       if self.b < 0: return f"{self.a:g}-{-self.b:g}i"
       return f"{self.a:g}+{self.b:g}i"

   def __add__(self, y):      # complex number addition
       a = self.a + y.a
       b = self.b + y.b
       return Cmp_No(a,b)
   
   def __sub__(self, y):      # complex number subtraction
       a = self.a - y.a
       b = self.b - y.b
       return Cmp_No(a,b)

   def __mul__(self, y):      # complex number multiplication
       a = self.a * y.a - self.b * y.b
       b = self.a * y.b + self.b * y.a
       return Cmp_No(a,b)

   def __truediv__(self, y):  # complex number division
       r = y.mag2()
       a = (self.a * y.a + self.b * y.b)/r
       b = (self.b * y.a - self.a * y.b)/r
       return Cmp_No(a,b)

   def __eq__(self, y):       # comparing magnitudes of two complex numbers
       diff = self.mag2() - y.mag2() 
       if diff > 0.0: return 1
       elif diff < 0.0: return -1
       return 0

# end of "Cmp_No.py"


# Following should be inside "main.py"

# from Cmp_No import *
z1 = Cmp_No(); z1.input()
z2 = Cmp_No(); z2.input()

print(z1, "+", z2, "=", z1+z2)   # Task 0
print(z1, "-", z2, "=", z1-z2)   # Task 1
print(z1, "x", z2, "=", z1*z2)   # Task 2
print(z1, "/", z2, "=", z1/z2)   # Task 3
print(z1, "==", z2, "=", z1==z2) # Task 4