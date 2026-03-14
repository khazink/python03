import math


def parse_position(position: tuple) -> tuple:
    for i in position:
        try:
            int(i)
        except ValueError:
            print(f"Error parsing coordinate: invalid literal for int() with "
                  f"base 10: {i}")
            print("Error details - Type: ValueError, Args(\"invalid literal "
                  f"for int() with base 10: '{i}'\",)")
            return
    return(position)


def calculate_distance(position1: tuple, position2: tuple) -> float:
    x1, y1, z1 = position1
    x2, y2, z2 = position2
    return math.sqrt((x2 - x1)**2 + (y2-y1)**2 +(z2-z1)**2)


def main() -> None:
    pos_create = (10, 20, 5)
    position = parse_position(pos_create)
    if position is None:
        return
    print(f"Position created: {pos_create}")
    pos_origin = (0, 0, 0)
    distance = calculate_distance(pos_create, pos_origin)
    print(f"Distance between {pos_origin} and {pos_create}: {distance:.2f}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    main()