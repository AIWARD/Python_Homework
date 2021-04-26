def triangle(num) :
    if num%2==0 :
        return False
    for i in range(num):
        print(" "*(num-i),"*"*(2*i-1))
    return True

if triangle(int(input("请输入一个数"))) :
    print("打印完毕")
else:
    print("输入有误，无法打印")
