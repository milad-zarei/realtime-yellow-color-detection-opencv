import cv2
import numpy as np
from PIL import Image

cap = cv2.VideoCapture(0)

# محدوده رنگ زرد در فضای HSV
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsvImage, lower_yellow, upper_yellow)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
