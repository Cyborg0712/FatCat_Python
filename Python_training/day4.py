'''
a = int(input("nhap vao a: "))
b = int(input("nhap vao b: "))
if(a<b):
    print("a is smaller than b")
elif(a==b):
    print("a is equal b")
else:
    print("a is bigger than b")
'''
# Exercise
#5
'''n = int(input("nhập vào n: "))
if(n%2==0):
    print("chẵn")
else:
    print("lẻ")'''
#6
''' dtb = float(input("nhập vào điểm trung bình: "))
if dtb>=9.0:
    print("Giỏi")
elif dtb>7.0 and dtb<9.0:
    print("Khá")
elif dtb>5.0 and dtb<7.0:
    print("Trung bình")
else:
    print("Yếu")
'''
#7
'''
n = int(input("nhập vào năm: "))
if((n % 4 == 0 and n % 100 != 0) or n%400==0):
    print("năm nhuận")
else:
    print("năm không nhuận")
'''
#8
'''
m = int(input("nhập vào tháng: "))
if m==2:
    y = int(input("nhập vào năm: "))
    if(( y%4==0 and y % 100!=0 ) or y%400==0):
        print(29)
    else:
        print(28)
elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print(31)
else:
    print(30)
'''
#9
'''
from math import sqrt
a = float(input("nhập vào a: "))
b = float(input("nhập vào b: "))
c = float(input("nhập vào c: "))
print(f"Phương trình đã nhập: {a}x^2 + {b}x + {c} = 0")
delta = (b**2) - (4*a*c)
if(delta < 0):
    print("Vô nghiệm")
elif(delta == 0):
    print(f"x1 = x2 = {-b/(2*a)}")
elif(delta > 0):
    print(f"x1 = {(-b+sqrt(delta))/(2*a)} \n x2 = {(-b-sqrt(delta))/(2*a)}")
'''

#10
'''
m = int(input("nhập vào tháng: "))
if m==1 or m==2 or m==3:
    print("Quý 1")
elif m==4 or m==5 or m==6:
    print("Quý 2")
elif m==7 or m==8 or m==9:
    print("Quý 3")
else:
    print("Quý 4")

'''


