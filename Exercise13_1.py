import numpy as np 
import cv2

c = np.load('calib.npy', allow_pickle=True).item()


# Use the fully illuminated image (0) and the dark image (1)

im_on = cv2.imread('sequence/frames0_0.png', cv2.IMREAD_GRAYSCALE).astype(float)
im_off = cv2.imread('sequence/frames0_1.png', cv2.IMREAD_GRAYSCALE).astype(float)

mask = (im_on - im_off) > 10.0

# 1. How would you find the intrinsics?

# 2. What about the extrinsics?