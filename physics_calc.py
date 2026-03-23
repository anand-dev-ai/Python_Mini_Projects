import math

def calculate_range(velocity, angle_degree):
    g = 9.8  # Gravity in m/s^2
    angle_rad = math.radians(angle_degree)
    # Formula: (v^2 * sin(2*theta)) / g
    range_m = (velocity**2 * math.sin(2 * angle_rad)) / g
    return round(range_m, 2)

# Test the function
v = float(input("Enter velocity (m/s): "))
a = float(input("Enter angle (degrees): "))

result = calculate_range(v, a)
print(f"The object will travel {result} meters.")
