def check(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter n: "))

for i in range(1, n+1):
    print(i, "->", check(i))