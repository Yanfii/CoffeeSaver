import json, os, io


with io.open('ParsedJson/parsedMonthly-final.json', 'r') as f:
    data = json.load(f)



for i in range(len(data)):
    location = data[i]['Location']
    age = data[i]['Age']
    location = location[:-1]
    location = location.replace(' ', '-')
    print(location)
    path = 'ParsedJson/'+location

    if not os.path.exists(path):
        os.makedirs(path)
    
    if age < 17:
        filename = '/0-16.json'
    elif age < 25:
        filename = '/17-25.json'
    elif age < 35:
        filename = '/26-35.json'
    elif age < 45:
        filename = '/36-45.json'
    elif age < 60:
        filename = '/46-60.json'
    else:
        filename = '/60+.json'
        
    if not os.path.isfile(path+filename):
        f=open(path+filename, 'w+')
        f.write('[]')
        f.close()

    with io.open(path+filename, 'r') as inFile:
        datum = json.load(inFile)
    
    datum.append(data[i])

    with io.open(path+filename, 'w') as outFile:
        json.dump(datum, outFile)
    
    print(i)






    
    
