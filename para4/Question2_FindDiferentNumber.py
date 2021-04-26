def selfPop(one,two,three,four):
    tur = (one,two,three,four)  # 把输入作为元组保存，防止更改
    times = 0

    #  构想:在循环中对列表使用Pop操作保证元素不重复出现
    for i in tur:
        # 每次循环建立列表，且Pop出不同的元素，保证首位不重复
        list1 = list(tur)       
        list1.pop(list1.index(i))
    
        for j in list1:
            # 每次循环生成一个只有两个元素的列表
            list2 = list(list1)
            first = list2.pop(list2.index(j))
    
            # 打印首位后，正反序输出数组元素即可
            print("\n第",times,"个组合为:",first,end="")
            times += 1
            for k in list2: print(k,end="")
            # print(*list2,end="") 其作用等同于for k in list2: print(k,end="")，不过seq无法为空
            print("\n第",times,"个组合为:",first,end="")
            times += 1
            list2.reverse()
            for k in list2:  print(k,end="")
            # print(*list2,end="")
    
    return times

print("\n共有{:d}个组合".format(selfPop(input("第一个数"),input("第二个数"),input("第三个数"),input("第四个数"))))





