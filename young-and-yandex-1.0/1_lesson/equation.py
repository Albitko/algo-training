from math import sqrt

a = int(input())
b = int(input())
c = int(input())

if a == 0:
    if b ** b == c or (b == 0 and c == 0):
        print("MANY SOLUTIONS")
    else:
        print("NO SOLUTION")
else:
    x = int(((c ** 2) - b) / a)

    answer = int(sqrt(a * x + b))

    if answer == c:
        print(x)
    else:
        print("NO SOLUTION")
