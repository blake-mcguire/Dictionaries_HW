# a dictionary is an ordered collection of keyvalue pairs
# where each key is unique and each key is associated with a value
# a dictionary is mutable, unordered, and indexed
# a dictionary is created using curly braces {}

kitchen = {}

print(kitchen)
print(type(kitchen))

# storing key-value pairs in a dictionary

kitchen = {
    # Key  :  Value
    "dish": "biryani",
    "price": 100,
    "quantity": 2
}

# Keys in a dictionary should be unique
Kitchen = {
    "dish": "biryani",
    'price': 100,
    'quantity': 2,
    'dish': 'pulao'
}

print(Kitchen)

# WHat can we use as keys in a dictionary?
# 1. Strings
# 2. Numbers
# 3. Tuples
# 4. Boolean
# 5. Float
# 6. Complex
# 7. None


# Most
int_dict = {
    1: "first key",
    2: "second key",
    3: "third key"
}

print(int_dict)

# Accessing values in a dictionary
# dictionary_name[key]

print(int_dict[1])

# be careful when using integers as keys because it makes the code less readable

# usinng number strigns as keys

new_dict = {
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four"
}
print(new_dict['1'])

# new error< key error, happens when you try to access a key that does not exist in the dictionary

# dict.get(key) <- return a value from a key in oour dictionary
# can defien a second argument to return if the key does not exist

print(new_dict.get('1', 'key does not exist'))

# Adding and updating our dictionary
community_center = {
    'Smash Tournament': '7pm',
    'Yoga Class': '5am'
    
}
# Adding to a dictionary
# Dictname[key] = value to be added
community_center['Zumba Class'] = '6pm'
print(community_center)
community_center['art session'] = '3pm'
print(community_center)
community_center['Knitting'] = '4pm'

# What if the key already exists?
# It will update the value of the key
community_center['Zumba Class'] = '6:30pm'
# updaring a key-value pair

# Creating a counter dictionary
counter = {}
pokemon_cards = ["Charmander", "Pikachu", "Charmander", "Bulbasaur", "Pikachu", "Squirtle", "Pikachu", "Bulbasaur", "Charmander", "Squirtle"]


# Creating a counter dictionary: Takes a list of items and returns a dictionary with the count of each item as the value for each key
for card in pokemon_cards:
    if card in counter:
        counter[card] += 1
    else:
        counter[card] = 1
        
print(counter)

# Look into python tutor   to see how the code is working

# Removing key-value pairs from a dictionary
#  .pop(key, value_if_not_found) <- removes a key-value pair from a dictionary
inventory = {
    'apples': 430,
    'bananas': 312,
    'oranges': 525,
}
removed_item = inventory.pop('apples', 'item not found') # returns the value of the key-value pair that was removed
print(removed_item)
# Popping a key that does not exist
attempted_pop = inventory.pop('grapes', 'item not found')
print(attempted_pop)
#  .popitem() <- removes the last key-value pair from a dictionary
last_item = inventory.popitem()
print(last_item)
print(inventory)
# Dictionaries are ordered in python 3.7 and above
# before dictionaries were unordered .popitem() would remove a random key-value pair

#  del dictname[key] <- removes a key-value pair from a dictionary
inventory['starfruit'] = 100
del inventory['starfruit']
print(inventory)

# .clear() <- removes all key-value pairs from a dictionary
inventory.clear()
print(inventory)

# dict.keys() -> list of all keys ina dictionary
contacts = {
    'name':'Alice', "age": 30, 'phone': '123-456-7890'
}
for key in contacts.keys():
    print(key)

# looping through keys and using them to access values
print('Here is your contact list')
for key in contacts.keys():
    print(f'{key}: {contacts[key]}')
    
# by default looping through a dictionary accesses its keys
for info in contacts:
    print(f"{info}: {contacts[info]}")

# dict.values() -> list all of the values in a dictionary
temps = {"Monday": 97, "Tuesday": 92, "Wednesday": 94}
print(temps.values())
print("Here is the forecast for the next 3 days")
for temp in temps.values():
    print(temp)

#dict.items() -> return a list of tuples with the key in the first position and the value in the second position

book_ratings = {
    "Harry Potter": 9,
    "The Hobbit": 7,
    "The Hunger Games": 8
}
print(book_ratings.items())

for item in book_ratings.items():
    print(item) # prints a tuple for each key-value apir int he dictionary
    
for book, rating in book_ratings.items():
    print(f"{book} is rated {rating}")
    
# USing sorted() on a dictionaries keys ot valuess
colors = {'red': 2, 'blue': 3, 'green': 1}
print(sorted(colors)) #['blue', 'green', 'red']
print(sorted(colors.values())) # [1, 2, 3]
print(sorted(colors.items())) # [('blue', 3), ('green', 1), ('red', 2)]
print(sorted(colors.keys())) # ['blue', 'green', 'red']

# dict.updated({key: value}) -> updates a dictionary with another dictionary
colors.update({'yellow': 4})
print(colors)

kitchen = {
    "dish": "biryani",
    "price": 100,
    "quantity": 2
}

# Updatibg a current key-value pair
kitchen.update({"price": 150})
print(kitchen)
# updating multiple key-value pairs
kitchen.update({"price": 150, "quantity": 3})
print(kitchen)  

