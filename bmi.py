height=float(input("Please enter your height (in Centimeters):"))
weight=float(input("Please enter your weight (in Kilograms):"))
bmi=weight/(height/100)**2
print("Your BMI is", bmi)
if bmi<=18.4:
    print("You are underweight.")
elif bmi<=24.9:
    print("You are healthy.")
elif bmi<=29.9:
    print("You are overweight.")
elif bmi<=34.9:
    print("You are obese.")
else:
    print("You are extremely obese.")