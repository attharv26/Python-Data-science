import cv2
video = cv2.VideoCapture(r"C:\Users\ASUS\Downloads\3997798-uhd_2160_4096_25fps.mp4")
while True:
    status, frame = video.read()
    frame = cv2.resize(frame, (0,0), fx=.20, fy=.20)
    if not status:
        break
    newframe = frame*10
    bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('video frame', frame)
    cv2.imshow('new video frame', newframe)
    cv2.imshow('b/w', bw)
    cv2.imshow('rgb', rgb)
    if cv2.waitKey(1)==27:
        break
video.release()
cv2.destroyAllWindows()