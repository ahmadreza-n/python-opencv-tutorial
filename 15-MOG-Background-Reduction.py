# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2

cap = cv2.VideoCapture('./www/people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
  _, frame = cap.read()

  fgmask = fgbg.apply(frame)

  cv2.imshow('Original', frame)
  cv2.imshow('fg', fgmask)

  k = cv2.waitKey(5) & 0xff
  if k == 27:
    break

cap.release()
cv2.destroyAllWindows()
