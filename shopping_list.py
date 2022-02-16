# make a list to hold onto our items
shopping_list = []

# print out instructions on how to use the app
print("What should we pick up at the store? ")
print("Enter 'DONE' to stop adding items.")

new_item = None

# be able to quit the app
while new_item != 'DONE':
    # ask for new items
    new_item = input("> ")
    # add new items to our list
    shopping_list.append(new_item)

# print out the list
print(shopping_list)
input("Press Enter to quit...")
