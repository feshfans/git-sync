# -*- coding: utf-8 -*-

import inspect
import os
import json
class config :

    __jsonObj={};
    @staticmethod
    def __getConfigFile():
        this_file =inspect.getfile(inspect.currentframe())
        dirPath = os.path.dirname(this_file)
        return os.path.join(dirPath,"config.json")

    @staticmethod
    def __parseJson():
        jsonfile=file(config.__getConfigFile(), mode="r")
        config.__jsonObj=json.load(jsonfile,"UTF-8")

    @staticmethod
    def getDir():
        if not config.__jsonObj.has_key("dir"):
            config.__parseJson()

        return config.__jsonObj['dir']

    @staticmethod
    def getGit():
        if not config.__jsonObj.has_key("git"):
            config.__parseJson()

        return config.__jsonObj['git']



if __name__ == '__main__':
    print  config.getDir()
    print config.getGit()