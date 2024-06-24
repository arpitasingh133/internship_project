temp = float(input("Enter the temp: "))
print("Enter in terms of C or F")
unit = input("is this in Celsius or Fahrenheit: ")


if unit == "C" :
    temp = (9*temp)/5+32
    print(f"The temp in Fahrenheit is: {temp} F")
elif unit == "F" :
    temp = (temp - 32) * 5/9
    print(f"The temp in Celcius is: {temp} C ")
else :
    print("Invalid unit")
