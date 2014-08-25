import csv

intersections = set()

# Streets.csv is a .csv file with the onStreets in the first column
# and crossStreets in the second column.
with open('Streets.csv','rb') as streets:
	reader = csv.reader(streets)
	for row in reader:
		intersections.add(row[0] + ' & ' + row[1])

# StreetsImproved.csv will be a .csv file with a columns containing
# the formated intersection names ('onStreet & crossStreet').
with open('StreetsImproved.csv','wb') as imp:
    writer = csv.writer(imp)
    for intersection in intersections:
    	writer.writerow([intersection])