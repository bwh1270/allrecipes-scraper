from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import json
import pickle
import csv
import pandas as pd
from tqdm import tqdm
from recipe_scrapers import scrape_html
from utils import load_url_list


# Funtion to crawl the urls about categories from top category to lower
def get_url_categories(url_lists: list):
    
    temp_lists = []
    cnt = 0; 
    
    for url in tqdm(url_lists):
        
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        html_urls = soup.find_all('li', 
                                  {'class': "comp taxonomy-nodes__item mntl-block"})
        
        if len(html_urls) != 0:
            for html in html_urls:
                temp = re.search('(?<=href="https://www.allrecipes.com/)(.*)(?=/")',
                                 str(html))
                if temp != None:
                    temp = "https://www.allrecipes.com/" + str(temp.group() + '/')
                    temp_lists.append(temp)
                    
        # if the url is at the lowest category, cnt increases
        else: 
            # print("\nThere is no sub urls.")
            cnt += 1
    
    print(f"\n{cnt} of the urls don't have lower urls\n")
    temp_set = set(temp_lists) # remove the overlapped urls
    low_url_lists = list(temp_set)
    
    return low_url_lists, cnt