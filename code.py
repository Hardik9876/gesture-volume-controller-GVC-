
import cv2
import mediapipe as mp

import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
   # print(result.multi_hand_landmarks)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            for id , lm in enumerate(hand.landmark):
               # print(id,lm)
                h,w,c = img.shape
                cx,cy = int(lm.x*w) , int(lm.y*h)
                print(cx,cy)
                if(id==0):
                    cv2.circle(img,(cx,cy),23,(255,0,12),cv2.FILLED)

            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)

    Ctime = time.time()
    fps = 1 / (Ctime - pTime)
    pTime = cTime
 #   fps = int(fps)

    fps = str(fps)


    cv2.putText(img, fps[0:3], (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)

    cv2.imshow("image", img)
    cv2.waitKey(1)
