p = int(input("请输入本金"))
R = float(input("请输入年利率(请输入小数形式)"))
T = int(input("请输入存款年限"))
print("最终得到的复利息为:",p*((1+R)**T)-p)