import string
import os


def frecuencia_palabras(ruta_fichero):
    """

    Problema 2. Frecuencia de palabras en un texto. 
    Escribe una función que reciba por parámetro una lista de palabras y la ruta a un fichero de texto y devuelva un diccionario que muestre cuantas veces 
    aparecen las distintas palabras de la lista en el fichero de texto. Haz un pequeño programa que la ponga a prueba. 
    Requisitos: 
    1. Eliminar signos de puntuación y convertir todo a minúsculas. 
    2. Usar un diccionario donde la clave sea la palabra y el valor su frecuencia. 
    3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra. 

    """
    # Leer el contenido del fichero
    with open(ruta_fichero, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    
    # REQUISITO 1: Eliminar signos de puntuación y convertir todo a minúsculas
    contenido = contenido.lower()
    translator = str.maketrans('', '', string.punctuation)
    contenido_sin_puntuacion = contenido.translate(translator)
    
    # Dividir el texto en palabras
    palabras_texto = contenido_sin_puntuacion.split()
    
    # REQUISITO 2: Usar un diccionario donde la clave sea la palabra y el valor su frecuencia
    frecuencias = {}
    for palabra in palabras_texto:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    
    # REQUISITO 3: Mostrar las palabras y sus frecuencias ordenadas por palabra
    frecuencias_ordenadas = dict(sorted(frecuencias.items()))
    
    return frecuencias_ordenadas


def main():
    print("=" * 70)
    print("FRECUENCIA DE PALABRAS EN UN TEXTO - Ejercicio 2")
    print("=" * 70)
    
    # PASO 1: Solicitar el texto y guardarlo en un fichero
    print("\nIntroduce el texto a analizar:")
    print("-" * 70)
    print("Escribe o pega el texto (cuando termines, escribe 'FIN' en la siguiente línea y pulsa ENTER):")
    print()
    
    lineas = []
    while True:
        linea = input()
        if linea.strip().upper() == 'FIN':
            break
        lineas.append(linea)
    
    print(f"\nTexto capturado correctamente")
    
    # PASO 2: Solicitar la ruta donde guardar el fichero
    print("\n" + "=" * 70)
    print("PASO 2: Ruta para guardar el fichero")
    print("-" * 70)
    print("Introduce la ruta donde guardar el fichero:")
    print("  Ruta completa: C:\\Users\\Usuario\\Documents\\mi_texto.txt")
    print("  Solo directorio: C:\\Users\\Usuario\\Documents\\ (se usará 'texto_guardado.txt')")
    print("  Solo nombre: mi_texto.txt (se guardará en la carpeta que esté guardado el script)")
    print()
    
    ruta_input = input("Ruta: ").strip()
    
    # Si la ruta termina en \ o /, es un directorio, agregar nombre de archivo por defecto
    if ruta_input.endswith('\\') or ruta_input.endswith('/'):
        ruta_fichero = os.path.join(ruta_input, 'texto_guardado.txt')
        print(f"Nota: Se guardará como '{os.path.basename(ruta_fichero)}' en ese directorio")
    # Si solo pone nombre de archivo, usar la carpeta del script
    elif not os.path.dirname(ruta_input):
        ruta_script = os.path.dirname(os.path.abspath(__file__))
        ruta_fichero = os.path.join(ruta_script, ruta_input)
    else:
        ruta_fichero = ruta_input
    
    # Guardar el texto en la ruta especificada
    try:
        with open(ruta_fichero, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lineas))
        print(f"\nFichero guardado exitosamente en: {ruta_fichero}")
    except Exception as e:
        print(f"\nError al guardar el fichero: {e}")
        return
    
    # PASO 3: Procesar el fichero aplicando los 3 requisitos
    print("\n" + "=" * 70)
    print("PROCESANDO FICHERO...")
    print("=" * 70)
    print("Requisito 1: Eliminando signos de puntuación y convirtiendo a minúsculas")
    print("Requisito 2: Generando diccionario con palabra:frecuencia")
    print("Requisito 3: Ordenando palabras alfabéticamente")
    
    # Llamar a la función
    resultado = frecuencia_palabras(ruta_fichero)
    
    # PASO 3: Mostrar el diccionario de frecuencias
    print("\n" + "=" * 70)
    print("DICCIONARIO DE FRECUENCIAS (ordenado alfabéticamente)")
    print("=" * 70)
    print(f"{'PALABRA':<25} {'FRECUENCIA':>15}")
    print("-" * 70)
    
    total_palabras = 0
    for palabra, frecuencia in resultado.items():
        print(f"{palabra:<25} {frecuencia:>15}")
        total_palabras += frecuencia
    
    print("-" * 70)
    print(f"{'TOTAL DE PALABRAS:':<25} {total_palabras:>15}")
    print(f"{'PALABRAS ÚNICAS:':<25} {len(resultado):>15}")
    print("=" * 70)
    
    # Estadísticas adicionales
    print("\nESTADÍSTICAS:")
    print("-" * 70)
    palabra_mas_frecuente = max(resultado.items(), key=lambda x: x[1])
    palabra_menos_frecuente = min(resultado.items(), key=lambda x: x[1])
    
    print(f"Palabra más frecuente: '{palabra_mas_frecuente[0]}' ({palabra_mas_frecuente[1]} veces)")
    print(f"Palabra menos frecuente: '{palabra_menos_frecuente[0]}' ({palabra_menos_frecuente[1]} vez/veces)")
    
    # Mostrar palabras que aparecen solo una vez
    palabras_unicas_freq = [p for p, f in resultado.items() if f == 1]
    if len(palabras_unicas_freq) > 0:
        print(f"Palabras que aparecen solo 1 vez: {len(palabras_unicas_freq)}")
    
    print("=" * 70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        print("\n")
        input("Presiona ENTER para salir...")
