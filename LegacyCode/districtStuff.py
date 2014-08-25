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

with open('OnSt_CrossSt_Districts.csv', 'rU') as data:
    reader = csv.reader(data)
    districtDict = {}
    for row in reader:
        districtDict[row[0] + ' & ' + row[1]] = row[2]

routeDistrict = {}
#route = 1
errorCount = 0
for route in routeDict.keys():
    districts = set()
    for s in routeDict[route]:
        try:
            districts.add(districtDict[s])
        except KeyError:
            errorCount += 1
            pass
#    print str(route) + ' : ' + str(len(districts)) + ' districts'
    distSet = set()
    for s in districts:
        distSet.add(s)
#        print '\t' + s
    routeDistrict[route] = distSet
#print errorCount

for s in set(districtDict.values()):
    count = 0
    for route in routeDict.keys():
        if s in routeDistrict[route]:
            count += 1
    #print s + ' : ' + str(count)

districtTotals = {}

with open('OnsOffsPerRoute.csv', 'rU') as data:
    reader = csv.reader(data)
    for row in reader:
        try:
            if not districtDict[row[8] + ' & ' + row[10]] in districtTotals.keys():
                districtTotals[districtDict[row[8] + ' & ' + row[10]]] = float(row[5]) + float(row[6])
            else:
                districtTotals[districtDict[row[8] + ' & ' + row[10]]] += float(row[5]) + float(row[6])
        except KeyError:
            pass

for s in districtTotals.keys():
    print s + ' : ' + str(districtTotals[s])