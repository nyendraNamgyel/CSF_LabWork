a, b, c = map(int, input("Enter three numbers: ").split())

if a > b:
    if a > c:
        print(a, "is the largest number")
    else:
        print(c, "is the largest number")
else:
    if b > c:
        print(b, "is the largest number")
    else:
        print(c, "is the largest number")