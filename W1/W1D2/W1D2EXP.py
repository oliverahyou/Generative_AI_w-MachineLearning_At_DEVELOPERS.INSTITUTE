#Exercise 1: Hello World
from idlelib.query import CustomRun
from tkinter.constants import SEL_LAST
print('Hello world\n'*4)
#Exercise 2: Some Math
print((99^3)*8)
#Exercise 3: What is the output?
#>>> 5 < 3 FALSE
#>>> 3 == 3 TRUE
#>>> 3 == "3" FALSE
#>>> "3" > 3 FALSE, ERROR
#>>> "Hello" == "hello" FALSE
print(5 < 3)
print(3 == 3)
print(3 == "3")
#print("3" > 3)
print("Hello" == "hello")
#Exercise 4: Your computer brand
computer_brand = 'Dell'
print(f'I have a {computer_brand} computer.')
#Exercise 5: Your information
name = 'Oliver Ah You'
age = 29
shoe_size = 40
info = 'Wabalabadubdub!'
print(f'{info}. My name is {name}, and I am {age} years old.' )
#Exercise 6: A & B
a = 1
b = 0
if a > b:
    print('Hello World')
#Exercise 8: What’s your name?
a = input('Enter any number to continue')
if int(a) % 2 != 0:
    print('sweggity sweg')
#Exercise 8: What’s your name?
my_name = 'Oliver'
a = input('Hi. What is your name?')
if a == my_name:
    print('Wawaweewaaa')
#Exercise 9: Tall enough to ride a roller coaster
a = input('Enter your height in centimeters to continue')
if int(a) > 145:
    print('You are tall enough to ride this roller coaster!')
else:
    print('You are not tall enough to ride this roller coaster! Come back again when you grow taller!')

