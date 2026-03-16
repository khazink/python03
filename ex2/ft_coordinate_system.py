import math


def parse_position(position: tuple) -> tuple:
        try:
            return tuple(int(x) for x in position)
        except ValueError as e:
            print(f"Error parsing coordinate: {e}")
            print(f"Error details - Type: ValueError, Args: {e.args}")
            raise ValueError


def calculate_distance(position1: tuple, position2: tuple) -> float:
    x1, y1, z1 = position1
    x2, y2, z2 = position2
    return math.sqrt((x2 - x1)**2 + (y2-y1)**2 +(z2-z1)**2)


def main() -> None:
    pos_create = (10, 20, 5)
    try:
         position = parse_position(pos_create)
    except ValueError:
         pass
    else:
        print(f"Position created: {position}")
    pos_origin = (0, 0, 0)
    distance = calculate_distance(pos_create, pos_origin)
    print(f"Distance between {pos_origin} and {pos_create}: {distance:.2f}")
    parse_coordinate = (3,4,0)
    print()
    print(f"Parsing coordinates: {parse_coordinate}")
    try:
         position = parse_position(parse_coordinate)
    except ValueError:
         pass
    else:
         print(f"Parsed position: {position}")
    distance = calculate_distance(parse_coordinate, pos_origin)
    print(f"Distance between {pos_origin} and {parse_coordinate}: {distance:.2f}")
    print()
    print(f"Parsing coordinates: {parse_coordinate}")
    parse_coordinate = ("abc", "def", "ghi")
    try:
         position = parse_position(parse_coordinate)
    except ValueError:
         pass
    else:
         print(f"Parsed position: {position}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    main()