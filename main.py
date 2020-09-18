# Solving 3.18

a = 3
b = 4
c = 5

# (a)
if a < b:
    print("OK")

# (b)
if c < b:
    print("OK")

# (a)
if a + b == c:
    print("OK")

# (a)
if a ** 2 + b ** 2 == c ** 2:
    print("OK")



# Solving 3.22

lst = [2, 3, 69, 4, 5, 6, 7, 8, 9, 16]  # Example list, values can be changed to anything

for i in lst:  # Runs through vals of lst and determines if they are squared whether or not they are divisible by 8
    if (i ** 2) % 8 == 0:
        print({i})



# Solving 3.23

# (a) 0 1
for i in range(2):
    print(i, end=" ")
print("\n")  # Just to make it easier to read returns new line after each problem part

# (b) 0
for i in range(1):
    print(i, end=" ")
print("\n")

# (c) 3 4 5 6
for i in range(3, 7):
    print(i, end=" ")
print("\n")

# (d) 1
for i in range(1, 2):
    print(i, end=" ")
print("\n")

# (e) 0 3
for i in range(0, 4, 3):
    print(i, end=" ")
print("\n")

# (f) 5 9 13 17 21
for i in range(5, 22, 4):
    print(i, end=" ")
