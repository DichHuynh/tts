import cv2
import numpy as np

def text2ASCII7(text):
    code = ""
    for char in text:
        ascii_code = ord(char)
        binary_code = format(ascii_code, '07b')
        code += binary_code
    return code

def decode_ascii(encoded_text):
    decoded_text = ''
    for i in range(0, len(encoded_text), 7):
        encoded_char = encoded_text[i:i+7]
        decoded_char = chr(int(encoded_char, 2))  # Chuyển đổi mã ASCII 7 bit thành ký tự
        decoded_text += decoded_char
    return decoded_text

text = "DUY DUONG DICH TIN"
encoded_text = ""
# Giả sử 1 ký tự bị lỗi ở vị trí đầu tiên của mỗi từ
words = text.split()
for word in words:
    encoded_char = text2ASCII7(word)
    error_encoded = '0' + encoded_char[1:]
    encoded_text += error_encoded

decoded = decode_ascii(encoded_text)
print("Encoded text:", encoded_text)
print("Decoded text:", decoded)