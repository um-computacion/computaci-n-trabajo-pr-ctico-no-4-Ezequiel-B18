def factorial_iterative(num):
    """
    Calcula el factorial de un número utilizando un enfoque iterativo.

    Args:
        num (int): El número para calcular su factorial. Debe ser no negativo.

    Returns:
        int: El factorial del número de entrada.

    Raises:
        ValueError: Si el número es negativo.

    Examples:
        >>> factorial_iterative(5)
        120
        >>> factorial_iterative(0)
        1
    """
    if num < 0:
        raise ValueError('Los factoriales no estan definidos para numeros negativos.')

    factorial_res = 1
    
    for i in range(1, num + 1):
        factorial_res *= i
    
    return factorial_res

def factorial_recursive(num):
    """
    Calcula el factorial de un número utilizando un enfoque recursivo.

    Args:
        num (int): El número para calcular su factorial. Debe ser no negativo.

    Returns:
        int: El factorial del número de entrada.

    Raises:
        ValueError: Si el número es negativo.

    Examples:
        >>> factorial_recursive(5)
        120
        >>> factorial_recursive(0)
        1
    """
    if num < 0:
        raise ValueError('Los factoriales no estan definidos para numeros negativos.')

    if num == 0 or num == 1:
        return 1
    
    return num * factorial_recursive(num - 1)

def main():
    """
    Función principal que interactúa con el usuario para calcular factoriales.
    Permite al usuario ingresar números y muestra sus factoriales calculados
    tanto de forma iterativa como recursiva.
    """
    while True:
        try:
            num = int(input("Ingrese un numero para aplicarle su factorial: "))
            print(f"El factorial de su numero es: {factorial_iterative(num)}\nY lo mismo pero calculado de otra forma: {factorial_recursive(num)}")
        except:
            print("Error: Por favor ingrese un numero valido.")

        continuar = input("¿Desea agregar otro numero? (y/n) ")
        if continuar.lower() != "y":
            break

if __name__ == '__main__':
    main()