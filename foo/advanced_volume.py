import math

def calculate_advanced_volume(radius, precision=10):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    volume = (4/3) * math.pi * (radius ** 3)
    return round(volume, precision)
