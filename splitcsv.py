# -*- coding: utf-8 -*-
#
#方案1
import os
import sys
import csv

# # 初始化编码
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# # 读取本地csv文件
# csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_back.csv')
# csv_reader = csv.reader(open(csv_path, 'rb'))
# csv_reader.next()
# i = j = 1
# with open(csv_path, 'rb') as csv_reader:
#     for row in csv_reader:
#         if i % 1048576 == 0:
#             print u"CSV文件split%s已生成成功" % j
#             j += 1
#         # 写入csv
#         csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test' + str(j) + '.csv')
#         with file(csv_path, 'ab+') as csv_file:
#             csv_write = csv.writer(csv_file)
#             # 文件不存在则写入头部
#             if os.path.getsize(csv_path) == 0:
#                 csv_write.writerow(['id', 'age', 'name'])
#             # 写入数据
#             csv_write.writerow([row[0], row[1], row[2]])
#             csv_file.close()
#             i += 1
#             # 关闭连接

#方案2

# import csv
# import os
# spath = os.path.dirname(os.path.abspath(__file__))
# source_csv_path = os.path.join(spath, 'test_back.csv')
#
# with open(source_csv_path, 'r') as file:
#     csvreader = csv.reader(file)
#     a = next(csvreader)
#     print(a)
#     i = j = 1
#     for row in csvreader:
#         # print(row)
#         # print('i is %s, j is %s'%(i,j))
#         # 没1000个就j加1， 然后就有一个新的文件名
#         if i % 1048576 == 0:
#             j += 1
#             # print("csv %s 生成成功"%j)
#         csv_path = os.path.join(spath,  str(j) + '.csv')
#         # print('/'.join(path.split('/')[:-1]))
#         print(csv_path)
#         # 不存在此文件的时候，就创建
#         if not os.path.exists(csv_path):
#             with open(csv_path, 'w') as file:
#                 csvwriter = csv.writer(file)
#                 csvwriter.writerow(['image_url'])
#                 csvwriter.writerow(row)
#             i += 1
#         # 存在的时候就往里面添加
#         else:
#             with open(csv_path, 'a') as file:
#                 csvwriter = csv.writer(file)
#                 csvwriter.writerow(row)

#方案3 实测有效150M 3秒
import os
import time

def mkSubFile(lines, head, srcName, sub):
    [des_filename, extname] = os.path.splitext(srcName)
    filename = des_filename + '_' + str(sub) + extname
    print('make file: %s' % filename)
    fout = open(filename, 'w')
    try:
        fout.writelines([head])
        fout.writelines(lines)
        return sub + 1
    finally:
        fout.close()


def splitByLineCount(filename, count):
    fin = open(filename, 'r')
    try:
        head = fin.readline()
        buf = []
        sub = 1
        for line in fin:
            buf.append(line)
            if len(buf) == count:
                sub = mkSubFile(buf, head, filename, sub)
                buf = []
        if len(buf) != 0:
            sub = mkSubFile(buf, head, filename, sub)
    finally:
        fin.close()


if __name__ == '__main__':
    begin = time.time()
    splitByLineCount('test_back.csv', 1000000)
    end = time.time()
    print('time is %d seconds ' % (end - begin))
