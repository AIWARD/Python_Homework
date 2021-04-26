import wordcloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

text = open("source\sanguo.txt", "r", encoding="UTF-8")
words = text.read()
text.close()
background = np.array(Image.open("source\WordCloudBackground.png"))
params = dict(
    background_color = "white" ,
    width = 1000,
    height = 860,
    max_words = 100,
    mask = background
)
wordcloud = wordcloud.WordCloud(**params,font_path="C:\\Windows\\Fonts\\STFANGSO.ttf")
wordpic = wordcloud.generate(words)
plt.imshow(wordpic)
plt.axis("off")
plt.show()
