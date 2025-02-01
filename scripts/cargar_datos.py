import pandas as pd

def cargar_datos_sin_duplicados(path):

    # Leemos los datos
    df= pd.read_csv(path)

    # Eliminamos duplicados
    df=df.drop_duplicates(subset=[col for col in df.columns if col != 'ID'])

    return df
    