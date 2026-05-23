import matplotlib.pyplot as plt

# Tus tiempos (usa los tuyos)
tiempo_original = 39.1348
tiempo_optimizado = 0.1242

versiones = ['Original', 'Optimizado']
tiempos = [tiempo_original, tiempo_optimizado]

plt.bar(versiones, tiempos, color=['red', 'green'])
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de ejecución')
plt.grid(axis='y', alpha=0.3)

# Mostrar valores en las barras
for i, v in enumerate(tiempos):
    plt.text(i, v + 1, f"{v:.4f}s", ha='center')

plt.savefig('comparacion_tiempos.png')
plt.show()