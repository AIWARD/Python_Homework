import numpy as np

arrayInterval = np.arange(0,1,0.01)
arrayNormal = np.random.randn(100)

print("加法运算结果为:",np.add(arrayInterval,arrayNormal))
print("减法运算结果为:",np.subtract(arrayInterval, arrayNormal))
print("乘法运算结果为:",np.multiply(arrayInterval,arrayNormal))
print("除法运算结果为:",np.divide(arrayInterval,arrayNormal))