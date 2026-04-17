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
            yyyymm = "{0}{1:0>2}".format(str(year), str(month))
            jsonData = getTourismStatsItem(yyyymm, nat_cd, ed_cd)
            if (jsonData['response']['header']['resultMsg'] == 'OK'):
                # 데이터가 없는 마지막 항목인 경우 ----
                if jsonData['response']['body']['items'] == '':
                    dataEnd = "{0}{1:0>2}".format(str(year), str(month-1))
                    print("데이터 없음.... \n제공되는 통계 데이터는 %s년 %s월까지입니다." % (str(year), str(month-1)))
                    break
                #jsonData를 출력하여 확인 ----
                print(json.dumps(jsonData, indent=4, sort_keys=True, ensure_ascii=False))

                natName = jsonData['response']['body']['items']['item']['netKorNm']
                natName = natName.replace(' ', '')
                num = jsonData['response']['body']['items']['item']['num']
                ed = jsonData['response']['body']['items']['item']['ed']
                print('[ %s_%s : %s ]' % (natName, yyyymm, num))
                print('--------------------------------------------')
                jsonResult.append({'nat_name':natName, 'nat_cd':nat_cd, })



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