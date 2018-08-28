fname = input("Enter file name: ")
fh = open(fname)

email_count = {}
for line in fh:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    words = line.split()
    email = words[1]
    email_count[email] = email_count.get(email, 0) + 1

max_count = None
max_email = None
for email, count in email_count.items():
    if max_count is None or count > max_count:
        max_count = count
        max_email = email

print(max_email, max_count)
