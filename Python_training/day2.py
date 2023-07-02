print("*"*40)
str1 = "You should "
str2 = "keep fighting"
str3 = "every single "
str4 = "day"
str_total1 = str1 + str2
str_total2 = str3 + str4
print(str_total1)
print(str_total2)
print("*"*40)

a = 7
b = 12
print("Tổng = ", a+b)
print("Hiệu = ", a-b)
print("Tích = ", a*b)
print("Thương = ", a/b)
print("Chia lấy dư = ", a % b)
print("Lũy thừa = ", a**a)
print("Chia lấy nguyên = ", b//a)

a = 5
a += 7
a -= 2
print(a)

# exercise
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5

print(i1+(i2*i3))  # 1
print(i1*(i2+i3))  # 2
print(i1/(i2+i3))  # 3
print(i1//(i2+i3))  # 4
print(i1/i2+i3)  # 5
print(i1//i2+i3)  # 6
print(3+4+5/3)  # 7
print(3+4+5//3)  # 8
print((3+4+5)/3)  # 9
print((3+4+5)//3)  # 10
print(d1+(d2*d3))  # 11
print(d1+d2*d3)  # 12
print(d1/d2-d3)  # 13
print(d1/(d2-d3))  # 14
print(d1+d2+d3/3)  # 15
print((d1+d2+d3)/3)  # 16
print(d1+d2+(d3/3))  # 17
print(3*(d1+d2)*(d1-d3))  # 18

# Homework
# import math
r = float(input("Nhập vào bán kính: "))
pi = 3.14
# math.pi
# print("Chu vi", 2*r*pi)
# print("Diện tích", (r**2)*pi)
print(f"chu vi : {2*r*pi}, \ndien tich: {(r**2)*pi}")
