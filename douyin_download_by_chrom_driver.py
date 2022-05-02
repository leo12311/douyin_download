import requests
import re
from selenium import webdriver
import requests
import time
import os

from selenium.webdriver.common.by import By


def drop_down():
    for x in range(1,100,4):
        time.sleep(1)
        j = x / 9
        js = 'document.documentElement.scrollTop=document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)
#leo
url = 'https://www.douyin.com/user/MS4wLjABAAAA6VYuBeetlGsLBlc0ySJZ5D9b6eQEoQ3V3h9PmGUiVzs'
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
# url ='https://www.douyin.com/user/MS4wLjABAAAA6VYuBeetlGsLBlc0ySJZ5D9b6eQEoQ3V3h9PmGUiVzs?showTab=like'
#game
# url ='https://www.douyin.com/user/MS4wLjABAAAAjLUwOKKSgzwqPZItt-n1h4qu_RvSNfi4kqjMAueujAyrT3uxFx6tD4Xcl7OL7n9M?relation=1'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)
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
    'cookie': 'ttwid=1%7Cg_Q0FswESHl5zEuFzgIevsPVRIveUMQhHusXB_T9JLM%7C1650735867%7Ca35868eec8b196b8e9e898beec1264ff8d19eea13446bfba03162002408c3e54; _tea_utm_cache_6383=undefined; passport_csrf_token=83224f5e967b6f430ea30cd7b1c3b5d3; passport_csrf_token_default=83224f5e967b6f430ea30cd7b1c3b5d3; s_v_web_id=verify_l2c5ikx3_70s4M0cx_ggdn_4P9X_8UwJ_KW3czGnNNRu1; _tea_utm_cache_1300=undefined; ttcid=44616dc9a57c4210aadcc4c9c507250325; MONITOR_WEB_ID=d95aee85-e97b-4e30-a2d5-83f5602067b2; THEME_STAY_TIME=299501; IS_HIDE_THEME_CHANGE=1; __ac_nonce=0626582fd00b8d8a99f65; __ac_signature=_02B4Z6wo00f01myHm3QAAIDBpDtSaM9s2oJsp5.AAPlTKD5kTUGsDcjmVhlPzH7PYYvY3g5daUVTxgOL08oRPWTzJsb4AqvaqYM6.65z1TyF2irCBEuTelb89rRjjZbQ2ydIyywFUXBMTKEd17; douyin.com; strategyABtestKey=1650819839.394; pwa_guide_count=2; n_mh=NIMzHXUK2pnQGgDYWE1t9hOr6wjNH28uUQpDgQXZijo; sso_uid_tt=8016b074e4f9b6768be5de5c8041eb5f; sso_uid_tt_ss=8016b074e4f9b6768be5de5c8041eb5f; toutiao_sso_user=0d20e35859b706b7d64514327182e4ce; toutiao_sso_user_ss=0d20e35859b706b7d64514327182e4ce; sid_ucp_sso_v1=1.0.0-KDQzYzEyNWQ3NDc4YmE0YzczNmY1MDkwNjU4ZWY3OWE1NTZmODAwOTYKHQjxvcf16AIQuYmWkwYY7zEgDDCdxbXWBTgGQPQHGgJsZiIgMGQyMGUzNTg1OWI3MDZiN2Q2NDUxNDMyNzE4MmU0Y2U; ssid_ucp_sso_v1=1.0.0-KDQzYzEyNWQ3NDc4YmE0YzczNmY1MDkwNjU4ZWY3OWE1NTZmODAwOTYKHQjxvcf16AIQuYmWkwYY7zEgDDCdxbXWBTgGQPQHGgJsZiIgMGQyMGUzNTg1OWI3MDZiN2Q2NDUxNDMyNzE4MmU0Y2U; odin_tt=c10ec8ff9a723ae0c014bbb0a7e065f49c3030c0fe526f51ef7a4766c2a55a5708f5575b6b5a19c840869a83809bfe9e; sid_guard=0d20e35859b706b7d64514327182e4ce%7C1650820283%7C5184000%7CThu%2C+23-Jun-2022+17%3A11%3A23+GMT; uid_tt=8016b074e4f9b6768be5de5c8041eb5f; uid_tt_ss=8016b074e4f9b6768be5de5c8041eb5f; sid_tt=0d20e35859b706b7d64514327182e4ce; sessionid=0d20e35859b706b7d64514327182e4ce; sessionid_ss=0d20e35859b706b7d64514327182e4ce; sid_ucp_v1=1.0.0-KDZlMDE4YTEzNDE0MGVmODY3ZWViODdmNmM4OTE5ZTkzYTBmZWE4OTgKHQjxvcf16AIQu4mWkwYY7zEgDDCdxbXWBTgGQPQHGgJsZiIgMGQyMGUzNTg1OWI3MDZiN2Q2NDUxNDMyNzE4MmU0Y2U; ssid_ucp_v1=1.0.0-KDZlMDE4YTEzNDE0MGVmODY3ZWViODdmNmM4OTE5ZTkzYTBmZWE4OTgKHQjxvcf16AIQu4mWkwYY7zEgDDCdxbXWBTgGQPQHGgJsZiIgMGQyMGUzNTg1OWI3MDZiN2Q2NDUxNDMyNzE4MmU0Y2U; FOLLOW_LIVE_POINT_INFO=MS4wLjABAAAA6VYuBeetlGsLBlc0ySJZ5D9b6eQEoQ3V3h9PmGUiVzs%2F1650902400000%2F0%2F1650820287112%2F0; msToken=GQokxM0PyHtVcVjyv1dCV7sglVLtpQmvSxHRcK74Yj3eNgxRBM-8_RXVRBGyl5D9wfSSVhYkRuWXnwyOTj1DFW2VzegSgMqozmUBQudmtGGVJjXRWMhj; tt_scid=papXZ.e9GnxjyhRXb-rMS-SbPr9rcXEVHomhmjJt2PQnmNT-UY9f3UG5JDZbf-DF50b6; home_can_add_dy_2_desktop=1; msToken=GH3lZqITKKOQHSqw2DbkepYdmbxRlIz6qfTl5Q_ObRSPx9jdEq4V_8fw3DXLu_wEGF3emMvlrHtddFb2cc1WVSE-abw1jfjinM8lESrmwaNlwUNzpzUH'
}

