import time
import unittest

import HTMLTestReport
import unitTest
if __name__ == "__main__":
    '''生成测试报告'''

    current_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    testunit = unittest.TestSuite()

    testunit.addTest(unitTest.unitTest("test01"))


    report_path = ".\\test\\" + current_time + '.html'  # 生成测试报告的路径
    fp = open(report_path, "wb")
    runner = HTMLTestReport.HTMLTestRunner(stream=fp, title=u"自动化打卡", description='自动化打卡演示报告', tester='Anchovy')
    runner.run(testunit)
    fp.close()
    print("完成："+report_path)
