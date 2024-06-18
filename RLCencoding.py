import cv2
import numpy as np

# read image and resize to 250x250
img = cv2.imread("ttslab2.jpg",cv2.IMREAD_GRAYSCALE)
_, img = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)
img_resize = cv2.resize(img, (250, 250))
# implement RLC encoding
encode_data = []
for i in range(img_resize.shape[0]):
    W = 0
    B = 0
    for j in range(img_resize.shape[1]):
        if img_resize[i, j] >= 127:
            W += 1
            if B > 0:
                B_binary = format(B, '08b')  # Use format for consistent length
                B_encode = B_binary + '00000000'
                encode_data.append(B_encode)
            B = 0
        else:
            B += 1
            if W > 0:
                W_binary = format(W, '08b')  # Use format for consistent length
                W_encode = W_binary + '11111111'  # Changed to 1s for decoding
                encode_data.append(W_encode)
            W=0
# print encoded data
print(encode_data)

# Giải mã dữ liệu RLC
shape = (250, 250)
def rlc_decode(encoded_data, shape):
    decoded_image = np.zeros(shape[0] * shape[1], dtype=np.uint8)
    index = 0
    for data in encoded_data:
        count = int(data[:8], 2)
        value = int(data[8:], 2)
        pixel_value = 255 if value == 255 else 0
        decoded_image[index:index + count] = pixel_value
        index += count
    return decoded_image.reshape(shape)

# Thực hiện giải mã
decoded_image = rlc_decode(encode_data, shape)
# calculate entropy
spatial_size = img_resize.size
encoded_size = len(encode_data)
entropy = spatial_size / encoded_size
print("Compression rate is:", entropy)
# Hiển thị ảnh gốc và ảnh đã giải mã
cv2.imshow("Original Image", img_resize)
cv2.imshow("Decoded Image", decoded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

rmse = np.sqrt(np.mean((img_resize - decoded_image) ** 2))
print("RMSE:", rmse)

