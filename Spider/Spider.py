#!/usr/bin/python
import url.url as URL
import content.content as Content
import storage.storage as Storage

class Spider(object):
    def __init__(self,url):
       self.url = URL(url)
    
    
