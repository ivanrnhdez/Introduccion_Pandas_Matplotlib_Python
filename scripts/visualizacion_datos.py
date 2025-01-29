import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def grafica_medias_asignaturas(df):

    # Filtrar solo las filas con calificaciones válidas (ignorar -1)
    presentados = df[df['Calificacion'] != -1]

    # Calcular la media de calificaciones por asignatura
    medias_asignaturas = presentados.groupby('Asignatura')['Calificacion'].mean()

    # Crear el diagrama de barras
    plt.figure(figsize=(8, 5))
    medias_asignaturas.plot(kind='bar', color='skyblue', edgecolor='black')

    # Personalizar el gráfico
    plt.title('Media de Calificaciones por Asignatura', fontsize=14)
    plt.xlabel('Asignatura', fontsize=12)
    plt.ylabel('Media', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()



def grafico_combinado_por_ciudad(df):

    # Filtrar solo las filas con calificaciones válidas (ignorar -1)
    presentados = df[df['Calificacion'] != -1]

    # Calcular la media de calificaciones por ciudad
    medias_ciudades = presentados.groupby('Ciudad')['Calificacion'].mean()

    # Calcular la cantidad de estudiantes por ciudad
    cantidad_estudiantes_ciudad = presentados['Ciudad'].value_counts()

    # Crear el gráfico combinado
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Gráfico de barras (Cantidad de estudiantes por ciudad)
    cantidad_estudiantes_ciudad.plot(kind='bar', color='lightgreen', edgecolor='black', ax=ax1, width=0.6, label='Cantidad de Estudiantes')
    ax1.set_ylabel('Cantidad de Estudiantes', fontsize=12, color='green')
    ax1.set_xlabel('Ciudad', fontsize=12)
    ax1.set_title('Cantidad de Estudiantes y Media de Calificaciones por Ciudad', fontsize=14)
    ax1.tick_params(axis='y', labelcolor='green')
    ax1.set_xticks(range(len(cantidad_estudiantes_ciudad)))
    ax1.set_xticklabels(cantidad_estudiantes_ciudad.index, rotation=45, ha='right')

    # Gráfico de líneas (Media de calificaciones por ciudad)
    ax2 = ax1.twinx()
    ax2.plot(medias_ciudades.index, medias_ciudades.values, color='blue', marker='o', linewidth=2, label='Media de Calificaciones')
    ax2.set_ylabel('Media de Calificaciones', fontsize=12, color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')

    # Añadir una leyenda
    fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9), bbox_transform=ax1.transAxes)

    # Ajustar diseño
    plt.tight_layout()
    plt.show()


def generar_graficos_edad_calificacion_genero(df):

    # Filtrar solo las filas con calificaciones válidas (ignorar -1)
    presentados = df[df['Calificacion'] != -1]
    
    # Buscar la ruta de los graficos
    ruta_carpeta = "outputs/graficos/"

    # Crear figura y subgráficos
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Gráfico de dispersión: Edad vs Calificación
    axes[0].scatter(presentados['Edad'], presentados['Calificacion'], color='blue', alpha=0.5)

    # Ajustar una línea de regresión (tendencia)
    coef = np.polyfit(presentados['Edad'], presentados['Calificacion'], 1)  # Ajuste lineal
    poly1d_fn = np.poly1d(coef)  # Función de la recta
    axes[0].plot(presentados['Edad'], poly1d_fn(presentados['Edad']), color='black', label="Tendencia")

    # Etiquetas y título
    axes[0].set_title("Relación entre Edad y Calificación")
    axes[0].set_xlabel("Edad")
    axes[0].set_ylabel("Calificación")

    # Gráfico de torta: Distribución por Género
    df['Genero'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'pink'], ax=axes[1])
    axes[1].set_title("Distribución de Género")
    axes[1].set_ylabel("")  # Quitar etiqueta del eje Y

    # Guardar la imagen
    ruta_imagen = os.path.join(ruta_carpeta, "grafico_edad_calificacion_genero.png")
    plt.tight_layout()
    plt.savefig(ruta_imagen, dpi=300)
    plt.close()

    print(f"Gráficos guardados en: {ruta_imagen}")


