name = "James"
height = 2
weight = 110

bmi = weight / (height ** 2)
print("bmi: ")
print(bmi)
if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")
print("A BMI of 25 is normal")