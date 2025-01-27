import pandas as pd

def analisis_datos_calificaciones(df):

    # Filtrar solo los alumnos que se presentaron (calificación != -1)
    presentados = df[df['Calificacion'] != -1]

    # Calcular porcentaje de presentados
    porcentaje_presentados = len(presentados)/ len(df) * 100

    # Calcular porcentaje total de aprobados
    aprobados_totales = presentados[presentados['Calificacion'] >= 5]
    porcentaje_total = len(aprobados_totales) / len(presentados) * 100

    # Calcular porcentaje de aprobados por asignatura
    aprobados_por_asignatura = presentados[presentados['Calificacion'] >= 5].groupby('Asignatura').size()
    total_por_asignatura = presentados.groupby('Asignatura').size()
    porcentaje_por_asignatura = (aprobados_por_asignatura / total_por_asignatura * 100).fillna(-1)

    # Calcular las notas medias por asignatura
    notas_medias_por_asignatura = presentados.groupby('Asignatura')['Calificacion'].mean().fillna(-1)

    # Crear un DataFrame combinado con porcentaje de aprobados y notas medias
    df_asignaturas = pd.DataFrame({
        'Media': notas_medias_por_asignatura,
        'Aprobados (%)': porcentaje_por_asignatura
    }).reset_index().sort_values('Media',ascending=False)

    # Imprimir el resultado por pantalla
    print("\n=== Análisis de Calificaciones ===\n")
    print(f'Porcentaje presentados totales: {porcentaje_presentados:.2f}%')
    print(f'Porcentaje aprobados totales: {porcentaje_total:.2f}%')
    print("\n=== Análisis por Asignaturas ===\n")
    print(df_asignaturas.to_string(index=False, float_format="%.2f"))



def analisis_avanzado_calificaciones(df):
    
    # Filtrar solo los alumnos que se presentaron (calificación != -1)
    presentados = df[df['Calificacion'] != -1]

    # 1. Distribución de géneros por asignatura
    distribucion_genero = presentados.groupby(['Asignatura', 'Genero']).size().unstack(fill_value=0)

    # 2. Top 3 mejores calificaciones por asignatura
    top_estudiantes = presentados.sort_values(['Asignatura', 'Calificacion'], ascending=[True, False]).groupby('Asignatura').head(3)

    # 3. Varianza y desviación estándar de las calificaciones por asignatura
    estadisticas_calificaciones = presentados.groupby('Asignatura')['Calificacion'].agg(['var', 'std']).fillna(0)

    # Imprimir resultados
    print("\n=== Distribución de Géneros por Asignatura ===\n")
    print(distribucion_genero.to_string(float_format="%.2f"))

    print("\n=== Top 3 Estudiantes con Mejores Calificaciones por Asignatura ===\n")
    asignaturas = top_estudiantes.groupby('Asignatura')
    for asignatura, grupo in asignaturas:
        print(f"{asignatura}")
        for _, fila in grupo.iterrows():
            print(f"  {fila['Nombre']:<10} {fila['Calificacion']:.2f}")

    print("\n=== Varianza y Desviación Estándar de Calificaciones por Asignatura ===\n")
    print(estadisticas_calificaciones.to_string(float_format="%.2f"))



