from flask import Flask, render_template, Response
import cv2
import logging
from ultralytics import YOLO

app = Flask(__name__)

# Configura el logger
logging.basicConfig(level=logging.DEBUG)

# Carga el modelo YOLO
model = YOLO('best.pt')

def generate_frames():
    cap = cv2.VideoCapture('http://192.168.1.7:4747/video')
    logging.debug("Entrando a generate_frames")

    while cap.isOpened():
        success, frame = cap.read()

        if success:
            # Realiza inferencia con el modelo YOLO
            results = model(frame, conf=0.25)
            annotated_frame = results[0].plot()

            # Codifica el frame anotado para la transmisión
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        else:
            logging.error("Error al leer el frame")
            break

    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
