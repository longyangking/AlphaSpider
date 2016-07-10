#!/usr/bin/python
import urllib

class storage(object):
    def __init__(self,resource):
        self.resource = resource
    
    def save(self,location):
        urllib.urlretrieve(self.resource,location)
