import cv2
from random import randrange

cout =0
car_detection = cv2.CascadeClassifier('cars.xml')
human_detection = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_fullbody.xml")
# human_detection_upper = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_upperbody.xml")
cam = cv2.VideoCapture('street1.mp4')
# cam.open("http://192.168.1.166:8080/video")
while cam.isOpened:
    _,org = cam.read()
    capture_successful,img = cam.read()
    grey_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    positions = car_detection.detectMultiScale(grey_scale)
    print(positions)

    human_position = human_detection.detectMultiScale(grey_scale)
    print(human_position)

    # human_position_upper = human_detection_upper.detectMultiScale(grey_scale)
    # print(human_position)

    # for x,y,w,h in human_position_upper:
    #     # cv2.rectangle(img, (x,y), (x+w,x+h), (randrange(255),randrange(255),randrange(255)),2)
    #     cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)

    for x,y,w,h in human_position:
        # cv2.rectangle(img, (x,y), (x+w,x+h), (randrange(255),randrange(255),randrange(255)),2)
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)

        cv2.putText(img,"Human",(x+w-45,y-5), fontScale = 1,
        fontFace=cv2.FONT_HERSHEY_PLAIN,color=(255,255,255))

    for x,y,w,h in positions:
        cout = cout +1
        # cv2.rectangle(img, (x,y), (x+w,x+h), (randrange(255),randrange(255),randrange(255)),2)
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)

        cv2.putText(img,'vehicle',(x+w-45,y-5), fontScale = 1,
        fontFace=cv2.FONT_HERSHEY_PLAIN,color=(255,255,255))

        # cv2.putText(img,str(cout),(50,50), fontScale = 3,
        # fontFace=cv2.FONT_HERSHEY_PLAIN,color=(255,255,255))
        # cout = int(cout)
        
    cv2.imshow("Self driving",img)
    cv2.imshow("Original",org)
    cv2.waitKey(1)
print("code completed")