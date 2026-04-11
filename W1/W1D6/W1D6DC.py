# Challenge 1: Letter Index Dictionary
my_string = "dodo"
my_string = "froggy"
my_string = "grapes"
my_string = input('Enter a word: ')
word_dict = {}
for index, char in enumerate(my_string):
    if char in word_dict:
        word_dict[char].append(index)
    else:
        word_dict[char] = [index]
    print(f"{index}: {char}")
print(word_dict)
# Challenge 2: Affordable Items
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet = "$100"
items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet = "$1"
wallet_value = int(wallet.replace("$", "").replace(",", ""))
basket = []
for item, price in items_purchase.items():
    price_value = int(price.replace("$", "").replace(",", ""))
    if wallet_value >= price_value:
        basket.append(item)
        wallet_value -= price_value
if not basket:
    print("Nothing")
else:
    print(sorted(basket))
print(f'Final wallet value: ${wallet_value}')

