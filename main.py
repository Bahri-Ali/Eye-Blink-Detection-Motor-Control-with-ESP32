


import cv2
import mediapipe as mp
import serial
import time
import numpy as np


SERIAL_PORT = '/dev/ttyUSB1'
BAUD_RATE = 115200

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # انتظار استقرار الاتصال

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)


LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]


def eye_aspect_ratio(landmarks, eye_indices):
    p1, p2, p3, p4, p5, p6 = [landmarks[i] for i in eye_indices]

    vertical1 = ((p2.x - p6.x)**2 + (p2.y - p6.y)**2)**0.5
    vertical2 = ((p3.x - p5.x)**2 + (p3.y - p5.y)**2)**0.5
    horizontal = ((p1.x - p4.x)**2 + (p1.y - p4.y)**2)**0.5

    return (vertical1 + vertical2) / (2.0 * horizontal)


def draw_eye(frame, landmarks, eye_indices, color):
    h, w, _ = frame.shape
    points = []

    for idx in eye_indices:
        x = int(landmarks[idx].x * w)
        y = int(landmarks[idx].y * h)
        points.append((x, y))

    points = np.array(points, dtype=np.int32)
    cv2.polylines(frame, [points], True, color, 2)



cap = cv2.VideoCapture(0)

last_state = None 


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

        left_ear = eye_aspect_ratio(landmarks, LEFT_EYE)
        right_ear = eye_aspect_ratio(landmarks, RIGHT_EYE)
        ear_avg = (left_ear + right_ear) / 2.0

        if ear_avg < 0.25:
            state = '0'   
            color = (0, 0, 255)  
        else:
            state = '1'  
            color = (0, 255, 0) 

        if state != last_state:
            ser.write((state + '\n').encode())
            last_state = state

        draw_eye(frame, landmarks, LEFT_EYE, color)
        draw_eye(frame, landmarks, RIGHT_EYE, color)

        cv2.putText(frame, f'EAR: {ear_avg:.2f}', (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow('Eye Tracking', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
ser.close()