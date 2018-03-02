# 计算图像的熵
import cv2 as cv
import numpy as np
import util
import math

def entropy(path):

    img = cv.imread(path)

    gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    hist = np.zeros(256)
    for gray in range(256):
        look_for = gray_img == gray
        hist[gray] = gray_img[look_for].size

    hist_new = np.delete(hist,np.where(hist == 0))

    p_hist = hist_new / sum(hist_new)       #频率矩阵

    h = 0 - np.sum(p_hist * np.log2(p_hist))

    return h

print(entropy("lena.jpg"))
print(entropy("1.png"))
print(entropy("2.jpg"))
print(entropy("3.jpg"))