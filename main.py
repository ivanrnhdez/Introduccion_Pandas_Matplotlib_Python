import os
from scripts.cargar_datos import cargar_datos_sin_duplicados
from scripts.tratar_datos import tratar_datos_alumnos, tratar_datos_calificaciones, combinar_datos


def main():

    # Ruta base del proyecto
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Ruta a los archivos CSV
    alumnos_path = os.path.join(base_path, "data/raw/alumnos.csv")
    calificaciones_path = os.path.join(base_path, "data/raw/calificaciones.csv")
    combinado_path = os.path.join(base_path, "data/processed/al_cal_combinado.csv")

    # Cargamos los datos de los CSVs
    df_alumnos = cargar_datos_sin_duplicados(alumnos_path)
    df_calificaciones = cargar_datos_sin_duplicados(calificaciones_path)

    # Tratamos los datos
    df_alumnos = tratar_datos_alumnos(df_alumnos)
    df_calificaciones = tratar_datos_calificaciones(df_calificaciones)

    # Combinamos los datos y los guardamos en un nuevo CSV
    df_combinado = combinar_datos(df_alumnos, df_calificaciones, combinado_path)





if __name__ == "__main__":
    main()