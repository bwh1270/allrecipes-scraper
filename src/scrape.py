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


# Funtion to scraping the recipe
def recipe_scraping(recipe_lists: list) -> object:
    
    columns = ['title', 'total_time', 'ingredients','instructions', 'servings', 'nutrients']
    df = pd.DataFrame([], columns=columns)
    i = 0
    
    for recipe in tqdm(recipe_lists):
        
        html = requests.get(recipe).content
        scraper = scrape_html(html=html, org_url=recipe)
    
        # If there is no information of specific column in recipes, just pass
        try:
            df.at[i, columns[0]] = scraper.title()
            df.at[i, columns[1]] = scraper.total_time()
            df.at[i, columns[2]] = scraper.ingredients()
            df.at[i, columns[3]] = scraper.instructions()
            df.at[i, columns[4]] = scraper.yields()
            df.at[i, columns[5]] = scraper.nutrients()
        
        except:
            pass
        
        i += 1

    #print(df.head())
    
    return df
