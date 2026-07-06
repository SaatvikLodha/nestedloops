num = int(input("Enter a number: "))
if num == 0:
    print("0 is the binary number")
else:
    b = ""
    while num:
        b = str(num % 2) + b
        num //= 2
    print(b, "is the binary number")