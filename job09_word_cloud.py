from turtle import back

import background as background
import family
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import collections
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

font_path = './malgun.ttf'
font_name = font_manager.FontProperties(
    fname=font_path).get_name()
plt.rc('font', family='NanumBarunGothic')

# df = pd.read_csv('./crawling_data/reviews_2017_2022.csv')
# words = df[df['titles']=='빅트립: 아기팬더 배달 대모험 (Big Trip)']['review'] #2471
# print(words.iloc[0]) # 문자열만 나오게
#
# words = wrods.iloc[0].split() #형태소기준으로 짜르기 리스트만들기
# print(words)

df= pd.read_csv('./crawling_data/reviews_2017_2022.csv')
words = df[df['titles']=='브라더 오브 더 이어 (Brother of the Year)']['review']
print(words.iloc[0])
words = words.iloc[0].split()
print(words)


# worddict = collections.Counter(wrods)
# worddict = dict(worddict)
# print(worddict)

worddict = collections.Counter(words)
worddict = dict(worddict)
print(worddict)

# wordcloud_img = WordCloud(
#     background_color='white', max_words=2000,
#     font_path=font_path).generagte_from_frequencies(worddict)

wordcloud_img = WordCloud(
    background_color='white', max_words=2000,
    font_path=font_path).generate_from_frequencies(worddict)


plt.figure(figsize=(12,12))
plt.imshow(wordcloud_img, interpolation='bilinear')
plt.axis('off')
plt.show()