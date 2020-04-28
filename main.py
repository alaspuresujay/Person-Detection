import cv2
import time
import sendmail
import os

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
sendmail.setEmail("Sender_Address", "Sender_Password", "Receiver_Address")

flag = True
prevnum = None
image_name = []

while True:
    t = time.localtime()
    t = t.tm_sec

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    num = len(faces)
    b, g, r = img[30, 218]
    r, b, g = int(r), int(b), int(g)
    print("detected-", num, len(image_name), flag)

    if (r + g + b) > 600:
        cv2.putText(img, str(time.strftime("%a %b %d,%Y  %H:%M:%S", time.localtime())), (50, 50), 2, 0.8, (0, 0, 0), 1, cv2.LINE_AA)
    else:
        cv2.putText(img, str(time.strftime("%a %b %d,%Y  %H:%M:%S", time.localtime())), (50, 50), 2, 0.8, (255, 255, 255), 1, cv2.LINE_AA)

    if num > 0 and t % 5 == 0 and flag:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            roi_color = img[y:y + h, x:x + w]
            cv2.imwrite('faces_detected.jpg', img)
            cv2.imwrite('images/' + str(x) + str(y) + '_faces.jpg', roi_color)
            image_name.append('images/' + str(x) + str(y) + '_faces.jpg')
        print(len(image_name), image_name)
        prevnum = num
        sendmail.sendEmail(image_name, num, 'faces_detected.jpg')
        flag = False
        # time.sleep(1)

    if num != prevnum:
        # print(flag)
        image_name.clear()
        flag = True

    cv2.imshow('frame', img)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
