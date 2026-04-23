#Exercise 10.1 
# Sift features and descriptors to match points between images, step for image stitching. 


#Find sift keypoints (kp1, kp2) and compute their descriptors (des1, des2) 
import cv2
import numpy as np

img1 = cv2.imread('im1.jpg', cv2.IMREAD_GRAYSCALE)          # queryImage
img2 = cv2.imread('im2.jpg', cv2.IMREAD_GRAYSCALE) # trainImage

sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# crossCheck=True ensures that matches are consistent in both directions
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

# Match descriptors.
matches = bf.match(des1, des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Visualize the matches 
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('Matches', img3)
cv2.waitKey(0)

