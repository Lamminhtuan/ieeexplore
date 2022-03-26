from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
dv = webdriver.Firefox()
#Nhập id của tác giả
id = '37269460700'
dv.get('https://ieeexplore.ieee.org/author/'+id)
#Nếu bị lỗi thì tăng giá trị delay để chờ trang load đầy đủ
delay = 15
time.sleep(delay)
author = dv.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/h1/span[1]').text
print(f'Author:{author}')
num = dv.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]').text
num = int(num)
pages = num // 25 + 1
items = []
dict = {'Title': []}
for i in range(1, pages + 1):
    url = "https://ieeexplore.ieee.org/author/"+id+"?searchWithin=%22Author%20Ids%22:"+id+"&history=no&sortType=newest&highlight=true&returnFacets=ALL&returnType=SEARCH&pageNumber={}".format(i)
    dv.get(url)
    # Nếu bị lỗi thì tăng giá trị time.sleep() để chờ trang load đầy đủ
    time.sleep(delay)
    paper = dv.find_elements(By.CLASS_NAME, 'List-results-items')
    for j, item in enumerate(paper, start=3):
        xpath = '/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/main/div[2]/div[2]/xpl-results-list/div[{}]/xpl-results-item/div[1]/div[1]/div[2]/h2'.format(j)
        title = item.find_element(By.XPATH, xpath).text
        print(title)
        items.append(title)
dict['Title'].extend(items)
df = pd.DataFrame(dict)
df.to_csv(author+'.csv')
dv.close()
