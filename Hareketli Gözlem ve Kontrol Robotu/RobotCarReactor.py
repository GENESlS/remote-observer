import cv2
import time
import pyautogui
import numpy as np
import os
#from skimage import measure
#from skimage import data, img_as_float
from skimage.metrics import structural_similarity as ssim
#from skimage.metrics import mean_squared_error
#from pushbullet import Pushbullet
from win10toast import ToastNotifier

#pb = Pushbullet('key')

toaster = ToastNotifier()

isSame = True
#x = 0
time.sleep(3)
while (isSame) :
    screen_shot_1 = pyautogui.screenshot(region=(665,347, 250, 200))
    screen_shot_1 = cv2.cvtColor(np.array(screen_shot_1), cv2.COLOR_RGB2BGR)
    gray_1 = cv2.cvtColor(screen_shot_1, cv2.COLOR_BGR2GRAY)

    time.sleep(0.5)

    screen_shot_2 = pyautogui.screenshot(region=(665,347, 250, 200))
    screen_shot_2 = cv2.cvtColor(np.array(screen_shot_2), cv2.COLOR_RGB2BGR)
    gray_2 = cv2.cvtColor(screen_shot_2, cv2.COLOR_BGR2GRAY)

    (score, diff) = ssim(gray_1, gray_2, full=True)
    diff = (diff * 255).astype("uint8")

    if (score < 0.75) :
        print("FARK VAR")
        toaster.show_toast("Sample Notification","Python is awesome!!!")
        isSame = False;
        #push = pb.push_note("RobotCar", "Detected Movement")

#difference = cv2.subtract(screen_shot_1, screen_shot_2)
#cv2.imshow("1",screen_shot_1)
#cv2.imshow("2",screen_shot_2)

#print("Structural Similarity Index: {}".format(score))
#os.system('pause')
