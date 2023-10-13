from pyzbar.pyzbar import decode
from PIL import Image

# Cargar la imagen que contiene el código QR
imagen = Image.open('D2-151-0001.jpg')

# Decodificar el código QR
codigos_qr = decode(imagen)

# Recorrer los códigos QR encontrados en la imagen
for codigo_qr in codigos_qr:
    data = codigo_qr.data.decode('utf-8')
    tipo = codigo_qr.type
    print(f'Tipo de código QR: {tipo}')
    print(f'Datos del código QR: {data}')
