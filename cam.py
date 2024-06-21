from ultralytics import YOLO
import cv2

model = YOLO('best.pt')
cap = cv2.VideoCapture('http://192.168.1.7:4747/video')

while cap.isOpened():

    succes, frame = cap.read()

    if succes:
        results = model(frame, conf = 0.25)

        annotated_frame = results[0].plot()

        cv2.imshow("YOLOV8 Inference", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    else:
        
        break

cap.release()
cv2.destroyAllWindows

