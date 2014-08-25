import csv

with open('latLngOnOffFinal.csv', 'wb') as output:
    writer = csv.writer(output)

    with open('latLngOnOff2125.csv', 'rU') as data1:
        reader = csv.reader(data1)

        for row in reader:
            writer.writerow([row[0],row[1],row[2],row[3]])

    with open('latLngOnOff4526.csv', 'rU') as data2:
        reader = csv.reader(data2)

        for row in reader:
            writer.writerow([row[0],row[1],row[2],row[3]])

    with open('latLngOnOff5160.csv', 'rU') as data3:
        reader = csv.reader(data3)

        for row in reader:
            writer.writerow([row[0],row[1],row[2],row[3]])