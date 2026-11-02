# Task 5: Mars Mission Report

# 1. Get information

distance = float(input("Enter distance to Mars (million km): "))
earth_age = float(input("Enter your age in Earth years: "))
earth_weight = float(input("Enter your weight in kg: "))


# 2. Calculate message travel time

distance_km = distance * 1_000_000

speed_of_light = 299792

one_way_seconds = int(distance_km / speed_of_light)

one_way_minutes = one_way_seconds // 60
remaining_seconds = one_way_seconds % 60


# 3. Calculate round trip time

round_trip_seconds = one_way_seconds * 2

round_trip_hours = round_trip_seconds // 3600
round_trip_minutes = (round_trip_seconds % 3600) // 60
round_trip_remaining_seconds = round_trip_seconds % 60


# 4. Calculate age on Mars

earth_days = earth_age * 365.25

mars_age = earth_days / 687


# 5. Calculate weight on Mars

mars_weight = earth_weight * 0.38


# 6. Calculate Earth week in Mars sols

mars_sol_seconds = (24 * 3600) + (39 * 60) + 35

earth_week_seconds = 7 * 24 * 3600

mars_sols = earth_week_seconds / mars_sol_seconds


# 7. Print Mars Mission Report

print(f"""
========== MARS MISSION REPORT ==========

Distance to Mars: {distance:.2f} million km

One-way message travel time:
{one_way_minutes} minutes and {remaining_seconds} seconds

Round-trip message travel time:
{round_trip_hours} hours, {round_trip_minutes} minutes,
and {round_trip_remaining_seconds} seconds

Your age on Mars: {mars_age:.2f} Mars years

Your weight on Mars: {mars_weight:.2f} kg

One Earth week equals {mars_sols:.2f} Mars sols

=========================================
""")


# 8. Comment

# A direct video call with family on Earth is not possible
# because messages take several minutes to travel between Earth and Mars.