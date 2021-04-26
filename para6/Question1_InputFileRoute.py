route = input("请输入路径") 
text = open(route,"w",encoding="utf8")
list = ["三国演义","水浒","西游记","红楼梦"]
for i in list:
    text.write(i)
    text.write("\n")
text.close()

