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


# Funtion to crawl the urls about recipes at the category urls

# title_recipes are the representative recipes at the top of the page.
def get_title_recipe(url_lists: list) -> list:
    temp_list = []
    cnt = 0
    
    for url in tqdm(url_lists):
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        html_url = soup.find_all('a', 
                                 {'class': 'comp card--image-top mntl-card-list-items mntl-document-card mntl-card card card--no-image'})
        if len(html_url) != 0:
            for html in html_url:
                temp = re.search('(?<=href="https://www.allrecipes.com/)(.*)(?=/")', str(html))
        
                if temp != None:
                    temp = "https://www.allrecipes.com/" + str(temp.group() + "/")
                    temp_list.append(temp)
        else:
            cnt += 1

    url_list = list(set(temp_list)) # remove the overlapped urls

    print(f"{cnt} of the urls does not have title recipe")
    print(f'{len(temp_list)-len(url_list)} of the recipe urls are removed because of overlapped.')
    
    return url_list


# other_recipes are all recipes except representative recipes at the same page.
def get_other_recipe(url_lists: list) -> list:
    temp_list = []
    cnt = 0
    
    for url in tqdm(url_lists):
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        html_url = soup.find_all('a', 
                                 {'class': 'comp mntl-card-list-items mntl-document-card mntl-card card card--no-image'}) # here different
        if len(html_url) != 0: 
            for html in html_url:
                temp = re.search('(?<=href="https://www.allrecipes.com/)(.*)(?=/")', str(html))
        
                if temp != None:
                    temp = "https://www.allrecipes.com/" + str(temp.group() + "/")
                    temp_list.append(temp)
        else:
            cnt += 1

    url_list = list(set(temp_list))

    print(f"{cnt} of the urls does not have title recipe")
    print(f'{len(temp_list)-len(url_list)} of the recipe urls are removed because of overlapped.')
    print(f'number of recipes: {len(url_list)}')
    
    return url_list