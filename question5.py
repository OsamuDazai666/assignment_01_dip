import cv2
import matplotlib.pyplot as plt 
import numpy as np

# img = cv2.imread("sample_images/red.png")
# img = cv2.imread("sample_images/blue.png")
# img = cv2.imread("sample_images/green.png")
img = cv2.imread("sample_images/white.png")
cv2.imshow("org img", img)


bgr_planes = cv2.split(img)
histSize = 255
histRange = (0, 256)
accumulate = False

b_hist = np.uint64(cv2.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate))
g_hist = np.uint64(cv2.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate))
r_hist = np.uint64(cv2.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate))

# saving histogram of each color 
plt.plot(np.arange(0, 255), b_hist, color='b')
plt.savefig('hist/b_histogram.png')
plt.clf()

plt.plot(np.arange(0, 255), r_hist, color='r')
plt.savefig('hist/r_histogram.png')
plt.clf()

plt.plot(np.arange(0, 255), g_hist, color='g')
plt.savefig('hist/g_histogram.png')
plt.clf()

# check which color
h, w = r_hist.shape
r_check = r_hist >=  (h * w) 
g_check = g_hist >=  (h * w)
b_check = b_hist >=  (h * w)

red_at_high_intensity = False
green_at_high_intensity = False
blue_at_high_intensity = False
for i in range(200, 255):
    if r_check[i] == True:
        red_at_high_intensity = True

    if g_check[i] == True:
        green_at_high_intensity = True

    if b_check[i] == True:
        blue_at_high_intensity = True


if red_at_high_intensity and green_at_high_intensity and blue_at_high_intensity:
    print("White Color")

elif red_at_high_intensity:
    print("Red Color")

elif green_at_high_intensity:
    print("Green Color")

elif blue_at_high_intensity:
    print("Blue Color")


cv2.waitKey(0)
cv2.destroyAllWindows()