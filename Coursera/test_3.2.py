score = input("Enter Score: ")
score_x = 0.0
try:
    score_x = float(score)
except:
    score_x = -1
if score_x < 0 or score_x > 1.0:
    print("Invalid score entered")
elif score_x >=  0.9:
    print("A")
elif score_x >= 0.8:
    print("B")
elif score_x >=0.7:
    print("C")
elif score_x >=0.6:
    print("D")
elif score_x < 0.6:
    print("F")

