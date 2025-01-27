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

    return {
        "dataframe_asignaturas": df_asignaturas
    }



def analisis_datos_asignaturas(df):
    
    # Filtrar solo los alumnos que se presentaron (calificación != -1)
    presentados = df[df['Calificacion'] != -1]

    # Distribución de géneros por asignatura
    distribucion_genero = presentados.groupby(['Asignatura', 'Genero']).size().unstack(fill_value=0)

    # Top 3 mejores calificaciones por asignatura
    top_estudiantes = presentados.sort_values(['Asignatura', 'Calificacion'], ascending=[True, False]).groupby('Asignatura').head(3)

    # Varianza y desviación estándar de las calificaciones por asignatura
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

    return {
        "distribucion_genero": distribucion_genero,
        "top_estudiantes": top_estudiantes,
        "estadisticas_calificaciones": estadisticas_calificaciones
    }



def exploracion_datos(df):
    
    # Estadísticas descriptivas básicas
    print("\n=== Estadísticas Descriptivas de Edad y Calificación ===\n")
    estadisticas = df[['Calificacion', 'Edad']].describe().transpose()
    print(estadisticas.to_string(float_format="%.2f"))
    
    # Matriz de correlación (Calificación y Edad)
    print("\n=== Matriz de Correlación ===\n")
    correlacion = df[['Calificacion', 'Edad']].corr()
    print(correlacion.to_string(float_format="%.2f"))
    
    # Distribución de calificaciones por rangos
    print("\n=== Distribución de Calificaciones (por Rangos) ===\n")
    bins = [0, 5, 7, 9, 10]
    etiquetas = ['Insuficiente', 'Aprobado', 'Notable', 'Sobresaliente']
    df['Rango'] = pd.cut(df['Calificacion'], bins=bins, labels=etiquetas, right=False)
    distribucion = df['Rango'].value_counts().sort_index()
    print(distribucion.to_string())
    
    # Media, mediana y std de calificaciones agrupadas por género
    print("\n=== Análisis por Género ===\n")
    genero_stats = df.groupby('Genero')['Calificacion'].agg(['mean', 'median', 'std', 'count']).fillna(0)
    genero_stats.rename(columns={
        'mean': 'Media',
        'median': 'Mediana',
        'std': 'Desv Estándar',
        'count': 'Cantidad'
    }, inplace=True)
    print(genero_stats.to_string(float_format="%.2f"))
    
    # Estadísticas por asignatura
    print("\n=== Estadísticas por Asignatura ===\n")
    asignatura_stats = df.groupby('Asignatura')['Calificacion'].agg(['mean', 'median', 'var', 'std', 'count']).fillna(0)
    asignatura_stats.rename(columns={
        'mean': 'Media',
        'median': 'Mediana',
        'var': 'Varianza',
        'std': 'Desv Estándar',
        'count': 'Cantidad'
    }, inplace=True)
    print(asignatura_stats.to_string(float_format="%.2f"))
    
    return {
        "estadisticas_descriptivas": estadisticas,
        "correlacion": correlacion,
        "distribucion_rangos": distribucion,
        "genero_stats": genero_stats,
        "asignatura_stats": asignatura_stats
    }



