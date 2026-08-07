def gen_fibonacci(n):
    first = 0
    second = 1

    for _ in range(n):
        yield first
        next_number = first + second
        first = second
        second = next_number


for number in gen_fibonacci(7):
    print("Fibonacci Number:", number)
    
    
    
    