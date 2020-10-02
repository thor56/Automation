from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

link = "https://app.affiliatable.io/posts"

def CreateTable(postTitle):
    pass

def InsertRow(title,url,image,description):
    pass


# Using an existing Chrome session
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

#       Change chrome driver path accordingly
chrome_driver = "D:\PROJECT\Automation\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver, options=chrome_options)

metadata_df = pd.read_csv("TableDetails.csv")
data_df = pd.read_csv("TableInput.csv")

# getting table metadata
for index, row in metadata_df.iterrows():
    CreateTable(row.postTitle)

# Looping and creating table rows
for index, row in data_df.iterrows():
    InsertRow(row.title,row.url,row.image,row.description)

#  Saving the table output to clipboard
