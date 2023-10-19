from PIL import Image, ImageEnhance
image_path = "C:\Users\augusto.soares\Desktop\photo_2023-07-24_11-58-52.jpg"

image = Image.open(image_path)

ajuste_brilho = lambda imagem, fatorBrilho: ImageEnhance.Brightness(imagem).enhance(fatorBrilho, lambda: "Imagem alterada.")

ajuste_brilho(image, 0.9)