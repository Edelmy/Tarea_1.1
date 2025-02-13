#   Codigo que implementa un esquema numerico 
#   para determinar la precision de una maquina
#Chay Dzul Edelmy
import numpy as np
import matplotlib.pyplot as plt

# Inicialización de variables
epsilon = 1.0
iteracion = 0
valores_epsilon = []
valores_iteracion = []

# Bucle para calcular la precisión de máquina
while 1.0 + epsilon != 1.0:
    iteracion += 1
    epsilon /= 2 #En cada iteración, epsilon se divide entre 2
    #El bucle se detiene cuando 1.0 + epsilon ya no es distinto de 1.0. 
    #Esto significa que epsilon es tan pequeño que no puede ser representado en la computadora
    print(f"Iteración: {iteracion}, Precisión de máquina: {epsilon}")
    valores_iteracion.append(iteracion)
    valores_epsilon.append(epsilon)

# Ajuste final de epsilon
epsilon *= 2
#Se multiplica por 2 para obtener el valor correcto de la precisión de máquina

print(f"Precisión de máquina: {epsilon}")

# Graficar los resultados
plt.plot(valores_iteracion, valores_epsilon, marker='o')
plt.xlabel('Iteraciones')
plt.ylabel('Epsilon')
plt.title('Evolución de la Precisión de Máquina')
plt.show()