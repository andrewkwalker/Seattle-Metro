from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

driver = webdriver.Firefox()

with open ('latLngOnOff5160.csv', 'wb') as output:
    writer = csv.writer(output)
    urlMain = 'http://maps.googleapis.com/maps/api/geocode/json?address='
    with open('StreetsImproved5160.csv', 'rU') as data:
        reader = csv.reader(data)
        for row in reader:
            lat = ''
            lng = ''
            temp = row[0]
            temp = temp.replace(' ','+').replace('&','%26')
            urlEnd = temp + ',+Seattle,+WA&sensor=true'
            driver.get(urlMain+urlEnd)
            latlng = driver.find_element_by_xpath('/html/body/pre')
            temp = latlng.text.replace('\n','')
            temp = ' '.join(temp.split()).split(' ')
            index = 0
            for elem in temp:
                if elem == '"lat"':
                    lat = temp[index+2]
                if elem == '"lng"':
                    lng = temp[index+2]
                index += 1
            onOff = row[0].split(' & ')
            if lat != '':
                writer.writerow([lat[0:-1], lng, onOff[0], onOff[1]])
            time.sleep(.2)

driver.quit()