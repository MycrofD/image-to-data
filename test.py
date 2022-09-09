#test file

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 20)
y = np.sin(x)

plt.plot(x,y, marker="*", linestyle=" ", color = "red", markersize=10)
#plt.plot(x,-y, marker="s", linestyle=" ", color = "green", markersize=10)
#plt. savefig("image.png")

from skimage.feature import blob_log
from skimage.color import rgb2gray
from skimage.io import imread

img = imread("image.png")
print(img.shape)
#480,640,4
#print(img)

#star_bounding_box = [(170,226),(214,251)]
cropped = img[320:345, 160:190, :]
print(cropped)
#cropped = img[star_bounding_box[0][1]:star_bounding_box[1][1], star_bounding_box[0][0]:star_bounding_box[0][1], :]
plt.imshow(cropped)
plt.savefig("cropped_img.png")


