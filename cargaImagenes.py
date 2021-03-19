import cv2
import numpy as np

#Cargar imagen a color
IRGB=cv2.imread('009.jpg')
print(IRGB)
print(IRGB.shape)
print ('líneas agregadas a rama 2')
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print (IGS)
print (IGS.shape)
cv2.imwrite('009GS.jpg',IGS)



