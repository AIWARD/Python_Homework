def reverse(str):
    print("该数字长度为",len(str),"\n其逆序为",str[::-1]) if len(str)<6 else print("该数字大于100000不合规")

reverse(input("请输入一个数"))