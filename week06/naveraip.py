# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json

client_id = '03q3GBTSdROX1euVlaPU'
client_secret = 'VfHH1QGnu2'

def main():

    node = 'news'
    srcText = input('검색어를 입력하세요: ')

    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)






def getNaverSearch(node, srcText, page_start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), page_start, display)
    
    url = base + node + parameters
    responseDecode = getRequestUrl(url)

    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)
    
def getRequestUrl(url):
    req = urllib.request.Request(rul)

    req.add