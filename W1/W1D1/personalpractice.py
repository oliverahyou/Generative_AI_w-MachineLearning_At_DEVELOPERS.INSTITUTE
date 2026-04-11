VAT_AMOUNT = 0.15
price = 300
total_price = price * VAT_AMOUNT
print(total_price)
print(type(3.14))
print(type(33))
print(type('helloworld'))
print(type('hellow0rld'))
#capitalise
print('helloworld'.capitalize())
#uppercase
print('helloworld'.upper())
#lowercase
print('PUPPY'.lower())
#replace
print('hello world'.replace('kitty', 'kit'))
description = "strings are..."
print(description.upper())
print(description.replace('are', 'is'))
print('strings')
#exercise: In the python shell, Create a variable called my_age, use python to know how old you will be in 123879 years
y_o_b = 1996
current_year = 2025
my_age= (current_year - y_o_b) + 123879
print('In 123879 years from now, I will be ' + str(my_age) + ' years old!')
#exercise: In the python shell, Create a variable called first_name and a variable called last_name, and then print your full name using those two variables
first_name = ('Oliver')
last_name = ('Ah You')
full_name = first_name + ' ' + last_name
print('My name is ' + full_name)
#booleans: true or false
#greater than
booleeean= 1>2
print(booleeean)
#greater than or equal to
booleeean = 3>=3
print(booleeean)
#lower than
booleeean = 1<1
print(booleeean)
#lower than or equal to
booleeean = 1<=1
print(booleeean)
#equal to
booleeean = 1==1
print(booleeean)
#not equal to
booleeean = 'potato' != 'potato'
print(booleeean)
#1. Check if x is less than y and y is greater than z.
#2. Verify if word1 is not equal to word2.
#3. Use the bool() function to check the boolean value of z and word1.
x = 5
y = 10
z = 0
word1 = 'hello'
word2 = 'world'
print(x < y and y > z)
print(word1 == word2)
print(bool(z))
print(bool(word1))