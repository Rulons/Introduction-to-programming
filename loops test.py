n = int(input("Enter a non-negative integer:"))
factorial =1
for i in range(1, n+1):
    factorial *=i
    print(f"{i}: {factorial}")
