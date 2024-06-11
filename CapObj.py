import cv2
import numpy as np
import imutils
import os

Datos = 'n'
if not os.path.exists(Datos):
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos)

# Dirección IP y puerto del servidor de video de DroidCam
url = 'http://192.168.1.7:4747/video'

# Usamos la URL en lugar del índice de la cámara
cap = cv2.VideoCapture(url)

x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo recibir el frame (streaming terminado?). Saliendo ...")
        break

    imAux = frame.copy()
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    objeto = imAux[y1:y2, x1:x2]
    objeto = imutils.resize(objeto, width=50)

    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite(Datos + '/objeto_{}.jpg'.format(count), objeto)
        print('Imagen guardada:' + '/objeto_{}.jpg'.format(count))
        count += 1
    if k == 27:
        break

    cv2.imshow('frame', frame)
    cv2.imshow('objeto', objeto)

cap.release()
cv2.destroyAllWindows()
