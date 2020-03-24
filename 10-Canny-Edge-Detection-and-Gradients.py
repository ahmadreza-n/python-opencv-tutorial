# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2

cap = cv2.VideoCapture(0)

while True:
  _, frame = cap.read()

  laplacian = cv2.Laplacian(frame, cv2.CV_64F)
  sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
  sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
  edges = cv2.Canny(frame, 80, 100)

  cv2.imshow('Original', frame)
  cv2.imshow('Laplacian', laplacian)
  cv2.imshow('Sobelx', sobelx)
  cv2.imshow('Sobely', sobely)
  cv2.imshow('Edges', edges)

  k = cv2.waitKey(5) & 0xFF
  if k == 27:
    break

cv2.destroyAllWindows()
cap.release()
