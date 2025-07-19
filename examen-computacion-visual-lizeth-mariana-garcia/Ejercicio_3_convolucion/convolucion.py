import matplotlib.pyplot as plt
import os

os.makedirs("graficos", exist_ok=True)

senal = [3, 5, 2, 6, 7, 4, 8, 1, 0, 2]

kernel = [1, 0, -1]

def convolucion_1d(senal, kernel):
    n = len(senal)
    k = len(kernel)
    pad = k // 2

    senal_padded = [0]*pad + senal + [0]*pad

    resultado = []
    for i in range(n):
        suma = 0
        for j in range(k):
            suma += senal_padded[i + j] * kernel[j]
        resultado.append(suma)
    return resultado

resultado = convolucion_1d(senal, kernel)


plt.figure()
plt.stem(senal)
plt.title("Señal Original")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.grid()
plt.savefig("graficos/senal_original.png")

plt.figure()
plt.stem(kernel)
plt.title("Kernel")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.grid()
plt.savefig("graficos/kernel.png")

plt.figure()
plt.stem(resultado)
plt.title("Resultado de la Convolución")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.grid()
plt.savefig("graficos/resultado.png")

print("Convolución completada y gráficos guardados en la carpeta 'graficos'.")
