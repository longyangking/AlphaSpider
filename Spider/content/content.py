#!/usr/bin/python

import re

class content(object):
    def __init__(self,text):
        self.text = text
    
    def getImg(self):
        reg = r'src="(.+?\.jpg)" pic_ext'
        imgre = re.compile(reg)
        imglist = re.findall(imgre,self.text)
        return imglist
