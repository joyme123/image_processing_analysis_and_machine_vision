import cv2 as cv
import numpy as np
import util

img = cv.imread("lena.jpg")

yiq = np.zeros(img.shape)

hsi = np.zeros(img.shape)

bgr1 = np.zeros(img.shape)

bgr2 = np.zeros(img.shape)

# RGB转到YIQ的公式
# OPENCV是BGR的顺序
# Y=0.299R+0.587G+0.114B
# I=0.596R-0.274G-0.322B
# Q=0.211R-0.523G+0.312B

for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        r = img[row][col][2]
        g = img[row][col][1]
        b = img[row][col][0]
        yiq[row][col][0] = (0.299*r + 0.587*g + 0.114*b) / 255
        yiq[row][col][1] = (0.596*r - 0.275*g - 0.321*b) / 255
        yiq[row][col][2] = (0.212*r - 0.523*g + 0.311*b) / 255
        hsi_item = util.rgb2hsi(r,g,b)
        hsi[row][col][0] = hsi_item[0]
        hsi[row][col][1] = hsi_item[1]
        hsi[row][col][2] = hsi_item[2]


# YIQ加噪声
# HSI加噪声
noise_level = 0.05
for row in range(img.shape[0]):
    for col in range(0,img.shape[1],2):
        if img.shape[1] - col + 1 < 1:
            break
        (yiq[row][col][0],yiq[row][col+1][0]) = util.gaussianNoise(yiq[row][col][0],yiq[row][col+1][0],1,noise_level)
        (yiq[row][col][1],yiq[row][col+1][1]) = util.gaussianNoise(yiq[row][col][1],yiq[row][col+1][1],0.596,0.596*noise_level)
        (yiq[row][col][2],yiq[row][col+1][2]) = util.gaussianNoise(yiq[row][col][2],yiq[row][col+1][2],0.523,0.523*noise_level)

        (hsi[row][col][0],hsi[row][col+1][0]) = util.gaussianNoise(hsi[row][col][0],hsi[row][col+1][0],360,360*noise_level)
        (hsi[row][col][1],hsi[row][col+1][1]) = util.gaussianNoise(hsi[row][col][1],hsi[row][col+1][1],1,noise_level)
        (hsi[row][col][2],hsi[row][col+1][2]) = util.gaussianNoise(hsi[row][col][2],hsi[row][col+1][2],1,noise_level)

        rgb1_tmp1 = util.yiq2rgb(yiq[row][col][0],yiq[row][col][1],yiq[row][col][2])
        rgb1_tmp2 = util.yiq2rgb(yiq[row][col+1][0],yiq[row][col+1][1],yiq[row][col+1][2])

        bgr1[row][col][2] = rgb1_tmp1[0]
        bgr1[row][col][1] = rgb1_tmp1[1]
        bgr1[row][col][0] = rgb1_tmp1[2]

        bgr1[row][col+1][2] = rgb1_tmp2[0]
        bgr1[row][col+1][1] = rgb1_tmp2[1]
        bgr1[row][col+1][0] = rgb1_tmp2[2]


        rgb2_tmp1 = util.hsi2rgb(hsi[row][col][0],hsi[row][col][1],hsi[row][col][2])
        rgb2_tmp2 = util.hsi2rgb(hsi[row][col+1][0],hsi[row][col+1][1],hsi[row][col+1][2])

        # print(rgb2_tmp1)

        bgr2[row][col][2] = rgb2_tmp1[0]
        bgr2[row][col][1] = rgb2_tmp1[1]
        bgr2[row][col][0] = rgb2_tmp1[2]

        bgr2[row][col+1][2] = rgb2_tmp2[0]
        bgr2[row][col+1][1] = rgb2_tmp2[1]
        bgr2[row][col+1][0] = rgb2_tmp2[2]

# print(img)
print(img)
print(bgr1)
# print(bgr2)

cv.imshow("source",img)
cv.imshow("yiqnoise",bgr1)
cv.imshow("hsinoise",bgr2)

cv.waitKey(0)
cv.destroyAllWindows()