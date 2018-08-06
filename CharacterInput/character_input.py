import datetime

name = raw_input("Give me your name: ")
print("Your name is " + name)
age = raw_input("Give me your age: ")
print("Your age is " + age)
current_year = datetime.datetime.now().year
print("Current year is: " + str(current_year))
future_year = current_year + (100-int(age))
print("You will turn 100 in year: " + str(future_year))