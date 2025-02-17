import os
from scripts.cargar_datos import cargar_datos_sin_duplicados
from scripts.tratar_datos import tratar_datos_alumnos, tratar_datos_calificaciones, combinar_datos
from scripts.analisis_datos import analisis_datos_calificaciones, analisis_datos_asignaturas, exploracion_datos
from scripts.visualizacion_datos import grafica_medias_asignaturas, grafico_combinado_por_ciudad, generar_graficos_edad_calificacion_genero
from scripts.generar_pdf import generar_pdf 


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


    while True:
        print("\n=== Menú Principal ===\n")
        print("1. Ver análisis de calificaciones")
        print("2. Ver análisis de asignaturas")
        print("3. Ver exploración de datos (EDA)")
        print("4. Ver gráfica de la media de las asignaturas")
        print("5. Ver gráfica combinada por ciudad")
        print("6. Generar gráficos (Edad vs Calificación y Género)")
        print("7. Generar análisis en PDF")
        print("0. Salir")

        opcion = input("\nElige una opción: ")

        while not opcion.isdigit():  # Verifica si no es un número
            print("Error: Debes ingresar un número válido.")
            opcion = input("Elige una opción (solo números): ")

        opcion = int(opcion)

        if(opcion == 1):
            analisis_datos_calificaciones(df_calificaciones)

        elif(opcion == 2):
            analisis_datos_asignaturas(df_combinado)

        elif(opcion == 3):
            exploracion_datos(df_combinado)

        elif(opcion == 4):
            grafica_medias_asignaturas(df_calificaciones)

        elif(opcion == 5):
            grafico_combinado_por_ciudad(df_combinado)

        elif(opcion == 6):
            generar_graficos_edad_calificacion_genero(df_combinado)

        elif(opcion == 7):
            generar_pdf()

        elif (opcion == 0):
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Error: Debes ingresar un número válido.")

        input("\nPresiona Enter para volver al menú...")  # Pausa para continuar




if __name__ == "__main__":
    main()