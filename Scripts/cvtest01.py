import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread(r'images\j032_1.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img2)
plt.show()

# cv2.namedWindow("test",cv2.WINDOW_NORMAL)
# cv2.imshow("test",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
