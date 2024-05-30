import argparse
from foo import calculate_volume, calculate_advanced_volume

def main():
    parser = argparse.ArgumentParser(description="Calculate volume of sphere using the Foo et al. model.")
    parser.add_argument("radius", type=float, help="Radius of the sphere")
    parser.add_argument("--pressure", type=float, default=1.0, help="Environmental pressure")
    parser.add_argument("--temperature", type=float, default=300, help="Environmental temperature")
    args = parser.parse_args()

    if args.pressure and args.temperature:
        volume = calculate_advanced_volume(args.radius, args.pressure, args.temperature)
    else:
        volume = calculate_volume(args.radius)

    print(f"Calculated Volume: {volume}")

if __name__ == "__main__":
    main()
