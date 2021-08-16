import time
import unittest

from selenium.webdriver.common.by import By

import HTMLTestReport
import tool

class unitTest(unittest.TestCase):

    def test01(self):
        # 登录
        b = tool.login("学号", "统一认证密码")
        tool.wait(1)
        # 所在地
        b.find_element_by_xpath("//input[@name='mqszd']").click()
        tool.wait(1)
        b.find_element_by_xpath('/html/body/div[2]/header/button[2]').click()
        tool.wait(1)
        # 4.近14天是否有与疫情中、高风险地区人员的接触史？
        b.find_element_by_xpath('//*[@id="question-form"]/ul/li[4]/div[2]/div/div/li[2]/label/div[2]/div').click()
        tool.wait(1)
        # 5.近14天是否有与疑似、确诊人员的接触史?
        b.find_element_by_xpath('//*[@id="question-form"]/ul/li[5]/div[2]/div/div/li[2]/label/div[2]/div').click()
        tool.wait(1)
        # 6.近21天是否有中高风险地区旅居史，近14天是否有中高风险地区所在区旅居史？
        b.find_element_by_xpath('//*[@id="question-form"]/ul/li[6]/div[2]/div/div/li[2]/label/div[2]/div').click()
        tool.wait(1)
        # 7.现是否处于医学观察状态？
        b.find_element_by_xpath('//*[@id="question-form"]/ul/li[7]/div[2]/div/div/li[2]/label/div[2]/div').click()
        tool.wait(1)
        # 9.现是否处于居家隔离状态？
        b.find_element_by_xpath('//*[@id="question-form"]/ul/li[9]/div[2]/div/div/li[2]/label/div[2]/div').click()
        tool.wait(1)
        # 11.现身体状况，是否存在发热体温、寒战、咳嗽、胸闷以及呼吸困难等症状？
        b.find_element_by_xpath('//*[@id="question-form"]/ul/li[11]/div[2]/div/div/li[2]/label/div[2]/div').click()
        tool.wait(1)
        # 12.同住家属近14天是否有与疫情中、高风险地区人员的接触史？
        b.find_element_by_xpath('//*[@id="question-form"]/ul/li[12]/div[2]/div/div/li[2]/label/div[2]/div').click()
        tool.wait(1)
        # 13.同住家属近14天是否有与疑似、确诊人员的接触史？
        b.find_element_by_xpath('//*[@id="question-form"]/ul/li[13]/div[2]/div/div/li[2]/label/div[2]/div').click()
        tool.wait(1)
        # 14.同住家属近14天是否到过疫情中、高风险地区？
        b.find_element_by_xpath('//*[@id="question-form"]/ul/li[14]/div[2]/div/div/li[2]/label/div[2]/div').click()
        tool.wait(1)
        # 15.同住家属现是否处于医学观察状态?
        b.find_element_by_xpath('//*[@id="question-form"]/ul/li[15]/div[2]/div/div/li[2]/label/div[2]/div').click()
        tool.wait(1)
        # 16.今日申领学校所在地健康码的颜色? What's the color of today's health code?
        b.find_element_by_xpath('//*[@id="question-form"]/ul/li[16]/div[2]/div/div/li[1]/label/div[2]/div').click()
        tool.wait(1)
        # 17.本人或家庭成员(包括其他亲密接触人员)是否有近28日入境或未来7日拟入境的情况?Have you or your family members(including other close contact persons) entered China over the past 28 days or plan to enter China in 7 days?
        b.find_element_by_xpath('//*[@id="question-form"]/ul/li[17]/div[2]/div/div/li[2]/label/div[2]/div').click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@class="button button-big button-fill btn-commit external"]').click()
        print("打卡成功!")


