from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

driver = webdriver.Firefox()
driver.get('http://www.editpad.org')
editpadHandle = driver.window_handles[0]

textbox = driver.find_element_by_xpath('/html/body/form/textarea')
textbox.send_keys(Keys.COMMAND + 'n')
latlongHandle = driver.window_handles.remove(editpadHandle)
driver.switch_to_window(latlongHandle)
driver.get('http://www.latlong.net')

with open('StreetsImproved.csv','rb') as inputdata:
	reader = csv.reader(inputdata)
	for row in reader:
		elem = driver.find_element_by_id('gadres')
		elem.click()
		elem.send_keys(str(row)[2:-2] + ', Seattle, WA')
		elem.send_keys(Keys.RETURN)

		elem = driver.find_element_by_id('coordinatesurl')
        elem.click()
        elem.send_keys(Keys.COMMAND + 'c')

        driver.switch_to_window(editpadHandle)

        textbox.click()
        textbox.send_keys(str(row) + ', ' + Keys.COMMAND + 'v')
        elem.send_keys(Keys.RETURN)

        driver.switch_to_window(latlongHandle)