from ultralytics import YOLO
import cv2
import math
import cvzone

model = YOLO("../weights/model_train_v2.pt")

classNames = ["Green", "Red", "Yellow"]

cap = cv2.VideoCapture("../data/semaforos2.mp4")

while True:
    success, img = cap.read()
    results = model(img, stream = True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Boxes
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

            # Confidence
            conf = math.ceil(box.conf[0] * 100) / 100

            # Class
            cls = int(box.cls[0])

            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)