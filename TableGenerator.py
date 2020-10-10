from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import re
import clipboard


link = "https://startblogging.co/affiliate-product-table-generator"

def InsertRow(title,url,image,description,count):

        # add product
    browser.find_element_by_xpath('/html/body/div/div/div/div[1]/main/div/div/div[1]/div/div/div[2]/button').click()
    # title
    browser.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div[1]/div/div/div[2]/div[1]/div[' + str(count + 1) + ']/div/div[1]/div[1]/div/div[1]/div/input').send_keys(title)
    # image
    image1 = re.search('src="(.*)" ></a>', image).group(1)
    browser.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div[1]/div/div/div[2]/div[1]/div[' + str(count + 1) + ']/div/div[2]/div[1]/div/div[1]/div/input').send_keys(image1)
    # url
    browser.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div[1]/div/div/div[2]/div[1]/div[' + str(count + 1) + ']/div/div[2]/div[2]/div/div[1]/div/input').send_keys(url)
    # description
    browser.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div[1]/div/div/div[2]/div[1]/div[' + str(count + 1) + ']/div/div[1]/div[3]/div/div[1]/div/textarea').send_keys(description)

# Using an existing Chrome session
# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

#       Change chrome driver path accordingly
# chrome_driver = "D:\PROJECT\Automation\chromedriver.exe"
# browser = webdriver.Chrome(chrome_driver, options=chrome_options)
firefox_Driver = "D:\PROJECT\Automation\geckodriver-v0.27.0-win64"
browser = webdriver.Firefox(firefox_Driver)


data_df = pd.read_csv("TableInput.csv")

browser.get(link)

# Looping and creating table rows
count = 0
for index, row in data_df.iterrows():
    InsertRow(row.title,row.url,row.image,row.description,count)
    count = count + 1
    time.sleep(2)

# adjusting the final table
browser.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div[1]/div/div/div[2]/div[1]/div[' + str(count + 1) + ']/div/div[2]/button').click()
# Fetching final table code
browser.find_element_by_xpath('/html/body/div/div/div/div[1]/main/div/div/div[1]/div/div/div[2]/div[2]/button[1]/span').click()
browser.find_element_by_xpath('/html/body/div/div/div/div[3]/div/div/div[2]/button[1]/span').click()

# storing the final table into a file
outFileName="final.txt"
outFile=open(outFileName, "w")
outFile.write(clipboard.paste())
outFile.close()

