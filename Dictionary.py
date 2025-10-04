my_dict = {
    "name": "FAHAD",
    "age": 24,
    "marks": [100,98,99],
    "subjects": ("PYTHON", "AI/ML", "JS",)
}
print(my_dict)
print(type(my_dict))
print(my_dict["name"])

my_dict["age"] = 25
print(my_dict["age"])

null_dict = {}
print(null_dict)

#Nested Dictionaries
student = {
    "name": "FAHAD",
    "age": 24,
    "marks": {
        "PYTHON": 100,
        "C++": 98,
        "AI/ML": 99,
    }
}

print(student)
print(student["marks"])
print(student["marks"]["PYTHON"])

print(student.keys())
print(student.values())
print(student.items())
print(len(student))
print(student.get("name1"))
student.update({"Number": 9055006369})
print(student)

address = {
    "city": "Srinagar",
    "state": "J&K",
    "address": "Lal bazar",
    "pincode": "190006"
}
student.update(address)
print(student)