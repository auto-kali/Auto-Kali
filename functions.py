# -*- coding: UTF-8 -*-

import os
import time

from termcolor import *

zwf=0

def restart():
    f = open("/usr/share/auto-kali/Auto-kali-path.conf")
    p = f.read()
    p = str(p)
    p = p.strip()
    os.system("python3 %s/master.py" % p)
    exit()
    pass

def  download():
    XC = input(colored("输入要使用的线程数  >>> ","yellow"))
    LJ = input(colored("输入要下载的文件链接  >>> ","yellow"))
    print (colored("初始化中Loding...","yellow"))
    os.system("apt-get -y install axel")
    print (colored("初始化完成","yellow"))
    os.system("axel -o /root/ -n"+ XC +' '+'\"'+LJ+'\"')
    os.system('reset')
    print (colored("文件存放路径：/root/","yellow"))
    print (colored("操作完成，3秒后重启脚本","yellow"))
    time.sleep(3)
    restart()
    exit()
    pass

class install_Manager():
    def help(self):
        print (colored('可安装的软件列表:                ',"yellow"))
        print (colored("┌───────────────────────────────────┐","yellow"))
        print (colored('│      软件名称        │   支持状态 │',"yellow"))
        print (colored("├───────────────────────────────────┤","yellow"))
        print (colored('│   1.网易云音乐       │     √      │',"yellow"))
        print (colored('│   2.PinYin or 输入法 │     √      │',"yellow"))
        print (colored('│   3.补全系统         │     √      │',"yellow"))
        print (colored('│   4.vm-tools         │     √      │',"yellow"))
        print (colored('│   5.QQirc            │     √      │',"yellow"))
        print (colored('│   6.mdk4             │     √      │',"yellow"))
        print (colored('│   7.bettercap(v1.6)  │     √      │',"yellow"))
        print (colored('│   8.powershell       │     √      │',"yellow"))
        print (colored("└───────────────────────────────────┘","yellow"))
    def __init__(self):
        pass
    def wyymusic(self):
        os.system('apt-get -y install gdebi')
        os.system('wget -P /tmp  http://d1.music.126.net/dmusic/netease-cloud-music_1.1.0_amd64_ubuntu.deb')
        os.system('gdebi /tmp/netease-cloud-music_1.1.0_amd64_ubuntu.deb')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","yellow"))
        time.sleep(3)
        restart()
        exit()
    def pinyin(self):
        os.system('apt-get -y install fcitx-pinyin')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","yellow"))
        time.sleep(3)
        restart()
        exit()
    def kalilinuxful(self):
        os.system('apt-get -y install kali-linux-all')
        print (colored("操作完成，3秒后重启脚本","yellow"))
        os.system('reset')
        time.sleep(3)
        restart()
        exit()
    def vmtools(self):
        os.system('apt-get update')
        os.system('apt-get -y install open-vm-tools-desktop fuse')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","yellow"))
        time.sleep(3)
        restart()
        exit()
    def qqirc(self):
        os.system("reset")
        print (colored("第一阶段:安装依赖!","red"))
        os.system("apt-get install perl  -y")
        os.system("apt-get install libssl-dev -y")
        os.system("apt-get install cpanminus -y")
        os.system("reset")
        print (colored("第二阶段:安装ircQQ","red"))
        os.system("cpanm Mojo::Webqq")
        os.system("cpanm -v Mojo::IRC::Server::Chinese")
        os.system("reset")
        print (colored("第三阶段:配置并运行!","red"))
        os.system("touch /home/qq.pl")
        irc = open("/home/qq.pl","a")
        irc.write("""#!/usr/bin/env perl
use Mojo::Webqq;
my ($host,$port,$post_api);
$host = "0.0.0.0"; #发送消息接口监听地址，没有特殊需要请不要修改
$port = 5000;      #发送消息接口监听端口，修改为自己希望监听的端口
my $client = Mojo::Webqq->new();
$client->load("ShowMsg");
$client->load("Openqq",data=>{listen=>[{host=>$host,port=>$port}], post_api=>$post_api});
$client->run();""")
        irc.close()
        print (colored("配置完成!","red"))
        os.system("echo 'perl /home/qq.pl' > ~/QQirc.sh")
        os.system("perl /home/qq.pl")
        restart()
        exit()
    def mdk4(self):
        os.system("reset")
        print (colored("第一阶段:安装依赖!","red"))
        os.system("apt-get -y install g++ git  libnl-3-dev libnl-genl-3-dev pkg-config libpcap-dev build-essential")
        print (colored("第二阶段:CLONE项目","red"))
        os.system('git clone https://github.com/aircrack-ng/mdk4.git "/home/mdk4"')
        print (colored("第二阶段:编译","red"))
        os.system('echo "cd /home/mdk4\nmake\nmake install" > /tmp/LS.sh')
        os.system("sh /tmp/LS.sh")
        os.system("rm /tmp/LS.sh")
        print (colored("操作完成，3秒后重启脚本","yellow"))
        time.sleep(3)
        restart()
        exit()
    def bettercap(self):
        f = open("/usr/share/auto-kali/Auto-kali-path.conf")
        p = f.read()
        p = str(p)
        p = p.strip()
        os.system("bash %s/scrips/install_old_bettercap.sh" % p)
        print (colored("操作完成，3秒后重启脚本 开启命令:bettercapj","yellow"))
        time.sleep(3)
        restart()
        exit()
    def powershell(self):
        DXCXX = input(colored("多线程下载(Y,N):"))
        if DXCXX == "Y":
            os.system('axel -o /tmp -n 25 "https://github.com/PowerShell/PowerShell/releases/download/v6.0.2/powershell_6.0.2-1.debian.9_amd64.deb"')
            os.system("dpkg -i /tmp/powershell_6.0.2-1.debian.9_amd64.deb")
            os.system("apt-get install -f -y")
            inst = open("/bin/powershell","w")
            inst.write("""#!/usr/bin/env bash
exec xterm -e pwsh &""")
            inst.close()
            print (colored("操作完成，3秒后重启脚本 开启命令:powershell","yellow"))
            time.sleep(3)
            restart()
            exit()
        if DXCXX == "N":
            os.system('wget -P /tmp "https://github.com/PowerShell/PowerShell/releases/download/v6.0.2/powershell_6.0.2-1.debian.9_amd64.deb"')
            os.system("dpkg -i /tmp/powershell_6.0.2-1.debian.9_amd64.deb")
            os.system("apt-get install -f -y")
            os.system("touch /bin/powershell")
            os.system("chmod 777 /bin/powershell")
            inst = open("/bin/powershell","w")
            inst.write("""#!/usr/bin/env bash
exec xterm -e pwsh &""")
            inst.close()
            print (colored("操作完成，3秒后重启脚本 开启命令:powershell","yellow"))
            time.sleep(3)
            restart()
            exit()
            pass
        pass
    pass

