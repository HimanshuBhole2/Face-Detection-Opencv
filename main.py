import cv2
print('HO')

cascicade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    # Here is our image will be read
    ret,img = cap.read()
    print(ret)
    g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    f = cascicade_face.detectMultiScale(g,1.3,5)

    # Here our face detection square code

    for(x,y,w,h) in f:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,225),4)



    cv2.imshow('img',img)

    k = cv2.waitKey(30) & 0Xff

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()