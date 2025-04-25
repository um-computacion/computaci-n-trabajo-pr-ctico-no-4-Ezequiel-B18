def fibonacci_iterative(num):
    """
    Calcula el n-ésimo número de la secuencia de Fibonacci utilizando un enfoque iterativo.

    Args:
        num (int): La posición en la secuencia de Fibonacci (empezando desde 0).
                  Debe ser no negativo.

    Returns:
        int: El n-ésimo número de Fibonacci.

    Raises:
        ValueError: Si el número es negativo.

    Examples:
        >>> fibonacci_iterative(0)
        0
        >>> fibonacci_iterative(1)
        1
        >>> fibonacci_iterative(6)
        8
    """
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
    """
    Calcula el n-ésimo número de la secuencia de Fibonacci utilizando un enfoque recursivo.

    Args:
        num (int): La posición en la secuencia de Fibonacci (empezando desde 0).
                  Debe ser no negativo.

    Returns:
        int: El n-ésimo número de Fibonacci.

    Raises:
        ValueError: Si el número es negativo.

    Examples:
        >>> fibonacci_recursive(0)
        0
        >>> fibonacci_recursive(1)
        1
        >>> fibonacci_recursive(6)
        8
    """
    if num < 0:
        raise ValueError('Fibonacci no esta definido para numeros negativos.')
    
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)

def main():
    """
    Función principal que interactúa con el usuario para calcular números de Fibonacci.
    Permite al usuario ingresar posiciones y muestra el número de Fibonacci correspondiente
    calculado tanto de forma iterativa como recursiva.
    """
    while True:
        try:
            num = int(input("Ingrese un numero para aplicarle fibonacci: "))
            print(f"El fibonacci de su numero es: {fibonacci_iterative(num)}\nY lo mismo pero calculado de otra forma: {fibonacci_recursive(num)}")
        except:
            print("Error: Por favor ingrese un numero valido.")
            continue

        continuar = input("¿Desea agregar otro numero? (y/n) ")
        if continuar.lower() != "y":
            break

if __name__ == '__main__':
    main()