# testando o segundo conjunto do livro "Introdução a Visão Computacional com Python e OpenCV"
# aqui eu testo os exemplos do segundo capitulo

import cv2
imagem = cv2.imread('saida.jpg')
imagem2 = cv2.imread('OpenCV_Logo.png')

#alterei os valores para criar algo diferente do livro

#exemplo 2(o primeiro exemplo ele só iria passar pixel por pixel "pintando")
for y in range(0, imagem2.shape[0]): #percorre linhas
 for x in range(0, imagem2.shape[1]): #percorre colunas
    imagem2[y, x] = (x%56,y%140,x%156)
cv2.imshow("Imagem modificada", imagem2)
cv2.waitKey()
cv2.imwrite("ex2cap2.jpg", imagem2)
#terceiro exemplo
for y in range(0, imagem.shape[0], 1):
 for x in range(0, imagem.shape[1], 1):
    imagem[y, x] = (0,(x*y)%256,0)
cv2.imshow("Imagem modificada-2", imagem)
cv2.waitKey(0)
cv2.imwrite("ex3cap2.jpg", imagem)
#quarto e ultimo exemplo, onde pegarei a imagem alterada e farei um pequeno esquema tendo o quarto exmplo como base

for y in range(0, imagem2.shape[0], 10):
    for x in range(0, imagem2.shape[1], 60):
        imagem2[y:y+5, x: x+5] = (255,65,187)

for y in range(0, imagem2.shape[0], 47):
    for x in range(0, imagem2.shape[1], 3):
        imagem2[y:y+5, x: x+5] = (125,165,18)

cv2.imshow("Imagem modificada", imagem2)
cv2.waitKey(0)
cv2.imwrite("abstrata.jpg", imagem2)