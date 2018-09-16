var accountId = '0c23ac69-08dd-4310-8cd1-8b10746c2acb_c18dca28-f10f-4a0a-b905-db636046bd4c'

var myInit = {
  method: 'GET',
  headers: {
    'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiZjI0NzBhNTMtOGI5Ni0zYjllLTg5NmItM2Y1Y2YxMmZkMzMxIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiIwYzIzYWM2OS0wOGRkLTQzMTAtOGNkMS04YjEwNzQ2YzJhY2IifQ.UCfyelzpPiRB-kk0l8FYNDowfDOJ5RHGkZ8h849hH5k'
  }
};

var myAccount = new Request('https://api.td-davinci.com/api/customers/' + accountId + '/accounts', myInit);

fetch(myTransactions)
  .then(response => response.json())
  .then(account => {
    var hashTable = {}
    account["result"].map(function(res){
      if(res["date"])
    })
    
  });
