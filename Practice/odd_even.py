number=int(raw_input("Enter a number:"))
if number % 2 ==0:
    if number % 4 == 0:
        print ("Number is even and divisble by 4")
    else:
        print("Even")
else:
    print("Odd")