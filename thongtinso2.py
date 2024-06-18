
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('thongtinso.jpg')
def sampling(image, fs):
    return image[::fs, ::fs, :]

for fs in [2, 4, 8]:
    sampled_img = sampling(image, fs)
    s = cv2.imread(f"img{fs}.png")
    cv2.imshow(f"Sampled Image (Ts = {fs})", sampled_img)
    cv2.waitKey(0)


def change_quantization_levels(image, levels):
    new_levels = 256 // levels
    # Chia tỷ lệ pixel về số mức lượng tử hoá mới
    image = np.floor_divide(image, new_levels) * new_levels
    return image

image = cv2.imread('thongtinso.jpg', cv2.IMREAD_GRAYSCALE)

# Thay đổi mức lượng tử hóa của ảnh với số mức lượng tử hoá mới
new_levels = 4
quantized_img = change_quantization_levels(image, new_levels)

plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(quantized_img, cmap='gray')
plt.title(f'Quantized Image (Levels: {new_levels})'), plt.xticks([]), plt.yticks([])
plt.show()
