import cv2
video = cv2.VideoCapture(0)
if video.isOpened()==False:
    print("unable to read frame :(")
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(video.get(cv2.CAP_PROP_FPS))
print(fps)
while True :
    ret,frame = video.read()
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1)==32:
        break
video.release()