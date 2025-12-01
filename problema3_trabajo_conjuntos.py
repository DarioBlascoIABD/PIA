def analizar_conjuntos(lista1, lista2):
    """

    Problema 3. Trabajo con conjuntos 
    Escribe una función que reciba dos listas de enteros y devuelva un diccionario con la siguiente información (ES OBLIGATORIO USAR CONJUNTOS PARA 
    CALCULARLOS) 
    1. La intersección de ambos conjuntos (elementos comunes). 
    2. La unión de ambos conjuntos (todos los elementos sin duplicados). 
    3. La diferencia simétrica (elementos que están en uno u otro conjunto, 
    pero no en ambos).

    """
    # Convertimos las listas a conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    # Calculamos operaciones usando conjuntos
    interseccion = conjunto1 & conjunto2
    union = conjunto1 | conjunto2
    diferencia_simetrica = conjunto1 ^ conjunto2
    
    # Creamos el diccionario con los resultados
    resultado = {
        'interseccion': sorted(list(interseccion)),
        'union': sorted(list(union)),
        'diferencia_simetrica': sorted(list(diferencia_simetrica))
    }
    
    return resultado


def main():
    print("=" * 60)
    print("TRABAJO CON CONJUNTOS - Problema 3")
    print("=" * 60)
    
    # Solicitar la primera lista
    print("\nIntroduce los elementos de la PRIMERA lista separados por espacios:")
    entrada1 = input("Lista 1: ")
    lista1 = [int(x) for x in entrada1.split()]
    
    # Solicitar la segunda lista
    print("\nIntroduce los elementos de la SEGUNDA lista separados por espacios:")
    entrada2 = input("Lista 2: ")
    lista2 = [int(x) for x in entrada2.split()]
    
    # Mostrar las listas ingresadas
    print("\n" + "-" * 60)
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print("-" * 60)
    
    # Llamar a la función
    resultado = analizar_conjuntos(lista1, lista2)
    
    # Mostrar resultados
    print("\nRESULTADOS:")
    print("=" * 60)
    print(f"\n1. INTERSECCIÓN (elementos comunes):")
    print(f"   {resultado['interseccion']}")
    print(f"   Cantidad: {len(resultado['interseccion'])} elementos")
    
    print(f"\n2. UNIÓN (todos los elementos sin duplicados):")
    print(f"   {resultado['union']}")
    print(f"   Cantidad: {len(resultado['union'])} elementos")
    
    print(f"\n3. DIFERENCIA SIMÉTRICA (en uno u otro, pero no en ambos):")
    print(f"   {resultado['diferencia_simetrica']}")
    print(f"   Cantidad: {len(resultado['diferencia_simetrica'])} elementos")
    
    print("\n" + "=" * 60)
    
    # Mostrar información adicional de las operaciones
    print("\nINFORMACIÓN ADICIONAL:")
    print("-" * 60)
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    print(f"Conjunto 1: {sorted(conjunto1)}")
    print(f"Conjunto 2: {sorted(conjunto2)}")
    print(f"\nElementos solo en Lista 1: {sorted(list(conjunto1 - conjunto2))}")
    print(f"Elementos solo en Lista 2: {sorted(list(conjunto2 - conjunto1))}")
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    finally:
        print("\n")
        input("Presiona ENTER para salir...")
