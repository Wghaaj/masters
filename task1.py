def caching_fibonacci():
    """
    Task 1: Fibonacci Caching

    Functions:
    caching_fibonacci() creates a cache dictionary and returns
    an inner function fibonacci(n). This function calculates
    Fibonacci numbers using recursion and stores the results
    in the cache to avoid repeating the same calculations.

    Result:
    The program calculates Fibonacci numbers and reuses
    previously saved values, making repeated calculations
    faster and more efficient.
    """

    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))
