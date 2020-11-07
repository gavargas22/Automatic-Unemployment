import pandas as pd
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#-----------------------------------------------------------------------------#

# Login to Texas Workforce Commission website.
# driver = webdriver.Firefox(
#     executable_path=r'D:\Users\Matt\Documents\GitHub\Automatic-Unemployment\geckodriver.exe'
# )

# def login(url,usernameID,passwordID,login_button):
#     driver.get(url)
#     time.sleep(3)
#     driver.find_element_by_id(usernameID).send_keys('Hiebs915')
#     driver.find_element_by_id(passwordID).send_keys('UB92E0Kww')
#     driver.find_element_by_name(login_button).click()

# login(
#     'https://login.apps.twc.state.tx.us/UBS/security/logon.do',
#     'field.label.username',
#     'field.label.password',
#     'method:logon'
# )

# def payment_request(payment_request):
#     driver.find_element_by_xpath(payment_request).click()
#     if (driver.find_element_by_class_name('page-name').text) == 'Early Filing':
#         print('Try to file again on:',
#         driver.find_element_by_class_name('page-block').text[162:180])
#         driver.quit()

# payment_request(
#     '/html/body/div/div[3]/div[1]/div/ul[1]/li[4]/a',
# )

#-----------------------------------------------------------------------------#
# Read excel file and check if 6 searches were completed in the past two weeks.
data = pd.read_excel(r'C:\Users\Matt\Dropbox\1 Job Search Related Items\Daily Work Log.xlsx', sheet_name='TWC Work Search Log')

df = pd.DataFrame(data, columns= ['Date of Activity', 'Work Search Count'])

start_date = '10-30-2020' # Have Sellenium pulled date.
end_date = '11-12-2020' # Have Sellenium pulled date.

after_start_date = (df[df['Date of Activity'] >= start_date])
before_end_date = (df[df['Date of Activity'] <= end_date])
between_two_dates = (df[(df['Date of Activity']>=start_date) & (df['Date of Activity']<=end_date)])

total_work_searches = between_two_dates.sum()






