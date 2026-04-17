# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json
import pandas as pd

SerciveKey = "3c9b5c5bbb8752d28c8e400504f7fe632c1d0e9d0f0cdaf570a48b5c62aaafe9"

"""### [CODE 0]"""


"""### [CODE 3]"""

def getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear):
    jsonResult = []
    result = []

    for year in range(nStartYear, nEndYear + 1):
        for month in range(1, 13):
            yyyymm = "{0}{1:0>2}".format(str(year), str(monte))
            




"""### [CODE 2]"""

def getTourismStatsItem(yyyymm, nat_cd, ed_cd):
    service_url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    parameters = "?_type=json&serviceKey = " + SerciveKey
    parameters += "&YM=" + yyyymm
    parameters += "&NAT_CD=" + nat_cd
    parameters += "&ED_CD=" + ed_cd

    url = service_url + parameters

    responseDecode = getRequestUrl(url)

    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)    

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