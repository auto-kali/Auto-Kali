# -*- coding=UTF8 -*-

import time
import os
from termcolor import *


def main():
    print (colored(
"""
############SETTINGS############
Update   更新Auto-kali
################################
""","yellow"))
    XX = input(colored("选项:","yellow"))
    if XX == "Update":
        f = open("/usr/share/auto-kali/Auto-kali-path.conf")
        p = f.read()
        p = str(p)
        p = p.strip()
        os.system("cd %s && git stash && git pull" % p)
        print (colored("操作完成，3秒后重启脚本","yellow"))
        time.sleep(3)
        exit()
    elif XX == "exit":
        exit()
    else:
        main()

if __name__ == '__main__':
    main()
