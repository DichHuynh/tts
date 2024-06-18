import cv2
import numpy as np

def quantization(img, delta):
    delta = 2 ** (8 - delta)
    image = np.uint8(np.floor(img.astype(float) / delta) * delta)
    return image

def sampling(img, t):
    return img[::t, ::t, :]

# Load the image
image = cv2.imread("thongtinso.jpg")

# Display original image
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# Perform sampling and quantization
for ts in [2, 4, 8]:
    sampled_img = sampling(image, ts)
    # cv2.imwrite(f"img{ts}.png", sampled_img)
    s = cv2.imread(f"img{ts}.png")
    cv2.imshow(f"Sampled Image (Ts = {ts})", sampled_img)
    cv2.waitKey(0)

for bits in [2, 4, 1]:
    quantized_img = quantization(image, bits)
    # cv2.imwrite(f"img{bits}.png", quantized_img)
    s = cv2.imread(f"img{bits}.png")
    cv2.imshow(f"Quantized Image (Bits = {bits})", quantized_img)
    cv2.waitKey(0)

cv2.destroyAllWindows()