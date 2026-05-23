import time

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def buscar_primos(limite):
    primos = []
    for num in range(1, limite + 1):
        if es_primo(num):
            primos.append(num)
    return primos

if __name__ == "__main__":
    limite = 100000
    inicio = time.time()
    primos = buscar_primos(limite)
    fin = time.time()
    print(f"Cantidad de primos encontrados: {len(primos)}")
    print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")