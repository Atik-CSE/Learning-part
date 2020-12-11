marks = float(input("Enter merks : "))
if marks >= 80 and marks <= 100:
    print("A+")
elif marks >= 70 and marks <= 100:
    print("A")
elif marks >= 60 and marks <= 100:
    print("A-")
elif marks >= 50 and marks <= 100:
    print("B")
elif marks >= 40 and marks <= 100:
    print("C")
elif marks >= 33 and marks <= 100:
    print("D")
else:
    print("F")