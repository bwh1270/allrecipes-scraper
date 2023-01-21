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
from extract_category_url import get_url_categories
from extract_recipe_url import get_title_recipe, get_other_recipe
from scrape import recipe_scraping


def main():
    
    # Top category url is the starting urls
    start_url = "https://www.allrecipes.com/recipes/"

    # make first category list in start_url page.
    first_url_list = []
    page = urlopen(start_url)
    soup = BeautifulSoup(page, "lxml")

    html_urls = soup.find_all('li', {'class': "comp taxonomy-nodes__item mntl-block"})
    for html in html_urls:
        temp = re.search('(?<=href="https://www.allrecipes.com/recipes)(.*)(?=/")', str(html))
        if temp != None:
            temp = "https://www.allrecipes.com/recipes" + str(temp.group() + "/")
            first_url_list.append(temp)

    """
    # save the first url list
    with open("../data/first_url_list", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(first_url_list)
        print("first_url_list saved successfully")
    """
    
    category_list = []
    old_cnt = 0
    temp_lists = first_url_list
    while (1):
        category_list += temp_lists
        print("------------")
        print({old_cnt})
        print(len(temp_lists))
        print("------------")
        low_url_lists, new_cnt = get_url_categories(temp_lists)
        
        # the lowest page must be more than one
        if ((new_cnt <= old_cnt) and (old_cnt > 0)):
            print("Crawling has just finished!")
            break;
        
        old_cnt = new_cnt
        temp_lists = low_url_lists

    
    category_list = list(set(category_list)) # remove the overlapped urls
    print(len(category_list))
    
    title_recipe_list = get_title_recipe(category_list)
    other_recipe_list = get_other_recipe(category_list)
    
    df_title_recipe = recipe_scraping(title_recipe_list)
    df_other_recipe = recipe_scraping(other_recipe_list)
    
    df_allrecipes = pd.concat([df_title_recipe, df_other_recipe])
    
    # save the allrecipes to csv file
    df_allrecipes.to_csv("../data/Allrecipes.csv", header=True, index=False)



if __name__ == "__main__":
    main()

    