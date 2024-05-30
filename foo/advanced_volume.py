from foo.volume import calculate_volume


def calculate_advanced_volume(radius, pressure, temperature):
    """Calculate adjusted volume based on environmental factors."""
    base_volume = calculate_volume(radius)
    return base_volume * pressure * (temperature / 300) 
