
user_weight = int(input("What is your weight?"))
user_height = int(input("What is your height?"))

def BMI_calculation(w, h):
    BMI = round(w / (h * h), 2)
    return BMI


print("your BMI is " + str(BMI_calculation(user_weight, user_height)))
