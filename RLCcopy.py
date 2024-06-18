import cv2
import numpy as np

img = cv2.imread("dichhuynh.jpg", cv2.IMREAD_GRAYSCALE)
resized_image = cv2.resize(img, (265, 265))
_, binary = cv2.threshold(resized_image, 200, 255, cv2.THRESH_BINARY)

check_gray = len(np.unique(binary))
print("Mức xám của ảnh là:",check_gray)

row = 127
selected_row = binary[row, :]
print("Giá trị điểm ảnh trong dòng thứ 128:",selected_row)

# Thực hiện mã hóa RLC
def encode_RLC(image):
    encoded_data = []
    height, width = image.shape[:2]
    for i in range(height):
        count = 1
        for j in range(width - 1):
            if image[i][j] == image[i][j + 1]:
                count += 1
            else:
                encoded_data.append((count, image[i][j]))
                count = 1
        encoded_data.append((count, image[i][width - 1]))
    return encoded_data
encoded_data = encode_RLC(binary)
def encode_row(image):
    encoded_data = []
    count = 1
    for i in range(len(image) - 1):
        if image[i] == image[i + 1]:
            count += 1
        else:
            encoded_data.append((count, image[i]))
            count = 1
    encoded_data.append((count, image[-1]))
    return encoded_data
encoded_one = encode_row(selected_row)
print("Kết quả mã hóa RLC cho dòng thứ 128:", encoded_one)

# Giải mã ảnh nén
def decode_RLC(encoded_data, height, width):
    decoded_image = np.zeros((height, width), dtype=np.uint8)
    current_row = 0
    current_col = 0
    for count, pixel in encoded_data:
        for _ in range(count):
            decoded_image[current_row][current_col] = pixel
            current_col += 1
            if current_col == width:
                current_row += 1
                current_col = 0
    return decoded_image

decoded_image = decode_RLC(encoded_data, binary.shape[0], binary.shape[1])

# Tính tỷ lệ nén
original_size = binary.size
encoded_size = len(encoded_data) * 2
compression_ratio = original_size / encoded_size

# Định lượng: Tính độ sai lệch RMSE
rmse = np.sqrt(np.mean((resized_image.astype(np.float32) - decoded_image.astype(np.float32)) ** 2))

# Hiển thị ảnh gốc và ảnh giải nén
cv2.imshow("Original Image", resized_image)
cv2.imshow("Decoded Image", decoded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Tỷ lệ nén:", compression_ratio)
print("Độ sai lệch RMSE:", rmse)