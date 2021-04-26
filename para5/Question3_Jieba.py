import jieba
file = open("source\sanguo.txt", "r",encoding="utf8").read()
countDic = {}
words = jieba.lcut(file)
for word in words:
    if (len(word)==1):
        continue 
    else:
        countDic[word] = countDic.get(word,0)+1
items = list(countDic.items())
items.sort(key=lambda x: x[1] , reverse=True)
for i in range(20):
    word,countDic = items[i]
    print("{0:<10}{1:>5}".format(word,countDic))
