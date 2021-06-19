import cv2 as cv
import numpy as np
from stackImages import stackImages
# imgGravity = cv.imread('gravity.jpg')

# cv.imshow('Gravity',imgGravity)
# cv.waitKey(3000)

# cap = cv.VideoCapture(r"C:\Users\Swarup\Videos\out.mp4")

# while True:
#     success, img = cap.read()
#     cv.imshow("out Video",img)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# captureWebCam = cv.VideoCapture(0)
# captureWebCam.set(3,640)
# captureWebCam.set(4,480)
# captureWebCam.set(10,100)

# while True:
#     success, img = captureWebCam.read()
#     cv.imshow("WebCam captured",img)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# bgr = cv.resize(cv.imread('DP.png'),(350,350))
# bgr = cv.resize(cv.imread('NotaGIF.jpeg'),(350,350))
# gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(bgr, (7,7),0)
# canny = cv.Canny(bgr,100,200)
# dilated = cv.dilate(canny,kernel = np.ones((3,3)),iterations=1)
# eroded = cv.erode(dilated,kernel = np.ones((3,3)),iterations=1)
# cropped = bgr[0:200,100:240]

# cv.imshow("BGR DP", bgr)
# cv.imshow("Gray DP", gray)
# cv.imshow("Blurred", blur)
# cv.imshow("Canny", canny)
# cv.imshow("Dilation",dilated)
# cv.imshow("Eroded",eroded)
# cv.imshow("Cropped",cropped)


# img = np.zeros((512,512,3))
# img[100:250,200:256] = 142,100,242
# cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,142,0),5)
# cv.rectangle(img,(0,0),(250,250),(0,0,255),10)
# cv.rectangle(img,(250,250),(343,343),(100,0,0),-1)
# cv.rectangle(img,(350, 350),(443,443),(0,00,100),cv.FILLED)
# cv.circle(img,center=(454,232),radius=30,color=(255,255,0),thickness=5)
# cv.putText(img,"Hello World!",(300,100),cv.FONT_HERSHEY_COMPLEX,1,(0,150,0)/,1)
# cv.getPerspectiveTransform, cv.warpPerspective

def empty(a):
    pass

cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",640,240)
cv.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
cv.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
cv.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
cv.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
cv.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    img = cv.imread('DP.png')
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv.getTrackbarPos("Val Max", "TrackBars")

    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv.inRange(imgHSV,lower,upper)
    imgResult = cv.bitwise_and(img,imgHSV,mask)

    imgStack = stackImages(0.5,([img,imgHSV],[mask,imgResult]))
    # cv.imshow("Stacked Images", imgStack)

    # if cv.waitKey(0) & 0xFF == ord('q'):
    #     break

