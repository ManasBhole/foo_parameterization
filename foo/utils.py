def validate_radius(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
