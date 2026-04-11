#Exercise 1: Favorite Numbers
my_fav_numbers = {7, 10}
my_fav_numbers.remove(10)
print(my_fav_numbers)
friend_fav_numbers = {6, 9}
our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)
#Exercise 2: Tuple
int_tup = (1, 2, 3)
print(int_tup)
int_tup.add(5)
print(int_tup)
#Reason: Some values remain constant, for example Date of Birth or Gender so using Tuple in this case can be more efficient when packing and unpacking large amounts of fixed values
#Exercise 3: List Manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket)
no_of_apples = basket.count("Apples")
print(no_of_apples)
basket.clear()
print(basket)
#Exercise 4: Floats
#Recap: A float is an integer containing decimal values whereas an integer is a whole number from negative infinity to infinity
#float_and_int = [ 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
start_int = 1.0
while start_int <= 5:
   start_int += 0.5
   print(start_int)
#Exercise 5: For Loop
numbers = range(1, 21)
for number in numbers:
   print(number)
for number in numbers:
   if number % 2 == 0:
        print(number)
#Exercise 6: While Loop
name = input('Enter your name:')
while True:
   if name.isdigit():
      name = input('Give the correct name:')
   else:
       print('Thank you')
       break
#Exercise 7: Favorite Fruits
fav_fruits = input('Enter your favourite fruits:')
fav_fruits_list = fav_fruits.split()
print(fav_fruits_list)
fruit = input('Name a fruit!')
if fruit in fav_fruits_list:
   print('You chose one of your favorite fruits! Enjoy!')
else:
   print('You chose a new fruit. I hope you enjoy it!')
#Exercise 8: Pizza Toppings
total_price = 10
toppings = []
while True:
   user_input = input('Enter a topping OR type "quit" to complete your order: ')
   print(f'Adding {user_input} to the toppings list')
   if user_input.lower() == 'quit':
       break
   toppings.append(user_input)
   total_price += 0.25
print('Final list of toppings:', toppings)
print('Total price:', total_price)
#Exercise 9: Cinemax Ticket
age_family = []
while True:
   age = input('Enter the age of the family member OR type "done" to finish: ')
   if age.lower() == 'done':
       break
   elif age.isdigit():
       age_family.append(int(age))
   else:
       print('Please enter a valid age or "done".')
price_under_3 = 0
price_3_to_12 = 10
price_above_12 = 15
total_cost = 0
for age in age_family:
   if age < 3:
       total_cost += price_under_3
   elif 3 <= age <= 12:
       total_cost += price_3_to_12
   else:
       total_cost += price_above_12
print('Total cost for the family tickets is:', total_cost)