class deb_Manager():
    def __init__(self):
        pass
    def help(self):
        print (colored('可安装的软件源列表:                 ',"yellow"))
        print (colored("┌───────────────────────────────────┐","yellow"))
        print (colored('│      软件源名称        │ 支持状态 │',"yellow"))
        print (colored("├───────────────────────────────────┤","yellow"))
        print (colored('│       1.中科大         │     √    │',"yellow"))
        print (colored('│       2.官方源         │     √    │',"yellow"))
        print (colored('│       3.手动(高级)     │     √    │',"yellow"))
        print (colored("└───────────────────────────────────┘","yellow"))
    def zkd(self):
        os.system('rm -rf /etc/apt/sources.list')
        os.system('echo "deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib\ndeb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib" >/etc/apt/sources.list')
        os.system('apt-get update --fix-missing')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","yellow"))
        time.sleep(3)
        restart()
        exit()
    def gfy(self):
        os.system('rm -rf /etc/apt/sources.list')
        os.system('echo "deb http://http.kali.org/kali kali-rolling main non-free contrib\ndeb-src http://http.kali.org/kali kali-rolling main non-free contrib" >/etc/apt/sources.list')
        os.system('apt-get update --fix-missing')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","yellow"))
        time.sleep(3)
        restart()
        exit()
    def sd(self):
        os.system("reset")
        print (colored(r'本模块作者:{"text":"josn"}',"red"))
        DAA = input(colored("help查看帮助,请选择模式  >>> ","yellow"))
        if DAA == "help":
            print (colored('                模式名称     介绍',"red"))
            print (colored('                w     覆盖之前的数据(危险)',"red"))
            print (colored('                a     追加写入(推荐)',"red"))
            DAA = input(colored("请选择模式  >>> ","yellow"))
        if DAA == "w":
            DA = open("/etc/apt/sources.list","w")
            XR = input(colored(r"写入\n即可换行,写入源地址  >>> ","yellow"))
            DA.write(XR)
            DA.close
            print (colored("操作完成，3秒后重启脚本","yellow"))
            time.sleep(3)
            restart()
            exit()
        if DAA == "a":
            DA = open("/etc/apt/sources.list","a")
            XR = input(colored(r"写入\n即可换行,写入源地址  >>> ","yellow"))
            DA.write(XR)
            DA.close()
            print (colored("操作完成，3秒后重启脚本","yellow"))
            time.sleep(3)
            restart()
            exit()
            pass
        pass
    pass

