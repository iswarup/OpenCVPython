import cv2 as cv
import numpy as np
from stackImages import stackImages


def empty(a):
    pass

cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",640,240)

cv.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv.createTrackbar("Hue Max", "TrackBars", 0, 179, empty)
cv.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv.createTrackbar("Sat Max", "TrackBars", 0, 255, empty)
cv.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv.createTrackbar("Val Max", "TrackBars", 0, 255, empty)

# cv.createTrackbar("Blue Min", "TrackBars", 0, 255, empty)
# cv.createTrackbar("Blue Max", "TrackBars", 0, 255, empty)
# cv.createTrackbar("Green Min", "TrackBars", 0, 255, empty)
# cv.createTrackbar("Green Max", "TrackBars", 0, 255, empty)
# cv.createTrackbar("Red Min", "TrackBars", 0, 255, empty)
# cv.createTrackbar("Red Max", "TrackBars", 0, 255, empty)

while True:
    img = cv.imread('./images/CRT.jpeg')
    cv.putText(img, "img", (30,20),
                cv.FONT_HERSHEY_COMPLEX, 1, (0, 150, 250), 3)
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    cv.putText(imgHSV, "imgHSV", (30, 20),
               cv.FONT_HERSHEY_COMPLEX, 1, (0, 150, 250), 3)

    h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv.getTrackbarPos("Val Max", "TrackBars")

    # print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv.inRange(imgHSV,lower,upper)
    imgResult = cv.bitwise_and(img,imgHSV,mask)
    cv.putText(mask, "mask", (30, 20),
               cv.FONT_HERSHEY_COMPLEX, 1, (0, 150, 250), 3)
    cv.putText(imgResult, "imgResult", (30, 20),
               cv.FONT_HERSHEY_COMPLEX, 1, (0, 150, 250), 3)

    imgStack = stackImages(0.5,([img,imgHSV],[mask,imgResult]))
    
    # b_min = cv.getTrackbarPos("Blue Min", "TrackBars")
    # b_max = cv.getTrackbarPos("Blue Max", "TrackBars")
    # g_min = cv.getTrackbarPos("Green Min", "TrackBars")
    # g_max = cv.getTrackbarPos("Green Max", "TrackBars")
    # r_min = cv.getTrackbarPos("Red Min", "TrackBars")
    # r_max = cv.getTrackbarPos("Red Max", "TrackBars")
    
    # lower = np.array([b_min,g_min,r_min])
    # upper = np.array([b_max,g_max,r_max])
    # mask = cv.inRange(img,lower,upper)

    # imgStack = stackImages(0.5,([img,mask]))
    
    cv.imshow("Stacked Images", imgStack)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break



# img = cv.imread('./images/shapes.png')
# imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# cv.imshow("Original",img)
# cv.imshow("HSV",imgHSV)
# cv.waitKey(0)
