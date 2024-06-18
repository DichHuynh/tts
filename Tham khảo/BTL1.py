import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = cv2.imread(r'C:\Users\Admin\Downloads\Thong tin so\BIG_ASSIGN\BTL.jpg')
img = cv2.resize(img,(200,200))
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
h,w = img.shape

index = 0
bits_level = [8,6,4,2,1]

def quantization(image, bl):
    global index
    index += 1
    img_tmp = np.floor(image/2**(8-bl)) * 2**(8-bl)
    img_tmp = img_tmp.astype(np.uint8)
    plt.subplot(2,3,index)
    plt.axis('off')
    plt.title('{} bits, {}'.format(bits_level[index - 1], img_tmp.shape))
    plt.imshow(img_tmp,cmap='gray')

for i in bits_level:
    quantization(img,i)
plt.show()
