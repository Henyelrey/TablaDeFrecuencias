Instrucciones de Uso – Tabla de Frecuencias
1. Inicio del Programa

Ejecuta el archivo Python con el código proporcionado.

Se abrirá una ventana titulada “Tabla de Frecuencias” en pantalla completa.

La ventana está dividida en tres secciones principales:

Entrada de datos (arriba)

Tabla de frecuencias (medio)

Botones de cálculo y gráficos (abajo)

2. Entrada de Datos

En la sección superior:

Límite Inferior (Li): Ingresa el valor mínimo del primer intervalo.

Límite Superior (Ls): Ingresa el valor máximo que cubre todos los datos.

Amplitud: Ingresa el tamaño de cada intervalo.

Ejemplo:

Li = 10

Ls = 50

Amplitud = 10

Luego presiona “Generar Intervalos”.

Se crearán automáticamente los intervalos y columnas para ingresar fi (frecuencia de cada intervalo).

3. Llenado de Frecuencias (fi)

En la tabla que aparece, ingresa la frecuencia absoluta de cada intervalo en la columna fi.

Asegúrate de que sean números enteros válidos.

4. Cálculo de Frecuencia Acumulada (Fi)

Presiona el botón “Calcular FI”.

La columna Fi se llenará automáticamente mostrando la frecuencia acumulada de cada intervalo.

5. Medidas de Posición y Proporción

Sección izquierda con botones:

Media: Calcula la media de los datos agrupados.

Mediana: Calcula la mediana de los datos.

Moda: Calcula la moda de los datos.

Cuartiles: Ingresa k (1 a 3) para calcular Q1, Q2 o Q3.

Deciles: Ingresa k (1 a 9) para calcular Dk.

Percentiles: Ingresa k (1 a 99) para calcular Pk.

Nota: Los resultados aparecerán en ventanas emergentes (messagebox).

6. Medidas de Dispersión

Sección central con botones:

Rango: Diferencia entre la mayor y menor marca de clase.

Varianza: Calcula la varianza de los datos agrupados.

Desviación Estándar: Calcula la desviación estándar.

Coeficiente de Variación (CV): Porcentaje de variación relativa a la media.

7. Gráficos

Sección derecha con botones:

Histograma: Muestra un histograma de frecuencias.

Polígono de Frecuencias: Muestra un gráfico de línea uniendo las marcas de clase y sus frecuencias.

Ojiva: Muestra la frecuencia acumulada como gráfico de línea.

Nota: Los gráficos se generan usando matplotlib y aparecerán en una ventana externa.

8. Consideraciones

Asegúrate de ingresar valores numéricos válidos en Li, Ls, amplitud y fi.

Li debe ser menor que Ls, y amplitud debe ser mayor que 0.

La tabla y los cálculos dependen de haber ingresado primero los intervalos y frecuencias.

Para cualquier error de ingreso, el programa mostrará una ventana de alerta (messagebox.showerror).
