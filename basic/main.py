import cv2

def set_image(image):
	return cv2.imread(image)

def save_image(img, name):
	cv2.imwrite(name, img)

def gray_scale(img):
	# Armazena altura e largura da imagem
	height, width, a = img.shape

	for x in range(height):
		for y in range(width):
			# Armazena a cor do pixel atual
			b, g, r = img[x,y]

			# Calcula media entre 'BGR' e encontra o cinza
			gray = (int(b) + int(g) + int(r)) // 3

			# Troca a cor do pixel pelo tom de cinza calculado
			img[x,y] = [gray]

def flip(img, direction):
	height, width, a = img.shape
	flipimg = img.copy()

	# Analisa a direção do flip
	if direction in "Xx":
		for x in range(height):
			for y in range(width):
				img[x,y] = flipimg[-x,y]
	elif direction in "Yy":
		for x in range(height):
			for y in range(width):
				img[x,y] = flipimg[x,-y]
	elif direction == "both":
		for x in range(height):
			for y in range(width):
				img[x,y] = flipimg[-x,-y]

def negative(img):
	height, width, a = img.shape

	for x in range(height):
		for y in range(width):
			# Armazena a cor do pixel atual
			b, g, r = img[x,y]

			# Troca a cor pelo tom de negativo
			img[x,y] = [(255 - b), (255 - g), (255 - r)]

def threshold(img, thresh = 127):
	height, width, a = img.shape

	for x in range(height):
		for y in range(width):
			# Armazena a cor do pixel atual
			b, g, r = img[x,y]

			# Calcula media entre 'BGR' e encontra o cinza
			gray = (int(b) + int(g) + int(r)) // 3

			# 'Arredonda' o cinza para preto ou branco
			if (gray > thresh):
				img[x,y] = [255]
			else:
				img[x,y] = [0]

img = set_image("image.png")

gray_scale(img)
flip(img, 'y')				# x , y or both
negative(img)
threshold(img)				# 'Limite' para arredondamento
save_image(img, "output.png")
