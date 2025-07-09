# Basic Loop Examples in One Code

# FOR loop - print numbers 1 to 5
print("FOR loop:")
for i in range(1, 6):
    print(i, end=' ')
print("\n")

# WHILE loop - print numbers 1 to 5
print("WHILE loop:")
count = 1
while count <= 5:
    print(count, end=' ')
    count += 1
print("\n")

# NESTED loop - multiplication table from 1 to 3
print("NESTED loop (Multiplication Table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end='\t')
    print()
