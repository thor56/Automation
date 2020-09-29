from selenium import webdriver
import time

browser = webdriver.Chrome()

link1 = 'https://affiliate-program.amazon.com/home'
link2 = 'https://www.amazon.com/gp/product/B01HK0W01E?pf_rd_r=P0CXCD91483KJ3R4HRKB&pf_rd_p=edaba0ee-c2fe-4124-9f5d-b31d6b1bfbee'

# First Part Associate Sign in
browser.get(link1)
u_name = browser.find_element_by_id('ap_email')
u_name.send_keys('tcfutube@gmail.com')
pass_wd = browser.find_element_by_id('ap_password')
pass_wd.send_keys('9441813435@rk')
button = browser.find_element_by_id('signInSubmit')

button.click()
time.sleep(5)

# Second part  --- Scrapping

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[1])
browser.get(link2)
time.sleep(5)

text = browser.find_element_by_id('amzn-ss-text-link')
text.click()

time.sleep(4)
text2 = browser.find_element_by_id('amzn-ss-full-link-radio-button')
text2.click()

time.sleep(2)
text3 = browser.find_element_by_id('amzn-ss-text-fulllink-textarea')
text_3 = text3.text
print(text_3)