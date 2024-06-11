from ultralytics import YOLO
import cv2

# Dirección IP y puerto del servidor de video de DroidCam
url = 'http://192.168.1.7:4747/video'

# Ajusta la resolución para reducir la latencia
cap = cv2.VideoCapture(url)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Ancho en píxeles
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Alto en píxeles
cap.set(cv2.CAP_PROP_FPS, 30)  # Intentar ajustar a 30 FPS

model = YOLO('best.pt')

while cap.isOpened():
    success, frame = cap.read()

    if success:
        # Procesamiento de inferencia con YOLO
        results = model(frame, conf=0.5)
        annotated_frame = results[0].plot()

        # Mostrar el frame anotado
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        print("No se pudo recibir el frame (streaming terminado?). Saliendo ...")
        break

cap.release()
cv2.destroyAllWindows()
