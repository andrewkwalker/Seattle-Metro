from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

driver = webdriver.Firefox()
driver.get('http://www.editpad.org')
editpadHandle = driver.window_handles[0]
elem = driver.find_element_by_xpath('/html/body')
elem.send_keys(Keys.COMMAND + 'n')
latlongHandle = driver.window_handles[1]
driver.switch_to_window(latlongHandle)
driver.get('http://www.latlong.net')

with open('StreetsImproved.csv','rb') as inputdata:
    reader = csv.reader(inputdata)
    for row in reader:
        temp = row[0]
        driver.switch_to_window(latlongHandle)
        elem1 = driver.find_element_by_id('gadres')
        elem2 = driver.find_element_by_id('coordinatesurl')
        elem1.click()
        time.sleep(.5)
        elem1.send_keys(str(temp) + ', Seattle, WA')
        elem1.send_keys(Keys.RETURN)
        elem2.click()
        elem2.send_keys(Keys.COMMAND + 'c')
        driver.switch_to_window(editpadHandle)
        elem3 = driver.find_element_by_xpath('/html/body/form/textarea')
        elem3.click()
        elem3.send_keys(str(temp) + ', ' + Keys.COMMAND + 'v')
        elem3.send_keys(Keys.RETURN)