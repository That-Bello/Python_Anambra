# BMI Calculator: Develop a program that calculates the
# Body Mass Index (BMI) based on user input for weight and height.

name = input("Your full named: ")

weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))
BMI = round((weight * 703) / (height * height), 1)
print("Your BMI is: ", BMI)

if BMI <= 0:
    if BMI < 18.5:
        print(name + ", you are underweight!")
    elif BMI <= 24.9:
        print(name + ", you have healthy weight!")
    elif BMI < 29.9:
        print(name + ", you are overweight!")
else:
    print(name + ", you are obese!")
