import jieba
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

comment_file_path = 'd:/jupyter/comment/wawa_first1.csv'

def cut_word():
    '''
    对数据分词
    :return: 分词后的数据
    
    with open(comment_file_path) as file:
        comment_txt = file.read()
        wordlist = jieba.cut(comment_txt, cut_all=True)
        wl = ' '.join(wordlist)
        # print(wl)
        return wl'''
    comment = pd.read_csv(comment_file_path)['评论']
    wordlist = jieba.cut(' '.join(comment), cut_all=True)
    wl = ' '.join(wordlist)
    return wl

def create_word_cloud():
    '''
    create wordcloud
    '''
    coloring = np.array(Image.open('d:/jupyter/wordcloud.png'))
    wordcloud = WordCloud(background_color='white', max_words=2000, mask=coloring, scale=5,
                          max_font_size=50, random_state=42, font_path='C:\Windows\Fonts\simsun.ttc')
    wordcloud.generate(cut_word())
    plt.figure(figsize=(8, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    create_word_cloud()