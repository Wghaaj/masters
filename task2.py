import re
from typing import Callable


def generator_numbers(text: str):
    """
    Task 2: Number Generator and Total Income

    Functions:
    generator_numbers() searches through the given text
    and uses yield to return each number as a float.
    sum_profit() takes the text and generator function,
    then adds all the extracted numbers together.

    Result:
    The program finds all valid numbers in the text
    and calculates their total sum. It uses a generator
    to process the numbers without creating an extra list.
    """

    pattern = r"(?<!\S)[+-]?\d+(?:\.\d+)?(?!\S)"
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income:.2f}")
