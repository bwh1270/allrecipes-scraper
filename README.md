# allrecipes-scraper
The recipe information will help the food domain, like food computing.
This code cand be classified into two modules. The Fisrt module is crawling which is about finding URLs on the web. The second module is scraping which is about extracting the data of recipe from one or more websites. This code is tested in Linux 16.04 LTS, Window10, and Window11. But, it will work in other environments. 


Just follow the installation part!


## Installation
You can clone or download this repository in your folder.
```
$ git clone https://github.com/bwh1270/allrecipes-scraper.git {your_folder_name}
```


And install the requirement packages.
```
$ pip install -r requirements.txt
```


Execute the main.py file. It may take long time depending on your internet speed. In my case, it took 4-5 hours.


##### Linux
```
$ python3 main.py
```
※ Be careful not to lose your internet connection.


##### Window
```
> python main.py
```
※ Be careful not to lose your internet connection.




## Modules
There are important three modules in src folder.
+ crawl_category_url.py
+ crawl_recipe_url.py
+ scrape.py



First one, the function to crawling the category urls from top category to the lowest categories. 


In the image below, Category url means the things inside the blue box. 


![image](https://user-images.githubusercontent.com/98958137/213866967-a042f967-68ab-4175-a25f-43ffbe1fb064.png)


Second, the function to crawling the recipe urls in each category urls.


Last, the function to scrape the recipe information in each recipe urls using the package of "/hhursev/recipe-scrapers"




--- 
This project is licensed under the terms of the MIT license.
