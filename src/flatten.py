def flatten(items):
        
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