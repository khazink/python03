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
        



def main() -> None:
    pos_create = (10, 20, 5)
    position = parse_position(pos_create)
    if position is None:
        return
    print("do something")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    main()