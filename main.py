import function

import cv2
import numpy

def main():
    img = function.SetImage("image.jpg")

    function.ShowImage(img)
    function.GrayScale(img)
    function.Flip(img, 'x')                                    # x , y or both
    function.Negative(img)
    function.Threshold(img, 50)                                 # 'Limite' para arredondamento
    function.ShowImage(img)

main()