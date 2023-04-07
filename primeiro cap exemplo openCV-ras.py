# testando o primeiro exemplo do livro "Introdução a Visão Computacional com Python e OpenCV"
# onde testamos as funções basicas da biblioteca numa imagem (que nesse caso usei a logo do opencv)

import cv2

# Leitura da imagem com a função imread()
imagem = cv2.imread('OpenCV_Logo.png')

print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem

print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem

print('Qtde de canais: ', end='')
print(imagem.shape[2])

# Mostra a imagem com a função imshow
cv2.imshow("Nome da janela", imagem)
cv2.waitKey() #espera pressionar qualquer tecla para continuar o programa

# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", imagem)
