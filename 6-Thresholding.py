# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2

img = cv2.imread('./www/bookpage.jpg')
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
retval2, grayTh = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled, 255,
                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval3, otsu = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('Original', img)
cv2.imshow('Gray scaled', grayscaled)
cv2.imshow('Binary threshold', threshold)
cv2.imshow('Binary threshold on gray scaled', grayTh)
cv2.imshow('Adaptive threshold gaussian', gaus)
cv2.imshow('Binary threshold + Otsu threshold', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
