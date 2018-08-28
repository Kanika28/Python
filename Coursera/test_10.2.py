fname = input("Enter file name: ")
fh = open(fname)

hours_count = {}
for line in fh:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    words = line.split()
    hr = words[5].split(":")[0]
    hours_count[hr] = hours_count.get(hr, 0) + 1

sorted_list = sorted(hours_count.items())
for k,v in sorted_list:
    print(k, v)
