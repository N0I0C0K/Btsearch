import requests
import json
#import unicodedata
import string
import pyaudio
import wave
import os

URL = 'http://music.zhuolin.wang/api.php?callback=jQuery111303909958994421281_1564923774351 '

def main():
    dr1 = {'name':'znja'}
    dr2 = {'name':'njskkndk'}
    list1 = [dr1,dr2]
    list2 = [1,2,3,4,5,6,7]
    list1[0]['name'] = 'snnkj'
    print(dr1['name'])
    print(list2.index(5,1,5))
    return 
    #return

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


