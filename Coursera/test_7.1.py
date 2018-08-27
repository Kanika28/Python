fname = input("Enter the file name:")
fhandle = open(fname)
content = fhandle.read()
print(content.upper().strip())
