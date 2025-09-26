# MUST BE RUN AS .py SCRIPT IN ORDER TO WORK.
# WARNING: RUNNING THIS CELL WILL KILL THE KERNEL IF YOU USE JUPYTER DIRECTLY

import cv2

img = cv2.imread('dog_backpack.jpg',cv2.IMREAD_GRAYSCALE)
while True:
    # Show the image with OpenCV
    cv2.imshow('window_name',img)
    # Wait for something on keyboard to be pressed to close window.
    #if we've waited at least one 1msec AND we've pressed the escape key (27)
    if cv2.waitKey(1) & 0xFF==27:
        break

cv2.destroyAllWindows()
#    cv2.waitKey()