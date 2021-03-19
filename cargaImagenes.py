import cv2
import numpy as np

#Cargar imagen a color
IRGB=cv2.imread('009.jpg')
print(IRGB)
print(IRGB.shape)
#Print líneas agragadas a rama 2
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print (IGS)
print (IGS.shape)
print ('Modificación en la rama main')
print(len(IRGB))


