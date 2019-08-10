import urllib3
import certifi
import json

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)
def get(ip='http://192.168.1.17:5000'):
    r = http.request('GET', ip+'/outside.csv')
    return json.loads(r.data)
print(get())