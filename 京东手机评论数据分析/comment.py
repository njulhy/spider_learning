import requests
import json
import os
import random
import time
import csv


product_id = [
    100011833542,
    100005185603,
    100009177376,
    100006349795,
    100006566869,
    100011263192,
    100005929301,
    100012014970,
    100012015170,
    100012545832,
    100010260254,
    100011351676,
    100011336094,
    100006771395,
    100006713417,
    100012749268,
    100012749276,
    100012820012,
    100007988988,
    100011924580,
    100011238400,
    100011513372,
    100011242578,
    100007043753,
]
product_type = [
    'readmik30pro',
    'huaweimate30',
    'huaweimate30pro',
    'galaxyS20',
    'oppofindx2',
    'oppoReno3',
    'oppoReno3Pro',
    'huaweip40',
    'huaweip40pro',
    'huaweihonor30',
    'huaweihonorv30pro',
    'xiaomi10pro',
    'xiaomi10',
    'oneplus8',
    'oneplus8pro',
    'nova7',
    'nova7pro',
    'vivoiQOONeo3',
    'vivoNEX3',
    'vivoS6',
    'vivoZ6',
    'nubiaHongmo',
    'tecentHeisha3',
    'meizu17',
]

product_dict = dict(zip(product_type, product_id))

def spider_comment(score=5, page=0, comment_file_path=None, product_id=100011833542):
    '''
    get comment of jd.com
    :param page:爬取第几页,默认为0
    '''
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98'\
        '&productId={}&score={}&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'.format(
            product_id, score, page)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Referer': 'https://item.jd.com{}.html'.format(product_id)
    }
    try:
        response1 = requests.get(url=url, headers=headers)
        response1.raise_for_status()
    except:
        print('爬取失败')
    # get json str
    comment_json_str = response1.text.split('(', 1)[1][:-2]
    # str to objective
    comment_dict = json.loads(comment_json_str)
    # get table data of comment
    comments = comment_dict['comments']

    for comment in comments:
        user = comment['nickname']
        score = comment['score']
        color = comment['productColor']
        size = comment['productSize']
        time = comment['creationTime']
        interval = comment['days']
        comment = comment['content']

        with open(comment_file_path, 'a', newline='') as file:
            row = (user, score, color, size, time, interval, comment)
            writer = csv.writer(file)
            writer.writerow(row)


def batch_spider_comment(product_id=0, comment_file_path=None):
    '''
    get batch comment data of jd.com
    '''

    if os.path.exists(comment_file_path):
        os.remove(comment_file_path)
    with open(comment_file_path, 'a', newline='') as file:
        row = ('user', 'score', 'color', 'size', 'time', 'interval', 'comment')
        writer = csv.writer(file)
        writer.writerow(row)
    for score in range(1, 6):
        for page in range(100):
            spider_comment(score, page, comment_file_path, product_id)
            #time.sleep(random.random())


if __name__ == '__main__':

    for idx in range(len(product_id)):
        comment_file_path = '/home/lhy/spider/{}_{}.csv'.format(product_type[idx], product_id[idx])
        batch_spider_comment(product_id[idx], comment_file_path)
        time.sleep(5)
