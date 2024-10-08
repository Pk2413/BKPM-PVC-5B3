import os
import cv2
import matplotlib.pyplot as plt

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, 'gambar', 'foto.jpg')


image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

equlized_image =cv2.equalizeHist(image)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Gambar Asli')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Gambar Equalization')
plt.imshow(equlized_image, cmap='gray')
plt.axis('off')

plt.show()