import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data/the_ambassadors.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 6))
plt.imshow(img_rgb)

src_points = np.array(plt.ginput(4, timeout=0), dtype=np.float32)
plt.close()

print(src_points.tolist())
