text = "X-DSPAM-Confidence:    0.8475"
tab_index = text.find('    ')
sval = text[tab_index+4:]
print(float(sval))
