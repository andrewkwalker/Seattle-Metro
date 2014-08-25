import csv

with open('routeStops.csv','rb') as data:
    reader = csv.reader(data)
    first = next(reader)
    routeDict = {int(first[0]) : set(first[1])}
    for row in reader:
        if not routeDict.has_key(int(row[0])):
            routeDict[int(row[0])] = set(row[1])
        else:
            routeDict[int(row[0])].add(row[1])

for sets in routeDict.values():
    x = []
    for items in sets:
        if len(items) < 5:
            x.append(items)
    for items in x:
        sets.remove(items)

print routeDict[216]
print routeDict[70]
print routeDict[71]
print routeDict[48]