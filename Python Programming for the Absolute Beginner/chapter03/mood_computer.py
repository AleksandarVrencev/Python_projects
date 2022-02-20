# Mood Computer
# Demonstrates the elif clause
# Aleksandar Vrencev
# 08.01.2017

import random

print("I sense your energy.  Your true emotions are coming across my screen.")
print("You are...")

mood = random.randint(1, 3)

if mood == 1:
    # happy
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | .     . |
       |  `...`  |
       -----------
       
       happy       """)
elif mood == 2:
    # neutral  
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | ------  |
       |         |
       -----------
        neutral    """)
elif mood == 3:
    # sad
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       |  .'.    |
       | '   '   |
       -----------
        sad       """)
else:
    print("Illegal mood value!  (You must be in a really bad mood).")

print("...today.")

input("\n\nPress the enter key to exit.")






