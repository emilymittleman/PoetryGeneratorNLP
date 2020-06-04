import urllib.request
import bs4 as bs
import pandas as pd
import re
import numpy as np
from multiprocessing import Pool
import time
import sys
# For simulating the table on the webpage which is dynamically loaded.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Reformats the string into readable text.
def pretty_text(text):
    final = (((text).replace(u'\xa0', u' ')).replace(u'\r ',u'\n'))
    return final

def parse(url):    
    try:
        hdr = {'User-Agent':'Mozilla/5.0'}
        req = urllib.request.Request(url,headers=hdr)
        sauce = urllib.request.urlopen(req, timeout=10).read()
        soup = bs.BeautifulSoup(sauce,'html.parser') #BeautifulSoup object

        # Data Extraction from the url.
        poem = (pretty_text(soup.find_all('div', class_="o-poem")[0].text))
        
        return poem

    except Exception as IndexError:
        return "\nno poem here\n"
    except Exception as e:
        print(e)
        return "\nno poem here\n"

def load(total_pages, total_batches):
    file_names = [""]*total_batches
    for i in range(0,total_batches):
        #File name formating.
        file_names[i] = "PoetryFoundationUrls"+str(i*total_pages+1)+"-"+str(total_pages*(i+1))+".txt"
    return file_names

def main():
    #File name details.
    '''
    total_pages = 10
    urls_per_page = 20
    total_batches = 5
    '''
    
    total_pages = 500
    urls_per_page = 20
    total_batches = 2
    
    total_poems = total_pages*urls_per_page
    
    url_file_names = load(total_pages, total_batches)
    file_name = url_file_names[1]
    file_name = 'PoetryFoundationUrls601-1000.txt'
    
    urls = np.loadtxt(file_name, dtype="str")

    # makes new file with the poems from URL's x - y 
    f = open("PoemData/PoetryFoundationData" + file_name[len("PoetryFoundationUrls"):], "w")

    for i in range(total_poems):
        f.write(parse(urls[i]) + "\n\n^^EOP^^\n")
        if (i+1) % 100 == 0:
            print(i+1)
        
    f.close()
    print("SUCCESSFUL")


if __name__ == '__main__':
    main()
