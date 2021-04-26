def reverse(*args):
    for i in range(len(args)):
        print(args[-(i+1)])
    print("输出完成") 

eval("print(reverse({:s}))".format(input("请输入参数(参数间用,隔离)")))