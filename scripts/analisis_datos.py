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
    aprobados_por_asignatura = presentados[presentados['Calificacion'] >= 5].groupby('Materia').size()
    total_por_asignatura = presentados.groupby('Materia').size()
    porcentaje_por_asignatura = (aprobados_por_asignatura / total_por_asignatura * 100).fillna(-1)

    # Calcular las notas medias por asignatura
    notas_medias_por_asignatura = presentados.groupby('Materia')['Calificacion'].mean().fillna(-1)

    # Crear un DataFrame combinado con porcentaje de aprobados y notas medias
    df_asignaturas = pd.DataFrame({
        'Media': notas_medias_por_asignatura,
        'Aprobados (%)': porcentaje_por_asignatura
    }).reset_index().sort_values('Media',ascending=False)

    # Imprimir el resultado por pantalla
    print(f'\nPorcentaje presentados totales: {porcentaje_presentados:.2f}%')
    print(f'Porcentaje aprobados totales: {porcentaje_total:.2f}%')
    print('\nAnálisis asignaturas:\n')
    print(df_asignaturas.to_string(index=False, float_format="%.2f"))



