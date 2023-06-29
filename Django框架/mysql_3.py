# -*- coding: utf-8 -*- 
# @Time : 6/15/23 12:58
# @Author : ANG

import pymysql

# 1.连接MySOL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="tusan34hao", charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 2.查询
cursor.execute("select * from admin")
# 3.获取结果
result = cursor.fetchall()
print(result)
# 4.关闭
cursor.close()
conn.close()
