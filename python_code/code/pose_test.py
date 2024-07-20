from pyfirmata import Arduino ,SERVO,util
from time import sleep
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

import handtrackingmodule as htm
import math

cap = cv2.VideoCapture(0)
detector = htm.handDetector()


port ='COM5'
pin_shoulder = 6
pin_elbow = 7
# pin_wrist = 12
pin_grip = 5

board = Arduino(port)

board.digital[pin_shoulder].mode=SERVO
board.digital[pin_elbow].mode=SERVO
# board.digital[pin_wrist].mode=SERVO
board.digital[pin_grip].mode=SERVO


def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    # sleep(0.015)

while True:
    with mp_pose.Pose(min_detection_confidence=0.6, min_tracking_confidence=0.6) as  pose:
        while cap.isOpened():
            # data = [000, 000]
            ret, frame = cap.read()

            img = detector.findHands(frame, draw=True)
            lmList = detector.findPosition(img, draw=False)
            if len(lmList) != 0:
                # print(lmList[4],lmList[8])
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]

                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                length = math.hypot(x2 - x1, y2 - y1)
                # print(length)

                distance = int(np.interp(length, [20, 100], [0, 180]))
                # str(distance).zfill(3)
                # distance = "%03d" % distance

                # data[0] = distance
                # print(data)

            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates
                hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                         landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                         landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                pinky = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                         landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].y]

                # Calculate angle
                angle_shoulder = int(calculate_angle(hip, shoulder, elbow))
                angle_elbow = int(calculate_angle(shoulder, elbow, wrist))
                # angle_wrist = int(calculate_angle(elbow, wrist, pinky))

                # Visualize angle
                cv2.putText(image, str(angle_elbow),
                            tuple(np.multiply(elbow, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )

                cv2.putText(image, str(angle_shoulder),
                            tuple(np.multiply(shoulder, [640, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )


                rotateservo(pin_shoulder, angle_shoulder)
                rotateservo(pin_elbow, angle_elbow)
                # rotateservo(pin_wrist, angle_wrist)
                rotateservo(pin_grip, distance)


                # arduino.sendData(data)
                print(angle_shoulder)
                print(angle_elbow)
                # print(angle_wrist)
                print(distance)

                # data.clear()

            except:
                pass

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=1, circle_radius=1),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=1, circle_radius=1)
                                      )

            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    # x=input("angle:")
    # y=input("angle2:")
    # if x=="1":
    #     for i in range(0,180):
    # rotateservo(pin1,x)
    # rotateservo(pin2,y)