from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd
import pickle
import json
import gc
import csv
import requests
from recipe_scrapers import scrape_html
from tqdm import tqdm


# If you save the any url lists for taking too long, 
# you can use this module to load saved file

# Function to loading the url list
def load_url_list(file) -> list:
    
    name = str(file)
    url_list = []
    
    with open(name, 'r', newline='') as f:
        reader = csv.reader(f)
        for read in reader:
            url_list = read
    
    return url_list