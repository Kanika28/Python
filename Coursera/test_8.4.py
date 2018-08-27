fname = input("Enter file name:")
fh = open(fname)

unique_words = list()
for line in fh:
    words = line.split()
    #print(words)
    for word in words:
        #print(word)
        if not word in unique_words:
            #print("here")
            unique_words.append(word)
            #print(unique_words)
#print(unique_words)
unique_words.sort()
print(unique_words)
