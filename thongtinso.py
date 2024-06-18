# change the sampling frequency of gray image
import cv2
import numpy as np
from matplotlib import pyplot as plt

def shift_freq(image, dx, dy):
    rows, cols = image.shape
    crow, ccol = rows // 2 , cols // 2

    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)

    # Tạo mặt nạ dịch chuyển tần số
    mask = np.zeros((rows, cols), np.uint8)
    mask[crow-dy:crow+dy, ccol-dx:ccol+dx] = 1

    # Áp dụng mặt nạ dịch chuyển tần số
    fshift = fshift * mask

    # Biến đổi Fourier ngược
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    return img_back

# Đọc ảnh xám từ đường dẫn file
img_gray = cv2.imread("thongtinso.jpg",cv2.IMREAD_GRAYSCALE)

# Thay đổi tần số lấy mẫu với dx = 50 và dy = 50
dx = 100
dy = 100
dx1 = 50
dy1 = 50
dx2 = 500
dy2 = 500
img2 =shift_freq(img_gray, dx2,dy2)
new_img = shift_freq(img_gray, dx1, dy1)

result_img = shift_freq(img_gray, dx, dy)
# cv2.imwrite('anh1.jpg',result_img)
# cv2.imwrite('anh2.jpg', new_img)
# cv2.imwrite('anh3.jpg', img2)
# Hiển thị ảnh gốc và ảnh với tần số được thay đổi
plt.subplot(221), plt.imshow(img_gray, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(result_img, cmap='gray')
plt.title('100'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(new_img, cmap='gray')
plt.title('50'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(img2, cmap='gray')
plt.title('500'), plt.xticks([]), plt.yticks([])
plt.show()

# nhận xét: anh sau khi lấy mẫu thì dung lượng lớn hơn
# nếu tăng tần số lên thì dung lượng tăng thêm và ảnh được
# rõ nét hơn