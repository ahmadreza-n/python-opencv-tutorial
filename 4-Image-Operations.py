# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2

img = cv2.imread('./www/watch.jpg', cv2.IMREAD_COLOR)

px = img[55, 55]
print(px)


# %%
roi = img[100:150, 100:150]
print(roi)


# %%
img[100:150, 100:150] = [255, 255, 255]
print(roi)


# %%
print(img.shape)
print(img.size)
print(img.dtype)


# %%
watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
