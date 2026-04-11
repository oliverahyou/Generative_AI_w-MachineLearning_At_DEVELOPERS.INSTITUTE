#Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dictionary = dict(zip(keys, values))
print(my_dictionary)
#Exercise 2: Cinemax #2
family = {
   'rick': 43, 
   'beth': 13, 
   'morty': 5, 
   'summer': 8
}
Price_under_3 = 0 
Price_3_to_12 = 10
Price_over_12 = 15
total_price = 0
for name, age in family.items():
   if age < 3:
       total_price += Price_under_3
   elif 3 <= age <= 12:
       total_price += Price_3_to_12
   else:
       total_price += Price_over_12
print(f'The total price for the family is: ${total_price}')
#Exercise 3: Zara
brand = {
   'name': 'Zara',
'creation_date': 1975,
'creator_name': 'Amancio Ortega Gaona',
'type_of_clothes': ['men', 'women', 'children', 'home'],
'international_competitors': ['Gap', 'H&M', 'Benetton'],
'number_stores': 7000,
'major_color': { 
   'France': 'blue', 
   'Spain': 'red', 
   'US': ['pink', 'green']
}
}
brand['number_stores'] = 2
print(brand['number_stores'])
brand['type_of_clothes'].append('Zara customers have a good sense of style')
print(brand['type_of_clothes'])
brand['country_creation'] = 'Spain'
print(brand)
if 'international_competitors' in brand:
   brand['international_competitors'].append('Desigual')
print(brand['international_competitors'][-1])
del brand['creation_date']
brand.pop('creation_date')
print(brand['international_competitors'][-1])
print('White, blue and red are the major colors in the US.')   
print(len(brand.keys()))
print(brand.keys())
more_on_zara = {
   'creation_date': 1975,
   'number_stores': 7000
}
brand.update(more_on_zara)
print(brand)
#Exercise 4: Disney Characters
users = [
   "Mickey",
    "Minnie", 
    "Donald", 
    "Ariel", 
    "Pluto"
]
user_dict = {user: index for index, user in enumerate(users)}
print(user_dict)
user_dict = {index: user for index, user in enumerate(users)}
print(user_dict)
sort_users = sorted(users)
print(sort_users)
user_dict = {user: index for index, user in enumerate(sort_users)}
print(user_dict)