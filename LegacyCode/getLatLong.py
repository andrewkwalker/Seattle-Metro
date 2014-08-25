from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

driver = webdriver.Firefox()

with open('latLngOnOff.csv', 'wb') as outputdata:
    writer = csv.writer(outputdata)
    with open('StreetsImproved.csv','rb') as inputdata:
        reader = csv.reader(inputdata)
        for row in reader:
            driver.get('https://geoservices.tamu.edu/Services/Geocode/Interactive/GeocodeSingleNonParsed.aspx')
            address = driver.find_element_by_id('ctl00_ctl00_ctl00_ctl00_ContentPlaceHolder1_ContentArea_ContentArea_ContentArea_txtStreetAddress')
            city = driver.find_element_by_id('ctl00_ctl00_ctl00_ctl00_ContentPlaceHolder1_ContentArea_ContentArea_ContentArea_txtCity')
            state = driver.find_element_by_id('ctl00_ctl00_ctl00_ctl00_ContentPlaceHolder1_ContentArea_ContentArea_ContentArea_dropDownState')
            code = driver.find_element_by_id('ctl00_ctl00_ctl00_ctl00_ContentPlaceHolder1_ContentArea_ContentArea_ContentArea_txtZip')
            address.send_keys(str(row[0]))
            city.send_keys('Seattle')
            state.click()
            state.send_keys('w')
            code.click()
            code.send_keys(Keys.RETURN)
            time.sleep(.5)
            lat = driver.find_element_by_id('ctl00_ctl00_ctl00_ctl00_ContentPlaceHolder1_ContentArea_ContentArea_ContentArea_txtLat')
            lng = driver.find_element_by_id('ctl00_ctl00_ctl00_ctl00_ContentPlaceHolder1_ContentArea_ContentArea_ContentArea_txtLon')
            writer.writerow([lat.text,lng.text,row[0]])
            time.sleep(13)