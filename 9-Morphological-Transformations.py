# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
  _, frame = cap.read()
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  lower_red = np.array([0, 100, 100])
  upper_red = np.array([179, 255, 255])

  mask = cv2.inRange(hsv, lower_red, upper_red)
  res = cv2.bitwise_and(frame, frame, mask=mask)

  kernel = np.ones((5, 5), np.uint8)

  erosion = cv2.erode(mask, kernel, iterations=1)
  erosionRes = cv2.bitwise_and(frame, frame, mask=erosion)

  dilation = cv2.dilate(mask, kernel, iterations=1)
  dilationRes = cv2.bitwise_and(frame, frame, mask=dilation)

  opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
  openingRes = cv2.bitwise_and(frame, frame, mask=opening)

  closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
  closingRes = cv2.bitwise_and(frame, frame, mask=closing)

  cv2.imshow('Frame', frame)
  cv2.imshow('Res', res)
  cv2.imshow('Maks', mask)
  cv2.imshow('Erosion', erosion)
  cv2.imshow('Erosion res', erosionRes)
  cv2.imshow('Dilation', dilation)
  cv2.imshow('Dilation res', dilationRes)
  cv2.imshow('Opening', opening)
  cv2.imshow('Opening res', openingRes)
  cv2.imshow('Closing', closing)
  cv2.imshow('Closing res', closingRes)

  k = cv2.waitKey(5) & 0xFF
  if k == 27:
    break

cv2.destroyAllWindows()
cap.release()
