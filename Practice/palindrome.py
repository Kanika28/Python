input = list(raw_input("Enter you string:"))
print input
print input[::-1]
if input == input[::-1]:
    print("Yay, it's a palindrome")
else:
    print("Try again")