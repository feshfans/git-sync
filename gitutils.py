# -*- coding: utf-8 -*-

from git import *



if __name__=="__main__":
    repo=Repo('C:/Users/Administrator/Desktop/blog/feshfans.github.io')
    print repo.is_dirty()
    print repo.untracked_files

    #print repo.active_branch.