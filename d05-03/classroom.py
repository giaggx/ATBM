
import math

# 1. Hàm giải phương trình bậc 2
def giai_phuong_trinh_bac_2(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có 2 nghiệm phân biệt x1 = {x1}, x2 = {x2}"
# Giải phương trình bậc 2
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
print(giai_phuong_trinh_bac_2(a, b, c))
# 2.a. Hàm kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 2.b. Hàm tìm tất cả các số nguyên tố <= n
def tim_so_nguyen_to(n):
    prime_numbers = []
    for i in range(2, n+1):
        if kiem_tra_so_nguyen_to(i):
            prime_numbers.append(i)
    return prime_numbers
# Kiểm tra số nguyên tố và tìm tất cả các số nguyên tố <= n
n = int(input("Nhập n: "))
print(f"{n} là số nguyên tố: {kiem_tra_so_nguyen_to(n)}")
print(f"Tất cả các số nguyên tố <= {n} là: {tim_so_nguyen_to(n)}")

# 3. Hàm tìm các số chia hết cho 7 nhưng không phải bội số của 5
def tim_so_chia_het_cho_7(n, m):
    numbers = []
    for i in range(n, m+1):
        if i % 7 == 0 and i % 5 != 0:
            numbers.append(i)
    return numbers
#Tìm các số chia hết cho 7 nhưng không phải bội số của 5 trong đoạn 2000 và 3200
numbers = tim_so_chia_het_cho_7(2000, 3200)
print("Các số chia hết cho 7 nhưng không phải bội số của 5 trong đoạn từ 2000 đến 3200 là:")
print(', '.join(map(str, numbers)))



