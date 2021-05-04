import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def preparation():
    '''
    1. 输入账号密码
    2. 分别点击"探迹拓客"和"企业查询"转到企业查询界面
    '''
    tmp_str1, tmp_str2 = "'请输入手机号码'", "'请输入密码'"
    input_phone = firefox.find_element_by_xpath("//input[@placeholder={}]".format(tmp_str1))
    input_passwd = firefox.find_element_by_xpath("//input[@placeholder={}]".format(tmp_str2))
    input_phone.clear()
    input_passwd.clear()
    input_phone.send_keys(u'******', Keys.RETURN)
    input_passwd.send_keys(u'******', Keys.RETURN)

    button1 = '//span[text()="探迹拓客"]'
    button2 = '//span[text()="企业查询"]'
    wait.until(EC.element_to_be_clickable((By.XPATH, button1))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, button2))).click()

def search_enterprise(keys='aa'):
    '''
    1. 按照关键字检索相关企业
    2. 点击第一相关的企业
    3. 转到该企业界面
    '''
    tmp_str3 = '//input[@class="ant-input" and @maxlength="50" and @type="text"]'
    search = firefox.find_element_by_xpath(tmp_str3)
    search.clear()
    time.sleep(2)
    search.send_keys(keys, Keys.RETURN)

    button3 = '//section[@class="_2wady"]/div[2]/div/h3/a'
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, button3))).click()

    firefox.implicitly_wait(200)
    firefox.switch_to.window(firefox.window_handles[1])
    time.sleep(5)

def overall_information():
    table1 = pd.read_html(firefox.find_element_by_xpath("//table[1]").get_attribute('outerHTML'))[0]
    table2 = pd.read_html(firefox.find_element_by_xpath("//table[2]").get_attribute('outerHTML'))[0]
    # table3 = pd.read_html(firefox.find_element_by_xpath("//table[3]").get_attribute('outerHTML'))[0]
    return pd.concat((table1, table2))

def shareholder_information(click_check, anchor):
    shareholder = pd.read_html(firefox.find_element_by_xpath("({})[1]/div/div/div/div/div/table".format(anchor)).get_attribute('outerHTML'))[0]
    while True:
        if firefox.find_element_by_xpath("{}[1]".format(click_check)).get_attribute('aria-disabled') == 'true': #按钮隐藏为真，则只有一页
            break
        else:
            firefox.find_element_by_xpath("{}[1]/a/i".format(click_check)).click()
            shareholder = pd.concat((shareholder, pd.read_html(firefox.find_element_by_xpath("({})[1]/div/div/div/div/div/table".format(anchor)).get_attribute('outerHTML'))[0]), axis=0)
    return shareholder

def main_staff(click_check, anchor):
    staff = pd.read_html(firefox.find_element_by_xpath("({})[2]/div/div/div/div/div/table".format(anchor)).get_attribute('outerHTML'))[0]
    while True:
        if firefox.find_element_by_xpath("{}[2]".format(click_check)).get_attribute('aria-disabled') == 'true': #按钮隐藏为真，则只有一页
            break
        else:
            firefox.find_element_by_xpath("{}[2]/a/i".format(click_check)).click()
            staff = pd.concat((staff, pd.read_html(firefox.find_element_by_xpath("({})[2]/div/div/div/div/div/table".format(anchor)).get_attribute('outerHTML'))[0]), axis=0)
    return staff

def invest_information(click_check, anchor):
    invest = pd.read_html(firefox.find_element_by_xpath("({})[3]/div/div/div/div/div/table".format(anchor)).get_attribute('outerHTML'))[0]
    while True:
        if firefox.find_element_by_xpath("{}[3]".format(click_check)).get_attribute('aria-disabled') == 'true': #按钮隐藏为真，则只有一页
            break
        else:
            firefox.find_element_by_xpath("{}[3]/a/i".format(click_check)).click()
            invest = pd.concat((invest, pd.read_html(firefox.find_element_by_xpath("({})[3]/div/div/div/div/div/table".format(anchor)).get_attribute('outerHTML'))[0]), axis=0)
    return invest

def detail_information():
    click_check = '(//li[@title="下一页"])' # 判断按钮是否可点击
    anchor = '//div[@class="ant-table-wrapper _18vkU" and @style="margin-bottom: 30px;"]'  # 提取股东信息、主要成员、对外投资

    shareholder = shareholder_information(click_check, anchor)
    staff = main_staff(click_check, anchor)
    invest = invest_information(click_check, anchor)

    return shareholder, staff, invest

def main():
    global firefox
    firefox = webdriver.Firefox()
    firefox.get('https://user.tungee.com/users/sign-in')
    global wait
    wait = WebDriverWait(firefox, 20)

    preparation()
    search_enterprise()
    overall_information().to_csv('over_all.csv')
    shareholder, staff, invest = detail_information()
    shareholder.to_csv('shareholder.csv')
    staff.to_csv('staff.csv')
    invest.to_csv('invest.csv')

    firefox.quit()

if __name__ == '__main__':
    main()
