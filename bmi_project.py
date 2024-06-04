

weight=float(input("Enter your weight(in kg):-\n"))
height=float(input("enter your height(in m):- \n"))

BMI=round(weight/(height*height),2)

if BMI<=18.5:
    print(f"Your BMI is {BMI} and you are underweight")
elif BMI>18.5 and BMI<=24.9:
    print(f"Your BMI is {BMI} and you are normal")
elif BMI>=25.0 and BMI<=29.9:
    print(f"Your BMI is {BMI} and you are overweight")
elif BMI>=30.0 and BMI<=34.9:
    print(f"Your BMI is {BMI} and you are obese")
elif BMI>=35.0:
    print(f"Your BMI is {BMI} and you are obese")






 




