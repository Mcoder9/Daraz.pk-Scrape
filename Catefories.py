from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.daraz.pk'
driver.get(url)


def select_cat(cat_list):
    i = 1
    for cat in cat_list:
        item = cat.get_attribute('innerHTML')
        print(f'{i}>: {item}')
        i += 1

def grand_dic(l1,l2):
    item_list = []
    link_list = []
    for item in l1:
        item_list.append(item.get_attribute('innerHTML'))
    for item in l2:
        link_list.append(item.get_attribute('href'))
    grand_item_dic = dict(zip(item_list,link_list))

cat_grand = driver.find_elements(By.CSS_SELECTOR, '.lzd-site-menu-root>li>a>span')
select_cat(cat_grand)
root = int(input('Select category\n>: '))

sub_items = driver.find_elements(By.CSS_SELECTOR,f'ul[data-spm="cate_{root}"]>li>a>span')
subroot_len = driver.find_elements(By.CSS_SELECTOR,f'.Level_1_Category_No{root}>li')
sub_item_dic = {}
for sub in range(1,len(subroot_len)+1):
    sub_item = driver.find_element(By.CSS_SELECTOR,f'li[data-cate="cate_{root}_{sub}"]>a>span').get_attribute('innerHTML')
    sub_item_link = driver.find_element(By.CSS_SELECTOR,f'li[data-cate="cate_{root}_{sub}"]>a').get_attribute('href')
    sub_item_dic.setdefault(sub_item,sub_item_link)

select_cat(sub_items)
sub = int(input('Select Sub_Category\n>: '))
goto = int(input('1>: Goto this \n99>: Goto Sub-Items\n>:'))
if goto==1:
    url = list(sub_item_dic.values())[sub-1]
    driver.get(url)

grand_items = driver.find_elements(By.CSS_SELECTOR,f'li[data-cate="cate_{root}_{sub}"]>ul>li>a>span')

for grand in range(1,len(grand_items)+1):
    grand_items = driver.find_elements(By.CSS_SELECTOR,f'li[data-cate="cate_{root}_{sub}"]>ul>li>a>span')
    grand_item_links = driver.find_elements(By.CSS_SELECTOR,f'li[data-cate="cate_{root}_{sub}"]>ul>li>a')
    item_list = []
    link_list = []
    for item in grand_items:
        item_list.append(item.get_attribute('innerHTML'))
    for item in grand_item_links:
        link_list.append(item.get_attribute('href'))
    grand_item_dic = dict(zip(item_list, link_list))

if goto==99:
    select_cat(grand_items)
    if select_cat(grand_items) is None:
        url = list(sub_item_dic.values())[sub-1]
        print('Nothing more Sub-Items')
    else:
        goto = int(input('Goto Sub-Item\n>: '))
        url = list(grand_item_dic.values())[goto-1]
    driver.get(url)
