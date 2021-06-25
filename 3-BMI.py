weight = float(input("Enter your weight in kgs : "))
height = float(input("Enter your height in mtrs : "))

bmi = weight / (height * height)

print("your bmi : ", bmi)

if (bmi < 18.5):
    print("Underweight")
elif (bmi > 18.5 and bmi < 25):
    print("Normal")
elif (bmi > 25 and bmi < 30):
    print("Overweight")
elif(bmi >= 30):
    print("Obese")
          
