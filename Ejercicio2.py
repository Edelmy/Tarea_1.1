import numpy as np
import matplotlib.pyplot as plt
#Chay Dzul Edelmy
# Función para calcular pi usando la serie de Leibniz
def leibniz_pi(n):
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

# Valor real de pi
true_pi = np.pi

# Aproxima pi con distintos valores de N
N_values = [10, 100, 1000, 10000]

# Se crean listas para almacenar los errores
errors_abs = []  # Error absoluto
errors_rel = []  # Error relativo
errors_cuad = []  # Error cuadrático

# Cálculo de errores para cada N
for N in N_values:
    approx_pi = leibniz_pi(N)  # Aproximación de pi
    error_abs = abs(true_pi - approx_pi)  # Error absoluto
    error_rel = error_abs / true_pi  # Error relativo
    error_cuad = (true_pi - approx_pi)**2  # Error cuadrático
    
    # Almacenar los errores en sus respectivos arreglos
    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    errors_cuad.append(error_cuad)
    
    # Se imprimen resultados en formato de tabla
    print(f"N={N}: Error absoluto={error_abs:.6e}, Error relativo={error_rel:.6e}, Error cuadrático={error_cuad:.6e}")

# Graficar los errores
plt.figure(figsize=(10, 6))
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o')
plt.plot(N_values, errors_rel, label='Error relativo', marker='s')
plt.plot(N_values, errors_cuad, label='Error cuadrático', marker='p')

plt.xscale('log')  # Escala logarítmica en el eje X
plt.yscale('log')  # Escala logarítmica en el eje Y
plt.xlabel('N (Número de términos)')
plt.ylabel('Error')
plt.title('Errores en la aproximación de pi (Serie de Leibniz)') #Etiqueta
plt.legend()
plt.grid(True)
plt.show()