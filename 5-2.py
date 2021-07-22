import cv2
import numpy as np


def show_pic(img, t=0):
    cv2.imshow('pic', img)
    cv2.waitKey()


image = cv2.imread('rubix.png')

image_2 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(image_2)

lower_Cyan = np.array([80, 35, 140])
upper_Cyan = np.array([100, 255, 255])

lower_yellow = np.array([20, 35, 140])
upper_yellow = np.array([40, 255, 255])

lower_magneta = np.array([140, 35, 140])
upper_magneta = np.array([160, 255, 255])

mask_C = cv2.inRange(image_2, lower_Cyan, upper_Cyan)
mask_Y = cv2.inRange(image_2, lower_yellow, upper_yellow)
mask_M = cv2.inRange(image_2, lower_magneta, upper_magneta)

result = cv2.bitwise_and(image, image, mask=mask_C)
result = cv2.bitwise_and(result, result, mask=mask_Y)
result = cv2.bitwise_and(result, result, mask=mask_M)

image[mask_C>0]=(0,0,255)
image[mask_Y>0]=(255,0,0)
image[mask_M>0]=(0,255,0)

show_pic(image)
