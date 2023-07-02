'''
n = int(input("nhập vào từ 1-> 99: "))
while n<1 or n>99:
    n=int(input("chỉ nhập từ 1-> 99: "))
print(n)
'''
while True:
    name = input("Họ tên: ")
    subject = input("Môn: ")
    score = input("Điểm: ")
    print(f"Tên: {name}  Môn: {subject}  Điểm: {float(score)}")
    if(float(score) > 7):
         print("Đủ điều kiện")
    else:
        print("Không đủ điều kiện")  
    exit = input("nhập n để thoát: ")       
    if(exit=="n" or exit =="N"):
          break
