#giải phương trình bậc nhất
if a == 0:
        if b == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
else:
        x = -b / a
        print("Nghiệm của phương trình là:", x)

 #giải phương trình bậc 2 
        # Tính delta
delta = b**2 - 4*a*c

    # Tính nghiệm
if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép:")
        print("x =", x)
else:
        real_part = -b / (2*a)
        imaginary_part = cmath.sqrt(abs(delta)) / (2*a)
        print("Phương trình có hai nghiệm phức:")
        print("x1 =", real_part, "+", imaginary_part, "i")
        print("x2 =", real_part, "-", imaginary_part, "i")