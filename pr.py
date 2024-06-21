import cv2

url = 'http://192.168.1.7:4747/video'

cap = cv2.VideoCapture(url)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

if not cap.isOpened():
    print("Error: No se pudo abrir el stream de video")
else:
    while cap.isOpened():
        success, frame = cap.read()
        if success:
            cv2.imshow("Test Video Feed", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            print("No se pudo recibir el frame (streaming terminado?). Saliendo ...")
            break

    cap.release()
    cv2.destroyAllWindows()
