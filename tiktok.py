import threading
import utils
import requests
proxies = {
}
sessionid = input('SessionID: ')
username = input('Username: ')
try:
    threads = int(input('Threads: '))
except: print('invalid thread count'); exit(2)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
    'Accept': '*/*',
    'Cookie': 'sessionid=' + sessionid
}
secUID = requests.get('https://www.tiktok.com/api/user/detail/?uniqueId=' + username, headers=headers)
if 'secUid' in secUID.text: secUID = secUID.json()['userInfo']['user']['secUid']; print(f'Found secUid [{secUID}]')
else: print('cant find secuid, are you sure session id is correct and from tiktok web?'); exit(0)
try:
    r = int(input('[1] Private Video\n[2] Delete Video\n[?] Choice: '))
    if r != 1 and r != 2: print('invalid choice'); exit(1)
except: print('number required'); exit(0)


def execute_video(vidId):
    if r == 1: url = f'https://api2-19.musical.ly/aweme/v1/aweme/modify/visibility/?aweme_id={vidId}&type=2&retry_type=no_retry&app_language=en&language=en&region=US&sys_region=US&carrier_region=AU&carrier_region_v2=505&build_number=8.0.0&timezone_offset=-18000&timezone_name=America%2FNew_York&mcc_mnc=&is_my_cn=0&fp=&iid=7035517353585133317&device_id=6909925976185112070&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=800&version_name=8.0.0&device_platform=android&ssmix=a&device_type=CPH2069&device_brand=OPPO&os_api=30&os_version=11&openudid=aa9cbb2600371100&manifest_version_code=2018080204&resolution=1080*2158&dpi=480&update_version_code=2018080204&_rticket=1638738337566&ts=1638738334&as=a156526a1ef981996d4355&cp=219f1f6fefdca296e1IiQm&mas=011c83457c29ac3aa2884b83e958634859acaccc2c266c9c9c8c1c'
    else: url = f'https://api2-t2.musical.ly/aweme/v1/aweme/delete/?aweme_id={vidId}&retry_type=no_retry&app_language=en&language=en&region=US&sys_region=US&carrier_region=AU&carrier_region_v2=505&build_number=8.0.0&timezone_offset=-18000&timezone_name=America%2FNew_York&mcc_mnc=&is_my_cn=0&fp=&iid=7035517353585133317&device_id=6909925976185112070&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=800&version_name=8.0.0&device_platform=android&ssmix=a&device_type=CPH2069&device_brand=OPPO&os_api=30&os_version=11&openudid=aa9cbb2600371100&manifest_version_code=2018080204&resolution=1080*2158&dpi=480&update_version_code=2018080204&_rticket=1638776770418&ts=1638776769&as=a1f6fb8aa1ac21cffd4355&cp=b3c0176117dca0f4e1Wg_o&mas=013068d951537896ca000637664b771b9facaccc2c266666c68c4c'
    headers = {
        'X-SS-QUERIES': 'dGMCA76ot3awALq2Nv3edxyWhApr9xWK%2BlmEijd1WnNylmFbxRx0wm95EoIpvNB3OsC1HO8SzMIENA51cwBS%2BrsN1T%2Butgt4rILc5cqsABMttXn3Bk8lrPnLgEj06weXXJb1ew%3D%3D',
        'X-SS-TC': '0',
        'User-Agent': 'com.zhiliaoapp.musically/2018080204 (Linux; U; Android 11; en_US; CPH2069; Build/RKQ1.200903.002; Cronet/58.0.2991.0)'
    }
    l = requests.get(url, headers=headers, cookies={'sessionid': sessionid})
    if l.json()['status_code'] == 0:
        print('Video Done | ' + vidId)

def get_videos():
    cursor = 0
    while 1:
        x_tt_params = {
            "aid":"1988",
            "app_name":"tiktok_web",
            "channel":"tiktok_web",
            "device_platform":"web_pc",
            "device_id":"7116500568952374786",
            "region":"AU",
            "priority_region":"AU",
            "os":"windows",
            "referer":"",
            "root_referer":"undefined",
            "cookie_enabled":"true",
            "screen_width":"1440",
            "screen_height":"900",
            "browser_language":"en-GB",
            "browser_platform":"MacIntel",
            "browser_name":"Mozilla",
            "browser_version":"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            "browser_online":"true",
            "verifyFp":"",
            "app_language":"en",
            "webcast_language":"en",
            "tz_name":"Australia/Sydney",
            "is_page_visible":"true",
            "focus_state":"true",
            "is_fullscreen":"false",
            "history_len":"5",
            "battery_info":"0.07",
            "from_page":"user",
            "secUid":secUID,
            "count":"30",
            "cursor":str(cursor),
            "language":"en",
            "userId":'undefined',
            "is_encryption":"1"
        }
        x_tt_params = utils.encrypt(x_tt_params)
        rs = requests.get('https://www.tiktok.com/api/post/item_list/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.07&browser_language=en-GB&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F103.0.5060.53%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7116500568952374786&device_platform=web_pc&focus_state=true&from_page=user&history_len=5&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=AU&referer=&region=AU&screen_height=900&screen_width=1440&tz_name=Australia%2FSydney&verifyFp=&webcast_language=en', headers={
            'X-Tt-Params': x_tt_params,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
            'Accept': '*/*'
        })
        if 'itemList' in rs.json():
            for item in rs.json()['itemList']:
                video_id = item['id']
                running = True
                while running:
                    if threading.active_count() <= threads:
                        running = False
                        threading.Thread(target=execute_video, args=((video_id,))).start()
        else: print('error fetching videos'); break
        if rs.json()['hasMore']: cursor = rs.json()['cursor']
        else: break
get_videos()
