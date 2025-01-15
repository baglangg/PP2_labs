#home 
print("Hello, World!")

#syntax
x = 5
y = "Hello, World!"

#comments
#a comment LOL

#variables
x, y, z = "Orange1", "NotBanana", "PossiblyCherry"
print(x)
print(y)
print(z)

x = y = z = "QuestionableOrange"
print(x)
print(y)
print(z)

fruits = ["DirtyApple", "StrangeBanana", "HappyCherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Is Python "
y = "a really "
z = "good Programming language????????"
print(x + y + z)

x = "Notawesome"

def myfunc():
  x = "Definetely awesome"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Python  DATA TYPES
x = 5
print(type(x))
#Bunch of data Types starting from str ending with memoryview

#Python NUMBERS
import random

print(random.randrange(1, 10))

#Python CASTING
x = int(1)   
y = int(2.8) 
z = int("3") #str input but label as int
print (x,y,z)
print(x+z)
#interactions with str and float

#Python Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

txt = "The best things in life are free!"
print("free" in txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)


