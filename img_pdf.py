import os
import img2pdf

imagenes_jpg_png = []

for archivo in os.listdir('./'): 
    if archivo.endswith(".jpg") or archivo.endswith(".png"):
        imagenes_jpg_png.append(archivo)


with open("documento.pdf", "wb") as documento:
	documento.write(img2pdf.convert(imagenes_jpg_png))
