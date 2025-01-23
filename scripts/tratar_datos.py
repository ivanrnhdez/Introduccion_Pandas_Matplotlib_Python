import pandas as pd

def tratar_datos_alumnos(df):

    # Eliminamos las filas que no tengan nombre o ciudad
    df = df.dropna(subset = ['Nombre', 'Ciudad'] )

    return df

def tratar_datos_calificaciones(df):

    # A los no presentados les asignamos un valor de -1
    df['Calificacion'] = df['Calificacion'].fillna(-1)

    # Eliminamos los valores nulos restantes
    df = df.dropna()

    return df

def combinar_datos(df1,df2,path):

    # Combinamos los datos por nombre
    df = pd.merge(df1, df2, on='Nombre', how='inner')

    # Renombramos los IDs originales para claridad
    df = df.rename(columns={"ID_x": "ID_Alumno", "ID_y": "ID_Calificacion"})

    # Ordenar por 'Asignatura' y luego por 'Calificación'
    df = df.sort_values(by=['Materia', 'Calificacion'], ascending=[True, False])

    # Generamos nuevos IDs que comienzan en 1
    df.insert(0, 'ID', range(1, len(df) + 1))

    # Reordenamos las columnas para que ID_Alumno y ID_Calificaciones estén al principio
    cols = ['ID', 'ID_Alumno', 'ID_Calificacion'] + [col for col in df.columns if col not in ['ID', 'ID_Alumno', 'ID_Calificacion']]
    df = df[cols]

    # Guardamos los datos en un nuevo CSV
    df.to_csv(path , index=False)

    return df


    