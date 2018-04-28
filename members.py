import csv
from pprint import pprint
import random

"""
members = []

with open("jack_hack 2018（回答） - フォームの回答 1.csv", "r") as fp:
    reader = csv.reader(fp)
    header = next(reader)
    for low in reader:
        if low[2] != "":
            members.append([low[1], low[2][0:1], 1, True])

pprint(members)
"""
members = [
 ['すぷーん', 'a', True, True],
 ['ゆーし', 'a', True, True],
 ['みちろー', 'b', True, True],
 ['だいず', 'c', True, True],
 ['きなこ', 'b', True, True],
 ['ちょん', 'a', True, True],
 ['なす', 'a', True, True],
 ['しょーい', 'a', True, True],
 ['しろ', 'c', True, False],
 ['あべべ', 'c', True, True],
 ['桑山 拓也', 'b', True, True],
 ['杉野 将史', 'c', False, True],
 ['赤池 佑介', 'c', False, True],
 ['鈴木一成', 'c', False, True],
 ['ブラザー', 'c', False, True],
 ['くろねこ', 'c', False, True],
 ['河合 駿介', 'c', False, True],
 ['くまちゃん', 'b', False, True],
 ['きりん', 'b', False, True],
 ['高井 佑輔', 'c', False, True],
 ['山本 和将', 'b', False, False],
 ['加藤 優吾', 'c', False, False],
 ['itoka', 'c', False, True],
 ['杉浦 航', 'c', False, False],
 ['松下 紗也輝', 'c', False, True],
 ['和田 哲弥', 'b', False, True]
]
groups = [
    [['a', True, True], ['c', False, True], ['c', False, True], ['c', False, False]],
    [['a', True, True], ['c', False, True], ['c', False, True], ['c', True, False]],
    [['a', True, True], ['c', True, True],  ['c', False, True], ['c', False, True]],
    [['a', True, True], ['c', False, True], ['c', False, True]],
    [['a', True, True], ['c', True, True],  ['c', False, True], ['c', False, False]],
    [['b', True, True], ['b', True, True],  ['b', False, True], ['b', False, False]],
    [['b', True, True], ['b', False, True], ['b', False, True]]
]
groups2 = [

]
made = []
for group in groups:
    buf = []
    for member in group:
        while True:
            pickup = random.choice(members)
            if pickup[1] == member[0] and pickup[2] == member[1] and pickup[3] == member[2]:
                buf.append(pickup[0])
                members.remove(pickup)
                break
    made.append(buf)

for i in range(len(made)):
    print("●グループ"+str(i+1))
    print("/".join(made[i]))