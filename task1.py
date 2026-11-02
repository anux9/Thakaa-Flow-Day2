# Part 1: Code Prediction

a = "7"
b = 3

print(type(a), type(b))
print(a * b)
print(int(a) * b)
print(a + str(b))
print(int(a) / b)
print(int(a) // b, int(a) % b)


# Part 2: Error Testing

name = input("Your name: ")
age = input("Your age: ")

#print("Hello " + name + ", in 5 years you will be " + age + 5)


# Part 3: Fixing the Error

# Method 1: Using +

print("Hello " + name + ", in 5 years you will be " + str(int(age) + 5))



# Part 4: Testing input()

age = int(input("Your age: "))
print(age)