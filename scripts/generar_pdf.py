import os
from fpdf import FPDF

def generar_pdf():
    # Pedir al usuario el nombre del gráfico
    nombre_grafico = input("Ingrese el nombre del gráfico a analizar (sin extensión): ")
    ruta_imagen = f"outputs/graficos/{nombre_grafico}.png"
    
    if not os.path.exists(ruta_imagen):
        print("El archivo no existe. Asegúrese de que el nombre es correcto y de que la imagen está en la carpeta correcta.")
        return
    
    # Pedir el título del análisis
    titulo = input("Ingrese el título del análisis: ")
    
    # Pedir el número de análisis dentro del gráfico
    while True:
        try:
            num_analisis = int(input("Ingrese la cantidad de análisis que va a hacer sobre la imagen: "))
            if num_analisis > 0:
                break
            else:
                print("Ingrese un número mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Pedir los análisis
    analisis_textos = []
    for i in range(num_analisis):
        texto = input(f"Ingrese el análisis {i+1}: ")
        analisis_textos.append(texto)

    print("\nGenerando PDF... (Puede tardar varios segundos)")
    
    # Crear el PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Agregar título
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, titulo, ln=True, align='C')
    pdf.ln(10)
    
    # Insertar imagen
    pdf.image(ruta_imagen, x=10, y=None, w=170)
    pdf.ln(10)
    
    # Agregar análisis
    pdf.set_font("Arial", size=12)
    for i, analisis in enumerate(analisis_textos, 1):
        pdf.multi_cell(0, 10, f"{i}. {analisis}")
        pdf.ln(5)
    
    # Guardar el PDF
    ruta_pdf = f"outputs/analisis/{nombre_grafico}_analisis.pdf"
    os.makedirs(os.path.dirname(ruta_pdf), exist_ok=True)
    pdf.output(ruta_pdf)
    
    print(f"PDF generado con éxito: {ruta_pdf}")
