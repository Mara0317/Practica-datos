def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        next_value = sequence[i-1] + sequence[i-2]
        sequence.append(next_value)
    
    return sequence

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    fib_sequence = fibonacci(n)
    print(f"Fibonacci sequence up to {n} numbers: {fib_sequence}")
    