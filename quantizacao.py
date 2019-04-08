# -*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread("cameraman.png", 0)
tam = img.shape
#Fazendo a amostragem...
#Recebendo dado do usuario p/ reduzir a imagem...
print("Digite um valor p/ reduzir a imagem: ")
d = int(input())
img_Reduzida = img[::d, ::d]
#salvando a imagem reduzida em disco...
cv2.imwrite("imagemReduzida.jpg", img_Reduzida)

#alterando rezolução
print("Digite um valor p/ mudar a escala : ")
val = int(input())

tam2 = [tam[0]//val,tam[1]//val]
img_alt = np.zeros(tam2, dtype=float)

for i in range(tam2[0]):
    for j in range(tam2[1]):
        img_alt[ i ,j] = float(img[i*val, j*val])
#salvando imagem alterada...
cv2.imwrite("imagemAlterada.jpg", img_alt)


##################Quantizacao##################################

print("Digite um valor p/ alterar a escala de cinza: ")
q = int(input())
#calculando a quantidade de tons de cinza de acordo
#com o valor de entrada pelo usuario...
img = np.uint8(img/q)*q
#mostra a imagem quantizada
cv2.imshow('Imagem Quantizada',img)


#cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imwrite("imagemQuantizada.jpg", img)
