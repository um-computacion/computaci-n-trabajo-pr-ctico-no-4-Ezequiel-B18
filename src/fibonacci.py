def fibonacci_iterative(num):
    if num < 0:
        raise ValueError('Fibonacci no esta definido para numeros negativos.')

    if num == 0:
        return 0
    if num == 1:
        return 1
    
    fib_anterior = 0
    fib_ahora = 1

    for i in range(2, num + 1):
        fib_siguiente = fib_anterior + fib_ahora

        fib_anterior = fib_ahora
        fib_ahora = fib_siguiente
    
    return fib_ahora

def fibonacci_recursive(num):
    pass

def main():
    pass

if __name__ == '__main__':
    main()