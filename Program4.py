count = 1

try:
    num = int(input("Enter a number: "))
    while count <= 10:
        print(num, "*", count, "=", (num * count))
        count += 1

except:
    print("Wrong input")