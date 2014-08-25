import csv

with open('routeStops.csv','wb') as output:
    writer = csv.writer(output)
    with open('OnsOffsPerRoute.csv','rb') as data:
        reader = csv.reader(data)
        next(reader)
        for row in reader:
            route = row[3]
            stop = row[8] + ' & ' + row[10]
            writer.writerow([route,stop])