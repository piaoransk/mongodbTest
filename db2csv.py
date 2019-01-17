#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient
import csv
import datetime,sys
#connect
def writecsv(dbcursor ):
    """
    pymongo.cursor.Cursor
    :dbcursor:pymongo.cursor.Cursor
    :counter:计数器
    :return:
    """
    i = 0
    for record in allRecordRes:
        # print("record = {%s}"%record)
        recordValueLst = []
        for field in fieldList:
            if field not in record:
                recordValueLst.append("None")
            else:
                recordValueLst.append(record[field])
        writer.writerow(recordValueLst)
        i = i + 1
        # if i ==2000:
        #     break
        sys.stdout.write("\r%s/%s" % (i+1, total))
        sys.stdout.flush

conn = MongoClient('localhost', 27017)
db = conn['mydb']  #连接mydb数据库，没有则自动创建
my_set = db['test_set']    #使用test_set集合，没有则自动创建
# db.authenticate("用户名", "密码")
starttime = datetime.datetime.now()
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
    wps_limit = 1048576 #wps行数上限
    allRecordRes = my_set.find()
    total = my_set.count_documents({})
    print "total is : ", total
    # data_list = list(allRecordRes)
    # print type(data_list)
    # 写入多行数据
    writecsv(allRecordRes)


    # print type(allRecordRes)
    # print dir(allRecordRes)

    # for i in progressbar.progressbar(range(total)):

endtime = datetime.datetime.now()
es_time = (endtime - starttime).seconds
print('\nspend time: %s'%es_time)