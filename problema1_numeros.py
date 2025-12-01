def procesar_lista(lista):
    """
    Problema 1. Procesamiento de una lista de enteros. 
    Crea una función que reciba una lista de enteros por parámetro y devuelva otra 
    lista, de acuerdo a las siguientes acciones: 
    1. Eliminar los números negativos de la lista. 
    2. Eliminar los valores que están repetidos, quedándonos con uno de ellos. 
    3. Ordenar los números resultantes de menor a mayor. 
    
    """
    # 1. Eliminar números negativos
    sin_negativos = [num for num in lista if num >= 0]
    
    # 2. Eliminar duplicados
    sin_duplicados = list(set(sin_negativos))
    
    # 3. Ordenar de menor a mayor
    sin_duplicados.sort()
    
    return sin_duplicados


# Programa principal
if __name__ == "__main__":
    try:
        print("=" * 60)
        print("PROCESADOR DE LISTAS - Problema 1")
        print("=" * 60)
        
        # Solicitar los números al usuario
        print("\nIntroduce los números enteros separados por espacios:")
        print("(Pueden ser positivos, negativos o repetidos)")
        entrada = input("Números: ")
        
        # Convertir la entrada a lista de enteros
        numeros = [int(x) for x in entrada.split()]
        
        print("\n" + "-" * 60)
        print(f"Lista ingresada: {numeros}")
        print("-" * 60)
        
        # Procesar la lista
        resultado = procesar_lista(numeros)
        
        # Mostrar resultados
        print("\nPROCESAMIENTO:")
        print("Eliminados números negativos")
        print("Eliminados duplicados")
        print("Ordenados de menor a mayor")
        
        print("\n" + "=" * 60)
        print("RESULTADO FINAL")
        print("=" * 60)
        print(f"Entrada:    {numeros}")
        print(f"Resultado:  {resultado}")
        print("=" * 60)
        
    except ValueError:
        print("\nError: Debes introducir solo números enteros separados por espacios.")
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        print("\n")
        input("Presiona ENTER para salir...")
