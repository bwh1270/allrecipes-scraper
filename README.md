# allrecipes-scraper
[![Latest Unstable Version](https://poser.pugx.org/buonzz/laravel-4-freegeoip/v/unstable.svg)](https://packagist.org/packages/buonzz/laravel-4-freegeoip) [![License](https://poser.pugx.org/buonzz/laravel-4-freegeoip/license.svg)](https://packagist.org/packages/buonzz/laravel-4-freegeoip)
---
The recipe information will help the food domain, like food computing.
This code cand be classified into two modules. The Fisrt module is crawling which is about finding URLs on the web. The second module is scraping which is about extracting the data of recipe from one or more websites. This code is tested in Linux 16.04 LTS, Window10, and Window11. But, it will work in other environments. 


Just follow the install part!

## Installation
---
You can clone or download this repository in your folder.
```
$ git clone https://github.com/bwh1270/allrecipes-scraper.git {your_folder_name}
```

And install the requirement packages.
```
$ pip install -r requirements.txt
```

Execute the main.py file. It may take long time depending on your internet speed. In my case, it took 4-5 hours.
```
$ python3 main.py
```
※ Be careful not to lose your internet connection.


## Modules
---
There are important three modules in src folder.
1. crawl_category_url.py
2. crawl_recipe_url.py
3. scrape.py


First one, the function to crawling the category urls from top category to the lowest categories. In the image below, Category url means the things inside the blue box.
![image](https://user-images.githubusercontent.com/98958137/213866967-a042f967-68ab-4175-a25f-43ffbe1fb064.png)


Second one, the function to crawling the recipe urls in each category urls.


And last, the function to scrape the recipe information with "/hhursev/recipe-scrapers" in each recipe urls.




Distributed under the MIT license. See LICENSE for more information.
