# -*- coding: utf-8 -*-
import time
import datetime
import os
from config import config
from pyquery.pyquery import PyQuery

class AddArticle :
    __myCss='<link rel="stylesheet" href="../stylesheets/my.css">';
    def __init__(self):
        self.currentTime=datetime.datetime(1970,1,1,0,0,0)

    def validfile(self):
        articleDir=config.getDir()+"/article"
        files=os.listdir(articleDir)
        for fileName in files:
            query=PyQuery(filename=articleDir+"/"+fileName)
            query('head').append(AddArticle.__myCss)
            f=file(articleDir+"/"+fileName+"2","w+")
            f.writelines(query.html().__str__())
            f.close()

    def __str__(self):
        print self.currentTime




class GitUtils :
    def __init__(self,gitPath,workDir):
        self.gitPath=gitPath
        self.workDir=workDir

    def gitStatus(self):
        print os.system(self.gitPath+" -C "+self.workDir+" status -s")

if __name__=='__main__' :
    #康会来
    git=GitUtils('C:/Users/Administrator/Desktop/blog/feshfans.github.io')
    git.gitStatus()

