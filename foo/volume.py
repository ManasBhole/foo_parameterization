def calculate_volume(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    volume = (4/3) * 3.141592653589793 * (radius ** 3)
    return volume