class bug_Manager():
    def __init__(self):
        pass
    def gpg(self):
        os.system('wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add')
        os.system('apt-get update')
        os.system('reset')
        print (colored("操作完成，3秒后重启脚本","yellow"))
        time.sleep(3)
        restart()
        exit()
    def boot(self):
        os.system("echo 'deb http://ppa.launchpad.net/yannubuntu/boot-repair/ubuntu bionic main ' >> /etc/apt/sources.list")
        os.system("echo 'deb-src http://ppa.launchpad.net/yannubuntu/boot-repair/ubuntu bionic main ' >> /etc/apt/sources.list")
        os.system("apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 60D8DA0B")
        os.system("apt-get update")
        os.system("apt-get install -y boot-repair")
        os.system("nohup boot-repair&")
        print (colored("操作完成，3秒后重启脚本","yellow"))
        time.sleep(3)
        restart()
        exit()
    def gnome_show_icon_on_desktp(self):
        print("""Warning:This fix script on "GNOME Shell >= 3.28 Nautilus >= 3.30" If you are another version This scripy maybe can't play a role of your PC.""")
        print("""If you don't know that meaning,You can try. (And your Language Unsupported!)""")
        #write shell script
        os.system("touch /tmp/fix.sh")
        script = open("/tmp/fix.sh",'w')
        script.write("""
if (whiptail --title "AUTO-KALI BUG FIX"  --yesno 'Warning:This fix script on "GNOME Shell >= 3.28 Nautilus >= 3.30" If you are another version This scripy maybe cant play a role of your PC.(Your Language Unsupported!)\n\nIf you press Yes button you will logout and Follow the steps to Compulete\n\n1.在终端内输入"gnome-tweaks"\n2.点击"扩展"\n3.找到"Desktop-icons"并开启' 20 70) then
    apt-get install gnome-shell nautilus gnome-shell-extension-desktop-icons -y
    echo "Logout in 3s"
    sleep 3
    gnome-shell --replace
    exit
else
    echo "Cancel"
    exit
fi""")
        script.close()
        os.system("bash /tmp/fix.sh")
        print (colored("操作完成，3秒后重启脚本","yellow"))
        time.sleep(3)
        restart()
        exit()
    def help(self):
        print (colored("┌──────────────────────────────────────┐","blue"))
        print (colored("│  gpg 修复apt-get时的数字签名错误     │","blue"))
        print (colored("│  boot 引导修复(必须运行在Xsession上) │","blue"))
        print (colored("│  gnome 显示桌面图标                  │","blue"))
        print (colored("└──────────────────────────────────────┘","blue"))
        pass
    pass

def deb():
    print (colored('输入help以查询支持的软件源',"green"))
    while (zwf==zwf):
        debX = input(colored('请写入您要变为的软件源“序号or中文”  >>> ',"yellow"))
        if debX == "help":
            deb_Manager.help(zwf)
        elif debX == "中科大" or debX == "1":
            deb_Manager.zkd(zwf)
            exit()
        elif debX == "官方源" or debX == "2":
            deb_Manager.gfy(zwf)
            exit()
        elif debX == "手动" or debX == "3":
            deb_Manager.sd(zwf)
            exit()
        elif debX == "exit":
            exit()
            pass
        pass
    pass

def install():
    print (colored('输入help以查询支持安装的软件',"green"))
    while (zwf==zwf):
        AZXX = input(colored('请写出您要安装的程序  >>> ',"yellow"))
        if AZXX == "help":
            install_Manager.help(zwf)
        elif AZXX ==  "网易云音乐" or AZXX == "1":
            install_Manager.wyymusic(zwf)
            exit()
        elif AZXX == "PinYin" or AZXX == "2" or AZXX == "输入法":
            install_Manager.pinyin(zwf)
            exit()
        elif AZXX == "补全系统"or AZXX == "3":
            install_Manager.kalilinuxful(zwf)
            exit()
        elif AZXX == "vm-tools" or AZXX == "4":
            install_Manager.vmtools(zwf)
            exit()
        elif AZXX == "QQirc" or AZXX == "5":
            install_Manager.qqirc(zwf)
            exit()
        elif  AZXX == "mdk4" or AZXX == "6":
            install_Manager.mdk4(zwf)
            exit()
        elif AZXX == "bettercap" or AZXX == "7":
            install_Manager.bettercap(zwf)
            exit()
        elif AZXX == "powershell" or AZXX == "8":
            install_Manager.powershell(zwf)
            exit()
        elif AZXX == "exit":
            exit()
            pass
        pass
    pass

