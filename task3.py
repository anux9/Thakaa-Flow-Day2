# Task 3: Invoice Calculator

# 1. Get customer information

customer = input("Enter customer name: ")
product = input("Enter product name: ")
unit_price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity: "))


# 2. Calculate the invoice

subtotal = unit_price * quantity

discount = subtotal * 0.10

after_discount = subtotal - discount

vat = after_discount * 0.15

total = after_discount + vat


# 3. Print the invoice

print(f"""
========== INVOICE ==========

Customer: {customer}
Product: {product}
Unit Price: {unit_price:.2f}
Quantity: {quantity}

Subtotal: {subtotal:.2f}
Discount (10%): {discount:.2f}
After Discount: {after_discount:.2f}
VAT (15%): {vat:.2f}

Total: {total:.2f}

=============================
""")


# 4. Comments

#ValueError: invalid literal for int() with base 10: '2.5'

#Explanation: 
#The error occurs because int() only accepts whole numbers.
#It cannot convert the decimal number 2.5 into an integer.