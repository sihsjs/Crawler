
# coding: utf-8

# In[13]:

import re
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import requests


# In[2]:

# driver = webdriver.Firefox()
# driver.get('https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20160729900681')

# html = driver.page_source
# soup = BeautifulSoup(html)


# In[3]:

# driver1 = webdriver.Firefox()
# driver1.get('https://dart.fss.or.kr/dsac001/mainY.do')
# html = driver1.page_source
# soup = BeautifulSoup(html)
# codes = soup.findAll('td')
# driver1.close()


# In[4]:

# codes[2].find('a')['href']
# codes[2].find('a')


# In[5]:

def get_dart_urls(driver, main_url='https://dart.fss.or.kr/dsac001/mainY.do'):
    driver.get(main_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    codes = soup.findAll('td')
    
    report_urls = {}
    for code in codes:
        href = ""
        url = ""
        if code.find('a') is not None:
            href = code.find('a')['href']
        if "rcpNo" in href:
            url = "http://dart.fss.or.kr" + href
            date = re.findall('\d+', url)[-1]
            date = pd.to_datetime(date[:8])
            if "최대주주등소유주식변동신고서" in code.find('a')['title']:
                if date in report_urls.keys():
                    report_urls[date].append(url)
                else:
                    report_urls[date] = []
                    report_urls[date].append(url)
    
    return report_urls


# In[6]:

def get_iframe_urls(driver, url):
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    src = "https://dart.fss.or.kr" + soup.findAll('iframe')[0]['src']
    return src


# In[128]:

def get_stock_changes(url):
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text, 'lxml')
    tables = soup.findAll('table', attrs={'id':"XFormD1_Form0_RepeatTable0"})
    for table in tables:
        for block in table.findAll('tr'):
            name = ""
            time_change = []
            amt_change = []
            spans = table.findAll('span')
            for index, span in enumerate(spans):
                if spans[index].contents == ['성명']:
                    name = spans[index+1].contents
                    gap = 0
                    while index+23+gap < len(spans):
                        time_change.append(spans[index+23+gap].contents)
                        amt_change.append(spans[index+27+gap].contents)
                        print(name, time_change[-1], amt_change[-1])
                        gap += 7    


# In[106]:

report_urls


# In[107]:

driver = webdriver.Firefox()
report_urls = get_dart_urls(driver)
iframe_urls = {}
for date in report_urls.keys():
    iframe_urls[date] = []
    urls = report_urls[date]
    for url in urls:
        iframe_urls[date].append(get_iframe_urls(driver, url))
driver.close()


# In[129]:

for date in report_urls.keys():
    for iframe_url in iframe_urls[date]:
        print(iframe_url)
        get_stock_changes(iframe_url)


# In[94]:




# In[ ]:




# In[ ]:

report_urls = get_dart_urls()


# In[ ]:

iframe_url = {}
for date in report_urls.keys():
    iframe_url[date] = []
    urls = report_urls[date]
    for url in urls:
        iframe_url[date].append(get_iframe_urls(url))


# In[ ]:

def get_iframe_urls(url):
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    src = "https://dart.fss.or.kr" + soup.findAll('iframe')[0]['src']
    driver.close()
    
    return src


# In[ ]:

driver = webdriver.Firefox()
driver.get(src)
driver.close()


# In[ ]:




# In[ ]:

soup.findAll('iframe')[0]['src']


# In[ ]:

codes[2].find('a')['href']


# In[ ]:

'rcpNo' in codes[1].find('a')['href']


# In[ ]:



