# Solve the problem.
# 05. Program to calculate BMI (Body Mass Index) of a person.
#     Body Mass Index is a simple calculation using a person's height and weight.
#     The formula is BMI = Kg/m² (use Alt+0178 for power subscript) where kg is a person's weight in 
#     kilograms and m² is their height  in metres squared.

a = weight_in_kg = float(input(" Enter the weight in kg:"))
b = height_in_meter = float(input("Enter height in meters:"))
bmi = a/b*b
print("BMI is:", bmi, "kg/m²")