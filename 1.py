def lower_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)

def upper_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

print("Choose the pattern to print:")
print("1. Lower Triangular")
print("2. Upper Triangular")
print("3. Pyramid")

choice = int(input("Enter your choice (1/2/3): "))
rows = int(input("Enter number of rows: "))

if choice == 1:
    print("\nLower Triangular Pattern:")
    lower_triangle(rows)
elif choice == 2:
    print("\nUpper Triangular Pattern:")
    upper_triangle(rows)
elif choice == 3:
    print("\nPyramid Pattern:")
    pyramid(rows)
else:
    print("Invalid choice!")
