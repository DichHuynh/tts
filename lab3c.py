def fakeError(matrix):
    matrix[0][4] = not matrix[0][4]
    matrix[2][4] = not matrix[2][4]
    matrix[5][4] = not matrix[5][4]
    matrix[9][4] = not matrix[9][4]
    matrix[12][4] = not matrix[12][4]
    matrix[0][0] = not matrix[0][0]
    matrix[2][0] = not matrix[2][0]
    matrix[5][0] = not matrix[5][0]
    matrix[9][0] = not matrix[9][0]
    matrix[12][0] = not matrix[12][0]

# Chuyển chuỗi "DUYDUONGDICHTIN" thành mã ASCII
name = "DUYDUONGDICHTIN"
ascii_values = [ord(char) for char in name]

# Tạo ma trận 2D 13x7 từ mã ASCII
example_matrix = [[0]*7 for _ in range(13)]
index = 0
for i in range(13):
    for j in range(7):
        if index < len(ascii_values):
            example_matrix[i][j] = ascii_values[index]
            index += 1

# Gọi hàm fakeError với ma trận chứa mã ASCII của chuỗi "DUYDUONGDICHTIN"
fakeError(example_matrix)


for row in example_matrix:
    print(row)

def fakeError(matrix):
    rows_to_update = [0, 2, 5, 9, 12]
    cols_to_update = [0, 4]
    for row in rows_to_update:
        for col in cols_to_update:
            matrix[row][col] = not matrix[row][col]
fakeError(text)
for row in tex:
    print(row)

11000000
10010101
10011001
11000000
10010101
10001111
10001110
10000111
11000000
10001001
10000011
10001000
11010000
10001001
10001110

def findSyndrome(codewords, res):
    HT = [
        [1, 1, 1],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    for i in range(17):
        for j in range(3):
            res[i][j] = 0
            for k in range(7):
                res[i][j] += codewords[i][k] * HT[k][j]
            res[i][j] %= 2
codewords = [[0, 1, 1, 0, 1, 0, 1],]
res = [[0, 0, 0] for _ in range(17)]
findSyndrome(codewords, res)

# In ra kết quả
for row in res:
    print(row)
1011
1000
1000
1011
1000
1000
1000
1000
1011
1000
1000
1000
1011
1000
1000
def fixError(error_matrix, matrix):
    e = [[0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1]]
    for i in range(17):
        s = str(error_matrix[i][0]) + str(error_matrix[i][1]) + str(error_matrix[i][2])
        if s == "000":
            for j in range(7):
                matrix[i][j] += e[0][j]
                matrix[i][j] %= 2
        else:
            for j in range(7):
                matrix[i][j] += e[7][j]
                matrix[i][j] %= 2
fixError(error_matrix, input_matrix)
for row in input_matrix:
    print(row)

DUYDUONGDICHTIN


G = [[1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]]
e = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]
