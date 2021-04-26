draw1 = open("source\draw1.py","r")
list = draw1.readlines()
print(list)

draw2 = open("source\draw2.py","w")
for i in list:
    str = i.replace("import turtle","import turtle as t") if "import turtle" in i else i.replace("turtle", "t")
    draw2.write(str)