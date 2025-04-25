def flatten(items):
    """
    Aplana una estructura de datos anidada (listas, tuplas, diccionarios) en una lista plana.

    Args:
        items: Una estructura de datos que puede contener listas anidadas, tuplas o diccionarios.

    Returns:
        list: Una lista plana que contiene todos los elementos no iterables de la estructura original.
              Para diccionarios, incluye tanto las claves como los valores.

    Examples:
        >>> flatten([1, 2, 3, 4])
        [1, 2, 3, 4]
        >>> flatten([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten([1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]])
        [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
    """
    result = []
    if not items:
        return []
    
    for item in items:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))

        elif isinstance(item, dict):
            for key in item:
                result.append(key)
                result.append(item[key])
        else:
            result.append(item)

    return result

def main():
    """
    Función principal que demuestra el uso de la función flatten con varios ejemplos.
    Imprime las estructuras originales y sus versiones aplanadas.
    """
    ejemplos = [
        [1, 2, 3, 4],
        [1, [2, 3], [4, [5, 6]]],
        [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
    ]
    
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"Ejemplo {i}:")
        print(f"Original: {ejemplo}")
        print(f"Aplanado: {flatten(ejemplo)}")
        print("-" * 40)

if __name__ == '__main__':
    main()