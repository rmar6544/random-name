# Split string method
# Ask for names seperated by comma and space
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Random name from a list without useing choice()
#this code will randomly print who will pay a bill at a restaurant.
import random
a = int(len(names))

b = random.randint(0,a-1)
print(f"{names[b]} is going to buy the meal today!")


