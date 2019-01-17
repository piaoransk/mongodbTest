#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import progressbar,sys,datetime

# for i in progressbar.progressbar(range(100)):
#     time.sleep(0.02)
starttime = datetime.datetime.now()
for i in range(10):
    sys.stdout.write('\r %s'%i)
    sys.stdout.flush() #强制刷新，将内存中的内容写入硬盘
    time.sleep(0.1) #推迟执行的秒数
    # if i == 19:
    #     sys.stdout.write('100%')

endtime = datetime.datetime.now()
es_time = (endtime - starttime).seconds
print('\nspend time: %s'%es_time)