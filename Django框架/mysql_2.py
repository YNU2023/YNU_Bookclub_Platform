# -*- coding: utf-8 -*- 
# @Time : 6/15/23 13:12 
# @Author : ANG

# -*- coding: utf-8 -*-
# @Time : 6/15/23 12:58
# @Author : ANG

import pymysql

while True:
    username = input("请输入用户名：")
    if username.upper() == 'Q':
        break
    password = input("请输入密码：")
    mobile = input("请输入手机号：")

    # 1.连接MySOL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="tusan34hao", charset='utf8', db='unicom')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2.发送指令
    sql = "insert into admin (username, password, mobile) values(%s, %s, %s )"
    cursor.execute(sql, [username, password, mobile])
    conn.commit()

    # 3.关闭
    cursor.close()
    conn.close()
