def add(a, b):
    return a + b

x, y = map(int, input("Enter two numbers: ").split())
print("Sum =", add(x, y))