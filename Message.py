import json
from enum import Enum

class MessageERROR(Exception):
    def __init__(self,value):
        self.value = value
    def __repr__(self):
        return str(self.value)

class MessageEnum(Enum):
    PLAYMUSIC = 1
    STOPMUSIC = 2

class Messager():
    __mesagelist = list()
    __mesageheadlist = list()
    head_ = 0
    tail_ = 0
    def __init__(self):
        self.__mesagelist = list()
        self.__mesageheadlist = list()
        self.head_ = 0
        self.tail_ = 0
        return
    
    def pushMessage(self,message):
        if (self.tail_ > self.head_):
            raise MessageERROR('ERROR:tail > head')
        self.__mesagelist.append(message)
        self.__mesageheadlist.append(message['target'])
        self.head_ += 1
        return
    def isinLine(self,target):
        if not target in self.__mesageheadlist:
            return False
        #if target in self.__mesageheadlist[self.tail_:self.head_]

messager = Messager()