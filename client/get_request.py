import urllib3
import certifi
import json

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)
def get(ip='http://127.0.1.1:5000'):
    r = http.request('GET', ip+'/inside.csv')
    return r.data
print(get())
