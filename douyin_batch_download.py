import requests # 调用requests库
import re
import json
import os
from bs4 import BeautifulSoup # 调用BeautifulSoup库


def download_video(title,video_name,video_url):
    res = requests.get(video_url).content
    intab = r'[?*/\|.:><]'
    title = re.sub(intab, "", title)
    video_name = re.sub(intab, "", video_name)
    baseFolder = 'E:\\douyin_video\\'+ title
    if not os.path.exists(baseFolder):
        os.makedirs(baseFolder)
    with open(baseFolder+'\\'+video_name+'.mp4',mode='wb') as f:
        f.write(res)
        f.close()



headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'cookie': 'passport_csrf_token=5f7828b6ac631c94890b640169a73cfd; passport_csrf_token_default=5f7828b6ac631c94890b640169a73cfd; ttwid=1%7Cudyb47B1B-qQzOhHe6xpKzGKgebLb_YB45dJNF0uIOs%7C1649156382%7C248a44fb235da3fdc913172c4a936da0f26c70f22563688fd1315c2bb684c3ff; _tea_utm_cache_6383=undefined; AB_LOGIN_GUIDE_TIMESTAMP=1649499667211; _tea_utm_cache_1300=undefined; ttcid=6f39ae99d9224d638eee985473c645e593; _tea_utm_cache_2285=undefined; n_mh=NIMzHXUK2pnQGgDYWE1t9hOr6wjNH28uUQpDgQXZijo; sso_uid_tt=797a77f8f7d433dc32043257bd1a592b; sso_uid_tt_ss=797a77f8f7d433dc32043257bd1a592b; toutiao_sso_user=fb693373ac8f86fb61a430f2ca7adbef; toutiao_sso_user_ss=fb693373ac8f86fb61a430f2ca7adbef; sid_ucp_sso_v1=1.0.0-KDBhYTgxOTY3MWYzMmI5MjFlNDc3NzRiZjRhMzhhMmUwNjNiZjFmZTIKHQjxvcf16AIQvb3FkgYY7zEgDDCdxbXWBTgGQPQHGgJsZiIgZmI2OTMzNzNhYzhmODZmYjYxYTQzMGYyY2E3YWRiZWY; ssid_ucp_sso_v1=1.0.0-KDBhYTgxOTY3MWYzMmI5MjFlNDc3NzRiZjRhMzhhMmUwNjNiZjFmZTIKHQjxvcf16AIQvb3FkgYY7zEgDDCdxbXWBTgGQPQHGgJsZiIgZmI2OTMzNzNhYzhmODZmYjYxYTQzMGYyY2E3YWRiZWY; odin_tt=c4b54578685a06281469a5d899ff2316289232086370707ee49f60470b5541942c35a0fa367af7f878c9542c2517d9f8; sid_guard=fb693373ac8f86fb61a430f2ca7adbef%7C1649499838%7C5184000%7CWed%2C+08-Jun-2022+10%3A23%3A58+GMT; uid_tt=797a77f8f7d433dc32043257bd1a592b; uid_tt_ss=797a77f8f7d433dc32043257bd1a592b; sid_tt=fb693373ac8f86fb61a430f2ca7adbef; sessionid=fb693373ac8f86fb61a430f2ca7adbef; sessionid_ss=fb693373ac8f86fb61a430f2ca7adbef; sid_ucp_v1=1.0.0-KGVjMzU3YWFlOTI3NTdiNjYxNzI1MDcxNjMxYzQ1MDA3MWEwZTcxNTYKHQjxvcf16AIQvr3FkgYY7zEgDDCdxbXWBTgGQPQHGgJobCIgZmI2OTMzNzNhYzhmODZmYjYxYTQzMGYyY2E3YWRiZWY; ssid_ucp_v1=1.0.0-KGVjMzU3YWFlOTI3NTdiNjYxNzI1MDcxNjMxYzQ1MDA3MWEwZTcxNTYKHQjxvcf16AIQvr3FkgYY7zEgDDCdxbXWBTgGQPQHGgJobCIgZmI2OTMzNzNhYzhmODZmYjYxYTQzMGYyY2E3YWRiZWY; THEME_STAY_TIME=299510; IS_HIDE_THEME_CHANGE=1; pwa_guide_count=3; live_can_add_dy_2_desktop=1; strategyABtestKey=1649524696.967; __ac_nonce=062525a28009cd47de390; __ac_signature=_02B4Z6wo00f01oJDPyQAAIDBSv.2OTJRJi6CYzuAAMLOr4yRjNAYBPKK5C4v.tv8oXJhWE.9wlnrWQxZSuMwpcGgKwmq8nz0Sox8QUQpXIaSGdXooFTEX-BC2YPW4p098cF70EQ5XzlYKB1N90; douyin.com; FOLLOW_NUMBER_YELLOW_POINT_INFO=MS4wLjABAAAA6VYuBeetlGsLBlc0ySJZ5D9b6eQEoQ3V3h9PmGUiVzs%2F1649606400000%2F0%2F0%2F1649565446812; s_v_web_id=verify_803774adf1d52f0d49027ee90d2cc57c; _tea_utm_cache_2018=undefined; FOLLOW_LIVE_POINT_INFO=MS4wLjABAAAA6VYuBeetlGsLBlc0ySJZ5D9b6eQEoQ3V3h9PmGUiVzs%2F1649606400000%2F0%2F0%2F1649566033815; msToken=Ngk7U50RiUF-TDnMqSMrbN154zdzo5AqWy3jWQosBxdbXvMOwAQb-ucv3hbECHMoTAwEynBqW-DUoqjQuhn8bzHEyn7ABQ0Bxnipv1eaUDSQm0GD3-YEzH_ZfTw0iVI=; msToken=RbQBIMrYFRBso70xSZOZE-Ep1d3vJnO6cF6Ri8f8pReIHaLqbeOSLfRbly0HlUrY5T5KDGtzlXmqYzWSk3vwEIVcqfZXZxOWWXmqWq2DD84YZuePM-XNd61rmcBybOc=; tt_scid=gAIvNexPnWic1IxCdOALZnf0mHjOhv6NkNTcEWX-XTBBhbrhymlNYVUCjFPfIZJka995; home_can_add_dy_2_desktop=0'
}
#xiaoshen
#url = 'https://www.douyin.com/user/MS4wLjABAAAANd8NI8CD61BckeGGaHT7FAUDK0WnLsSPLn7H4rDOXuk'
#jessie
# url = 'https://www.douyin.com/user/MS4wLjABAAAAwfxGbF1g6x8AiobOXhu-8KjLjb8ksGBvN9UQvx5bfhM'
#leo
# url = 'https://www.douyin.com/user/MS4wLjABAAAA6VYuBeetlGsLBlc0ySJZ5D9b6eQEoQ3V3h9PmGUiVzs'
#radio
# url = 'https://www.douyin.com/user/MS4wLjABAAAAm0JCC28eMcIIZcar64trqP_kqeqouQClL0Lje_FwIXk'
#temp
# url = 'https://www.douyin.com/user/MS4wLjABAAAAwlt32s-u8z-vKUqjf-esmBjA5sXjI0SBw0dWw3dND5Q'
#qiangge
url = 'https://www.douyin.com/user/MS4wLjABAAAAW098ULejU6a7W77QsGNQPVDt5M5aH3L68uMtPiX2Ptg'


