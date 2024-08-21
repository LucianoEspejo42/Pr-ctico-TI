"""
ENUNCIADO: 
Desarrollar una aplicación de software que calcule la entropía y redundancia, de una fuente con símbolos 
vistos en forma independiente y dependiente en O(1). 
Realizar comparaciones para diferentes archivos (*.txt, *.exe, *.zip etc.)

Entopia H(s) = ∑Pi * log2 (1/Pi)

Redundancia R = (Hmax - H(s))/Hmax
"""
import math
from collections import Counter

def calcular_entropia(probabilidades):
    entropia = sum(p * math.log2(1 / p) for p in probabilidades if p > 0)
    return entropia

def calcular_redundancia(entropia, num_simbolos):
    entropia_maxima = math.log2(num_simbolos)
    redundancia = (entropia_maxima - entropia) / entropia_maxima
    return redundancia

def procesar_archivo(archivo):
    with open(archivo, 'rb') as file:
        contenido = file.read()

    # Contar la frecuencia de cada byte en el archivo
    contador = Counter(contenido)
    
    # Calcular la probabilidad de cada símbolo
    total_simbolos = sum(contador.values())
    probabilidades = [freq / total_simbolos for freq in contador.values()]
    
    # Número de símbolos únicos
    num_simbolos = len(contador)

    # Calcular entropía y redundancia
    entropia = calcular_entropia(probabilidades)
    redundancia = calcular_redundancia(entropia, num_simbolos)

    return entropia, redundancia

def main():
    archivo = r"C:\Users\lucia\OneDrive\Escritorio\PracticoTeoria de la información\file\file.rar"
    try:
        entropia, redundancia = procesar_archivo(archivo)
        print(f"Entropía: {entropia:.4f} bits/símbolo")
        print(f"Redundancia: {redundancia:.4f}")
    except Exception as e:
        print(f"Error procesando el archivo: {e}")

if __name__ == "__main__":
    main()
