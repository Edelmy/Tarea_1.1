#Chay Dzul Edelmy
import matplotlib.pyplot as plt

# Función para calcular los errores
def calcular_errores(x, y, valor_real):
    diferencia = x - y
    error_abs = abs(valor_real - diferencia)
    error_rel = error_abs / abs(valor_real)
    error_pct = error_rel * 100
    print(f"Diferencia: {diferencia}")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel}")
    print(f"Error porcentual: {error_pct}%")
    return error_abs, error_rel, error_pct

# Valores de prueba que pasan a la función
valores = [(1.0000001, 1.0000000, 0.0000001), #Primer caso
           (1.000000000000001, 1.000000000000000, 0.000000000000001)] #Segundo caso

# Se crean listas para almacenar los errores
errores_abs = []
errores_rel = []
errores_pct = []

# Calcular errores para cada caso
#El ciclo for itera sobre cada caso de prueba en la lista valores
for x, y, real in valores:
    print(f"\nPara x={x}, y={y}:")
    error_abs, error_rel, error_pct = calcular_errores(x, y, real) #Se llama a la función para calcular los errores, y los resultados se añaden a las listas correspondientes
    errores_abs.append(error_abs) 
    errores_rel.append(error_rel)
    errores_pct.append(error_pct)

# Graficar los errores
indices = range(1, len(valores) + 1)  # Índices para los casos

plt.figure(figsize=(10, 6))
plt.plot(indices, errores_abs, label='Error absoluto', marker='o')
plt.plot(indices, errores_rel, label='Error relativo', marker='s')
plt.plot(indices, errores_pct, label='Error porcentual', marker='^')
plt.xlabel('Caso')
plt.ylabel('Errores')
plt.title('Errores Absoluto, Relativo y Porcentual')
plt.legend()
plt.grid(True)
plt.show()