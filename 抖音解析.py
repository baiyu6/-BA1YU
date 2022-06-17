#!/usr/bin/env python
import re
import requests
from lxml import etree
# -*- coding: utf-8 -*-
def video_get(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Mobile Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers, allow_redirects=False).text
    url = re.findall(r'/video/(\d*)', page_text)
    url_back=url[0]
    url_real = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + url_back
    page_text = requests.get(url=url_real, headers=headers, allow_redirects=False)
    video_url = str(page_text.json()['item_list'][0]['video']['play_addr']['url_list'][0])
    new_video_url = video_url.replace('/playwm/', '/play/')
    response = requests.get(url=new_video_url, headers=headers,allow_redirects=False).text
    video_finurl = re.findall(r'[a-zA-z]+://[^\s]*', response,re.M)
    print('解析完成无水印地址为:\n' + video_finurl[0])
def main():
        url = input('请输入抖音分享链接:')
        if url.find('v.douyin.com/') == -1:
            print('地址无效!请输入含v.douyin.com/的分享链接')
            main()
        else:
            video_get(url)

if __name__ == "__main__":
    main()





