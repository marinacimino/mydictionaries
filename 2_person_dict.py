person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]  # key is children but value is a list
person["pets"] = {
    "dog": "Fido",
    "cat": "Sox",
}  # key is pets but value is another dictionary

print(person)

# print(person.get("children")[1])
print(person["children"][1])

for i in person["children"]:
    print(i)

for i, j in person["pets"].items():
    print(f"Type of pet:{i} name of pet: {j}")
