
Dependancies
server:
flask, pandas, csv (using pip)

client:
urllib3, certifi, datetime, json (using pip)



Endpoint: 192.168.1.xx:5000/datanode
For posting temperature infomation to server csv files

requests: POST

String query: node = csv_file
where csv_file is either slab, inside or outside

body: requires json file 
    'temp' is temperature
    'time' is time of recording


Endpoint: 192.168.0.xx:5000/<csv_file>.csv
Getting csv files

requests: GET



