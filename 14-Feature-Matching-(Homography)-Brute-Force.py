# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2
import matplotlib.pyplot as plt

template = cv2.imread('./www/feature-matching-template.jpg', 0)
img = cv2.imread('./www/feature-matching-image.jpg', 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(template, None)
kp2, des2 = orb.detectAndCompute(img, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

img3 = cv2.drawMatches(template, kp1, img, kp2, matches[:10], None, flags=2)
plt.imshow(img3)
plt.show()
