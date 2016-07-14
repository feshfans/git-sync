# -*- coding: utf-8 -*-

import inspect
import os
import json


class Config :

    __jsonObj={};
    @staticmethod
    def __getConfigFile():
        this_file =inspect.getfile(inspect.currentframe())
        dirPath = os.path.dirname(this_file)
        return os.path.join(dirPath,"config.json")

    @staticmethod
    def __parseJson():
        jsonfile=file(Config.__getConfigFile(), mode="r")
        Config.__jsonObj=json.load(jsonfile,"UTF-8")

    @staticmethod
    def getDir():
        if not Config.__jsonObj.has_key("dir"):
            Config.__parseJson()

        return Config.__jsonObj['dir']

    @staticmethod
    def getGit():
        if not Config.__jsonObj.has_key("git"):
            Config.__parseJson()

        return Config.__jsonObj['git']



if __name__ == '__main__':
    print  Config.getDir()
    print Config.getGit()