def calculate_bmi(weight, height):
    return weight / (height ** 2)

while True:
    print(" BMI Calculator ")

    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive values.")
        continue

    bmi = calculate_bmi(weight, height)

    print(f"\nBMI: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal Weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")

    choice = input("\nDo you want to calculate again? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you for using BMI Calculator!")
        break