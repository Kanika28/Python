def computepay(hrs, rate):
    if hrs > 40:
        pay = 40 * rate + (hrs - 40) * 1.5 * rate
    else:
        pay = hrs * rate
    return pay

hrs=float(input("Enter the hours:"))
rate=float(input("Enter the rate:"))
pay = computepay(hrs, rate)
print(pay)    

