import fitz # PyMuPDF
from PIL import Image
import os

def convert_pdf_to_grayscale(input_pdf, output_pdf):
    # Abrir PDF de entrada
    pdf_document = fitz.open(input_pdf)

    # Lista para almacenar las imagenes PDF
    imagenes = []

    # Itena sobre cada pagina PDF
    for page_num in range(pdf_document.page_count):
        # Cargar pagina actual
        page = pdf_document.load_page(page_num)
        # convertir la pagina a una escala de grises
        pix = page.get_pixmap(colorspace=fitz.csGRAY)
        # Convertir la imagen en un objeto PIL
        img = Image.frombytes("L", [pix.width, pix.height], pix.samples)
        # Guarda la imagen en la lista
        imagenes.append(img)

    imagenes[0].save(output_pdf, save_all=True, append_images=imagenes[1:])

    print("Proceso exitoso")
    print("Por favor de enter para continuar")


# Especifica el archivo PDF de entrada
input_pdf = r"C:\Users\luis.murcia\OneDrive - Autonal SAS\Escritorio\Pruebas py\PDF COLOR\fichero (15) (1) (1).PDF"
# Especifica el archivo PDF de salida
output_pdf = r"C:\Users\luis.murcia\OneDrive - Autonal SAS\Escritorio\Pruebas py\PDF ESCALA GRISES\fichero_bn.pdf"

# Llama a la función para convertir el PDF a blanco y negro
convert_pdf_to_grayscale(input_pdf, output_pdf)