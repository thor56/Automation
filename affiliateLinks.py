import clipboard
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# browser = webdriver.Chrome()

link1 = 'https://affiliate-program.amazon.com/home'

bullets = []


def getAllData(link2):
    lis2 = []
    browser.get(link2)
    time.sleep(2)
    #      ASSOCIATE URL
    text_box = browser.find_element_by_id('amzn-ss-text-link')
    text_box.click()
    time.sleep(1)
    text_full_link = browser.find_element_by_id('amzn-ss-full-link-radio-button')
    text_full_link.click()
    time.sleep(1)
    text_url = browser.find_element_by_id('amzn-ss-text-fulllink-textarea')
    lis2.append(text_url.text)

    #      ASSOCIATE IMAGE URL
    image_box = browser.find_element_by_id('amzn-ss-image-link')
    image_box.click()
    time.sleep(1)
    image_url = browser.find_element_by_id('amzn-ss-image-textarea')
    lis2.append(image_url.text)

    #       PRODUCT TITLE
    product_title = browser.find_element_by_id('productTitle')
    lis2.append(product_title.text)

    #       PRODUCT DESCRIPTION
    html_list = browser.find_element_by_id("feature-bullets")
    items = html_list.find_elements_by_tag_name("li")
    desc_bullets = []
    for item in items:
        text = item.text
        desc_bullets.append(text)
    lis2.append(desc_bullets)
    bullets.append(desc_bullets)

    return lis2


def orderDescription(bullets):
    base_code = ''
    for desc in bullets:
        base_code = base_code + '<div class="cg-tbl-ul"><ul>'
        for bullet in desc:
            base_code = base_code + '<li>' + bullet + '</li>'
        base_code = base_code + '</ul></div>'
    return base_code


# Using an existing Chrome session
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

#       Change chrome driver path accordingly
chrome_driver = "D:\PROJECT\Automation\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver, options=chrome_options)


#       READING THE LINKS FROM EXCEL SHEET

links_df = pd.read_csv("links.csv")
lis = []
lis3 = []

for index, row in links_df.iterrows():
    lis.append(row.links)

#       ITERATING THROUGH EACH LINK

for link in lis:
    lis3.append(getAllData(link))

links_df2 = pd.DataFrame(lis3, columns=['url','image','title','description'])

links_df2.to_csv('TableInput.csv')

# storing the description as bullets into a file
outFileName="bullets.txt"
outFile=open(outFileName, "w")
outFile.write(orderDescription(bullets))
outFile.close()
