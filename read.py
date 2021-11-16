import cv2 as cv

"""
Open image
"""
#img = cv.imread('Photos/cat_large.jpg')

#cv.imshow('Cat', img)

"""
Reading Video
"""
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.waitKey(0)

