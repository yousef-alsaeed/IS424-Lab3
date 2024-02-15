maxList = []
count = 0

while count < 10:
    try:
        number = int(input("Enter a number: "))
        maxList.append(number)
        count += 1

    except:
        print("Has to be a number!")

maxList.sort()
print("Biggest number in the list is: ", maxList[-1])