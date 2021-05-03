from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="./chromedriver.exe")

# 2. Mở URL của post
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSe8ANxvWvTfd79UcJM1S5ZLrT7_5w_snVbyOQsk6C6_zNojRQ/viewform")

sleep(5)

label_fill = browser.find_elements_by_xpath("//div[@aria-level='3']")
print(len(label_fill))
for i in label_fill:
	print(i.text)

textbox_fill = browser.find_elements_by_xpath("//div[@class='quantumWizTextinputPaperinputInputArea']")
print(len(textbox_fill))
for j in textbox_fill:
	print(j.text)


# for i in range(5):
# 	classes = browser.find_element_by_class_name("freebirdFormviewerComponentsQuestionBaseTitle")

# 	print(classes.text)

# 6. Đóng browser
browser.close()