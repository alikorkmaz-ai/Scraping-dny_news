import requests
from bs4 import BeautifulSoup
import time
import random
import json


class Finder:
    
    def __init__(self):
        self.my_dict = {}
    
    def saveToFile(self, dict1):
        with open(f'economy.json', encoding="utf-8", mode='a') as file:
            s = json.dumps(dict1, sort_keys = False, ensure_ascii=False) + '\n'
            file.write(s)
    
    def getLinks(self, url):
        '''Using this function one can take all urls in given category link!'''
        page = requests.get(url)
        html = page.text
        soup = BeautifulSoup(html, 'html.parser')
        news = soup.find_all("a", {"class": ['box']})    
        for new in news:
            with open(f'urls.text', 'a') as file:
                file.write(new['href']+'\n')

    def randomChoser(self, i, a):
        url_list = []
        with open(f'{a}', 'r') as file:
            lines = file.readlines()
        for j in range(i):
            output = random.choice(lines)
            url_list.append(output)
        return url_list

    def getRandomNews(self, i, a):
        '''Using this function one can download all news which are chosen randomly!'''
        url_list = self.randomChoser(i,a)
        for line in url_list:
            url = line.strip()
            cate = url.replace('https://www.dunya.com/','').split("/")[:-1]
            category = str()
            for elem in cate:
                category = category + '_' + elem
            category = category[1:]
            page = requests.get(url)
            html = page.text
            soup = BeautifulSoup(html, 'html.parser')
            pub_date = soup.find_all("div", {"class": ['item-date']})[0].time['datetime'][:10]
            update = soup.find_all("div", {"class": ['item-date']})[1].time['datetime'][:10]
            title = soup.find("h1").text
            abstract = soup.find("h2").text
            content = soup.find("div", {"class": ['content-text']}).text
            html = soup.find("article")
            self.my_dict['published_date'] = pub_date
            self.my_dict['update'] = pub_date
            self.my_dict['category'] = category
            self.my_dict['url'] = url
            self.my_dict['title'] = title
            self.my_dict['abstract'] = abstract
            self.my_dict['content'] = content
            self.my_dict['html'] = str(html)
            
            self.saveToFile(self.my_dict)
            
    def getNews(self, a):
        '''Using this function one can download all news!'''
        url = line.strip()
        cate = url.replace('https://www.dunya.com/','').split("/")[:-1]
        category = str()
        for elem in cate:
            category = category + '_' + elem
        category = category[1:]
        page = requests.get(url)
        html = page.text
        soup = BeautifulSoup(html, 'html.parser')
        pub_date = soup.find_all("div", {"class": ['item-date']})[0].time['datetime'][:10]
        update = soup.find_all("div", {"class": ['item-date']})[1].time['datetime'][:10]
        title = soup.find("h1").text
        abstract = soup.find("h2").text
        content = soup.find("div", {"class": ['content-text']}).text
        html = soup.find("article")
        self.my_dict['published_date'] = pub_date
        self.my_dict['update'] = pub_date
        self.my_dict['category'] = category
        self.my_dict['url'] = url
        self.my_dict['title'] = title
        self.my_dict['abstract'] = abstract
        self.my_dict['content'] = content
        self.my_dict['html'] = str(html)
            
        self.saveToFile(self.my_dict)
        
finder = Finder()  

categories = [dunya, economy, finans, finansborsa, gundem, sektorler, sirketler]

for category in categories:
    line = f"https://www.dunya.com/{category}/"
    name = line.split('com')[-1].replace('/', ' ')
    for i in range(1,5037):
    url = line + str(i)
    finder.getLinks(url)
    print(f'{i}: taken!')
    time.sleep(2)

with open('urls.text', 'r') as f:
    lines = f.readlines()
i = 1
for line in lines:
    finder.getNews(line)
    print(f'{i}: taken!')
    time.sleep(2)
    i = i + 1
          
print('Process finished!')
