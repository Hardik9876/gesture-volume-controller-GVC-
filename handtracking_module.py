
import cv2
import mediapipe as mp

import time

class handDetector():
        def __init__(self,mode = False,maxHands=2,detection_confidence=0.5,track_confidence =0.5):
            self.mode = mode
            self.maxHands = maxHands
            self.detection_confidence = detection_confidence
            self.track_confidence = track_confidence

            self.mpHands = mp.solutions.hands
            self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detection_confidence,self.track_confidence)
            self.mpDraw = mp.solutions.drawing_utils

        def findHands(self,img,draw=True):
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.result = self.hands.process(imgRGB)
            # print(result.multi_hand_landmarks)

            if self.result.multi_hand_landmarks:
                for hand in self.result.multi_hand_landmarks:
                  if draw:
                      self.mpDraw.draw_landmarks(img, hand, self.mpHands.HAND_CONNECTIONS)
            return img

        def findPosition(self,img,handNo=0 , draw =True):

            lmlist= []
            if self.result.multi_hand_landmarks:
                myhand = self.result.multi_hand_landmarks[handNo]
                for id, lm in enumerate(myhand.landmark):
                    # print(id,lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                   # print(cx, cy)
                    lmlist.append([id,cx,cy])
                    if (draw):
                        cv2.circle(img, (cx, cy), 23, (255, 0, 12), cv2.FILLED)


            return lmlist

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img =detector.findHands(img)
        list = detector.findPosition(img)
        if(len(list)!=0):
            print(list[4])
        Ctime = time.time()
        fps = 1 / (Ctime - pTime)
        pTime = cTime
        #   fps = int(fps)
        fps = str(fps)
        cv2.putText(img, fps[0:3], (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)
        cv2.imshow("image", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()


