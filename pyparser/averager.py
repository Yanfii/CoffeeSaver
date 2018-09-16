import io, os, json
from os.path import isfile, join


dirList = [f for f in os.listdir('ParsedJson') if not isfile(join('ParsedJson', f))]
final = []

for i in dirList:
    jsonList = os.listdir(join('ParsedJson', i))
    temp2 = {}
    temp2['Location'] = i
    for j in jsonList:
        temp = {
            'DrugStore' : 0.0,
            'FastFood' : 0.0,
            'AutoService' : 0.0,
            'Supermarket' : 0.0,
            'Hardware' : 0.0,
            'Alcohol' : 0.0,
            'Cable/TV' : 0.0,
            'Hobby' : 0.0,
            'Movie' : 0.0,
            '0000' : 0.0
        }
        with io.open(join('ParsedJson', i, j), 'r', encoding='utf-8-sig') as curFile:
            data = json.load(curFile)

        for k in range(len(data)):
            for key in data[k]:
                if key != 'Age' and key != 'Location':
                    temp[key] = temp[key] + float(data[k][key])

        for key in temp:
            temp[key] = '{:0.2f}'.format(temp[key]/float(len(data)))

        temp2[j[:-5]] = temp
    final.append(temp2)

with open('finalAverage.json', 'w') as outfile:
    json.dump(final, outfile)