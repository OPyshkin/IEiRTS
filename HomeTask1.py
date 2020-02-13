import numpy as np
import pandas
import cv2
import PIL
import keras
import tensorflow

img = cv2.imread('gay.jpg')
n = 1
fin = np.zeros((len(img)-2, len(img[0])-2))
sobolx = [[-1,0,1],[-2,0,2],[-1,0,1]]
for i in range(1,len(img)-1):
    for j in range(1,len(img[i])-1):
        temp = [[img[i-1][j-1][n],img[i-1][j-0][n],img[i-1][j+1][n]],
                        [img[i+0][j-1][n],img[i+0][j-0][n],img[i+0][j+1][n]],
                        [img[i+1][j-1][n],img[i+1][j-0][n],img[i+1][j+1][n]]]
        temp1 = np.dot(sobolx,temp)
        fin[i-1][j-1] = temp1[1,1]
cv2.imshow("Hui",fin)
cv2.waitKey(0)
cv2.destroyAllWindows()
