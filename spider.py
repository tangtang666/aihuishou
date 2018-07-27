# coding:utf-8
import requests
import json
import jsonpath
import re
import time
import random
from lxml import etree
ua_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
headers = {
    'Host': 'www.aihuishou.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.aihuishou.com/product/25827.html',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '214',
    'Cookie': 'acw_tc=AQAAAP1GbV6ehggAhK2QPeFJEY3gPcys; portal_city=1; portal_city_default=1',
    'Connection': 'keep-alive',
    }
# response = requests.get(url1, headers=headers).text

def url(key):
    url1 = 'https://www.aihuishou.com/product/'
    url2 = 'https://www.aihuishou.com/util/GetSearchHot?pageSize=1000'
    url3 = 'https://www.aihuishou.com/'
    response = requests.get(url2, headers=ua_headers).text
    data = json.loads(response)
    idlist = jsonpath.jsonpath(data, "$..id")
    for item in idlist:
        id = item
        fullurl = url1 + str(id)
        print(fullurl)
    time.sleep(random.randint(5, 30))
    response1 = requests.get(fullurl, headers= ua_headers).text
    # html = etree.HTML(response1)
    # result = html.xpath()
    pattern = re.compile(r'<div id = "group-propertty" class="clearfix"></div>', re.S)
    contentlist = pattern.findall(response1)
    print(contentlist)


def send_post_request():
    url = "https://www.aihuishou.com/userinquiry/create"
    data = {
        'AuctionProductId': 17458,
        'ProductModelId': '',
        'PriceUnits': '2072;2453;2014;2023;6437;2100;2125;2118;2114;2067;5300;2106;2134;;;;;3168;2108;2026;2045;2104;2129;;;;;2808;'
    }
    # data = urllib.parse.urlencode(data).encode(encoding='UTF8')
    session = requests.Session()
    response = session.post(url, data=data, headers=headers).text
    print(response)
    key = json.loads(response)
    key = jsonpath.jsonpath(key, '$..data')
    key = key[0]['redirectUrl']
    # m = re.match(r'\d+', key).group(1)
    return key
    # print(m)


if __name__ == '__main__':
    send_post_request()
    # url()