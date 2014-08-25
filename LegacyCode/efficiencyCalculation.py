import csv
import numpy as np

routes = [1,2,3,4,5,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,25,26,27,28,
          29,82,83,84,99,60,61,62,64,65,66,67,68,70,71,72,73,74,75,76,77,30,
          32,31,33,36,37,40,41,43,44,47,48,49,50,55,56,57]

alpha = 1
beta = 1
gamma = .5
delta = .5

#route = 1

for route in routes:
    if route in routes:

        with open('TimeDistanceLoadofRoute.csv', 'rU') as load:
            reader = csv.reader(load)
            averageLoad = list()
            for row in reader:
                if row[0] == str(route):
                    averageLoad.append(float(row[11]))
                    C = float(row[18])
                    R = float(row[19])
            P = np.average(averageLoad)

        with open('OTPByRoute.csv', 'rU') as time:
            reader = csv.reader(time)
            averageTime = list()
            for row in reader:
                if row[0][:-1] == str(route):
                    averageTime.append(float(row[6][:-1]))
            T = np.average(averageTime)

        print str(route) + ' : ' + str((alpha*P + beta*T) / (gamma*C + delta*R))
        print '\tP =' + str(P)
        print '\tT =' + str(T)
        print '\tC =' + str(C)
        print '\tR =' + str(R)
    else:
        print "Route " + str(route) + " is not a valid route."