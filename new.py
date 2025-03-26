student_list = []
i = 0
while i < 2:
    name = input("Enter your name:")
    field = input("Enter the field:")
    gender = input("Gender (M or F):")
    address = input("Enter the address:")
    gender.lower()
    obj = {"name": name, "field": field, "gender": gender, "address": address}
    student_list.append(obj)
    i += 1

# print(student_list[0])

for item in student_list:
    if item["address"] == "Ktm":
        print("Name: ", item["name"])

male_list = []
female_list = []

for student in student_list:
    if student["gender"] == "m":
        male_list.append(student["name"])
    else:
        female_list.append(student["name"])

print("Male: ", male_list)
print("Female: ", female_list)


