# -*- coding: utf-8 -*-

from git import *
import sys
from config import Config

# 设置python的编码为UTF-8
reload(sys)
sys.setdefaultencoding('utf8')

class GitCommandWrapper(object):

    def __init__(self,gitDir):
        print gitDir
        self.repo=Repo(gitDir)
        self.git=self.repo.git

    def getModifiedFiles(self):
        lines = self.git.execute('git status -s')
        lines = [line.strip() for line in lines.split("\n")]
        for line in lines:
            if not line.startswith('M'):
                lines.remove(line)
        return lines


    def getAddFiles(self):
        '''
        获取需要增加的文件列表
        :return:
        '''
        return self.repo.untracked_files

    def commit(self, message, files=[]):
        """"
        提交修改文件，默认为全部
        :param message: 提交记录
        :param files: 提交的文件
        :return: 是否成功
        """
        pass
    def add(self,files=[]):
        '''
        添加文件
        :param files:需要添加的文件,默认为全部
        :return: 是否成功
        '''
        pass

    def push(self, **kwargs):
        pass

if __name__ == "__main__":

    gitCmd = GitCommandWrapper(Config.getDir())

    print gitCmd.getModifiedFiles()
    print gitCmd.getAddFiles()