import cv2
import sys

# Load test image 
image_path = 'week06_data/TestIm1.png'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Could not locate data frame at {image_path}")
    sys.exit()

# Create standard window frame layout
window_name = 'Canny Edge Tuning Window'
cv2.namedWindow(window_name)

# Dummy callback function required by cv2.createTrackbar
def nothing(x):
    pass

# Create real-time UI sliders initialized to your notes parameters
cv2.createTrackbar('Lower t1', window_name, 100, 255, nothing)
cv2.createTrackbar('Upper t2', window_name, 200, 255, nothing)

print("Tuning Dashboard Active. Adjust trackbars. Press 'q' or 'ESC' to exit.")

while True:
    # Read live trackbar values from user position adjustments
    t1 = cv2.getTrackbarPos('Lower t1', window_name)
    t2 = cv2.getTrackbarPos('Upper t2', window_name)
    
    # Run the core openCV optimization pipeline engine
    edges = cv2.Canny(img, threshold1=t1, threshold2=t2)
    
    # Render updated frame matrix out
    cv2.imshow(window_name, edges)
    
    # Intercept kill keys
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

cv2.destroyAllWindows()