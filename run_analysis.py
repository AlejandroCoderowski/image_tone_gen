from PIL import Image
from colormap import rgb2hex


image = ['<image_test.jpg>']

im = Image.open(image, 'r')
pix = im.load()

for ran in range(0,20):
	print(pix[ran,ran])

for ran in range(0,20):
	hex = rgb2hex(*pix[ran,ran])
	print(hex)
