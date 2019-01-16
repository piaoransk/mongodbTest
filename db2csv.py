#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient
import csv
#connect
conn = MongoClient('localhost', 27017)
db = conn['mydb']  #连接mydb数据库，没有则自动创建
my_set = db['test_set']    #使用test_set集合，没有则自动创建
# db.authenticate("用户名", "密码")

with open("test.csv", "wb") as csvfileWriter:
    writer = csv.writer(csvfileWriter)
    # 先写列名
    # 写第一行，字段名
    fieldList = [
        "_id",
        "age",
        "name",
    ]
    writer.writerow(fieldList)
    allRecordRes = my_set.find()
    # 写入多行数据
    # print type(allRecordRes)
    total = my_set.count_documents({})
    # for i in progressbar.progressbar(range(total)):
    for record in allRecordRes:
        print("record = {%s}"%record)
        recordValueLst = []
        for field in fieldList:
            if field not in record:
                recordValueLst.append("None")
            else:
                recordValueLst.append(record[field])
        try:
            writer.writerow(recordValueLst)
        except Exception as e:
            print("write csv exception. e = {e}")
