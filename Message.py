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
    def getAllMessagebyTargetName(self,target):
        if not target in self.__mesageheadlist:
            return False
        if target in self.__mesageheadlist[self.tail_:self.head_]:
            indexlist = []
            index = self.tail_-1
            while index+1 < self.head_:
                if not target in self.__mesageheadlist[index+1:self.head_]:
                    break
                index = self.__mesageheadlist.index(target,index+1,self.head_)
                if self.__mesagelist[index]['isUsed'] == True:
                    continue
                indexlist.insert(-1,index)
            resultmessageList = []
            for i in indexlist:
                self.__mesagelist[i]['isUsed'] = True
                resultmessageList.insert(-1,self.__mesagelist[i])        
            #self.__mesagelist[index]['isUsed'] = True
            return resultmessageList
        else:
            return False 
    def getAMessageByTargetName(self,target):
        if not target in self.__mesageheadlist:
            return False
        if target in self.__mesageheadlist[self.tail_:self.head_]:
            index = self.tail_ - 1
            while index+1 < self.head_:
                if not target in self.__mesageheadlist[index+1:self.head_]:
                    break
                index = self.__mesageheadlist.index(target,index+1,self.head_)
                if self.__mesagelist[index]['isUsed'] == False:
                    break   
            self.__mesagelist[index]['isUsed'] = True
            return self.__mesagelist[index]
        else:
            return False
    def readAllMessagebyTargetName(self,target):
        if not target in self.__mesageheadlist:
            return False
        if target in self.__mesageheadlist[self.tail_:self.head_]:
            indexlist = []
            index = self.tail_-1
            while index+1 < self.head_:
                if not target in self.__mesageheadlist[index+1:self.head_]:
                    break
                index = self.__mesageheadlist.index(target,index+1,self.head_)
                if self.__mesagelist[index]['isUsed'] == True:
                    continue
                indexlist.insert(-1,index)
            resultmessageList = []
            for i in indexlist:
                resultmessageList.insert(-1,self.__mesagelist[i])        
            return resultmessageList
        else:
            return False
        def readAMessageByTargetName(self,target):
            if not target in self.__mesageheadlist:
                return False
            if target in self.__mesageheadlist[self.tail_:self.head_]:
                index = self.tail_ - 1
                while index+1 < self.head_:
                    if not target in self.__mesageheadlist[index+1:self.head_]:
                        break
                    index = self.__mesageheadlist.index(target,index+1,self.head_)
                    if self.__mesagelist[index]['isUsed'] == False:
                        break   
                return self.__mesagelist[index]
            else:
                return False 
    def __popMessage(self,index):
        
        return
messager = Messager()