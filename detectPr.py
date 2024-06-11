import cv2

# Dirección IP y puerto del servidor de video de DroidCam
url = 'http://192.168.1.7:4747/video'

cap = cv2.VideoCapture(url)

Classif = cv2.CascadeClassifier('cascade.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo recibir el frame (streaming terminado?). Saliendo ...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    toy = Classif.detectMultiScale(gray,
                                   scaleFactor=5,
                                   minNeighbors=91,
                                   minSize=(170,78))

    for (x, y, w, h) in toy:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'RedBull', (x, y-10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:  # La tecla Esc para salir
        break

cap.release()
cv2.destroyAllWindows()
