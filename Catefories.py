from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.daraz.pk'
driver.get(url)
# Get attributes form list of elements
def get_cats(cat_list):
    i = 1
    for cat in cat_list:
        item = cat.get_attribute('innerHTML')
        print(f'{i}) {item}')
        i += 1

# Conver list to dictionary
def lists_to_dic(l1,l2):
    item_list = []
    link_list = []
    for item in l1:
        item_list.append(item.get_attribute('innerHTML'))
    for item in l2:
        link_list.append(item.get_attribute('href'))
    global child_subcats_dic
    child_subcats_dic = dict(zip(item_list,link_list))

def first():
    cats = driver.find_elements(By.CSS_SELECTOR, '.lzd-site-menu-root>li>a>span')
    get_cats(cats)
    select_cat = int(input('\nCategory>: '))

    parent_subcats = driver.find_elements(By.CSS_SELECTOR,f'ul[data-spm="cate_{select_cat}"]>li>a>span')
    parent_subcats_len = driver.find_elements(By.CSS_SELECTOR,f'.Level_1_Category_No{select_cat}>li')
    parent_subcats_dic = {}
    for p_subcat in range(1,len(parent_subcats_len)+1):
        parent_subcat = driver.find_element(By.CSS_SELECTOR,f'li[data-cate="cate_{select_cat}_{p_subcat}"]>a>span').get_attribute('innerHTML')
        parent_subcat_link = driver.find_element(By.CSS_SELECTOR,f'li[data-cate="cate_{select_cat}_{p_subcat}"]>a').get_attribute('href')
        parent_subcats_dic.setdefault(parent_subcat,parent_subcat_link)
    
    
    def second():
        get_cats(parent_subcats)
        select_p_subcat = int(input('\nCategory>Parent-Subcategory>: '))
        conf_sel = int(input('1): Yes Go \n99): Goto Child-Subcategories\n00) Return Back\n>:'))
        #Grand work
        child_subcats = driver.find_elements(By.CSS_SELECTOR,f'li[data-cate="cate_{select_cat}_{select_p_subcat}"]>ul>li>a>span')
        child_subcats_link = driver.find_elements(By.CSS_SELECTOR,f'li[data-cate="cate_{select_cat}_{select_p_subcat}"]>ul>li>a')
        lists_to_dic(child_subcats,child_subcats_link)

        if conf_sel == 1:
            key = list(parent_subcats_dic.keys())[select_p_subcat-1]
            url = list(parent_subcats_dic.values())[select_p_subcat-1]
            print('You selected',key)
            driver.get(url)

        if conf_sel==99:
            get_cats(child_subcats)
            print('00) Return back')
            if len(child_subcats)<=0:
                key = list(parent_subcats_dic.keys())[select_p_subcat-1]
                url = list(parent_subcats_dic.values())[select_p_subcat-1]
                print(f'There are no Child-Subcategories for this Parent-Subcategory \nSo, {key} is selected.')
            else:
                select_c_subcat = int(input('Category> Parent-Subcategory >Child-Subcategory:> '))
                if select_c_subcat == 00:
                    second()
                else:
                    key = list(child_subcats_dic.keys())[select_c_subcat-1]
                    url = list(child_subcats_dic.values())[select_c_subcat-1]
                    print('You selected',key)
            driver.get(url)
        if conf_sel == 00:
            first()
    second()
first()