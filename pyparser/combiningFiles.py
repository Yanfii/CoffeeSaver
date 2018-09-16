import io, os, json

final = []

for i in range(1, 34):
    with io.open('ParsedJson/Monthly/parsedMonthly-'+str(i)+'.json', 'r') as f:
        data = json.load(f)
    
    for j in range(len(data)):
        final.append(data[j])

for i in range(700, 734):
    with io.open('ParsedJson/Monthly/parsedMonthly-'+str(i)+'.json', 'r') as f:
        data = json.load(f)
    for j in range(len(data)):
        final.append(data[j])

with open('ParsedJson/parsedMonthly-all.json', 'w') as outfile:
        json.dump(final, outfile)

print('Proceesed file with '+str(len(final))+' data points.')

