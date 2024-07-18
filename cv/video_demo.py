import cv2

video = cv2.VideoCapture(r"C:\Users\Atharv\Downloads\SampleVideo_1280x720_1mb.mp4")
while True:
    status, frame = video.read()
    # print(status, frame)
    if not status:
        break
    cv2.imshow('video frame', frame)
    if cv2.waitKey(10) == 27:
        break
video.release()
cv2.destroyAllWindows()
