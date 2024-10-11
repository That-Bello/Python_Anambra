# Temperature Converter: Create # a program that converts temperatures
# between Celsius and Fahrenheit.

# Fahrenheit (F) = (C * 9/5) + 32
# Celsius (C) = (F - 32) * 5/9

temperature = input("Celsius or Fahrenheit (C/F): ")
temp_value = float(input("Enter the temperature value: "))

if temperature == "C":
    temp_value = round((9 * temp_value) / 5 + 32, 1)
    print(f"The Temperature in Fahrenheit is: {temp_value}F")
elif temperature == "F":
    temp_value - round((temp_value - 32) * 5 / 9, 1)
    print(f"The Temperature in Celsius is: {temp_value}C")
else:
    print(f"{temperature} is a invalid input, check")