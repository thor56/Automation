# Using an existing Chrome session
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import ast

# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#
# #       Change chrome driver path accordingly
# chrome_driver = "E:\PROJECTS\Automation\chromedriver.exe"
# browser = webdriver.Chrome(chrome_driver, options=chrome_options)


def orderDescription(description):
    base_code = ''
    desc = ast.literal_eval(description)
    for bullet in desc:
        base_code = base_code + '<li>' + bullet + '</li>'
    return base_code


def GenerateCode(index, title, link, description, sideHeading, paragraph):
    base_code = ''
    base_code = base_code + '<!-- wp:heading {"level":3} --><h3>' + str(index + 1) + ' <a href="' + link + '">' + title + '</a></h3><!-- /wp:heading --> <!-- wp:media-text --><div class="wp-block-media-text alignwide is-stacked-on-mobile"><figure class="wp-block-media-text__media"></figure><div class="wp-block-media-text__content"><!-- wp:list --><ul>' + orderDescription(description) + '</ul><!-- /wp:list --></div></div><!-- /wp:media-text --><!-- wp:buttons {"align":"center"} --><div class="wp-block-buttons aligncenter"><!-- wp:button --><div class="wp-block-button"><a class="wp-block-button__link" href="' + link + '">check on amazon</a></div><!-- /wp:button --></div><!-- /wp:buttons --><!-- wp:heading {"level":4} --><h4>' + sideHeading + '</h4><!-- /wp:heading --><!-- wp:paragraph --><p>' + paragraph + '</p><!-- /wp:paragraph -->'
    return base_code


PostDataFrame = pd.read_csv('post_desc.csv')
DataFromTable = pd.read_csv('TableInput.csv')

DataFromTable = DataFromTable.join(PostDataFrame)

code = ''

for index, row in DataFromTable.iterrows():
    code = code + GenerateCode(index, row.title, row.url, row.description, row.SideHeading, row.Paragraph)



# storing the description as bullets into a file
outFileName="test.txt"
outFile=open(outFileName, "w")
outFile.write(code)
outFile.close()
