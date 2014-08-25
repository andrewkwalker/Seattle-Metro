import csv
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

##################### Initialize model variables. #####################
alphaVal = raw_input('Enter an alpha value: ')
betaVal = raw_input('Enter a beta value: ')
gammaVal = raw_input('Enter a gamma value: ')
deltaVal = raw_input('Enter a delta value: ')
epsVal = raw_input('Enter an epsilon value: ')
zetaVal = raw_input('Enter a zeta value: ')

# A map from route numbers (str) to a set of stops (str).
routeToStop = {}
with open('routeStops.csv', 'rU') as data:
    reader = csv.reader(data)
    for row in reader:
        if not row[0] in routeToStop.keys():
            routeToStop[row[0]] = set(row[1].upper())
        else:
            routeToStop[row[0]].add(row[1].upper())
    for sets in routeToStop.values():
        temp = []
        for items in sets:
            if len(items) < 5:
                temp.append(items)
        for items in temp:
            sets.remove(items)

# A set of all stops (str).
stops = set()
for sets in routeToStop.values():
    for intersection in sets:
        stops.add(intersection)
stops = sorted(stops)

# A set of all routes (str).
tempRoutes = set()
for rt in routeToStop.keys():
    # Filler for code folding.
    tempRoutes.add(int(rt))
tempRoutes = sorted(tempRoutes)
routes = []
for rt in tempRoutes:
    # Filler for code folding.
    routes.append(str(rt))


# A map from stops (str) to district (str).
stopToDistrict = {}
with open('OnCrossDistrict.csv', 'rU') as data:
    reader = csv.reader(data)
    for row in reader:
        stopToDistrict[row[0].upper() + ' & ' + row[1].upper()] = row[2]

# A set of all districts (str).
districts = set()
for dist in stopToDistrict.values():
    # Filler for code folding.
    districts.add(dist)

# A map from district (str) to a set of route (str).
districtToRoute = {}
for dist in districts:
    routeSet = set()
    for rt in routes:
        for st in routeToStop[rt]:
            try:
                if stopToDistrict[st] == dist:
                    routeSet.add(rt)
            except KeyError:
                pass
    districtToRoute[dist] = routeSet

# A map from district (str) to number of passengers, ons and offs,
# per hour (float).
districtToUsage = {}
with open('OnsOffsPerRoute.csv', 'rU') as data:
    reader = csv.reader(data)
    temp = next(reader)
    for row in reader:
        try:
            if not stopToDistrict[row[8] + ' & ' + row[10]] \
            in districtToUsage.keys():
                districtToUsage[stopToDistrict[row[8] + ' & ' + row[10]]] \
                = float(row[5]) + float(row[6])
            else:
                districtToUsage[stopToDistrict[row[8] + ' & ' + row[10]]] \
                += float(row[5]) + float(row[6])
        except KeyError:
            pass

# A map from route (str) to cost per hour (float).
routeToCost = {}
with open('TimeDistanceLoadofRoute.csv', 'rU') as data:
    reader = csv.reader(data)
    temp = next(reader)
    temp = next(reader)
    for row in reader:
        if not row[0] in routeToCost.keys():
            try:
                routeToCost[row[0]] = float(row[18])
            except ValueError:
                pass

# A map from route (str) to load per hour (float).
routeToLoad = {}
with open('TimeDistanceLoadofRoute.csv', 'rU') as data:
    reader = csv.reader(data)
    temp = next(reader)
    temp = next(reader)
    for row in reader:
        if not row[0] in routeToLoad.keys():
            routeToLoad[row[0]] = float(row[11])
        else:
            routeToLoad[row[0]] += float(row[11])

# A map from route (str) to redundancy (int).
routeToRedundancy = {}
for rt in routes:
    temp = set()
    for stuff in routes:
        temp.add(stuff)
    temp.remove(rt)
    maxChain = 0
    for rt2 in temp:
        chain = set(routeToStop[rt]).intersection(set(routeToStop[rt2]))
        if len(chain) > maxChain:
            maxChain = len(chain)
    routeToRedundancy[rt] = maxChain

# A map from route (str) to on time percentage (float).
routeToOTP = {}
with open('OTPByRoute.csv', 'rU') as data:
    reader = csv.reader(data)
    count = 1
    while count < 4:
        temp = next(reader)
        count += 1
    while count < 221:
        temp = next(reader)
        if temp[0][:-1] in routeToOTP.keys():
            routeToOTP[temp[0][:-1]] = \
            np.average([routeToOTP[temp[0][:-1]], float(temp[6][:-1])])
        else:
            routeToOTP[temp[0][:-1]] = float(temp[6][:-1])
        count += 1

# A map from route (str) to a set of districts (str) the route
# passes through.
routeToDistrict = {}
for rt in routes:
    dist = set()
    temp = routeToStop[rt]
    for st in temp:
        try:
            dist.add(stopToDistrict[st])
        except KeyError:
            pass
    routeToDistrict[rt] = dist

# A map from route (str) to a sum of usage across all districts
# the route passes through (float).
routeToService = {}
for rt in routes:
    rtSum = 0
    for dist in routeToDistrict[rt]:
        rtSum += districtToUsage[dist]
    routeToService[rt] = rtSum

#######################################################################

# The passenger load for each route.
P = []
for rt in routes:
    P.append(routeToLoad[rt])
zP = stats.zscore(P)

# These were left out of metro's data, we put in an average number.
leftOut = ['522', '540', '542', '545', '550', '554', '555', '556', 
           '560', '671', '672', '673', '674']
for s in leftOut:
    routeToOTP[s] = 77.0

# The on time percentage for each route.
T = []
for rt in routes:
    T.append(routeToOTP[rt])
zT = stats.zscore(T)

# The hourly cose for each route.
C = []
for rt in routes:
    C.append(routeToCost[rt])
zC = stats.zscore(C)

# The redundancy factor of each route.
R = []
for rt in routes:
    R.append(routeToRedundancy[rt])
zR = stats.zscore(R)

# The service score of each route.
S = []
for rt in routes:
    S.append(routeToService[rt])
zS = stats.zscore(S)

# Processing and displaying data.
measures = []

for k in range(0,len(routes)):
    measure = float(zetaVal)*(float(alphaVal)*zP[k] + \
              float(betaVal)*zT[k]) + (float(gammaVal)*zC[k] + \
              float(deltaVal)*zR[k]) + \
              float(epsVal)*zS[k]
    measures.append(measure)
    print 'Route ' + routes[k] + ' has a measure of ' + str(measure)

#measures.remove(max(measures))
#measures.remove(min(measures))

print 'The mean score is ' + str(np.mean(measures))
print 'The median score is ' + str(np.median(measures))
print 'The STD is ' + str(np.std(measures))
print 'The maximum score is ' + str(max(measures))
print 'The minimum score is ' + str(min(measures))

hist, bins = np.histogram(measures, bins = 1000)
width = 0.7 *(bins[1]-bins[0])
center = (bins[:-1]+bins[1:])/2
plt.bar(center, hist, align = 'center', width = width)

plt.show()