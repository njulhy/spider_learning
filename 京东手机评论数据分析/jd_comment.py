import requests
import json
import os
import random
import time

comment_file_path = 'd:/jupyter/comment.txt'

def spider_comment(page=0):
    '''
    get comment of jd.com
    :param page:爬取第几页，默认为0
    '''
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1263013576&score=0'\
        '&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1' % page
    headers = {'user-agent': 'Mozilla/5.0', 'Referer': 'https://item.jd.com/1263013576.html'}
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
    except:
        print('爬取失败')
    # get json str
    r_json_str = r.text[20:-2]
    # str to objective
    r_json_obj = json.loads(r_json_str)
    # get table data of comment
    r_json_comments = r_json_obj['comments']
    
    for r_json_comment in r_json_comments:
        with open(comment_file_path, 'a+') as file:
            file.write(r_json_comment['content'] + '\n')
        # print(r_json_comment['content'])

def batch_spider_comment():
    '''
    get batch comment data of jd.com
    '''
    if os.path.exists(comment_file_path):
        os.remove(comment_file_path)
    for i in range(100):
        spider_comment(i)
        time.sleep(random.random() * 4)


if __name__ == '__main__':
    batch_spider_comment()