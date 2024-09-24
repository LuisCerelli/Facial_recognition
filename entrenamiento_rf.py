import cv2
import os
import numpy as np

dataPath = '/Users/luisalbertocerelli/Desktop/00-Todo/03_Python_practicas/08_facial_recognition/data'
peopleList = os.listdir(dataPath)
print('Listado de personal: ', peopleList)

labels = []
facesData = []
label = 0

for nameDir in peopleList:
    personPath = os.path.join(dataPath, nameDir)  # Obtener la ruta completa
    # Verificar si es un directorio y no un archivo como .DS_Store
    if os.path.isdir(personPath):
        print(f"Leyendo las imágenes de {nameDir}")

        for fileName in os.listdir(personPath):
            print(f"Procesando archivo: {fileName}")
            imagePath = os.path.join(personPath, fileName)
            image = cv2.imread(imagePath, 0)  # Leer imagen en escala de grises
            if image is None:
                print(f"Error al leer la imagen {fileName}, ignorando...")
                continue
            
            facesData.append(image)
            labels.append(label)

        label += 1  # Pasar al siguiente label para la siguiente persona
    else:
        print(f"Ignorando archivo: {nameDir}")

print('labels= ', labels)  
print('Número de etiquetas 0: ', np.count_nonzero(np.array(labels) == 0))
print('Número de etiquetas 1: ', np.count_nonzero(np.array(labels) == 1))

#metodos de entrenamiento, 1)EigenFace, 2)FisherFace 3)LBPHFace

#face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Entrenando el reconocedor de rostros
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

#Almacenando el modelo obtenido
#face_recognizer.write('modeloEigenFace.xml')
#face_recognizer.write('modeloFisherFace.xml')
face_recognizer.write('modeloLBPHFace.xml')

print('Modelo Almacenado...')