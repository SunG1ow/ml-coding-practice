# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json
import pandas as pd

SerciveKey = "3c9b5c5bbb8752d28c8e400504f7fe632c1d0e9d0f0cdaf570a48b5c62aaafe9"

"""### [CODE 0]"""



"""### [CODE 1]"""

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.rulopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
    
main()