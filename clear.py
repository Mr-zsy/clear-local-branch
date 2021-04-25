#!/usr/bin/python3
#coding:utf-8

import os

# 白名单自动跳过
# auto pass
whiteList = [
    
]

os.system("git branch > .branch")

fileHandler = open(".branch",  "r")
while  True:
    line = fileHandler.readline().strip()
    # print "branch:" + line
    if  not  line  :
        break;
    if (line[0]  == "*") or (line == "master") or (line in whiteList):
        # print "pass:" + line
        continue;
    else:
        os.system("git branch -D {0}".format(line))
    print(line.strip())
fileHandler.close()

os.system("rm .branch")
