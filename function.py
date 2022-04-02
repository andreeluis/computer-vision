import numpy
import cv2

def SetImage(image):
    return cv2.imread(image)

def ShowImage(img):
    cv2.imshow('imagem', img)
    cv2.waitKey()

def GrayScale(img):
    height, width, a = img.shape                    # Armazena altura e largura da imagem

    for x in range(height):
        for y in range(width):
            b, g, r = img[x,y]                      # Armazena a cor do pixel atual
            gray = (int(b) + int(g) + int(r)) // 3  # Calcula media entre 'BGR' e encontra o cinza
            img[x,y] = [gray]                       # Troca a cor do pixel pelo tom de cinza calculado

def Flip(img, direction):
    height, width, a = img.shape
    flipimg = img.copy()                            # Cria uma copia da imagem original

    if direction in "Xx":                           # Sequencia de If's para analizar a escolha do user
        for x in range(height):
            for y in range(width):
                img[x,y] = flipimg[-x,y]
    if direction in "Yy":
        for x in range(height):
            for y in range(width):
                img[x,y] = flipimg[x,-y]
    if direction == "both":
        for x in range(height):
            for y in range(width):
                img[x,y] = flipimg[-x,-y]

def Negative(img):
    height, width, a = img.shape                            
    for x in range(height):
        for y in range(width):
            b, g, r = img[x,y]                              # Armazena a cor do pixel atual
            img[x,y] = [(255 - b), (255 - g), (255 - r)]    # Troca a cor pelo tom de negativo

def Threshold(img, thresh = 127):
    height, width, a = img.shape
    for x in range(height):
        for y in range(width):
            b, g, r = img[x,y]                              # Armazena a cor do pixel atual
            gray = (int(b) + int(g) + int(r)) // 3          # Calcula media entre 'BGR' e encontra o cinza
            if (gray > thresh):                             # 'Arredonda' o cinza para preto ou branco
                img[x,y] = [255]
            else:
                img[x,y] = [0]