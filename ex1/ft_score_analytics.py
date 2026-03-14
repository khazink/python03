import sys


def score_crusher(score: list) -> None:
    print(f"Scores processed: {", ".join(str(i) for i in score)}")
    print(f"Total players: {len(score)}")
    print(f"Total score: {sum(score)}")
    print(f"Average score: {sum(score)/len(score)}")
    print(f"High score: {max(score)}")
    print(f"Low score: {min(score)}")
    print(f"Score range: {max(score) - min(score)}")


def main() -> None:
    arg_len = len(sys.argv)
    if arg_len < 2:
        print("No score provided. Usage: python3 ft_score_analytics.py "
              "<score1><score2> ...")
        return
    score = []
    for index, arg in enumerate(sys.argv[1:]):
        try:
            arg = int(arg)
        except ValueError:
            print("value error")
            return
        else:
            score.append(arg)
    score_crusher(score)


if __name__ == "__main__":
    print("=== Player Score Analytics")
    main()
