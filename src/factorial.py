def factorial_iterative(num):
    if num < 0:
        raise ValueError('Los factoriales no estan definidos para numeros negativos')

    factorial_res = 1
    
    for i in range(1, num + 1):
        factorial_res *= i
    
    return factorial_res

def factorial_recursive(num):
    pass

def main():
    pass

if __name__ == '__main__':
    main()