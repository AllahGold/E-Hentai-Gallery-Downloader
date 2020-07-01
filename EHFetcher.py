# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:44:32 2020

E-Hentai Image Downloader

@author: rx03@126.com
"""

import requests
import shutil
import time
import random

def download_web_image(image_url = '', filename = ''):
    
    # If no filename assigned, use its original name from web
    if filename == '':
        filename = image_url.split("/")[-1]
    
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True, proxies=proxy)
    
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')
        
    time2sleep = 1 + 4 * random.random()
    time.sleep(time2sleep)
        
    return 0;

""" Get the HTML codes of a webpage
"""
def get_webpage_code(url='', ):
    response = requests.get(url, proxies=proxy)
    return response.text;

""" Add header to pretend the request is from a browser, otherwise will be detected and banned
"""
def get_webpage_code_header(url=''):
    
    headerz = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ja;q=0.6,zh-TW;q=0.5',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            }
    response = requests.get(url, headers=headerz, proxies=proxy)
    return response.text;


def download_EHentai_comic(page_url='', num_pages=1):
    
    comic_designation = page_url.split('/')[-1].split('-')[0]
    
    for i in range(0, num_pages):
        
        page = get_webpage_code_header(page_url)
        
        first = 0
        lookfor_imgurl_end = False
        lookfor_href = False
        lookfor_href_end = False
        image_src = ''
        nextpage_url = ''
        for i in range(0, len(page)):
            
            if page[i:i+8] == 'id="img"':
                first = i+14
                lookfor_imgurl_end = True
            if lookfor_imgurl_end == True and i >= first:
#                print(page[i])
                if page[i] == '"':
                    image_src = page[first:i]
                    lookfor_imgurl_end = False
            
            if page[i:i+11] == 'a id="next"':
                lookfor_href = True
            if lookfor_href == True:
                if page[i:i+6] == 'href="':
                    first = i+6
                    lookfor_href = False
                    lookfor_href_end = True
            if lookfor_href_end == True and i >= first:
                if page[i] == '"':
                    nextpage_url = page[first:i]
                    lookfor_href_end = False
        
        print('----------')
        print('image_src:',image_src)
        print('')
        print('nextpage_url:',nextpage_url)
        print('-------------')
        
        time2sleep = 1 + 4 * random.random()
        time.sleep(time2sleep)
        download_web_image(image_src)
        page_url = nextpage_url
        
    return 0;

proxy = {
    'http': 'http://127.0.0.1:1081',
    'https': 'https://127.0.0.1:1081'
    }

"""
┌─────────────────────────────────────────────────────────────
│                HOW TO USE
│     
│ Call the download_EHentai_comic function with 2 parameters:
│ url string of the starting page, and number of successive pages you would like to download
│ 
│ Example: download_EHentai_comic('https://e-hentai.org/s/ba2b98ab0b/1670957-1', 3)
│ 
│ Set proxy to an empty value if you don't use a proxy.
└─────────────────────────────────────────────────────────────
"""