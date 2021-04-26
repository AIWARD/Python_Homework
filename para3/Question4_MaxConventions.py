m = int(input("请输入一个数字"))
n = int(input("请再输入一个数字"))

i = n if m>n else m
while ( m%i!=0 or n%i !=0 ):
    i -= 1

print("最大公约数是",i)