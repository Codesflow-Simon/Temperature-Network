import urllib3
import certifi
import json
import datetime as dt

def post(diction, node, ip='http://192.168.1.11:5000'):
    def dtconvert(attribute):
        if isinstance(attribute, dt.datetime):
            return attribute.__str__()

    send = json.dumps(diction, default=dtconvert)

    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where()
    )
    try:
        r = http.request('POST', ip+'/datanode?node='+node, body=send)
    except urllib3.exceptions.MaxRetryError:
        print('server down')
