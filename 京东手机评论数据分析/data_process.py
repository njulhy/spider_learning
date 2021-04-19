import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from operator import itemgetter
import json

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

def count_color(sorted_list):
    with open('d:/jupyter/comment/color_count.txt', 'a') as f:
        for idx in range(len(sorted_list)):
            color = pd.read_csv(all_path[idx])['color'].value_counts()
            score = pd.read_csv(all_path[idx])['score'].value_counts()
            f.write("{}, {} \n".format(
                all_path[idx].split('_')[0].split('/')[-1],
                str(score.to_dict())
                ))

product_dict = dict(zip(product_type, product_id))
sorted_list = sorted(product_dict.items(), key=itemgetter(0))
#print(sorted_list)
all_path = []
for a in range(len(sorted_list)):
    all_path.append('d:/jupyter/comment/{}_{}.csv'.format(sorted_list[a][0], sorted_list[a][1]))
print(all_path)
count_color(sorted_list)




'''
100011833542 # readmik30pro         2999 23w   91%
100005185603 # huaweimate30         4500 49w   97%
100009177376 # huaweimate30pro      6399 45w   97%
100006349795 # galaxy s20       	6999 1.7w  94%
100006566869 # oppofindx2			4999 1w    94%
100011263192 # oppoReno3			2699 3.7w  95%
100005929301 # oppoReno3pro			3699 4.3w  95%
100012014970 # huawei p40       	4488 16w   97%
100012015170 # huawei p40pro    	6488 21w   97%
100012545832 # huawei honor30   	3189 10w   95%
100010260254 # huawei honorv30pro   3089 19w   96%
100011351676 # xiaomi10pro      	4999 13w   92%
100011336094 # xiaomi10         	3999 32w   91%
100006771395 # oneplus8         	4599 9.5w  93%
100006713417 # oneplus8pro      	5999 6.4w  94%
100012749268 # nova7            	2999 10w   96%
100012749276 # nova7pro         	4099 4w    96%
100012820012 # vivo iQOO Neo3       2998 12w   93%
100007988988 # vivo NEX 3           4998 2.5w  95%
100011924580 # vivo S6              2498 3w    94%
100011238400 # vivo Z6              2198 7w    95%
100011513372 # 努比亚 nusorted_listia 红魔    3499 3.2w  91%
100011242578 # 腾讯黑鲨游戏手机3    3699 6.5w  92%
100007043753 # 魅族17               3699 1.5w  92%
'''