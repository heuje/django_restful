# -*- coding: utf-8 -*-
# __author__ = "yw"
import unittest
from BSTestRunner import BSTestRunner
import time,yaml
from mysql_action import DB
import logging.config

CON_LOG = 'log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

# 数据初始化操作
db=DB()
f = open('datas.yaml', 'r')
datas = yaml.load(f)
db.init_data(datas)

# 指定测试用例和测试报告的路径
test_dir = '.'
report_dir = './reports'

#加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_django_restful.py')

# 定义报告的文件格式
# now = time.strftime("%Y-%m-%d %H_%M_%S")
now = time.strftime("%Y%m%d%H%M%S")
report_name = report_dir + '/' + now + 'test_report.html'

# 运行用例并生成测试报告
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title=" API Test Report", description="Django Restful Api Test Report")
    logging.info('Start API Test'.center(30,'='))
    runner.run(discover)