res = requests.get(url = url,headers = headers)
#print(res.text)
title = re.findall('<title data-react-helmet="true">(.*?)</title>',res.text)[0]
video_names = re.findall('<p class="iQKjW6dr">(.*?)</p>',res.text)

#print(re.findall('<p class="iQKjW6dr">(.*?) ',res.text))
#print(video_names)

soup = BeautifulSoup(res.text,'html.parser') # 把网页解析为BeautifulSoup对象
video_name_lists = soup.find_all(class_='iQKjW6dr')
# print(video_name_lists)
#print(video_name_lists[0].text.replace('\n',''))
print(title)
#get video list from profile
lists = soup.find_all(class_='B3AsdZT9 chmb2GX8 UwG3qaZV')
index = 0
for ss in lists:
    #get video link
    li_url = ss['href']
    li_url = li_url.replace('//','https://')
    #print(li_url)
    res_li = requests.get(url=li_url,headers=headers)
    res_url = re.findall('src(.*?)vr%3D%22',res_li.text)
    #print(res_url)
    #get network url
    for res_url_li in res_url:
        #print(res_url_li)
        video_temp_url = requests.utils.unquote(res_url_li)
        #print(video_temp_url)
        video_url = video_temp_url.replace('":"','https:')
        print(video_url)
        # video_name = video_names[index]
        video_name = video_name_lists[index].text.replace('\n','')
        if video_name == '':
            video_name = title.replace('的主页 - 抖音','_')  + str(index)
        print(video_name)
        download_video(title,video_name,video_url)
        index = index + 1
        #break due 4 video url with same content(F5 - load balance)
        break
    #break




