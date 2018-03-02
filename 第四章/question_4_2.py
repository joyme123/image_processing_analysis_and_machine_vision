import cv2 as cv
import numpy as np

mat = cv.imread("lena.jpg")
mat = cv.cvtColor(mat,cv.COLOR_BGR2GRAY)
max_row = mat.shape[0]
max_col = mat.shape[1]

result = np.zeros([256,256])

#关系r是南、或东、或同一
for row in range(mat.shape[0]):
    for col in range(mat.shape[1]):
        p1 = mat[row][col]      #同一
        result[p1][p1] += 1

        if row+1 < max_row:
            ps = mat[row+1][col]  #南点
            result[p1][ps] += 1

        if col+1 < max_col:
            pe = mat[row][col+1]  #东点
            result[p1][pe] += 1

print(result)