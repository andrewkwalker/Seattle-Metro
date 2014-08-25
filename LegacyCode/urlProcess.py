import csv

with open('urlFormatted.csv', 'wb') as out:
    writer = csv.writer(out)
    with open('url.csv','rU') as url:
        reader = csv.reader(url)
        for row in reader:
            lat = float(row[1][31:40])
            lng = float(row[1][46:len(row[1])+1])
            writer.writerow([lat, lng, row[0].split(' & ')[0],
                            row[0].split(' & ')[1]])