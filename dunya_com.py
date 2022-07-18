import requests
from bs4 import BeautifulSoup
import time



class Finder:
    
    def getLinks(self, url, name):
        
        page = requests.get(url)
        html = page.text
        soup = BeautifulSoup(html, 'html.parser')
        news = soup.find_all("a", {"class": ['box']})    
        for new in news:
            with open(f'{name}.text', 'a') as file:
                file.write(new['href']+'\n')

finder = Finder()  

line = "https://www.abc.com/sirketler/"
name = line.split('com')[-1].replace('/', ' ')

for i in range(1,1389):
    url = line + str(i)
    finder.getLinks(url, name)
    print(f'{i}: taken!')
    time.sleep(2)
          
print('Process finished!')
