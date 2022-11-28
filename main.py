from Stitcher import Stitcher
import cv2
import  numpy as np
# 读取图片
img1 = cv2.imread('img2.png')
img2 = cv2.imread('img1.png')


# 图片拼接
stitcher = Stitcher()
result, vis = stitcher.stitch([img1, img2], showMatches=True)
# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
cv2.namedWindow('keypoints matches',0)
cv2.resizeWindow('keypoints matches',(img1.shape[1]+img2.shape[1],img1.shape[0]))
cv2.imshow('keypoints matches',vis)
cv2.namedWindow('result',0)
cv2.resizeWindow('result',(img1.shape[1]+img2.shape[1],img1.shape[0]))
cv2.imshow('result', result)
cv2.waitKey(0)

