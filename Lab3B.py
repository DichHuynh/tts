import cv2
import numpy as np
path = "ttslab21.jpg"  # Thay đường dẫn ở đây
image = cv2.imread(path)
# Hàm chuyển ảnh thành ảnh nhị phân với màu đen và trắng
image_resized = cv2.resize(image, (256, 256))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)


# Resize ảnh về kích thước 256x256


# Chuyển ảnh về ảnh nhị phân màu đen và trắng

# Đếm số mức xám trong ảnh
num_gray_levels = len(np.unique(binary))

# In ra số mức xám
print("Số mức xám trong ảnh nhị phân là:", num_gray_levels)

# Hiển thị ảnh nhị phân
cv2.imshow("Binary Image", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()