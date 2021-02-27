from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.daraz.pk/smartphones/?spm=a2a0e.home.cate_1.1.6a274937HKedFN'
driver.get(url)

def scrape_by_css(css,attr):
    if attr == 's':
        try:
            em_txt = driver.find_element(By.CSS_SELECTOR, css).text
        except:
            try:
                em_txt = driver.find_element(By.CSS_SELECTOR, css).get_attribute('innerHTML') 
            except NoSuchElementException:
                em_txt = None
        return em_txt
    else:
        ems = driver.find_elements(By.CSS_SELECTOR, css)
        for em in ems:
            try:
                em_txt = em.get_attribute('innerHTML')
            except:
                em_txt = em.text
            return em_txt


PD_links_list = []
PD_links = driver.find_elements(By.CSS_SELECTOR,'.c2prKC .c16H9d>a')
for PD in PD_links: PD_links_list.append(PD.get_attribute('href'))
for url in PD_links_list:
    driver.get(url)
    print('Product URL: ',url)
    PD_img = driver.find_element(By.CSS_SELECTOR,'.gallery-preview-panel__image').get_attribute('src')
    print('Image URL',PD_img)
    PD_Title = scrape_by_css('.pdp-mod-product-badge-title','s')
    print(PD_Title)
    PD_Price = scrape_by_css('span.pdp-price_size_xl','s')
    print(PD_Price)
    # Ratings = driver.find_element(By.CSS_SELECTOR,'.pdp-stars_size_s+ .pdp-review-summary__link').text
    Avg_Score = scrape_by_css('span.score-average','s')
    print(Avg_Score)
    Pv_Sel_Rat = scrape_by_css('.rating-positive','s')
    print(Pv_Sel_Rat)
    Avg_Shiping = scrape_by_css('.info-content:nth-child(2) .seller-info-value','s')
    print(Avg_Shiping)
    Avg_Chat_res = scrape_by_css('.info-content:nth-child(3) .seller-info-value','s')
    print(Avg_Chat_res)
    Delivery_Time = scrape_by_css('.delivery-option-item__time','s')
    print(Delivery_Time)
    Sold_by = scrape_by_css('.seller-name__detail-name','s')
    print(Sold_by)






# pages = driver.find_elements(By.CSS_SELECTOR,'ul.ant-pagination>li')
# for next in range(1,len(pages)-1):
#     driver.find_element(By.CSS_SELECTOR,"li[title='Next Page']>a").click()

