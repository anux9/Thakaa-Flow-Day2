# Task 1 - Code Prediction

## Part 1: Predict the Output

### 1.
Code: print(type(a), type(b))
Prediction: str, int
Actual output: <class 'str'> <class 'int'>

### 2.
Code: print(a * b)
Prediction: 777
Actual output: 777

### 3.
Code: print(int(a) * b)
Prediction: 21
Actual output: 21

### 4.
Code: print(a + str(b))
Prediction: 73
Actual output: 73

### 5.
Code: print(int(a) / b)
Prediction: 2.3333333333333335
Actual output: 2.3333333333333335

### 6.
Code: print(int(a) // b, int(a) % b)
Prediction: 2, 1
Actual output: 2 1



## Part 2: What is a Variable?

A variable is like a box that stores information.
We give each box a name so we can find its value later.
In Python, we use variables to store data such as names and numbers.



## Part 3: Finding and Fixing Errors

### Error:
Traceback (most recent call last):
  File "c:\Users\An\Desktop\Day2\task1.py", line 19, in <module>
    print("Hello " + name + ", in 5 years you will be " + age + 5)
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
PS C:\Users\An\Desktop> 

### Reason:
The error happens because Python cannot add a string and an integer directly.

### Fix using Concatenation (+):
print("Hello " + name + ", in 5 years you will be " + str(int(age) + 5))

### Fix using f-string:
print(f"Hello {name}, in 5 years you will be {int(age) + 5}")



## Part 4: Understanding input()

### Input:
twenty

### Error:
ValueError: invalid literal for int() with base 10: 'twenty'

### Explanation:
The input() function returns a string.
When we enter "twenty", Python cannot convert it
into an integer using int() because it is not a numeric value.