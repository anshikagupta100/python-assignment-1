def fibonacci():
    n = int(input("Enter the number of Fibonacci terms: "))
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    print(f"The first {n} numbers in the Fibonacci sequence are: {fib_sequence}")

fibonacci()