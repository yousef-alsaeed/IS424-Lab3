Celsius = input("Enter the temperature in Celsius: ")

try:
    Fahrenheit = 9 / 5 * float(Celsius) + 32
    print("Temperature in Fahrenheit is ", Fahrenheit)

except:
    print("Wrong input, try again")
