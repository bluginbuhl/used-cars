from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

URL = "https://www.vinaudit.com/market-value-tool"

chromeOptions = Options()
chromeOptions.headless = True
chromeOptions.add_argument("--log-level=3")

driver = webdriver.Chrome(PATH, options=chromeOptions)
driver.get(URL)


def parse_price(element):
    price = ""
    string = element.get_attribute("innerHTML")
    price += string.split(" ")[0][1:]
    return int(price.replace(',', ''))

def parse_mileage():
    mileage = ""
    string = driver.find_element_by_id('va_mv_mileage_text').get_attribute("innerHTML")
    mileage += string.split(" ")[0].replace(',', '')
    return int(mileage)

    
def get_vehicle_make_and_model():
    return driver.find_element_by_id('va_mv_vehicle1_text').get_attribute("innerHTML")
    

def get_market_values(vin):
    driver.refresh()
    market_values = {}
    driver.find_element_by_name('vin').send_keys(vin)
    driver.find_element_by_class_name('avia-button').click()
    time.sleep(1)
    
    below_mkt = driver.find_element_by_id('va_mv_leftlabel_text')
    avg_mkt = driver.find_element_by_id('va_mv_average_text')
    above_mkt = driver.find_element_by_id('va_mv_rightlabel_text')
    
    car_info = get_vehicle_make_and_model().split(' ')
    
    market_values['vin'] = vin
    market_values['year'] = car_info[0]
    market_values['make'] = car_info[1]
    market_values['model'] = car_info[2]
    if car_info[3]:
        # note: this is not quite perfect
        market_values['trim'] = car_info[3]
    market_values['mileage'] = parse_mileage()
    market_values['below'] = parse_price(below_mkt)
    market_values['average'] = parse_price(avg_mkt)
    market_values['above'] = parse_price(above_mkt)
    
    # driver.refresh()
    
    return market_values

# Paste VINs in the list
VIN_LIST = [
    # e.g.: 
    "5XYKT3A69DG353356",
]


df = pd.DataFrame()

for vin in VIN_LIST:
    print(f'Getting info for VIN: {vin}')
    d = get_market_values(vin)
    df = df.append(d, ignore_index=True)

column_order = ['vin', 'year', 'make', 'model', 'trim', 'mileage', 'below', 'average', 'above']

df = df[column_order]
print('\n -- DATA SUMMARY --')
print(df)