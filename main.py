from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
dv = webdriver.Firefox()
#Nhập id của tác giả
id = '37268947300'
dv.get('https://ieeexplore.ieee.org/author/'+id)
#Nếu bị lỗi thì tăng giá trị time.sleep() để chờ trang load đầy đủ
time.sleep(10)
num = dv.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]').text
num = int(num)
perpage = num // 25 + 1
items = []
dict = {'Title': []}
for j in range(1, perpage+1):
    url = "https://ieeexplore.ieee.org/author/"+id+"?searchWithin=%22Author%20Ids%22:"+id+"&history=no&sortType=newest&highlight=true&returnFacets=ALL&returnType=SEARCH&pageNumber={}".format(j)
    dv.get(url)
    # Nếu bị lỗi thì tăng giá trị time.sleep() để chờ trang load đầy đủ
    time.sleep(10)
    paper = dv.find_elements(by=By.CLASS_NAME, value='List-results-items')
    i = 3
    for item in paper:
        xpath="""/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/main/div[2]/div[2]/xpl-results-list/div[%s]/xpl-results-item/div[1]/div[1]/div[2]/h2"""%(i)
        title = item.find_element(by=By.XPATH, value=xpath).text
        print(title)
        items.append(title)
        i += 1
dict['Title'].extend(items)
df = pd.DataFrame(dict)
df.to_csv('output.csv')
dv.close()