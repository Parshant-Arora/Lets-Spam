from selenium import webdriver
from time import sleep
from config import CHROME_PROFILE_PATH

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)

#setup the driver
driver = webdriver.Chrome(executable_path='path/to/chromedriver',options=options)

#connect to whatsapp
driver.get('https://web.whatsapp.com/')
input('Press enter after whatsapp has opened without any issue ')

name = input('Enter the name of user or group : ')
msg = input('Enter your message to spam: ')
count = int(input('Enter the count : '))
#Use sleep commands if your internet is slow

#search name of user, click it, find message box, type message and then send
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)) 
user.click()

msg_box = driver.find_element_by_xpath('//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_4sWnG') #Note that these keys may change in future
    button.click()

'''
▒▒▒▄▄▄▄▄▄▄▄▄
░▄███████▀▀▀▀▀▀███████▄
░▐████▀▒DIDDLY▒▒▒▒▀██████▄
░███▀▒▒▒▒SPAMLY▒▒▒▒▒▀█████
░▐██▒▒▒▒▒▒DOODLY▒▒▒▒▒▒████▌
░▐█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▌
░░█▒▄▀▀▀▀▀▄▒▒▄▀▀▀▀▀▄▒▐███▌
░░░▐░░░▄▄░░▌▐░░░▄▄░░▌▐███▌
░▄▀▌░░░▀▀░░▌▐░░░▀▀░░▌▒▀▒█▌
░▌▒▀▄░░░░▄▀▒▒▀▄░░░▄▀▒▒▄▀▒▌
░▀▄▐▒▀▀▀▀▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒█
░░░▀▌▒▄██▄▄▄▄████▄▒▒▒▒█▀
░░░░▄██████████████▒▒▐▌
░░░▀███▀▀████▀█████▀▒▌
░░░░░▌▒▒▒▄▒▒▒▄▒▒▒▒▒▒▐
░░░░░▌▒▒▒▒▀▀▀▒▒▒▒▒▒▒▐
'''

