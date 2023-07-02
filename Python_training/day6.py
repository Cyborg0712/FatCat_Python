'''
a = int(input("nhập vào a: "))
if(a%2==0):
    for i in range(1,6,1):
        a+=i
    print(f"Tổng: {a}")
else:
    print("Tôi không tính tổng sổ lẻ, bye bye")
'''   
'''
n = int(input("nhập vào n: "))
sum = 0
if(n>=5):
    for i in range(1,n+1,1):
        if(i%2!=0 and i!=3):
            sum+=i
    print(f"tổng lẻ: {sum}")
else:
    print("chỉ tính tổng lẻ >=5")
'''
'''
n = int(input("nhập vào n: "))
sum = 0
for i in range(1,n+1,2):
    if(i==3):
        break
    sum += i
print(f"Tổng lẻ: {sum}")
'''
'''
for i in range(10,50,1):
    if(i%3!=0):
        continue
    else:
        print(i)
'''
'''
x=1
sum = 0
for i in range(1,11,1):
    x*=i
    sum+=x
print(f"Tổng: {sum}")
'''
'''
for i in range(1,1001,1):
    total=0
    for j in range(1,i,1):
        if(i%j==0):
            total+=j
    if(total==i):
        print(f"Số {i} là số hoàn hảo")
'''
'''
x = int(input("nhập vào x: "))
n = int(input("nhập vào n: "))
sum = 0
for i in range(1,n+1,1):
    x**=i
    n*=i
    s = x/n
    sum+=s
print(f"Tổng: {sum}")
'''
'''
x = int(input("nhập vào x: "))
n = int(input("nhập vào n: "))
sum = 0
for a in range(1,n+1,1):
    tu = (x**a)
    mau = 1
    for k in range(1,a+1,1):
        mau=mau*a
    sum = sum+(tu/mau)
print(f"Tổng: {sum}")    
'''
while True:
    n = int(input("nhập vào số n: "))
    count = 0
    for x in range(1,n+1,1):
        if(n%x==0):
            count+=1
    if(count==2):
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không là số nguyên tố")
    exit=input("Bạn có muốn tiếp tục (y/n)? ")
    if(exit=="n" or exit=="N"):
        break