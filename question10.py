import cv2

img = cv2.imread("low_contrast_imgs/ex3.jpg")
h, w, c = img.shape
img = cv2.resize(img, (int(w * 0.4), int(h * 0.4))) # adjust the size according to the image dys

b, g, r = cv2.split(img)

eq_b = cv2.equalizeHist(b)
eq_g = cv2.equalizeHist(g)
eq_r = cv2.equalizeHist(r)

hist_eq = cv2.merge([eq_b, eq_g, eq_r])


cv2.imshow("original", img)
cv2.imshow("histogram eq image", hist_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()