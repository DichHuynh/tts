import numpy as np

# Chuỗi đầu vào
st = 'PHAN NGOC QUY TRAN VAN TU NGUYEN MINH TRUNG DUONG DUC MANH DUONG VAN QUAN'

# Chuyển chuỗi sang dạng ASCII
as_bytes = bytearray(st, 'utf-8')

# Chuyển ASCII sang binary và chia thành các bits 7-bit
bas = np.unpackbits(as_bytes)
bas = np.reshape(bas, (-1, 7))

# Thêm bit 0 vào cuối mỗi bộ 7 bits
bl4 = np.hstack((bas, np.zeros((len(bas), 1), dtype=int)))
bl4 = np.reshape(bl4, (-1, 4))

# Ma trận G
G = np.array([[1, 0, 0, 0, 1, 1, 1],
             [0, 1, 0, 0, 0, 1, 1],
             [0, 0, 1, 0, 1, 0, 1],
             [0, 0, 0, 1, 1, 1, 0]])

# Nhân ma trận bl4 với G modulo 2
bl7 = np.mod(np.dot(bl4, G), 2)

# Tính lỗi
error = np.zeros_like(bl7, dtype=int)
error[:, 0] = 1

# XOR để tạo đoạn mã thông tin gửi đi
r = np.bitwise_xor(bl7, error)

# Ma trận H
H = np.array([[1, 0, 1, 1, 1, 0, 0],
             [1, 1, 0, 1, 0, 1, 0],
             [1, 1, 1, 0, 0, 0, 1]])

s = np.mod(np.dot(r, H.T), 2)

# Ma trận E
E = np.array([[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 1, 0],
             [0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0]])

e_idx = np.mod(np.dot(s, np.array([4, 2, 1])), 8)
e = np.array([E[i] for i in e_idx])

# XOR với đoạn mã nhận được để khôi phục lại đoạn mã thông tin ban đầu
r = np.bitwise_xor(r, e)[:, :4]
print( r)
# Chuyển đổi từ bits sang ASCII
# infor = ''.join([chr(int(''.join(map(str, r[i])), 2) for i in range(len(r))])

print(infor)