import time
import math

def es_primo_optimizado(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Solo revisamos hasta la raíz cuadrada, y solo números impares
    limite = int(math.sqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True

def buscar_primos_optimizado(limite):
    # Usamos list comprehension para crear la lista
    return [num for num in range(2, limite + 1) if es_primo_optimizado(num)]

if __name__ == "__main__":
    limite = 100000
    inicio = time.time()
    primos = buscar_primos_optimizado(limite)
    fin = time.time()
    print(f"Cantidad de primos encontrados: {len(primos)}")
    print(f"Tiempo de ejecución optimizado: {fin - inicio:.4f} segundos")