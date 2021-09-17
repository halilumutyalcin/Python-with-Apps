######################################
########                      ########
# https://github.com/halilumutyalcin #
########                      ########
######################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
browser.get("https://www.instagram.com")
time.sleep(2)

username = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
username.send_keys("") # USERNAME
time.sleep(2)

password = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys("") # PASSWORD
password.submit()
time.sleep(5)

notnow = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
notnow.click()
time.sleep(3)

noti = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
noti.click()
time.sleep(3)

post = browser.get("") # LINK

comment_button = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
comment_button.click()

comment = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/section[3]/div/form/textarea')

for i in range(5):#Write how many you want in range expression
    comment.send_keys("COMMENT")
    time.sleep(5)
    comment.submit()
