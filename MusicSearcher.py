import json
import requests

class MusicSearcher:
    URL =  'http://music.zhuolin.wang/api.php?callback=jQuery111303909958994421281_1564923774351 '
    headers = {
        #'Host': 'music.zhuolin.wang',
        #'Connection': 'keep-alive',
        #'Content-Length': '54',
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        #'Origin': 'http://music.zhuolin.wang',
        'X-Requested-With': 'XMLHttpRequest',
        #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        #'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'Referer': 'http://music.zhuolin.wang/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    cookie = {
        'UM_distinctid': '169aa89725120a-087ab004b54892-9333061-144000-169aa897252acf',
        '__SDID': '44c6a52bc7ce2e19',
        'CNZZDATA1260050386': '588805887-1553341797-http%253A%252F%252Flink.zhihu.com%252F%7C1564919555'
    }
    def __init__(self):
        return
    def getMusicByKeyword(self,keyword):
        data = {
            'types': 'search',
            'count': '20',
            'source': 'netease',
            'pages': '1',
            'name': keyword
        }
        response = requests.post(self.URL,data = data,headers = self.headers,cookies = self.cookie)
        str1 = str(response.content.decode('unicode_escape'))
        index1 = str1.find('(')
        index2 = str1.rfind(')')
        str1 = '{\"music\":' + str1[index1+1:index2] + '}'
        result = json.loads(str1)
        return result
    def getMusicByID(self,musicID):
        data = {
            'types':'url',
            'id':str(musicID),
            'source':'netease'
        }
        response = requests.post(self.URL,data = data,headers = self.headers,cookies = self.cookie)
        resulttext = response.content.decode('utf-8')
        #str2 = str(response.text)
        resultjson = toJsonStr(resulttext)
        resultjson['url'] = handleURL(resultjson['url'])
        return resultjson['url']
    def getMusicHEXbyURL(self, musicurl):
        response = requests.get(musicurl)
        if (response.status_code != 200):
            print('ERROR:can not get music by url')
        return response.content
    

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