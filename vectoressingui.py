import matplotlib.pyplot as plt
import numpy as np

# Función para graficar un vector
def graficar_vector(vector_origen, vector_destino):
    # Crea una nueva figura
    plt.figure()
    
    # Establece el origen y el destino del vector
    origen = np.array(vector_origen)
    destino = np.array(vector_destino)

    # Dibuja el vector usando quiver
    plt.quiver(origen[0], origen[1], destino[0], destino[1], angles='xy', scale_units='xy', scale=1, color='b')

    # Ajusta los límites del gráfico
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Establece el aspecto del gráfico
    plt.gca().set_aspect('equal', adjustable='box')

    # Agrega etiquetas
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    
    plt.grid(True)

    # Muestra el gráfico
    plt.show()

# Ejemplo de uso
origen = (0, 0)  # Origen del vector
destino = (3, 4)  # Destino del vector

# Llamada a la función para graficar el vector
graficar_vector(origen, destino)
