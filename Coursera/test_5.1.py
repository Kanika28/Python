count=0
total=0.0

while True:
    sval = input("Enter the number:")
    if sval == 'done':
        break;
    try:
        fval = float(sval)
    except:
        continue
    count = count + 1
    total = total + fval

print("Count", count)
print("Sum", total)
print("Average", total/count)
