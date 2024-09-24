import cv2
import os
import imutils

personName = 'Andrea'
dataPath = '/Users/luisalbertocerelli/Desktop/00-Todo/03_Python_practicas/08_Reconocimiento_Facial/Data'
personPath = dataPath + '/' + personName
#print(personPath)
if not os.path.exists(personPath):
    print('Carpeta creada: ',personPath)
    os.makedirs(personPath)

cap = cv2.VideoCapture('Andrea.MOV')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:
    ret, frame = cap.read()
    if ret == False:break
    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    k = cv2.waitKey(1)
    if k == 27 or count >=300:
        break
