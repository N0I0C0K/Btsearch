import requests
import json
#import unicodedata
import string

URL = 'http://music.zhuolin.wang/api.php?callback=jQuery111303909958994421281_1564923774351 '

def main():
    headers = {
        #'Host': 'music.zhuolin.wang',
        #'Connection': 'keep-alive',
        #'Content-Length': '54',
        #'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        #'Origin': 'http://music.zhuolin.wang',
        #'X-Requested-With': 'XMLHttpRequest',
        #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        #'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'Referer': 'http://music.zhuolin.wang/',
        #'Accept-Encoding': 'gzip, deflate',
        #'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    cookie = {
        'UM_distinctid': '169aa89725120a-087ab004b54892-9333061-144000-169aa897252acf',
        '__SDID': '44c6a52bc7ce2e19',
        'CNZZDATA1260050386': '588805887-1553341797-http%253A%252F%252Flink.zhihu.com%252F%7C1564919555'
    }
    data = {
        'types': 'search',
        'count': '20',
        'source': 'netease',
        'pages': '1',
        'name': 'nick'
    }
    data1 = {
        'types':'url',
        'id':'448749148',
        'source':'netease'
    }
    response = requests.post(URL,data = data,headers = headers,cookies = cookie)
    #str1 = bytes(response.text,'GBK')
    #str2 = str(response.text,encoding = 'ascii')
    print(response.content)
    str2 = response.content.decode('unicode_escape')
    js1 = toJsonStr2(str2)
    #str2 = str(response.text)
    '''js1 = toJsonStr(str2)
    js1['url'] = handleURL(js1['url'])
    music_response = requests.get(js1['url'])
    if (music_response.status_code != 200):
        print('ERROR')
        return
    with open('music.wav','wb') as playfile:
        for chunk in music_response.iter_content(1024):
            playfile.write(chunk)
    return '''
    return

def handleURL(origin_url):
    str1 = str(origin_url).strip('/')
    return str1

def toJsonStr(text):
    str1 = str(text)
    index1 = str1.find('{')
    index2 = str1.rfind('}')
    str1 = str1[index1:index2+1]
    js1 = json.loads(str1)
    return js1

def toJsonStr2(text):
    str1 = str(text)
    index1 = str1.find('(')
    index2 = str1.rfind(')')
    str1 = '{\"music\":' + str1[index1+1:index2] + '}'
    print(str1)
    js1 = json.loads(str1)
    return js1

if __name__ == "__main__":
    main()


