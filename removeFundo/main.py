from rembg import remove
from PIL import Image
# Importar imagem original
img = Image.open('Imagem do WhatsApp de 2024-01-24 à(s) 10.55.54_03e19b26.jpg')
# Remove fundo da imagem
img_without_back = remove(img)
# Sala imagem sem fundo
img_without_back.save('img_without_back03.png')