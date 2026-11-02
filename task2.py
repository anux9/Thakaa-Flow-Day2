# Task 2: My Thakaa Flow ID Card

# 1. Create Variables

name = "Alanoud Abdullah"
city = "Riyadh"
major = "AI"
age = 25
coded_before = True
study_hours = 2.5


# 2. Print the ID Card using Concatenation (+)

print("=== " + name + " ===")
print("City: " + city)
print("Major: " + major)
print("Age: " + str(age))
print("Coded before: " + str(coded_before))
print("Study hours: " + str(study_hours))


# 3. Print the ID Card using f-string

print(f"=== {name} ===")
print(f"City: {city}")
print(f"Major: {major}")
print(f"Age: {age}")
print(f"Coded before: {coded_before}")
print(f"Study hours: {study_hours}")


# 4. Print the entire card using one print statement

print(f"""
=== {name} ===
City: {city}
Major: {major}
Age: {age}
Coded before: {coded_before}
Study hours: {study_hours}
""")


# 5. Print the type of each variable

print(type(name))
print(type(city))
print(type(major))
print(type(age))
print(type(coded_before))
print(type(study_hours))


# 6. Comment

# I prefer f-string because it is easier to read and write.