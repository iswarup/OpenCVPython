import cv2

# img = cv2.imread('gravity.jpg')

# cv2.imshow('Gravity',img)
# cv2.waitKey(3000)


# cap = cv2.VideoCapture(r"C:\Users\Swarup\Videos\out.mp4")

# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

captureWebCam = cv2.VideoCapture(0)
captureWebCam.set(3,640)
captureWebCam.set(4,480)
captureWebCam.set(10,100)

while True:
    success, img = captureWebCam.read()
    cv2.imshow("WebCam captured",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
