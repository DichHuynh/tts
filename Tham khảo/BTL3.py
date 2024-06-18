import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = cv2.imread(r'C:\Users\Admin\Downloads\Thong tin so\BIG_ASSIGN\BTL.jpg')
img = cv2.resize(img,(200,200))
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
h,w,d = img.shape

def sample(img, fs):
    img_tmp = np.zeros((h//fs,w//fs,d))
    for i in range(0,h - fs + 1,fs):
        for j in range(0,w - fs + 1,fs):
            img_tmp[i//fs,j//fs,0] = np.median(img[i:i+fs,j:j+fs,0])
            img_tmp[i//fs,j//fs,1] = np.median(img[i:i+fs,j:j+fs,1])
            img_tmp[i//fs,j//fs,2] = np.median(img[i:i+fs,j:j+fs,2])
    img_tmp = img_tmp.astype(np.uint8)
    return img_tmp


img2 = sample(img,2)
img4 = sample(img,4)
img6 = sample(img,6)
img8 = sample(img,8)
plt.subplot(2,3,1)
plt.title('{}'.format(img.shape))
plt.imshow(img,cmap = 'gray')
plt.subplot(2,3,2)
plt.title('{}, fs = {}'.format(img2.shape,2))
plt.imshow(img2,cmap = 'gray')
plt.subplot(2,3,3)
plt.title('{}, fs = {}'.format(img4.shape,4))
plt.imshow(img4,cmap = 'gray')
plt.subplot(2,3,4)
plt.title('{}, fs = {}'.format(img6.shape,6))
plt.imshow(img6,cmap = 'gray')
plt.subplot(2,3,5)
plt.title('{}, fs = {}'.format(img8.shape,8))
plt.imshow(img8,cmap = 'gray')
plt.show()