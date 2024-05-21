# mã hóa và giải mã 1 đoạn văn nhập vào bàn phím
#
def mahoa(text, k):
    kq = ""
    # duyệt chuỗi
    for i in range(len(text)):
        char = text[i]
        # kiểm tra các ký tự hoa
        if char.isupper():
            kq += chr((ord(char) + k - 65) % 26 + 65)
        # các ký tự thuòng
        else:
            kq += chr((ord(char) + k - 97) % 26 + 97)
    return kq


text = str(input("nhập chuỗi cần mã hóa (Encrypting):"))

k = int(input("nhập khóa K cần mã hóa :"))

print("bản được mã hóa (Cipher):" + mahoa(text, k))


def giaima(text, k):
    kqGiaiMa = ""
    #
    for i in range(len(text)):
        char2 = text[i]
        # kiểm tra các ký tự  hoa
        if char2.isupper():
            kqGiaiMa += chr((ord(char2) - k - 65) % 26 + 65)
        # các ký tự thuòng
        else:
            kqGiaiMa += chr((ord(char2) - k - 97) % 26 + 97)

    return kqGiaiMa


text2 = str(input("nhập chuỗi cần giải mã:"))

k2 = int(input("nhập khóa K cần giải hóa :"))

print("bản được giải mã:" + mahoa(text2, k2))
