from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.daraz.pk/smartphones/?spm=a2a0e.home.cate_1.1.6a274937HKedFN'
driver.get(url)

def scrape(css):
    try:
        elem = driver.find_element(By.CSS_SELECTOR, css).text
        return elem
    except Exception:
        None

PD_links_list = []
PD_links = driver.find_elements(By.CSS_SELECTOR,'.c2prKC .c16H9d>a')
for PD in PD_links: PD_links_list.append(PD.get_attribute('href'))
for url in PD_links_list:
    driver.get(url)
    print('Product URL: ',url)
    PD_img = driver.find_element(By.CSS_SELECTOR,'.gallery-preview-panel__image').get_attribute('src')
    print(PD_img)
    PD_Title = scrape('.pdp-mod-product-badge-title') #driver.find_element(By.CSS_SELECTOR,'.pdp-mod-product-badge-title').text
    print(PD_Title)
    PD_Price = scrape('span.pdp-price_size_xl')# driver.find_element(By.CSS_SELECTOR,'span.pdp-price_size_xl').text
    print(PD_Price)
    # Ratings = driver.find_element(By.CSS_SELECTOR,'.pdp-stars_size_s+ .pdp-review-summary__link').text
    Avg_Score = scrape('span.score-average')#driver.find_element(By.CSS_SELECTOR,'span.score-average').text
    print(Avg_Score)
    Pv_Sel_Rat = scrape('.rating-positive')#driver.find_element(By.CSS_SELECTOR,'.rating-positive').text
    print(Pv_Sel_Rat)
    Avg_Shiping = scrape('.info-content:nth-child(2) .seller-info-value')#driver.find_element(By.CSS_SELECTOR,'.info-content:nth-child(2) .seller-info-value').text
    print(Avg_Shiping)
    Avg_Chat_res = scrape('.info-content:nth-child(3) .seller-info-value')#driver.find_element(By.CSS_SELECTOR,'.info-content:nth-child(3) .seller-info-value').text
    print(Avg_Chat_res)
    Delivery_Time = scrape('.delivery-option-item__time')#driver.find_element(By.CSS_SELECTOR,'.delivery-option-item__time').text
    print(Delivery_Time)
    Sold_by = scrape('.seller-name__detail-name')#driver.find_element(By.CSS_SELECTOR,'.seller-name__detail-name').text
    print(Sold_by)






# pages = driver.find_elements(By.CSS_SELECTOR,'ul.ant-pagination>li')
# for next in range(1,len(pages)-1):
#     driver.find_element(By.CSS_SELECTOR,"li[title='Next Page']>a").click()

