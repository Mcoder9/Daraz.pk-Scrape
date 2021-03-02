from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install())
import time
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException  
import pyperclip,sys
sys.setrecursionlimit(2000)

def OTP_Verification():
    try:
        pyperclip.copy(input('Enter OTP: '))
        filed = driver.find_element(By.CSS_SELECTOR,'._27cR_W>input:nth-child(2)')
        filed.click()
        action = ActionChains(driver) 
        action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        driver.find_element(By.CSS_SELECTOR,'._35rr5y').click()
    except:
        pass
def check_stock():
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'._2_ItKR .items-center div+ div')))
        stock = driver.find_element(By.CSS_SELECTOR,'._2_ItKR .items-center div+ div').text.split()
        if int(stock[0])>0:
            print(f'{stock} piece available')
            pass
        else:
            print('Out of stock')
            driver.refresh()
            time.sleep(0.5)
            check_stock()
    except IndexError as IE:
        print(IE)
        check_stock()


login_url = 'https://shopee.com.my/buyer/login?next=https%3A%2F%2Fshopee.com.my%2F'
driver.get(login_url)
driver.maximize_window()
driver.implicitly_wait(5)
try:
    driver.find_element(By.CSS_SELECTOR,'div.language-selection__list > div:nth-child(1) > button').click() # Language select
except:
    pass
try:
    driver.find_element_by_css_selector('.shopee-popup__close-btn').click() # Pop-up remove
except:
    pass

# # Login
# driver.find_element(By.NAME,'loginKey').send_keys('0192482084')# haiderjoia185@gmail.com # 0192482084
# driver.find_element(By.XPATH,'//*[@placeholder="Password"]').send_keys('Testfiver123')
# wait = WebDriverWait(driver, 10)
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'._2h_2_Y')))
# driver.find_element(By.CSS_SELECTOR,'._2h_2_Y').click() # Submit

# #Verify-OTP
# OTP_Verification()
input('Stop: ')

try:
    driver.find_element_by_css_selector('.shopee-popup__close-btn').click() # Pop-up remove
except:
    pass

# Stock Checking
PS5_URL = (input('Enter the Url of PS5:'))
driver.get(PS5_URL)
check_stock()
# Buy and Checkout
driver.find_element(By.CSS_SELECTOR,'.product-variation:nth-child(1)').click() # Variation
driver.find_element(By.CSS_SELECTOR,'.QpIzUA:nth-child(2)').click() # Buy-Now
wait = WebDriverWait(driver, 10)
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button>.cart-page-footer__checkout-text')))
check_out = driver.find_element(By.CSS_SELECTOR,'.shopee-button-solid--primary')
driver.execute_script("arguments[0].click();", check_out)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.checkout-payment-setting__payment-methods-tab>span:nth-child(4)')))
# driver.find_element(By.CSS_SELECTOR,'.checkout-payment-setting__payment-methods-tab>span:nth-child(4)').click()
try:
    driver.find_element(By.CSS_SELECTOR,'span:nth-child(1) .product-variation--selected')
except NoSuchElementException:
    driver.find_element(By.CSS_SELECTOR,'span:nth-child(1) .product-variation').click()
driver.find_element(By.CSS_SELECTOR,'.stardust-button').click() # Place order
driver.find_element(By.ID,'pay-button').click() # pay-button


