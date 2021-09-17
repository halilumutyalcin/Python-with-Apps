######################################
########                      ########
# https://github.com/halilumutyalcin #
########                      ########
######################################


from selenium import webdriver
import time

browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
browser.get("https://web.whatsapp.com")
# scan qr code in 10sec
time.sleep(10)
search = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
search.click()
search.send_keys("Not")  # enter full contact name
time.sleep(5)
choose = browser.find_element_by_xpath(
    "/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[10]/div/div/div[2]")
choose.click()
time.sleep(5)
msgbar = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
msgbar.clear()
msgbar.click()
# if you send one message, use it
"""
msgbar.send_keys("MESSAGE")
time.sleep(2)
send = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]")
send.click()
"""
# if you send a lot different words or sentence, use it
for i in range(200):  # enter num of times in range for how many send you want
    msgbar.send_keys("")  # enter first message
    send = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]")
    send.click()
    time.sleep(1)
    # if you want more, please copy and paste line(25-26-27) here then, watch it
