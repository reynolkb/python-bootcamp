# ---------------------------------------- Working with images in Python ----------------------------------------
# from PIL import Image
# mac = Image.open('example.jpg')
# print(type(mac))
# print(mac.size)
# print(mac.filename)
# print(mac.format_description)

# mac.crop((0,0,100,100))
# pencils = Image.open('pencils.jpg')
# print(pencils.size)

# ---------------------------------------- Image Exercises ----------------------------------------
from PIL import Image
words = Image.open('word_matrix.png')
mask = Image.open('mask.png')

mask = mask.resize((1015,599))
mask.putalpha(200)
words.paste(mask,(0,0),mask)
print(words)