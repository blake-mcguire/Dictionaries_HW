garage = {}

space_remaining = 100
attic_space = 30
workshop_space = 40
# turn value into a list
# get the sum of the value[0] for items whos value index[1] was equal to 'x' location

def add_item(garage):
    item = input("What item would you like to add to the garage?")
    space = int(input("How many cubic feet does the item take up?"))
    
    item_space = garage.values()
    total_space = sum(item_space)
    if total_space + space < space_remaining:
        garage.update({item:  space})
    else:
        print("That is too large for your garage! you need more space!")
    
def remove_item(garage):
    item = input("what item would you like to remove? ")
    if item in garage:  
        del garage[item]
    else:
        print("That item is not in your garage!")


def get_space_remaining(garage):
    for item, values in garage.items():
        print(f"-- {item}: Size {values} Cubic Feet")
    space = garage.values()
    total_space = sum(space)
    print(f'Your total space taken up is: {total_space} feet')
    print(f"You have {space_remaining - total_space} feet remaining")


def main(garage):
    while True:
        response = input("""
                         1. to add to your garage, 
                         2. to remove items from your garage
                         3. to view Your garage inventory and remaining space
                         4. To leave your garage
                         """)
        
        if response == '1':
            add_item(garage)
        elif response == '2':
            remove_item(garage)
        elif response == '3':
            get_space_remaining(garage)
        elif response == '4':
            break
        else:
            print('Please enter a valid input')
            
main(garage)



# ====================================================================================================

# garage = {}

# space_remaining = 100
# attic_space = 30
# workshop_space = 40
# # turn value into a list
# # get the sum of the value[0] for items whos value index[1] was equal to 'x' location

# def add_item(garage):
#     item = input("What item would you like to add to the garage?")
#     space = int(input("How many cubic feet does the item take up?"))
#     location =input('Where would you like it to go? Attic, Garage or Workshop?')
#     if location == 'Garage':
#         garage_items = {}
#         for item, values in garage.items():
#             if values[1] == 'Garage'
                 
#     item_space = garage.values()
#     total_space = sum(item_space)
#     if total_space + space < space_remaining:
#         garage.update({item:  [space, location]})
#     else:
#         print("That is too large for your garage! you need more space!")
    
# def remove_item(garage):
#     item = input("what item would you like to remove? ")
#     if item in garage:  
#         del garage[item]
#     else:
#         print("That item is not in your garage!")


# def get_space_remaining(garage):
#     for item, values in garage.items():
#         print(f"-- {item}: Size {values} Cubic Feet")
#     space = garage.values()
#     total_space = sum(space)
#     print(f'Your total space taken up is: {total_space} feet')
#     print(f"You have {space_remaining - total_space} feet remaining")


# def main(garage):
#     while True:
#         response = input("""
#                          1. to add to your garage, 
#                          2. to remove items from your garage
#                          3. to view Your garage inventory and remaining space
#                          4. To leave your garage
#                          """)
        
#         if response == '1':
#             add_item(garage)
#         elif response == '2':
#             remove_item(garage)
#         elif response == '3':
#             get_space_remaining(garage)
#         elif response == '4':
#             break
#         else:
#             print('Please enter a valid input')
            
# main(garage)