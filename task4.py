# Task 4: Automated Booking Confirmation

# 1. Get booking information

customer_name = input("Enter customer name: ")
service = input("Enter service: ")
date = input("Enter booking date: ")
time = input("Enter booking time: ")
service_price = float(input("Enter service price: "))
booking_no = int(input("Enter booking number: "))
session_minutes = int(input("Enter session length in minutes: "))


# 2. Calculate deposit and remaining amount

#قبل التعديل: deposit = service_price * 0.30

deposit = service_price * 0.25

remaining = service_price - deposit


# 3. Convert minutes into hours and minutes

hours = session_minutes // 60
minutes = session_minutes % 60


# 4. Create booking code

booking_code = f"TF-2026-{booking_no:04d}"


# 5. Create confirmation message

message = f"""
========== BOOKING CONFIRMATION ==========

Hello {customer_name}!

Service: {service}
Date: {date}
Time: {time}

Booking Code: {booking_code}

Service Price: {service_price:.2f}
Deposit (30%): {deposit:.2f}
Remaining Amount: {remaining:.2f}

Session Duration: {hours} hours and {minutes} minutes

==========================================
"""

print(message)


# 6. Comment

# The deposit percentage can be changed in the deposit calculation line.