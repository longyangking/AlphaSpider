#!/usr/bin/python

import urllib

class URL(object):
    def __init__(self,url):
        self.url = url
    
    def getPage(self):
        self.page = urllib.urlopen(self.url)
    
    def getHtml(self):
        html = page.read()
        return html
