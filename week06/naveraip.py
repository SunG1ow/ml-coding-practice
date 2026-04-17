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
    