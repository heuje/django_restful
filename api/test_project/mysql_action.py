# -*- coding: utf-8 -*-
# __author__ = "yw"
# 封装一些数据库的操作，该脚本执行后初始化测试用户；
from pymysql import connect
import yaml
import logging

class DB():
    def __init__(self):
        logging.info('init data'.center(30,'='))
        logging.info('connect db...')
        self.conn = connect(host='127.0.0.1',user='root',password='',db='django_restful')

    def clear(self, table_name):
        logging.info('clear db...')
        clear_sql = 'truncate ' + table_name + ';'
        with self.conn.cursor() as cursor:
            # 清除外键约束
            cursor.execute("set foreign_key_checks=0")
            cursor.execute(clear_sql)
        self.conn.commit()

    def insert(self,table_name, table_data):
        logging.info('insert db...')
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"

        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())

        logging.info(key)
        logging.info(value)

        insert_sql = "insert into " + table_name + "(" + key + ")" + "values" + "(" + value + ");"
        logging.info(insert_sql)

        with self.conn.cursor() as cursor:
            cursor.execute(insert_sql)
        self.conn.commit()

    def close(self):
        logging.info('close db...')
        self.conn.close()
        logging.info('init data finished'.center(30, '='))

    def init_data(self, datas):
        logging.info('init db...')
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table,d)
        self.close()


if __name__ == '__main__':
    db = DB()
    # db.clear('api_user')
    # db.clear('api_group')
    # user_data = {
    #     'id': 1,
    #     'username': '51zxw',
    #     'email': '51zxw@163.com',
    #     'groups': 'http://127.0.0.1:8000/groups/1/'
    # }
    # db.insert('api_user', user_data)
    # group_data = {
    #     'id': 1,
    #     'name':'Developer'
    # }
    # db.insert('api_group', group_data)
    # db.close()

    # 初始化数据
    f = open('datas.yaml','r')
    datas = yaml.load(f)
    db.init_data(datas)

