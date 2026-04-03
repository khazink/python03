from typing import Generator, Any, Dict
from data_generator import PixelDataGenerator
import time

def event_stream(count: int) -> [Dict[str, Any], None, None]:
    gen = PixelDataGenerator()
    events = gen.generate_exercise_data(5, count=count)
    for event in events:
        yield event


def fibonacci_gen() -> Generator[int, None, None]:
    a, b  = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_gen() -> Generator[int, None, None]:
    n = 2
    while True:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else:
            yield n
        n += 1
        

def main() -> None:
    total_count = 1000
    print(f"Processing {total_count} game events...")
    total_processed = 0
    high_level_players = 0
    treasure_events = 0
    levelup_events = 0
    start_time = time.time()
    for event in event_stream(total_count):
        total_processed += 1

    print()
    print("=== Generator Demonstration ===")
    fib = fibonacci_gen()
    fib_list = [str(next(fib)) for _ in range(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")


if __name__ == "__main__":
    print("=== Data Stream Processor ===")
    main()