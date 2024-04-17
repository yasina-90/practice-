# 1- adad ro entekhab kone computer ba random beine 0 ta 10
# 2-bad biad az akrbar begire entekhabesho
# 3- age entekhab hamon bood bege k barande shodi
# 4- age bozorgte ya kochektar k bege baz adad ro begire
# 5- bar ejaze bede in kar ro kone
# end


from gettext import npgettext
import random

import numpy

comp_choice = random.randint(0, 11)

user_choice = int(input("Enter your choice: "))
again = True
times = 5

for times in range(times):
    if user_choice == comp_choice:
        print("You win!")
        break
    elif user_choice < comp_choice:
        print("Your number is lower than computer's guess")
        print("try again!")
        continue
    elif user_choice > comp_choice:
        print("Your number is higher than computer's guess")
        print("try again!")
        continue
    else:
            print("Invalid input")
            print("try again!")
            continue