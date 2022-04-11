import requests
import re
from selenium import webdriver
import requests
import time
import os

def drop_down():
    for x in range(1,100,4):
        time.sleep(1)
        j = x / 9
        js = 'document.documentElement.scrollTop=document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)
#leo
#url = 'https://www.douyin.com/user/MS4wLjABAAAA6VYuBeetlGsLBlc0ySJZ5D9b6eQEoQ3V3h9PmGUiVzs'
#qiangge
#url = 'https://www.douyin.com/user/MS4wLjABAAAAW098ULejU6a7W77QsGNQPVDt5M5aH3L68uMtPiX2Ptg'
#jessie
# url = 'https://www.douyin.com/user/MS4wLjABAAAAwfxGbF1g6x8AiobOXhu-8KjLjb8ksGBvN9UQvx5bfhM'
#aibijiao
#url = 'https://www.douyin.com/user/MS4wLjABAAAAs0n3zon_4WuLit6gqZOPr2wVydZP6RYOQopO6kD_TYo'
#python auto
# url = 'https://www.douyin.com/user/MS4wLjABAAAAeGtTBYfEYZ5CqqhvsF2nANCZ1aAuHBDYmrIqyvCr8ppQIOXVykK4Buk1Fm7Z0wE-'
#siyu-video-maker
# url = 'https://www.douyin.com/user/MS4wLjABAAAASTYKNahWZcPHSX6vExEb6wqsL4ReR7miI7rjK-znD5tkQR_x-s7RZxt_YwSx2YPl'
#like
url ='https://www.douyin.com/user/MS4wLjABAAAA6VYuBeetlGsLBlc0ySJZ5D9b6eQEoQ3V3h9PmGUiVzs?showTab=like'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(30)
drop_down()

