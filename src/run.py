import time, math, threading

collectors = {}
publishers = {}
runningCollectors = {}
runningPublishers = {}
data = {}

def run(saveSync = 0):
    """
    Run the application.
    saveSync: 0 = Save when all values are updated, 1 = save with cached data on updated data, 2 = save only updated values when a value is updated Only applies to collectors that support it.
    """
    data['lastSync'] = int(time.time())
    for i in collectors:
        runningCollectors[i] = threading.Thread(target=collectors[i]["function"], kwargs={"interval":collectors[i]["interval"], "repeat":collectors[i]["repeat"], "name":i}).start()
        

def updateTime():
    """
    Update the last sync time.
    """
    minOffset = math.inf
    for item in data:
        if item != 'lastSync' and data[item]["offset"] < minOffset:
            minOffset = data[item]["offset"]
    data['lastSync'] += minOffset
    for item in data:
        if item != 'lastSync':
            data[item]["offset"] -= minOffset