counter_top_stuff = {"Toaster": 1, 
                     "Microwave": 1, 
                     "Coffee Maker": 1,
                     'Rice Cooker': 2,
                     }
# combining two dictionaries
kitchen.update(counter_top_stuff)
print(kitchen)

# dictionary.setdefault(key, value) -> returns the value of a key in a dictionary

# if the key does not exist, it adds the key-value pair to the dictionary

inventory = {
    'apples': 430,
    'bananas': 312,
    'oranges': 525,
}
inventory.setdefault('grapes', 18)
print(inventory)

apples = inventory.setdefault('apples')
print(apples)

# with no second argument - add the key to the dictionary with a value of None
inventory.setdefault('canteloupe')
print(inventory)
# Cannot slice a dictionary
# print(inventory[2:])


# Create a dictionary with 2 key value pairs to start 
# then update with assignemnt: 2 new key value pairs
# then use ,update() to add 3 more key value pairs
# then deletew as many items as you like with pop or del

blakes_dict = {
    'name': 'Blake',
    'age': 19
}
blakes_dict['height'] = '6ft'   
blakes_dict['weight'] = '178lbs'
blakes_dict.update({'hair': 'brown', 'eyes': 'blue', 'knuckles': 'unpopped'})
blakes_dict.pop('knuckles')


# nesting collections in a dictionary
# ie; having a value for a key that is a list

# most frequently applied in api
library = {
    'Fantasy': ['Harry Potter', 'The Hobbit'],
    'Sci-Fi': ['Dune', 'Star Wars'],
    'Mystery': ['Sherlock Holmes', 'Nancy Drew']
    }

# Accessing a list that is a value in a dictionary
fantasy_books = library['Fantasy']
print(fantasy_books)
for book in fantasy_books:
    print(book)
    
for book in library["Sci-Fi"]:
    print(book)
    
print(library['Mystery'][0])

print(library['Fantasy'][1])

# adding an item to a list that is a value in a dictionary
library['Fantasy'].append('Lord of the Rings')
print(library)

# Looping through a dictionaried items and then the contents of its values 

for genre, books in library.items():
    print(f"Here are the books for the {genre} genre: ")
    for book in books:
        print(f" ~ {book}")
        
# Dictionaries in lists
art_gallery = [
    {'Title': 'Starry night', "Artist": "Van Gogh", "Year": 1888},
    {'Title': 'The Scream', 'Artist': 'Munch', 'Year': 1939},
    {'Title': 'Guernica', 'Artist': 'Picasso', 'Year': 1937}
]
art_gallery.append({'Title': "The Persistence of Memory", "Artist": "Dali", "Year": 1931})

for artwork in art_gallery:
    print(artwork["Title"], artwork['Artist'], artwork['Year'])

for artwork in art_gallery:
    for info, value in artwork.items():
        print(f"{info}: {value}")
        
        
# dicts with3in dicts

museum_exhibits = {
    # each key represents a msueuem exhibit
    "Ancient Egypt": {
        "Artifact":['Sphynx', 'Pyramids'],
        "Famous Pharaohs": ['Tut', 'Cleopatra']
        
    },
    "Renaissance": {
        "Notable Artists": ['Leonardo', 'Michelangelo', 'Rafael'],
        "Keyworks": ['Mona Lisa', 'The Last Supper']
    }    
}

museum_exhibits['Ancient Egypt']["Recent Discoveries"] = ['New Tomb', 'Ancient Slabs']
print()
print(museum_exhibits)

museum_exhibits["Ancient Egypt"]["Famous Pharaohs"].append('Ramses')
print(museum_exhibits)

# Looping through all the items

for exhibit, details in museum_exhibits.items():
    print(f"Exhibit: {exhibit}")
    for section, items in details.items():
        print(f' - section {section}')    
        for item in items:
            print(f"   -- {item}")
            
# setting checkpoints within nested dicts
ancient_egypt = museum_exhibits['Ancient Egypt']
# ======================================================================================

# create a shopping cart application the key will be the item the value will be the price

shopping_cart = {
    
}

def add_item(cart):
    # store item as a key
    item = input("What Would You Like To Add to your cart?: " )
    quantity = int(input(f"How many of {item} would you like? "))
    price = float(input(f"How much does {item} cost? "))
    # atore total price as a value
    total_item_price = quantity * price
    
    cart[item] = total_item_price
    
def remove_item(cart):
    item = input("What Would You Like to Remove? ")
    if item not in cart:
        print("you dont have that item in your cart")
    else:
        del cart[item]

def view_cart(cart):
    for item, price in cart.items():
        print(f"{item}: {price}")
        total = calculate_total(cart)
        print(f"Your current cart total: {total}")

def calculate_total(cart):
    prices = cart.values()
    total = sum(prices)
    print(f"Your total is: {total}")


def main(cart):
    while True:
        response = input("What would you like to do? 1. Add 2. Remove 3. View 4. Get Total")
        
        if response == '1':
            add_item(cart)
        elif response == '2':
            remove_item(cart)
        elif response == '3':
            view_cart(cart)
            
        elif response == '4':
            calculate_total(cart)
        else:
            print('please enter a valid response')
            
main(shopping_cart)
