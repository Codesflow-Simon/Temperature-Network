import urllib3
import certifi
import json
import datetime as dt

def post(diction, ip='http://172.17.0.4:5000'):
    def dtconvert(attribute):
        if isinstance(attribute, dt.datetime):
            return attribute.__str__()

    send = json.dumps(diction, default=dtconvert)

    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where()
    )
    r = http.request('POST', ip+'/datanode?node=outside', body=send)

print(post({'temp': 22, 'time': dt.datetime.now()}))