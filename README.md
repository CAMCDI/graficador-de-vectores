```markdown
# Graficador de Vectores en 2D

Este proyecto es una herramienta sencilla en Python para graficar vectores en un plano 2D. Utiliza las bibliotecas `matplotlib` y `numpy` para crear gráficos interactivos y manejar las operaciones vectoriales de manera eficiente.

## Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes bibliotecas:

- `matplotlib`: Para la creación de gráficos.
- `numpy`: Para manipular operaciones vectoriales.

Puedes instalar estas dependencias utilizando `pip`:

```bash
pip install matplotlib numpy
```

## Uso

### Graficar un vector

El programa permite graficar un vector en 2D especificando su origen y su destino. A continuación se explica el uso básico del código:

1. **Definir el origen y el destino del vector**:
   - El origen es el punto desde donde empieza el vector.
   - El destino es el punto donde termina el vector.

2. **Llamar a la función `graficar_vector`** para dibujar el gráfico. Esta función recibirá como parámetros las coordenadas del origen y del destino del vector.

3. El gráfico generado mostrará el vector en un plano 2D, donde se dibujarán los ejes de coordenadas para facilitar la visualización.

### Explicación de la función `graficar_vector`:

- **Parámetros**:
  - `vector_origen`: Tupla o lista con las coordenadas del origen del vector (por ejemplo, `(0, 0)`).
  - `vector_destino`: Tupla o lista con las coordenadas del destino del vector (por ejemplo, `(3, 4)`).
  
- **Proceso**:
  - Se crea una figura utilizando `matplotlib`.
  - Se utiliza la función `quiver` para dibujar el vector.
  - Los ejes se ajustan y se añade una cuadrícula para facilitar la visualización.
  
- **Resultado**:
  - Se abre una ventana mostrando el gráfico con el vector dibujado.

## Contribuciones

Si deseas contribuir a este proyecto, puedes hacerlo mediante un **pull request**. Asegúrate de seguir las buenas prácticas de código y documentación.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
