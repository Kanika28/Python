f=lambda s:('Not a palindrome', "Palindrome")[s[::].lower() == s[::-1].lower()]

print (f(raw_input("Enter you string:")))

x = ('Not a palindrome', "Palindrome", "abc")
print(x[0])
print(x[1])
print(x[True])
print(x[False])
