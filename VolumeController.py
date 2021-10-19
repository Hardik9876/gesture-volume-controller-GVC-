import time
import math
import cv2
import numpy as np
import mediapipe
import handtracking_module as ht
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

width = 640
height = 480
pTime = 0

cap = cv2.VideoCapture(0)
cap.set(3, width)  # 3 is for width
cap.set(4, height)  # 4 is for height

detector = ht.handDetector(detection_confidence=0.75)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()  # range is (-65.25 to 0)   0 means 100 vol and -65.25 means 0 vol

maxVolume = volRange[1]
minVolume = volRange[0]

vol = 0
volBar=400
volPercentage=0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    if (len(lmlist) != 0):
        # print(lmlist[4],lmlist[8])
        x1, y1 = lmlist[4][1], lmlist[4][2]  # for thumb tip
        x2, y2 = lmlist[8][1], lmlist[8][2]  # for index finger tip

        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2  # //2 gives floor value

        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)

        # or approx hand range was 50 to 275
        # and volume range was -65 to 0

        vol = np.interp(length, [50, 275], [-65, 0])  # this converts our 50 to 300 range into -65 to 0 range
        volBar =np.interp(length,[50,275],[400,150])
        volPercentage = np.interp(length, [50, 275], [0, 100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if (length < 50):
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'Vol:{int(volPercentage)}%', (40, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

    cv2.imshow("image", img)
    cv2.waitKey(1)
