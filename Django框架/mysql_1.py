# -*- coding: utf-8 -*- 
# @Time : 6/15/23 12:58 
# @Author : ANG

import pymysql

# 1.连接MySOL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="tusan34hao", charset='utf8', db='unicom')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 2.发送指令
cursor.execute("insert into admin (username, password, mobile) values('huangzeqiao', '123456', '13888888888' )")
conn.commit()
# 3.关闭
cursor.close()
conn.close()
