import json
import io, os

for x in range(1, 34):
    with io.open('Datasets/TD-World-BankTransactions-v2.0-'+str(x)+'.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)

    final = []
    for i in range(len(data)):
        if data[i]['Type'] == 'VISA':
            totalSum = 0
            transActions = {}
            for j in range(1, len(data[i]['Transactions'])):
                dateValid = False
                date = data[i]['Transactions'][j]['PostDate']

                #if date[5:7] == '09':
                #    if int(date[8:10]) > 7 and int(date[8:10]) < 16:
                #        dateValid = True

                if date[5:7] == '08':
                    if int(date[8:10]) >= 15:
                        dateValid = True
                if date[5:7] == '09':
                    if int(date[8:10]) >= 15:
                        dateValid = True

                if dateValid:
                    try:
                        merchant = data[i]['Transactions'][j]['MerchantCategoryCode']
                        cashMoney = data[i]['Transactions'][j]['CurrencyAmount']
                        if merchant == '4899':
                            merchant = 'Cable/TV'
                        elif merchant == '5251':
                            merchant = 'Hardware'
                        elif merchant == '5411':
                            merchant = 'Supermarket'
                        elif merchant == '5541':
                            merchant = 'AutoService'
                        elif merchant == '5814':
                            merchant = 'FastFood'
                        elif merchant == '5921':
                            merchant = 'Alcohol'
                        elif merchant == '7832':
                            merchant = 'Movie'
                        elif merchant == '5945':
                            merchant = 'Hobby'
                        elif merchant == '5912':
                            merchant = 'DrugStore'
                        else:
                            print(merchant)
                            break

                        if merchant in transActions:
                            transActions[merchant] = transActions[merchant]+cashMoney
                        else:
                            transActions[merchant] = cashMoney
                            
                        totalSum = totalSum + cashMoney
                    except KeyError:
                        pass
            for key in transActions:
                transActions[key] = '{:0.2f}'.format(transActions[key])
            transActions['0000'] = '{:0.2f}'.format(totalSum)
            final.append(transActions)

    #path = 'ParsedJson/Monthly'
    #os.mkdir(path)

    with open('ParsedJson/Monthly/parsedMonthly-'+str(x)+'.json', 'w') as outfile:
        json.dump(final, outfile)

    print('Proceesed file '+str(x)+' with '+str(len(final))+' data points.')