from flask import Flask, render_template, request
from tabulate import tabulate
from operator import itemgetter

app = Flask(__name__)

@app.route('/')
def dash():
    return render_template('iterative.html')

@app.route('/search', methods=['POST', 'GET'])
def home():
    additionalCost = request.form['additionalCost']
    overheadCost = request.form['overheadCost']
    storageCost = request.form['storageCost']
    aboveAdditional = request.form['aboveAdditional']
    availableMax = request.form['availableMax']
    toMakeMax = request.form['toMakeMax']
    input_string = request.form['input_string']

    inStock = 0
    toMake = 0
    leftOver = 0
    value = 0
    count = 0
    tempRequired = 0
    varCount = 0

    valueData = []

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

    finalCost = itemsFinal[0]["value"])

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

    return render_template("result.html", data1=resultTable, imagen=finalCost)
