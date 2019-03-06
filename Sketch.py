import cv2
import numpy as np

def sketch (image):
    #converter a imagem em escala de cinza

    imagemcinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #usando o filtro gaussiando de borragem para limpar a imagem

    imagemcinzablur = cv2.GaussianBlur(imagemcinza, (5,5), 0)

    #Extrair as bordas

    canny_borda = cv2.Canny(imagemcinzablur, 40, 50)

    ret, mask = cv2.threshold(canny_borda, 200, 255, cv2.THRESH_BINARY_INV)
    return mask


webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    cv2.imshow('Camera', sketch(frame))
    if cv2.waitKey(1) == 27: #Numero da Tecla Esc para sair
        break

webcam.release()
cv2.destroyAllWindows()