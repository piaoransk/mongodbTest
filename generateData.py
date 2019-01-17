#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient
import datetime,progressbar,sys
import time
from progressbar import ProgressBar
conn = MongoClient('localhost', 27017)
db = conn.mydb  #连接mydb数据库，没有则自动创建
my_set = db.test_set    #使用test_set集合，没有则自动创建
#插入


starttime = datetime.datetime.now()
total = 100
# for i in progressbar.progressbar(range(total)):
for i in range(total):
    name = "xyhtest"+str(i)
    my_set.insert({"name": name, "age": i})
    sys.stdout.write("\r%s/%s"%(i+1,total))
    sys.stdout.flush()
endtime = datetime.datetime.now()
print "\nescape time: %s s "%(endtime - starttime).seconds
# #查询全部
# for i in my_set.find():
#     print(i)
# #查询name=zhangsan的
# for i in my_set.find({"name":"zhangsan"}):
#     print(i)
# print(my_set.find_one({"name":"zhangsan"}))
