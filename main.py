# -*- coding: utf-8 -*-
from operator import itemgetter

additionalCost = int(input("[Additional worker cost] Please enter your additional cost: "))
overheadCost = int(input("[Overhead costs] Please enter your overhead cost: "))
storageCost = int(input("[Held in stock cost] Please enter your storage cost: "))
aboveAdditional = int(input("[Value required additional worker] Above which value to require additional cost? "))
availableMax = int(input("[Maxium in stock each month] Please enter maxium 'items' available: "))
toMakeMax = int(input("[Maxium value can be made] Please enter maxium 'items' can be made: "))

inStock = 0
toMake = 0
leftOver = 0
value = 0
count = 0
tempRequired = 0
varCount = 0

valueData = []

input_string = raw_input("[Start from first month to last month] Enter number of item demanded (Each separated by space): ")
requestOrder = input_string.split()

for count in range(0, len(requestOrder)):
    requestOrder[count] = int(requestOrder[count])
    count = count + 1

firstRun = True

for i in range(count):
    tempRequired = requestOrder[count - 1 - i]
    if firstRun == True:
        varCount = 1
        for j in range(availableMax + 1):
            inStock = j
            toMake = int(tempRequired - inStock)
            if toMake > -1 and toMake <= toMakeMax:
                leftOver = tempRequired - inStock - toMake
                if leftOver == 0:
                    if toMake <= aboveAdditional and toMake > 0:
                        value = (inStock*storageCost) + overheadCost
                        valueData.append({'stage': varCount, 'state': inStock, 'action': toMake, 'destination': leftOver, 'value': value})
                    elif toMake == 0:
                        value = (inStock*storageCost)
                        valueData.append({'stage': varCount, 'state': inStock, 'action': toMake, 'destination': leftOver, 'value': value})
                    elif toMake >= 0 and toMake > aboveAdditional:
                        value = (inStock*storageCost) + overheadCost + additionalCost
                        valueData.append({'stage': varCount, 'state': inStock, 'action': toMake, 'destination': leftOver, 'value': value})
        firstRun = False

    else:
        varCount = varCount + 1
        lastRun = False
        if lastRun == False:
            if i == count - 1:
                for valueD in valueData:
                    inStock = 0
                    for k in range(availableMax + 1):
                        leftOver = k
                        toMake = int(tempRequired + leftOver - inStock)
                        if toMake > -1 and toMake <= toMakeMax:
                            leftOver = inStock + toMake - tempRequired
                            if leftOver >= 0 and leftOver <= availableMax:
                                if toMake <= aboveAdditional and toMake > 0:
                                    if valueD['stage'] == varCount - 1 and valueD['state'] == leftOver:
                                        value = (inStock*storageCost) + overheadCost + valueD['value']
                                        valueData.append({'stage': varCount, 'state': inStock, 'action': toMake, 'destination': leftOver, 'value': value})
                                elif toMake == 0:
                                    if valueD['stage'] == varCount - 1 and valueD['state'] == leftOver:
                                        value = (inStock*storageCost) + valueD['value']
                                        valueData.append({'stage': varCount, 'state': inStock, 'action': toMake, 'destination': leftOver, 'value': value})
                                elif toMake >= 0 and toMake > aboveAdditional:
                                    if valueD['stage'] == varCount - 1 and valueD['state'] == leftOver:
                                        value = (inStock*storageCost) + overheadCost + additionalCost +valueD['value']
                                        valueData.append({'stage': varCount, 'state': inStock, 'action': toMake, 'destination': leftOver, 'value': value})
                lastRun = True

            else:
                for valueD in valueData:
                    for j in range(availableMax + 1):
                        inStock = j
                        for z in range(availableMax + 1):
                            leftOver = z
                            toMake = int(tempRequired + leftOver - inStock)
                            if toMake > -1 and toMake <= toMakeMax:
                                leftOver = inStock + toMake - tempRequired
                                if leftOver >= 0 and leftOver <= availableMax:
                                    if toMake <= aboveAdditional and toMake > 0:
                                        if valueD['stage'] == varCount - 1 and valueD['state'] == leftOver:
                                            value = (inStock*storageCost) + overheadCost + valueD['value']
                                            valueData.append({'stage': varCount, 'state': inStock, 'action': toMake, 'destination': leftOver, 'value': value})
                                    elif toMake == 0:
                                        if valueD['stage'] == varCount - 1 and valueD['state'] == leftOver:
                                            value = (inStock*storageCost) + valueD['value']
                                            valueData.append({'stage': varCount, 'state': inStock, 'action': toMake, 'destination': leftOver, 'value': value})
                                    elif toMake >= 0 and toMake > aboveAdditional:
                                        if valueD['stage'] == varCount - 1 and valueD['state'] == leftOver:
                                            value = (inStock*storageCost) + overheadCost + additionalCost +valueD['value']
                                            valueData.append({'stage': varCount, 'state': inStock, 'action': toMake, 'destination': leftOver, 'value': value})

finalData = []

for value in valueData:
    if value['stage'] == count:
        finalData.append(value)
itemsFinal = sorted(finalData,key=lambda x: x['value'])
print("\n")
print("The minimise cost: £",itemsFinal[0]["value"])

# ---------

mylist = valueData

mylist = sorted(mylist, key=itemgetter('stage', 'state', 'action', 'destination', 'value'))
mylist = sorted(mylist, key=lambda k: (k['stage'], k['state'], k['action'], k['destination'], k['value']))

seen = set()
resultTable = []

for dic in mylist:
    key = (dic['stage'], dic['state'], dic['action'], dic['destination'])

    if key in seen:
        continue

    resultTable.append(dic)
    seen.add(key)

print("\n")

print("Stage\tState\tAction\tDestination\tValue")
for i in resultTable:
    print(" ",i['stage'],"\t ",i['state'],"\t ",i['action'],"\t    ",i['destination'],"\t       ",i['value'])
