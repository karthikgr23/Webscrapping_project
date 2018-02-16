#class="nba-player-index"

from selenium import webdriver
from bs4 import BeautifulSoup
#import time

driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver.get("http://www.imdb.com/chart/top?ref_=nv_mv_250_6")
soup = BeautifulSoup(driver.page_source,'lxml')
table = soup.find('table',class_ = 'chart full-width')
a =soup.find_all('a')
for td in table.find_all('td',class_ = 'titleColumn'):
    print(td.text.strip().replace('\n','').replace('      ',' ' ))
    print("link="+ td.a['href'],end='\n')
    #time.sleep(1)
    
