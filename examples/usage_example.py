from foo.volume import calculate_volume
from foo.advanced_volume import calculate_advanced_volume

radius = 5
volume = calculate_volume(radius)
advanced_volume = calculate_advanced_volume(radius, precision=5)
print(f"Volume: {volume} cubic units")
print(f"Advanced Volume: {advanced_volume} cubic units")
