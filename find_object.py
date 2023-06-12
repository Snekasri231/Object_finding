import cv2
import numpy as np
import time

cap = cv2.VideoCapture(1)  # Capture the video

while True:
    ret, frame = cap.read()
    start_time = time.time()
    while time.time() - start_time < 5:
        sky= frame[30:150, 100:250]
    hsv = cv2.cvtColor(sky, cv2.COLOR_BGR2HSV)
    lower_copper = np.array([0, 0, 0])
    upper_copper = np.array([120, 110, 240])
    mask = cv2.inRange(hsv, lower_copper, upper_copper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area = cv2.countNonZero(mask)
    density = area / (frame.shape[0] * frame.shape[1])
    # Convert the area to integer format
    area = int(area)
    print("Contour area:", area)
    if  area >=60000 and area <=75000:
        print("Part is not Working")                
    elif  area >=80000 and area <= 88000:
        print("part is Working")
    else:
        print("There is no object")
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