# print(driver.page_source)
video_li_lists = driver.find_elements_by_class_name('ECMy_Zdt') #.find_elements_by_class_name('B3AsdZT9')
# video_li_lists = driver.find_elements(By.CLASS_NAME,'ECMy_Zdt')
print(video_li_lists)
# full_title = driver.find_element_by_tag_name('title').get_attribute('text')
# print(driver.find_element(By.TAG_NAME,'title'))
page_text = driver.page_source
# print(driver.find_element(By.XPATH,'/html/head/title').text)
# full_title = driver.find_element(By.TAG_NAME,'title')
# full_title = re.findall('<p class="iQKjW6dr">(.*?)</p>',res.text)
# print(full_title)
#full_title = 'Lex软件工作室的主页 - 抖音'
title = re.findall('<title>(.*?)的主页', page_text)[0]
# print(page_text)
print(len(video_li_lists))
index = 0
for video_li in video_li_lists:
    video_li_a = video_li.find_element_by_class_name('B3AsdZT9')
    li_url = video_li_a.get_attribute('href')
    # print(li_url)
    # print(video_li_a.find_element_by_tag_name('img').get_attribute('alt'))
    # video_name = video_li_a.find_element_by_class_name('t-img-loaded').get_attribute('alt')
    video_name  = video_li_a.find_element_by_tag_name('img').get_attribute('alt')
    # print(li_url
    video_name = video_name.replace(title+ '：' , '').replace('\n','')
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



