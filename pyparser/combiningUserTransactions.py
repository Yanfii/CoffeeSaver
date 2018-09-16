import io, os, json
final = []

with io.open('ParsedJson/parsedMonthly-all.json', 'r') as f:
    data = json.load(f)

# with io.open('ParsedJson/parsedWeekly-all.json', 'r') as f:
#     data = json.load(f)

with io.open('data.json', 'r') as f:
    data2 = json.load(f)

for i in range(len(data)):
    temp = {**data2[i], **data[i]}
    final.append(temp)
    print(i)

with open('ParsedJson/parsedMonthly-Final.json', 'w') as outfile:
        json.dump(final, outfile)

print('Proceesed file with '+str(len(final))+' data points.')