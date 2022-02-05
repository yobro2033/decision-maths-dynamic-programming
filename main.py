additionalCost = int(input("Please enter your additional cost: "))
overheadCost = int(input("Please enter your overhead cost: "))
storageCost = int(input("Please enter your storage cost: "))
aboveAdditional = int(input("Above which value to require additional cost? "))
availableMax = int(input("Please enter maxium 'items' available: "))
toMakeMax = int(input("Please enter maxium 'items' can be made: "))

inStock = 0
toMake = 0
leftOver = 0
value = 0
count = 0
tempRequired = 0
varCount = 0

valueData = []
requestOrder = []


while True:
    try:
        item = int(input("Enter number of item demanded (leave blank and enter to stop): "))
        requestOrder.append(item)
        count = count + 1
    except ValueError:
        break

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

print(valueData)
