import sys


def main() -> None:
    arg_len = len(sys.argv)
    if arg_len < 2:
        print("No arguments provided!")
        print("Program name:", sys.argv[0])
    else:
        print("Program name:", sys.argv[0])
        print("Arguments received:", arg_len - 1)
        for i, arg in enumerate(sys.argv[1:], start = 1):
            print(f"Argument {i}: {arg}" )
    print("Total arguments:", arg_len, "\n")


if __name__ == "__main__":
    print("=== Command Quest ===")
    main()