def download_video(title,video_name,video_url):
    res = requests.get(video_url).content
    intab = r'[?*/\|.:><"]'
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
    'cookie': '__ac_nonce=06253e29800da301bbd01; __ac_signature=_02B4Z6wo00f01iuS-7QAAIDB4y4yqcYiTH4rs98AAOjF7e; ttwid=1%7C0iELeKAlbxdZCjV2Xodh09QimSZTCprcX6c9sAgIzgM%7C1649664664%7Cf0f9984716754c72e842abd44677d3c13329e5c2f517555090de55c0674883b2; _tea_utm_cache_6383=undefined; strategyABtestKey=1649664665.946; passport_csrf_token=6bda2d23cfef85bd8a4c5467eabc99ba; passport_csrf_token_default=6bda2d23cfef85bd8a4c5467eabc99ba; s_v_web_id=verify_l1ufqz0m_chQIVGfb_Byes_4ILB_904e_E8DIQgALXAd4; AB_LOGIN_GUIDE_TIMESTAMP=1649664665908; msToken=dzc9FLFQkiLMkV9CN9vl7lXKeNkcxgggiK9hmjdRvDTz-OZCoGtGDirXThLnsHDQ_Cnkuc4Kaecdxne78UqmjZuI_tBXfssdNhGU8mjUtVxkMGKhdZ3ISZp3LPXjFY0=; ttcid=a9847ea954064ad393e902eced25512e14; tt_scid=1.YqDmH.DT1HIp6Tesb5RKs7kVjinAUrU-Iwdub1.M1sV-rn.hIuEjQy8GMx.kHU30c0; n_mh=NIMzHXUK2pnQGgDYWE1t9hOr6wjNH28uUQpDgQXZijo; sso_uid_tt=97e78ef0501bf91a98b5650f7013300a; sso_uid_tt_ss=97e78ef0501bf91a98b5650f7013300a; toutiao_sso_user=2ee0a18f209e38fc0030ceecec514ff3; toutiao_sso_user_ss=2ee0a18f209e38fc0030ceecec514ff3; sid_ucp_sso_v1=1.0.0-KGI0Y2Q3NjM2NTA4YzU5NjJhMTA5NjQyMTliNTg1Zjc1YWMyMzQ0ZDcKHQjxvcf16AIQvsXPkgYY7zEgDDCdxbXWBTgGQPQHGgJsZiIgMmVlMGExOGYyMDllMzhmYzAwMzBjZWVjZWM1MTRmZjM; ssid_ucp_sso_v1=1.0.0-KGI0Y2Q3NjM2NTA4YzU5NjJhMTA5NjQyMTliNTg1Zjc1YWMyMzQ0ZDcKHQjxvcf16AIQvsXPkgYY7zEgDDCdxbXWBTgGQPQHGgJsZiIgMmVlMGExOGYyMDllMzhmYzAwMzBjZWVjZWM1MTRmZjM; msToken=wyVw_wau9LcjeZilsnR9WTecbzvFTYW7Oaeb6MG-M3w3ZcKoc09QTm4oUp4QEQy1SmPcXICxT1yBfXqGJLzcoQw8H8ALIewEIximd_JrtiGB8uVS5TznTQb5OglASBw=; odin_tt=f023116ca7dde18edf8b701976ace4dee468c49c3003080a1991eac5fd24fd77b23ac1912d5c9883d3989c2d1deadaf2; sid_guard=2ee0a18f209e38fc0030ceecec514ff3%7C1649664703%7C5184000%7CFri%2C+10-Jun-2022+08%3A11%3A43+GMT; uid_tt=97e78ef0501bf91a98b5650f7013300a; uid_tt_ss=97e78ef0501bf91a98b5650f7013300a; sid_tt=2ee0a18f209e38fc0030ceecec514ff3; sessionid=2ee0a18f209e38fc0030ceecec514ff3; sessionid_ss=2ee0a18f209e38fc0030ceecec514ff3; sid_ucp_v1=1.0.0-KGMyYWMwNTU1Njc0NGY2OGM4ZTdmNGZmY2RiN2VjMWEyYTMzNDE0YmUKHQjxvcf16AIQv8XPkgYY7zEgDDCdxbXWBTgGQPQHGgJobCIgMmVlMGExOGYyMDllMzhmYzAwMzBjZWVjZWM1MTRmZjM; ssid_ucp_v1=1.0.0-KGMyYWMwNTU1Njc0NGY2OGM4ZTdmNGZmY2RiN2VjMWEyYTMzNDE0YmUKHQjxvcf16AIQv8XPkgYY7zEgDDCdxbXWBTgGQPQHGgJobCIgMmVlMGExOGYyMDllMzhmYzAwMzBjZWVjZWM1MTRmZjM; _tea_utm_cache_2285=undefined; home_can_add_dy_2_desktop=1; THEME_STAY_TIME=41522'
}


video_li_lists = driver.find_elements_by_class_name('ECMy_Zdt') #.find_elements_by_class_name('B3AsdZT9')
full_title = driver.find_element_by_tag_name('title').get_attribute('text')
title = re.findall('(.*?)的主页', full_title)[0]
index = 0
for video_li in video_li_lists:
    video_li_a = video_li.find_element_by_class_name('B3AsdZT9')
    li_url = video_li_a.get_attribute('href')
    video_name = video_li_a.find_element_by_class_name('tt-img-loaded').get_attribute('alt')
    # print(li_url
    video_name = video_name.replace(title+ '：' , '').replace('\n','');
    if video_name == '':
        video_name = title.replace('的主页 - 抖音', '_') + str(index)
    res_li = requests.get(url=li_url,headers=headers)
    res_url = re.findall('src(.*?)vr%3D%22',res_li.text)

    #get network url
    for res_url_li in res_url:
        #unicode url
        video_temp_url = requests.utils.unquote(res_url_li)
        video_url = video_temp_url.replace('":"','https:')
        print('downloading:' + str(index + 1) + '/' + str(len(video_li_lists)))
        print(video_name)
        download_video(title,video_name,video_url)
        index = index + 1
        #break due 4 video url with same content(F5 - load balance)
        break


#driver.close()



