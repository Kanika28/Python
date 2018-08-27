fname = input("Enter file name:")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    fval = float(line[line.find(':') + 1 :])
    total = total + fval
print("Average spam confidence:", total/count)
