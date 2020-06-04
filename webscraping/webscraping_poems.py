'''
    Webscraping poetryfoundation.org for poems
'''

import urllib.request
import bs4 as bs
import re
# selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def pretty_text(text):
    final = (((text).replace(u'\xa0', u' ')).replace(u'\r ',u'\n'))
    return final

# create a BeautifulSoup object
#url = "https://www.poetryfoundation.org/poems/150097"
url = "https://www.poetryfoundation.org/poetrymagazine/poems/152094/fingers-on-a-gay-man"
header = {'User-Agent' : 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=header)
sauce = urllib.request.urlopen(req).read()
soup = bs.BeautifulSoup(sauce, 'html.parser') #BeautifulSoup object

poem = (pretty_text(soup.find_all('div', class_="o-poem")[0].text))
print(poem)

'''
# path for the chrome driver
path = r"/Users/emilymittleman/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path = path)

site = "https://www.poetryfoundation.org/poems/browse#page=&sort_by=recently_added"
driver.get(site)

html_source = driver.page_source

soup = bs.BeautifulSoup(html_source, features='html.parser')
soup.find_all("a", href=re.compile('.*/poems/[0-9]+/.*'))
'''
