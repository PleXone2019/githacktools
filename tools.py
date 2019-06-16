#!/usr/bin/python3

from os import name, system, path
from requests import get
from languages import english, vietnamese

def action(language,inputs):
    from githacktools import clear, home_page, choose_lang,info_gathering, vulner_analysis, passwd_attack, web_apps, wireless_attack, exploit_tools, sniff_spoof, malware_bypass, ddos_tools, downloader_installer
    from banner import githacktools_banner

    if inputs.upper() == "HELP":
        print(language.help)
    elif inputs.upper() == "CHANGELOG":
        print(language.changelog)
    elif inputs.upper() == "ABOUT":
        print(language.about_githacktools)
    elif inputs.upper() == "HOMEP":
        clear()
        githacktools_banner(language)
        home_page(language)
    elif inputs.upper() == "LANG":
        clear()
        choose_lang(language)
    elif inputs.upper() == "EXIT":
        print(language.exiting)
        exit()
    elif inputs.upper() == "INFOGARTHER":
        clear()
        info_gathering(language)
    elif inputs.upper() == "VULNER":
        clear()
        vulner_analysis(language)
    elif inputs.upper() == "PASSWD":
        clear()
        passwd_attack(language)
    elif inputs.upper() == "WEBAPPS":
        clear()
        web_apps(language)
    elif inputs.upper() == "WIRELESS":
        clear()
        wireless_attack(language)
    elif inputs.upper() == "EXPLOITER":
        clear()
        exploit_tools(language)
    elif inputs.upper() == "SNIFFSPOOF":
        clear()
        sniff_spoof(language)
    elif inputs.upper() == 'MALWARER':
        clear()
        malware_bypass(language)
    elif inputs.upper() == 'DDOSER':
        clear()
        ddos_tools(language)
    elif inputs.upper() == 'INSTALLER':
        clear()
        downloader_installer(language)

def download(url):
    filename = url.split('/')[-1]
    with get(url, stream=True) as re:
        re.raise_for_status()
        with open(filename, 'wb') as file:
            for chunk in re.iter_content(chunk_size=8192): 
                if chunk:
                    file.write(chunk)

def the_path(language,tool):
    try:
        paths = str(input(language.path_folder.format(tool))).strip()
        action(language,paths)

        if (paths.upper() == 'HELP' or paths.upper() == 'CHANGELOG' or paths.upper() == 'ABOUT'):
            the_path(language,tool)

        elif path.exists(paths) == True:
            return paths

        else:
            print(language.doesnt_exists)
            the_path(language, tool)

    except KeyboardInterrupt:
        print(language.exiting)
        exit()
    except IndexError:
        print(language.invalid)
        the_path(language,tool)


def billcipher(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python3 = str(input(language.installed_or_not.format('Python 3.7'))).strip()
            action(language,python3)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)
            ruby = str(input(language.installed_or_not.format('Ruby-lang'))).strip()
            action(language,ruby)

            if (git[0].upper() == 'Y' and python3[0].upper() == 'Y' and python2[0].upper() == 'Y' and ruby[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif python3[0].upper() == 'N':
                    print(language.downloading.format('python-3.7.3.exe'))
                    download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                    print(language.note_python3)
                    system('.\\python-3.7.3.exe')

                elif ruby[0].upper() == 'N':
                    print(language.downloading.format('rubyinstaller-2.6.3-1-x86.exe'))
                    download('https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.3-1/rubyinstaller-2.6.3-1-x86.exe')
                    print(language.note_ruby)
                    system('.\\rubyinstaller-2.6.3-1-x86.exe')

                elif (git.upper() == 'HELP' or python3.upper() == 'HELP' or python2.upper() == 'HELP' or ruby.upper() == 'HELP'):
                    billcipher(language)

                elif (git.upper() == 'CHANGELOG' or python3.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG' or ruby.upper() == 'CHANGELOG'):
                    billcipher(language)

                elif (git.upper() == 'ABOUT' or python3.upper() == 'ABOUT' or python2.upper() == 'ABOUT' or ruby.upper() == 'ABOUT'):
                    billcipher(language)

                else:
                    print(language.invalid)
                    billcipher(language)
   
            print(language.installing.format("BillCipher"))
            system("""cd C:\\ && git clone https://github.com/GitHackTools/BillCipher
            cd BillCipher
            sudo pip install -r requirements.txt && sudo pip3 install -r requirements.txt""")
            print(language.done.format("BillCipher"))
            print(language.note_tools.format('BillCipher','python3 billcipher.py'))

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'BillCipher')
                print(language.installing.format("BillCipher"))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install httrack ruby")

                elif path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S httrack ruby")
                    
                system("""cd {} && sudo git clone https://github.com/GitHackTools/BillCipher
                cd BillCipher
                sudo pip2 install -r requirements.txt && sudo pip3 install -r requirements.txt
                sudo git clone https://github.com/urbanadventurer/WhatWeb
                cd WhatWeb && sudo make install""".format(paths))
                print(language.done.format('BillCipher'))
                print(language.note_tools.format('BillCipher','python3 billcipher.py'))

        print(language.readmore.format('BillCipher', 'http://bit.ly/2BNaVJI'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def leaked(language):
    print(language.leaked_read_only)
    print(language.readmore.format('Leaked', 'http://bit.ly/2Qy3v08'))


def devploit(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    devploit(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    devploit(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    devploit(language)

                else:
                    print(language.invalid)
                    devploit(language)

            print(language.installing.format('Devploit'))
            system("cd C:\\ && git clone https://github.com/zD4NI3LH/Devploit")
            print(language.done.format('Devploit'))
            print(language.note_tools.format('Devploit', 'python Devploit'))

        else:
            if path.exists('/usr/bin/pacman') == True:
                paths = the_path(language,'Devploit')
                system("cd {} && sudo git clone https://github.com/zD4NI3LH/Devploit".format(paths))
                print(language.done.format('Devploit'))
                print(language.note_tools.format('Devploit', 'python2 Devploit'))

            else:
                if path.exists('/usr/bin/Devploit') == True:
                    print(language.installed.format('Devploit'))    

                else:
                    paths = the_path(language,'Devploit')
                    print(language.installing.format('Devploit'))
                    system("""cd {} && sudo git clone https://github.com/zD4NI3LH/Devploit
                    cd Devploit && sudo bash install""".format(paths))
                    print(language.done.format('Devploit'))
                    
                print(language.note_tools2.format('Devploit','Devploit','Terminal'))

        print(language.readmore.format('Devploit', 'http://bit.ly/2KU7BMF'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def gorecon(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
               paths = the_path(language,'Gorecon')
               print(language.installing.format('Gorecon'))

               if path.exists('/usr/bin/apt') == True:
                   system("sudo apt install golang-go")

               elif path.exists('/usr/bin/pacman') == True:
                   system("sudo pacman -S go")

               system("""cd {} && sudo go get "github.com/devanshbatham/gorecon"
               cd gorecon && sudo go get "github.com/gocolly/colly"
               sudo go get "github.com/fatih/color" && sudo go get "github.com/likexian/whois-go" """.format(paths))
               print(language.done.format('Gorecon'))
               print(language.note_tools.format('Gorecon','go run gorecon.go'))

        print(language.readmore.format('Gorecon','http://bit.ly/2KykK2p'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def dracnmap(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'Dracnmap')
                print(language.installing.format('Dracnmap'))
                
                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install nmap")

                elif path.exists('usr/bin/pacman') == True:
                    system("sudo pacman -S nmap")

                system("cd {} && sudo git clone https://github.com/Screetsec/Dracnmap".format(paths))
                print(language.done.format('Dracnmap'))
                print(language.note_tools.format('Dracnmap', 'bash dracnmap-v2.2.sh'))

        print(language.readmore.format('Dracnmap','http://bit.ly/2sTQtlS'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def nmap(language):
    try:
        if name == 'nt':
            print(language.installing.format('Nmap'))
            print(language.downloading.format('nmap-7.70-setup.exe'))
            download('https://nmap.org/dist/nmap-7.70-setup.exe')
            system('.\\nmap-7.70-setup.exe')
            print(language.done.format('Nmap'))
            print(language.note_tools2.format('Nmap','nmap','CMD'))

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                if path.exists('/usr/bin/nmap') == True:
                    print(language.installed.format('Nmap'))

                else:
                    print(language.installing.format('Nmap'))

                    if path.exists('/usr/bin/apt') == True:
                        system("sudo apt install nmap")
                        
                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S nmap")

                    print(language.done.format('Nmap'))
                    
                print(language.note_tools2.format('Nmap','nmap','Terminal'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def sublist3r(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python3 = str(input(language.installed_or_not.format('Python 3.7'))).strip()
            action(language,python3)

            if (git[0].upper() == 'Y' and python3[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')
                    
                elif python3[0].upper() == 'N':
                    print(language.downloading.format('python-3.7.3.exe'))
                    download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                    print(language.note_python3)
                    system('.\\python-3.7.3.exe')

                elif (git.upper() == 'HELP' or python3.upper() == 'HELP'):
                    sublist3r(language)

                elif (git.upper() == 'CHANGELOG' or python3.upper() == 'CHANGELOG'):
                    sublist3r(language)

                elif (git.upper() == 'ABOUT' or python3.upper() == 'ABOUT'):
                    sublist3r(language)

                else:
                    print(language.invalid)
                    sublist3r(language)

            print(language.installing.format("Sublist3r"))
            system("""cd C:\\ && git clone https://github.com/aboul3la/Sublist3r
            cd Sublist3r && pip install -r requirements.txt""")

        else:
            paths = the_path(language, 'Sublist3r')
            print(language.installing.format('Sublist3r'))
            system("""cd {} && sudo git clone https://github.com/aboul3la/Sublist3r
            cd Sublist3r && sudo pip install -r requirements.txt""".format(paths))

        print(language.done.format('Sublist3r'))
        print(language.note_tools.format('Sublist3r','python sublist3r.py'))
        print(language.readmore.format('Sublist3r','http://bit.ly/2LCZ18X'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def sslscan(language):
    try:
        if name == 'nt':
            print(language.installing.format('SSLScan'))
            print(language.downloading.format('sslscan-win-1.11.11-rbsec.zip'))
            download('https://github.com/rbsec/sslscan/releases/download/1.11.11-rbsec/sslscan-win-1.11.11-rbsec.zip')
            print(language.note_sslscan)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)
            
            else:
                if path.exists('/usr/bin/sslscan') == True:
                    print(language.installed.format('SSLScan'))

                else:
                    print(language.installing.format('SSLScan'))

                    if path.exists('/usr/bin/apt') == True:
                        system('sudo apt install sslscan')

                    elif path.exists('/usr/bin/pacman') == True:
                        system('sudo pacman -S sslscan')

                    print(language.done.format('SSLScan'))

                print(language.note_tools2.format('SSLScan','sslscan','Terminal'))

        print(language.readmore.format('SSLScan', 'http://bit.ly/2MAQBNo'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def dnsmaper(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language, 'DNSMaper')
            print(language.installing.format('DNSMaper'))
            system("""cd {} && sudo git clone https://github.com/le4f/dnsmaper
            cd dnsmaper && sudo pip2 install requests geoip2 signal""".format(paths))
            print(language.done.format('DNSMaper'))
            print(language.note_tools.format('DNSMaper','python2 dnsmaper.py'))

        print(language.readmore.format('DNSMaper', 'http://bit.ly/2MoEx57'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def a2sv(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if path.exists('/usr/bin/pacman') == True:
                paths = the_path(language,'A2SV')
                print(language.installing.format('A2SV'))
                system("""cd {} && sudo git clone https://github.com/hahwul/a2sv
                cd a2sv && sudo pip2 install argparse netaddr""".format(paths))
                print(language.done.format('A2SV'))
                print(language.note_tools.format('A2SV','python2 a2sv.py'))
                
            else:
                if path.exists('/usr/bin/a2sv') == False:
                    print(language.installed.format('A2SV'))

                else:
                    paths = the_path(language, 'A2SV')
                    print(language.installing.format('A2SV'))
                    system("""cd {} && sudo git clone https://github.com/hahwul/a2sv
                    cd a2sv && sudo bash install.sh""".format(paths))
                    print(language.done.format('A2SV'))
                    
                print(language.note_tools2.format('A2SV','a2sv','Terminal'))

        print(language.readmore.format('A2SV','http://bit.ly/2KCDPz7'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def shodanhat(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    shodanhat(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    shodanhat(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    shodanhat(language)

                else:
                    print(language.invalid)
                    shodanhat(language)

            system("""cd C:\\ && git clone https://github.com/HatBashBR/ShodanHat
            cd ShodanHat && pip uninstall nmap && pip install shodan python-nmap""")

        else:
            paths = the_path(language,'ShodanHat')
            print(language.installing.format('ShodanHat'))
            system("""cd {} && sudo git clone https://github.com/HatBashBR/ShodanHat"
            sudo pip2 uninstall nmap && sudo pip2 install shodan python-nmap""".format(paths))
  
        print(language.done.format('ShodanHat'))
        print(language.note_tools.format('ShodanHat','python2 shodanhat.py'))
        print(language.readmore.format('ShodanHat','http://bit.ly/2KQnpDn'))
        
    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def hatcloud(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            ruby = str(input(language.installed_or_not.format('Ruby-lang'))).strip()
            action(language,ruby)

            if (git[0].upper() == 'Y' and ruby[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif ruby[0].upper() == 'N':
                    print(language.downloading.format('rubyinstaller-2.6.3-1-x86.exe'))
                    download('https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.3-1/rubyinstaller-2.6.3-1-x86.exe')
                    print(language.note_ruby)
                    system('.\\rubyinstaller-2.6.3-1-x86.exe')

                elif (git.upper() == 'HELP' or ruby.upper() == 'HELP'):
                    hatcloud(language)

                elif (git.upper() == 'CHANGELOG' or ruby.upper() == 'CHANGELOG'):
                    hatcloud(language)

                elif (git.upper() == 'ABOUT' or ruby.upper() == 'ABOUT'):
                    hatcloud(language)

                else:
                    print(language.invalid)
                    hatcloud(language)

            print(language.installing.format('HatCloud'))
            system("cd C:\\ && git clone https://github.com/HatBashBR/HatCloud")

        else:
            paths = the_path(language,'HatCloud')
            print(language.installing.format('HatCloud'))
            system("cd {} && sudo git clone https://github.com/HatBashBR/HatCloud".format(paths))

        print(language.done.format('HatCloud'))
        print(language.note_tools.format('HatCloud','ruby hatcloud.rb'))
        print(language.readmore.format('HatCloud','http://bit.ly/2KAJC9m'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def sub6(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git[0].upper() == 'HELP' or python2[0].upper() == 'HELP'):
                    sub6(language)

                elif (git[0].upper() == 'CHANGRLOG' or python2[0].upper() == 'CHANGRLOG'):
                    sub6(language)

                elif (git[0].upper() == 'ABOUT' or python2[0].upper() == 'ABOUT'):
                    sub6(language)

                else:
                    print(language.invalid)
                    sub6(language)

            print(language.installing.format('sub6'))
            system("cd C:\\ && git clone https://github.com/YasserGersy/sub6")

        else:
            paths = the_path(language, 'sub6')
            print(language.installing.format('sub6'))
            system("cd {} && sudo git clone https://github.com/YasserGersy/sub6".format(paths))

        print(language.done.format('sub6'))
        print(language.note_tools.format('sub6','python2 sub6.py'))
        print(language.readmore.format('sub6','http://bit.ly/2Gh75td'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def masscan(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if path.exists('/usr/bin/masscan') == True:
                print(language.installed.format('Masscan'))

            else:
                paths = the_path(language,'Masscan')
                print(language.installing.format('Masscan'))
                system("""cd {} && sudo git clone https://github.com/robertdavidgraham/masscan
                cd masscan && sudo make install""".format(paths))
                print(language.done.format('Masscan'))

            print(language.note_tools2.format('Masscan','masscan','Terminal'))

        print(language.readmore.format('Masscan','http://bit.ly/2HqigzG'))
                    
    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def dnsmap(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/local/bin/dnsmap') == True or path.exists('/usr/bin/dnsmap') == True):
                print(language.installed.format('dnsmap'))

            else:
                paths = the_path(language,'dnsmap')
                print(language.installing.format('dnsmap'))
                system("""cd {} && sudo git clone https://gitlab.com/kalilinux/packages/dnsmap.git
                cd dnsmap && sudo make install""".format(paths))
                print(language.done.format('dnsmap'))

            print(language.note_tools2.format('dnsmap','dnsmap','Terminal'))

        print(language.readmore.format('dnsmap','http://bit.ly/2HoZiZX'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def infosploit(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    infosploit(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    infosploit(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    infosploit(language)

                else:
                    print(language.invalid)
                    infosploit(language)

            print(language.installing.format('InfoSploit'))
            system("cd C:\\ && git clone https://github.com/CybernetiX-S3C/InfoSploit")
            print(language.done.format('InfoSploit'))
            print(language.note_tools.format('InfoSploit','python Infosploit.py'))
 
        else:
            if path.exists('/usr/bin/Infosploit') == True:
                print(language.installed.format('InfoSploit'))

            else:
                paths = the_path(language,'InfoSploit')
                print(language.installing.format('InfoSploit'))
                system("""cd {} && sudo git clone https://github.com/CybernetiX-S3C/InfoSploit
                cd InfoSploit && sudo bash install""".format(paths))
                print(language.done.format('InfoSploit'))
                
            print(language.note_tools2.format('InfoSploit','Infosploit','Terminal'))

        print(language.readmore.format('InfoSploit','http://bit.ly/2LUfN4w'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def infoga(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'Infoga')
            print(language.installing.format('Infoga'))
            system("""cd {} && sudo git clone https://github.com/m4ll0k/Infoga
            cd Infoga && sudo python2 setup.py install""".format(paths))
            print(language.done.format('Infoga'))
            print(language.note_tools.format('Infoga','python2 infoga.py'))

        print(language.readmore.format('Infoga','http://bit.ly/2F6ioDW'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def httrack(language):
    try:
        if name == 'nt':
            print(language.installing.format('HTTrack'))
            print(language.downloading.format('httrack-3.49.2.exe'))
            download('https://download.httrack.com/httrack-3.49.2.exe')
            system('.\\httrack-3.49.2.exe')
            print(language.done.format('HTTrack'))

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                if path.exists('/usr/bin/httrack') == True:
                    print(language.installed.format('HTTrack'))
                    
                else:
                    print(language.installing.format('HTTrack'))

                    if path.exists('/usr/bin/apt') == True:
                        system('sudo apt install httrack')

                    elif path.exists('/usr/bin/pacman') == True:
                        system('sudo pacman -S httrack')

                    print(language.done.format('HTTrack'))
                    
                print(language.note_tools2.format('HTTrack','httrack','Terminal'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def apt2(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'APT2')
            print(language.installing.format('APT2'))
            system(""""cd {} && sudo git clone https://github.com/MooseDojo/apt2
            sudo pip2 install unqlite scapy""".format(paths))
            print(language.done.format('APT2'))
            print(language.note_tools.format('APT2','python2 apt2.py'))

        print(language.readmore.format('APT2', 'http://bit.ly/2WVHP0z'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def inspy(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'InSpy')
            print(language.installing.format('InSpy'))
            system("""cd {} && sudo git clone https://github.com/leapsecurity/InSpy
            cd InSpy && sudo pip2 install -r requirements.txt""".format(paths))
            print(language.done.format('InSpy'))
            print(language.note_tools.format('InSpy','python2 InSpy.py'))

        print(language.readmore.format('InSpy','http://bit.ly/2n8P9J1'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def setoolkit(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'SEToolkit')
                print(language.installing.format('SEToolkit'))
                metasploit(language)
                system("""cd {} && sudo git clone https://github.com/trustedsec/social-engineer-toolkit set
                cd set && sudo pip2 install -r requirements.txt""".format(paths))
                print(language.done.format('SEToolkit'))
                print(language.note_tools.format('SEToolkit','sudo python2 setoolkit'))

        print(language.readmore.format('SEToolkit','http://bit.ly/2EkvcHi'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def phishx(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'PhishX')
                print(language.installing.format('PhishX'))

                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S python-setuptools sendemail php xterm")

                system("""cd {} && sudo git clone https://github.com/rezaaksa/PhishX
                cd PhishX && sudo bash installer.sh""".format(paths))
                print(language.done.format('PhishX'))
                print(language.note_tools.format('PhishX','python3 PhishX.py'))

        print(language.readmore.format('PhishX','http://bit.ly/2N7IM01'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def phisherman(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'PhisherMan')
            print(language.installing.format('PhisherMan'))
            system("cd {} && sudo git clone https://github.com/FDX100/Phisher-man".format(paths))
            print(language.done.format('PhisherMan'))
            print(language.note_tools.format('PhisherMan','sudo python2 phisherman.py'))

        print(language.readmore.format('PhisherMan','http://bit.ly/2QLy5DL'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def aron(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                if path.exists('/usr/bin/aron') == True:
                    print(language.installed.format('Aron'))

                else:
                    paths = the_path(language, 'Aron')
                    print(language.installing.format('Aron'))

                    if path.exists('/usr/bin/apt') == True:
                        system("sudo apt install golang-go")

                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S go")

                    system("""cd {} && sudo git clone https://github.com/m4ll0k/Aron
                    cd Aron && sudo go get github.com/m4ll0k/printer"
                    sudo go env | grep -i gopath && sudo export GOPATH=$HOME/go
                    sudo go build aron.go && sudo cp aron /usr/bin/""".format(paths))
                    print(language.done.format('Aron'))

                print(language.note_tools2.format('Aron','aron','Terminal'))

        print(language.readmore.format('Aron','http://bit.ly/2MkbKyj'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def evilginx2(language):
    try:
        if name == 'nt':
            print(language.installing.format('Evilginx'))
            print(language.downloading.format('evilginx_windows_x86_2.3.0.zip'))
            download('https://github.com/kgretzky/evilginx2/releases/download/2.3.0/evilginx_windows_x86_2.3.0.zip')
            print(language.note_evilginx2)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                if path.exists('/usr/bin/apt') == True:
                    paths = the_path(language, 'Evilginx 2')
                    print(language.installing.format('Evilginx 2'))
                    system("""cd {} && wget https://github.com/kgretzky/evilginx2/releases/download/2.3.0/evilginx_linux_x86_2.3.0.zip
                    sudo apt install unzip && unzip evilginx_linux_x86_2.3.0.zip -d evilginx2
                    cd evilginx2 && sudo bash install.sh""".format(paths))

                elif path.exists('/usr/bin/pacman') == True:
                    print(language.installing.format('Evilginx 2'))
                    system("sudo pacman -S go && sudo pacman -S evilginx")

                print(language.done.format('Evilginx 2'))
                print(language.note_tools2.format('Evilginx 2','evilginx','Terminal'))

        print(language.readmore.format('Evilginx 2','http://bit.ly/2O8cWFS'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def infinity(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    infinity(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    infinity(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    infinity(language)

                else:
                    print(language.invalid)
                    infinity(language)

            print(language.installing.format('infinity'))
            system("""cd C:\\ && pip install mechanize
            git clone https://github.com/s0md3v/infinity""")

        else:
            paths = the_path(language,'infinity')
            print(language.installing.format('infinity'))
            system("""cd {} && sudo pip2 install mechanize
            sudo git clone https://github.com/s0md3v/infinity""".format(paths))

        print(language.done.format('infinity'))
        print(language.note_tools.format('infinity','python2 infinity.py'))
        print(language.readmore.format('infinity','http://bit.ly/2EZriD5'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def credsniper(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'CredSniper')

                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S virtualenv gnupg certbot")

                system("""cd {} && sudo git clone https://github.com/ustayready/CredSniper
                cd CredSniper && sudo bash install.sh""".format(paths))
                print(language.done.format('CredSniper'))
                print(language.note_tools.format('CredSniper','python3 credsniper.py'))

        print(language.readmore.format('CredSniper','http://bit.ly/2yXXrc1'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def ghost_phisher(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'Ghost Phisher')
                print(language.installing.format('Ghost Phisher'))
                metasploit(language)
                system("cd {} && sudo git clone https://github.com/savio-code/ghost-phisher".format(paths))
                print(language.done.format('Ghost Phisher'))
                print(language.note_tools2.format('Ghost Phisher','sudo python2 ghost.py','ghost-phisher/Ghost-Phisher'))

        print(language.readmore.format('Ghost Phisher','http://bit.ly/2HeR83c'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def subdomain_analyzer(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    subdomain_analyzer(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    subdomain_analyzer(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    subdomain_analyzer(language)

                else:
                    print(language.invalid)
                    subdomain_analyzer(language)

            print(language.installing.format('SubDomain-Analyzer'))
            system("""cd C:\\ && git clone https://github.com/El3ct71k/SubDomain-Analyzer
            cd SubDomain-Analyzer && pip install -r requirements.txt""")  

        else:
            paths = the_path(language,'SubDomain-Analyzer')
            print(language.installing.format('SubDomain-Analyzer'))
            system("""cd {} && git clone https://github.com/El3ct71k/SubDomain-Analyzer
            cd SubDomain-Analyzer && sudo pip2 install -r requirements.txt""".format(paths))
            
        print(language.done.format('SubDomain-Analyzer'))
        print(language.note_tools.format('SubDomain-Analyzer','python subdomain-analyzer.py'))
        print(language.readmore.format('SubDomain-Analyzer','http://bit.ly/2NKLU2J'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def sqlmap(language):
    try:
        if name == 'nt':
            python3 = str(input(language.installed_or_not.format('Python 3.7'))).strip()
            action(language,python3)

            if python3[0].upper() == 'Y':
                pass

            elif python3[0].upper() == 'N':
                print(language.downloading.format('python-3.7.3.exe'))
                download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                print(language.note_python3)
                system('.\\python-3.7.3.exe')

            elif (python3.upper() == 'HELP' or python3.upper() == 'CHANGELOG' or python3.upper() == 'ABOUT'):
                sqlmap(language)

            else:
                print(language.invalid)
                sqlmap(language)

            print(language.installing.format('SQLMap'))
            system("pip install sqlmap")

        else:
            print(language.installing.format('SQLMap'))
            system("sudo pip3 install sqlmap")
            
        print(language.done.format('SQLMap'))
        print(language.note_tools2.format('SQLMap','sqlmap','Terminal & CMD'))
        print(language.readmore.format('SQLMap','http://bit.ly/2zArNjX'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def sqlmate(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    sqlmate(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    sqlmate(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    sqlmate(language)

                else:
                    print(language.invalid)
                    sqlmate(language)

            print(language.installing.format('SQLMate'))
            system("""cd C:\\ && git clone https://github.com/s0md3v/sqlmate
            cd sqlmate && pip install -r requirements.txt""")

        else:
            paths = the_path(language,'SQLMate')
            print(language.installing.format('SQLMate'))
            system("""cd {} && sudo git clone https://github.com/s0md3v/sqlmate
            cd sqlmate && sudo pip2 install -r requirements.txt""".format(paths))
            
        print(language.done.format('SQLMate'))
        print(language.note_tools.format('SQLMate', 'python2 sqlmate'))
        print(language.readmore.format('SQLMate','http://bit.ly/2C0DwXW'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def searchsploit(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                if path.exists('/usr/bin/searchsploit') == True:
                    print(language.installed.format('SearchSploit'))

                else:
                    print(language.installing.format('SearchSploit'))

                    if path.exists('/usr/bin/apt') == True:
                        system("sudo apt install go-exploitdb")

                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudp pacman -S exploitdb")

                    print(language.done.format('SearchSploit'))

                print(language.note_tools2.format('SearchSploit','searchsploit','Terminal'))

        print(language.readmore.format('SearchSploit','http://bit.ly/2svkh4C'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def brakemen(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'Brakeman')
                print(language.installing.format('Brakeman'))

                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S ruby")

                elif path.exists('/usr/bin/apt') == True:
                    system("sudo apt install ruby")

                system("""cd {} && sudo git clone https://github.com/presidentbeef/brakeman
                cd brakeman && sudo gem build brakeman.gemspec && sudo gem install brakeman*.gem""".format(paths))
                print(language.done.format('Brakeman'))

            print(language.note_tools.format('Brakeman','ruby /bin/brakeman'))

        print(language.readmore.format('Brakeman','http://bit.ly/2L8GhKi'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def whatweb(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if path.exists('/usr/bin/whatweb') == True:
                print(language.installed.format('WhatWeb'))

            else:
                paths = the_path(language,'WhatWeb')
                print(language.installing.format('WhatWeb'))
                system("""cd {} && sudo git clone https://github.com/urbanadventurer/WhatWeb
                cd WhatWeb && sudo make install""".format(paths))
                print(language.done.format('WhatWeb'))

            print(language.note_tools2.format('WhatWeb','whatweb','Terminal'))

        print(language.readmore.format('WhatWeb','http://bit.ly/2H8IvZK'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def vulscan(language):
    try:
        if name == 'nt':
            print(language.installing.format('vulscan'))
            print(language.downloading.format('nmap-7.70-setup.exe'))
            download('https://nmap.org/dist/nmap-7.70-setup.exe')
            system('.\\nmap-7.70-setup.exe')
            
        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                print(language.installing.format('vulscan'))

                if path.exists('/usr/bin/apt') == True:
                    system('sudo apt install nmap')

                elif path.exists('/usr/bin/pacman'):
                    system('sudo pacman install nmap')

        print(language.downloading.format('vulscan-master.zip'))
        download('https://github.com/scipag/vulscan/archive/master.zip')
        print(language.readmore.format('vulscan','http://bit.ly/2DQfjbc'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def takeover(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    takeover(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    takeover(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    takeover(language)

                else:
                    print(language.invalid)
                    takeover(language)

            print(language.installing.format('TakeOver'))
            system("cd C:\\ && git clone https://github.com/m4ll0k/takeover")

        else:
            paths = the_path(language,'TakeOver')
            print(language.installing.format('TakeOver'))
            system("cd {} && sudo git clone https://github.com/m4ll0k/takeover".format(paths))

        print(language.done.format('TakeOver'))
        print(language.note_tools.format('TakeOver','python2 takeover.py'))
        print(language.readmore.format('TakeOver','http://bit.ly/2uPGGvN'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def openvas(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)
            else:
                print(language.installing.format('OpenVAS'))

                if path.exists('/usr/bin/pacman') == True:
                    system('sudo pacman -S openvas')

                elif path.exists('/usr/bin/apt') == True:
                    system('sudo apt install openvas')

                print(language.done.format('OpenVAS'))
                print(language.note_tools2.format('OpenVAS','openvas-start','Terminal'))

        print(language.readmore.format('OpenVAS','http://bit.ly/2FtrxnV'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def droid_hunter(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                    print(language.unknow_distro)

            else:
                if path.exists('/usr/bin/dhunter') == True:
                    print(language.installed.format('Droid-Hunter'))

                else:
                    paths = the_path(language,'Droid-Hunter')
                    print(language.installing.format('Droid-Hunter'))

                    if path.exists('/usr/bin/apt') == True:
                        system("sudo apt install ruby")

                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S ruby")

                    system("""cd {} && sudo git clone https://github.com/hahwul/droid-hunter
                    cd droid-hunter && sudo bash install.sh""".format(paths))
                    print(language.done.format('Droid-Hunter'))

                print(language.note_tools2.format('Droid-Hunter','dhunter','Terminal'))

        print(language.readmore.format('Droid-Hunter','http://bit.ly/2tY1Nuj'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def patrowl(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'PatrOwl')
                print(language.installing.format('PatrOwl'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install curl rabbitmq-server postgresql build-essential")

                elif path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S curl rabbitmq postgresql base-devel")

                system("""cd {} && sudo git clone https://github.com/Patrowl/PatrowlManager && cd PatrOwlManager
                sudo pip2 install virtualenv && sudo pip2 install -r requirements.txt""".format(paths))
                print(language.done.format('PatrOwl'))
                print(language.note_tools.format('PatrOwl','start-server.sh'))

        print(language.readmore.format('PatrOwl','http://bit.ly/2InjYAy'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def infection_monkey(language):
    try:
        if name == 'nt':
            print(language.installing.format('Infection Monkey'))
            print(language.downloading.format('monkey-windows-32.exe'))
            download("https://github.com/guardicore/monkey/releases/download/v1.6.3/monkey-windows-32.exe")
            system(".\\monkey-windows-32.exe")

        else:
            if path.exists('/usr/bin/apt') == True:
                print(language.installing.format('Infection Monkey'))
                system("""sudo wget https://github.com/guardicore/monkey/releases/download/v1.6.2/infection_monkey_deb.1.6.2.tgz
                sudo tar xvzf infection_monkey_deb.1.6.2.tgz && sudo dpkg -i monkey_island.deb""")
                print(language.done.format('Infection Monkey'))

            else:
                print(language.run_well.format('Debian & Windows'))

        print(language.readmore.format('Infection Monkey','http://bit.ly/2sldHOf'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def vuls(language):
    try:
        from platform import architecture

        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if architecture()[0] == "64bit":
                paths = the_path(language,'Vuls')
                print(language.installing.format('Vuls'))
                system("""cd {} && sudo mkdir vuls && cd vuls
                sudo wget https://github.com/future-architect/vuls/releases/download/v0.7.0/vuls_0.7.0_linux_amd64.tar.gz
                sudo tar xvzf vuls_0.7.0_linux_amd64.tar.gz && sudo chmod +x vuls""".format(paths))
                print(language.done.format('Vuls'))
                print(language.note_tools.format('Vuls','sudo ./vuls'))

            else:
                print(language.only_compatible.format("64-bit OS"))

        print(language.readmore.format('Vuls','http://bit.ly/2kxngpY'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def wpseku(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'WPSeku')
            print(language.installing.format('WPSeku'))
            system("""cd {} && sudo git clone https://github.com/m4ll0k/WPSeku
            cd WPSeku && sudo pip3 install -r requirements.txt""".format(paths))
            print(language.done.format('WPSeku'))
            print(language.note_tools.format('WPSeku','python3 wpseku.py'))

        print(language.readmore.format('WPSeku','http://bit.ly/2D8be1N'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def wpscan(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                if path.exists('/usr/bin/wpscan') == True:
                    print(language.installed.format('WPScan'))

                else:
                    if path.exists('/usr/bin/apt') == True:
                        paths = the_path(language,'WPScan')
                        print(language.installing.format('WPScan'))
                        system("""sudo apt install libcurl4-openssl-dev libxml2 libxml2-dev libxslt1-dev ruby ruby-bundler ruby-dev build-essential libgmp-dev zlib1g-dev
                        cd {} && sudo git clone https://github.com/wpscanteam/wpscan
                        cd wpscan && sudo bundle install && sudo rake install""".format(paths))

                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S wpscan")

                    print(language.done.format('WPScan'))
                    
                print(language.note_tools2.format('WPScan','wpscan','Terminal'))

        print(language.readmore.format('WPScan','https://github.com/wpscanteam/wpscan'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def routersploit(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'RouterSploit')
            print(language.installing.format('RouterSploit'))
            system("""cd {} && sudo git clone https://github.com/threat9/routersploit
            cd routersploit && sudo python3 pip install -r requirements.txt""".format(paths))
            print(language.done.format('RouterSploit'))
            print(language.note_tools.format('RouterSploit','python3 rsf.py'))

        print(language.readmore.format('RouterSploit','http://bit.ly/2s94mcV'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def xsstrike(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'XSStrike')
            print(language.installing.format('XSStrike'))
            system("""cd {} && sudo git clone https://github.com/s0md3v/XSStrike
            cd XSStrike && sudo pip3 install -r requirements.txt""".format(paths))
            print(language.done.format('XSStrike'))
            print(language.note_tools.format('XSStrike','python3 xsstrike.py'))

        print(language.readmore.formt('XSStrike','http://bit.ly/2iGBEv9'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def striker(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'Striker')
            print(language.installing.format('Striker'))
            system("""cd {} && sudo git clone https://github.com/s0md3v/Striker
            cd Striker && sudo pip3 install -r requirements.txt""".format(paths))
            print(language.done.format('Striker'))
            print(language.note_tools.format('Striker','python3 striker.py'))

        print(language.readmore.formt('Striker','http://bit.ly/2EFQG1z'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def raptor(language):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(language,'Raptor')
            print(language.installing.format('Raptor'))
            system("""cd {} && sudo git clone https://github.com/dpnishant/raptor
            cd raptor && sudo bash install.sh""".format(paths))
            print(language.done.format('Raptor'))
            print(language.note_tools.format('Raptor','sudo bash start.sh'))

        else:
            if name == 'nt':
                print(language.doesnt_support_windows)
                print(language.wsl)
            
            else:
                print(language.run_well.format('Debian'))

        print(language.readmore.format('Raptor','http://bit.ly/2sAtbBq'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def breacher(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')
                    
                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    breacher(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    breacher(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    breacher(language)

                else:
                    print(language.invalid)
                    breacher(language)

            print(language.installing.format("Breacher"))
            system("cd C:\\ && git clone https://github.com/s0md3v/Breacher")

        else:
            paths = the_path(language,'Breacher')
            print(language.installing.format('Breacher'))
            system("cd {} && sudo https://github.com/s0md3v/Breacher".format(paths))

        print(language.done.format("Breacher"))
        print(language.note_tools.format("Breacher","python2 breacher.py"))
        print(language.readmore.format("Breacher","http://bit.ly/2ohlBa5"))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def wascan(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'WAScan')
            print(language.installing.format('WAScan'))
            system("cd {} && sudo git clone https://github.com/m4ll0k/WAScan".format(paths))
            print(language.done.format('WAScan'))
            print(language.note_tools.format('WAScan','python2 wascan.py'))

        print(language.readmore.format('WAScan','http://bit.ly/2HL9OZG'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def xsser(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if path.exists('/usr/bin/xsser') == True:
                print(language.installed.format('XSSer'))

            else:
                paths = the_path(language,'XSSer')
                print(language.installing.format('XSSer'))
                system("""cd {} && sudo git clone https://github.com/epsylon/xsser && cd xsser/xsser
                sudo pip2 install pycurl xmlbuilder geoip BeautifulSoup && sudo python2 setup.py install""".format(paths))
                print(language.done.format('XSSer'))
                
            print(language.note_tools2.format('XSSer','xsser','Terminal'))

        print(language.readmore.format('XSSer','http://bit.ly/2DwhImM'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def spectre_meldown_checker(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'spectre-meltdown-checker')
            print(language.installing.format('spectre-meltdown-checker'))
            system("cd {} && sudo git clone https://github.com/speed47/spectre-meltdown-checker".format(paths))
            print(language.done.format('spectre-meltdown-checker'))
            print(language.note_tools.format('spectre-meltdown-checker','sudo bash spectre-meltdown-checker.sh'))

        print(language.readmore.format('spectre-meltdown-checker','http://bit.ly/30JWP47'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def brutedum(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'BruteDum')
                print(language.installing.format('BruteDum'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install nmap hydra medusa ncrack")

                elif path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S nmap hydra medusa ncrack")

                system("""cd {} && sudo git clone https://github.com/GitHackTools/BruteDum""".format(paths))
                print(language.done.format('BruteDum'))
                print(language.note_tools.format('BruteDum','python3 brutedum.py'))

        print(language.readmore.format('BruteDum','http://bit.ly/2ISotWY'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def ftpbruter(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python3 = str(input(language.installed_or_not.format('Python 3.7'))).strip()
            action(language,python3)

            if (git[0].upper() == 'Y' and python3[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')
                    
                elif python3[0].upper() == 'N':
                    print(language.downloading.format('python-3.7.3.exe'))
                    download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                    print(language.note_python3)
                    system('.\\python-3.7.3.exe')

                elif (git.upper() == 'HELP' or python3.upper() == 'HELP'):
                    ftpbruter(language)

                elif (git.upper() == 'CHANGELOG' or python3.upper() == 'CHANGELOG'):
                    ftpbruter(language)

                elif (git.upper() == 'ABOUT' or python3.upper() == 'ABOUT'):
                    ftpbruter(language)

                else:
                    print(language.invalid)
                    ftpbruter(language)

            print(language.installing.format('FTPBruter'))
            system("cd C:\\ && git clone https://github.com/GitHackTools/FTPBruter")

        else:
            paths = the_path(language,"FTPBruter")
            print(language.installing.format("FTPBruter"))
            system("cd {} && sudo git clone https://github.com/GitHackTools/FTPBruter".format(paths))

        print(language.done.format("FTPBruter"))
        print(language.note_tools.format("FTPBruter","python3 ftpbruter.py"))
        print(language.readmore.format("FTPBruter","http://bit.ly/2IzrGtk"))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def hash_buster(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python3 = str(input(language.installed_or_not.format('Python 3.7'))).strip()
            action(language,python3)

            if (git[0].upper() == 'Y' and python3[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')
                    
                elif python3[0].upper() == 'N':
                    print(language.downloading.format('python-3.7.3.exe'))
                    download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                    print(language.note_python3)
                    system('.\\python-3.7.3.exe')

                elif (git.upper() == 'HELP' or python3.upper() == 'HELP'):
                    hash_buster(language)

                elif (git.upper() == 'CHANGELOG' or python3.upper() == 'CHANGELOG'):
                    hash_buster(language)

                elif (git.upper() == 'ABOUT' or python3.upper() == 'ABOUT'):
                    hash_buster(language)

                else:
                    print(language.invalid)
                    hash_buster(language)

            print(language.installing.format('Hash-Buster'))
            system("cd C:\\ && git clone https://github.com/s0md3v/Hash-Buster")
            print(language.done.format("Hash-Buster"))
            print(language.note_tools.format('Hash-Huster','python hash.py'))

        else:
            if path.exists('/usr/local/bin/buster') == True:
                print(language.installed.format('Hash-Buster'))

            else:
                paths = the_path(language,'Hash-Buster')
                print(language.installing.format('Hash-Buster'))
                system("""cd {} && sudo git clone https://github.com/s0md3v/Hash-Buster
                cd Hash-Buster && sudo make install""".format(paths))
                print(language.done.format("Hash-Buster"))
                
            print(language.note_tools2.format("Hash-Buster",'buster','Terminal'))

        print(language.readmore.format('Hash-Buster','http://bit.ly/2GxqhPL'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def socialbox(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'SocialBox')
            print(language.installing.format('SocialBox'))

            if path.exists('/usr/bin/pacman') == True:
                system("sudo pacman -sS tor")

            system("""cd {} && sudo git clone https://github.com/TunisianEagles/SocialBox
            cd SocialBox && sudo bash install.sh""".format(paths))
            print(language.done.format('SocialBox'))
            print(language.note_tools.format('SocialBox','bash SocialBox.sh'))

        print(language.readmore.format('SocialBox','http://bit.ly/2NJ6GnQ'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def blazy(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    blazy(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    blazy(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    blazy(language)

                else:
                    print(language.invalid)
                    blazy(language)

            print(language.installing.format('Blazy'))
            system("""cd C:\\ && git clone https://github.com/s0md3v/Blazy
            cd Blazy && pip install -r requirements.txt""")

        else:
            paths = the_path(language,'Blazy')
            print(language.installing.format('Blazy'))
            system("""cd {} && sudo git clone https://github.com/s0md3v/Blazy
            cd Blazy && sudo pip2 install -r requirements.txt""".format(paths))

        print(language.done.format('Blazy'))
        print(language.note_tools.format('Blazy', 'python2 blazy.py'))
        print(language.readmore.format('Blazy','http://bit.ly/2owpqYx'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def ncrack(language):
    try:
        if name == 'nt':
            print(language.installing.format('Ncrack'))
            print(language.downloading.format('ncrack-0.6-setup.exe'))
            download('https://nmap.org/ncrack/dist/ncrack-0.6-setup.exe')
            system(".\\ncrack-0.6-setup.exe")
            print(language.done.format('Ncrack'))
            print(language.note_tools2.format('Ncrack','ncrack','CMD'))

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                if path.exists('/usr/bin/ncrack') == True:
                    print(language.installed.format('Ncrack'))

                else:
                    print(language.installing.format('Ncrack'))
                    if path.exists('/usr/bin/apt') == True:
                        system("sudo apt instal ncrack")

                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S ncrack")

                    print(language.done.format('Ncrack'))
                    
                print(language.note_tools2.format('Ncrack','ncrack','Terminal'))
                    
        print(language.readmore.format('Ncrack','http://bit.ly/2BxF3Y8'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def kickthemout(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'KickTheOut')
            print(language.instaling.format('KickThemOut'))

            if path.exists('/usr/bin/pacman') == True:
                system("sudo pacman -S tcpdump")

            elif path.exists('/usr/bin/apt') == True:
                system("sudo apt install tcpdump")

            system("""cd {} && sudo git clone https://github.com/k4m4/kickthemout
            cd kickthemout && sudo pip3 uninstall nmap && sudo pip3 install -r requirements.txt""".format(paths))
            print(language.done.format('KickThemOut'))
            print(language.note_tools.format('KickThemOut','sudo python3 kickthemout.py'))

        print(language.readmore.format('KickThemOut','http://bit.ly/30SMUJC'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def sniffair(language):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(language,'SniffAir')
            print(language.installing.format('SniffAir'))
            system("""cd {} && sudo git clone https://github.com/Tylous/SniffAir
            cd SniffAir && sudo bash setup.sh""".format(paths))
            print(language.done.format('SniffAir'))
            print(language.note_tools.format('SniffAir','python2 SniffAir.py'))

        else:
            if name == 'nt':
                print(language.doesnt_support_windows)
            else:
                print(language.run_well.format('Debian'))

        print(language.readmore.format('SniffAir','http://bit.ly/2U06v5S'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def wifi_pumpkin(language):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(language,'WiFi-Pumpkin')
            print(language.installing.format('WiFi-Pumpkin'))
            system("""cd {} && sudo https://github.com/P0cL4bs/WiFi-Pumpkin
            cd WiFi-Pumpkin && sudo bash installer.sh --install""".format(paths))
            print(language.done.format('WiFi-Pumpkin'))

        else:
            if name == 'nt':
                print(language.doesnt_support_windows)
            else:
                print(language.run_well.format('Debian'))

        print(language.readmore.format('WiFi-Pumpkin','http://bit.ly/2MFWIjB'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def airgeddon(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                if path.exists('/usr/bin/airgeddon') == True:
                    print(language.installed.format('Airgeddon'))

                else:
                    if path.exists('/usr/bin/pacman') == True:
                        system("""sudo pacman -S bettercap bully ccze crunch dsniff ethtool ettercap hashcat sslstrip lighttpd john hostapd iptables nftables pciutils pixiewps reaver usbutils
                        sudo wget https://github.com/v1s1t0r1sh3r3/airgeddon/raw/master/binaries/arch/airgeddon-git-9.20-1-any.pkg.tar.xz
                        sudo pacman -U pacman -U airgeddon-git-9.20-1-any.pkg.tar.xz""")

                    elif path.exists('/usr/bin/apt') == True:
                        system("""sudo wget https://github.com/v1s1t0r1sh3r3/airgeddon/raw/master/binaries/kali/airgeddon_9.20-1_all.deb
                        sudo dpkg -i airgeddon_9.20-1_all.deb""")

                    print(language.done.format('Airgeddon'))
                    
                print(language.note_tools2.format('Airgeddon','sudo airgeddon','Terminal'))

        print(language.readmore.format('Airgeddon','http://bit.ly/2tOQ5Dd'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def pikarma(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'PiKarma')
                print(language.installing.format('PiKarma'))
                
                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install aircrack-ng")

                elif path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S aircrack-ng")

                system("""cd {} && sudo git clone https://github.com/WiPi-Hunter/PiKarma && sudo pip2 install termcolor""".format(paths))
                print(language.done.format('PiKarma'))
                print(language.note_tools.format('PiKarma','python2 PiKarma.py'))

        print(language.readmore.format('PiKarma','http://bit.ly/2slyUaC'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def wifite2(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'Wifite 2')
                print(language.installing.format('Wifite 2'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install aicrack-ng tshark reaver bully cowpatty pyrit hashcat ncxtools hcxdumptool hcxpcaptool")

                elif path.exists('/usr/bin/pacman'):
                    system("sudo pacman -S aicrack-ng tshark reaver bully cowpatty pyrit hashcat ncxtools hcxdumptool hcxpcaptool")

                system("""cd {} && sudo git clone https://github.com/derv82/wifite2
                cd wifite2 && sudo python2 setup.py install""".format(paths))
                print(language.done.format('Wifite 2'))
                print(language.note_tools.format('Wifite2','sudo python2 Wifite.py'))

        print(language.readmore.format('Wifite 2','http://bit.ly/2Wvf4Lg'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def pixiewps(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)

        else:
            if path.exists('/usr/local/bin/pixiewps') == True:
                print(language.installed.format('PixieWPS'))

            else:
                paths = the_path(language,'PixieWPS')
                print(language.installing.format('PixieWPS'))
                system("""cd {} && sudo git clone https://github.com/wiire-a/pixiewps
                cd pixiewps && sudo make install""".format(paths))
                print(language.done.format('PixieWPS'))
                
            print(language.note_tools.format('PixieWPS','pixiewps','Terminal'))

        print(language.readmore.format('PixieWPS','http://bit.ly/2XgsHLs'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def fluxion(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'Fluxion')
                print(language.installing.format('Fluxion'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install aircrack-ng coreutils awk iw unzip bc xterm binutils macchanger php-cgi openssl pyrit")

                elif path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S aircrack-ng coreutils awk iw unzip bc xterm binutils macchanger php-cgi  pyrit")

                system("""cd {} && sudo git clone https://github.com/FluxionNetwork/fluxion
                cd fluxion && sudo git clone https://github.com/aircrack-ng/mdk4
                cd mdk4 && sudo make install
                cd {}/fluxion && sudo bash fluxion.sh -i""".format(paths,paths))
                print(language.done.format('Fluxion'))
                print(language.note_tools.format('Fluxion','sudo bash fluxion.sh'))

        print(language.readmore.format('Fluxion','http://bit.ly/2JJELln'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def reaver(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                if path.exists('/usr/bin/reaver') ==  True:
                    print(language.installed.format('Reaver'))

                else:
                    print(language.installing.format('Reaver'))

                    if path.exists('/usr/bin/apt') == True:
                        system("sudo apt install reaver build-essential libpcap-dev aircrack-ng pixiewps")

                    elif path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S reaver libpcap aircrack-ng pixiewps")

                    print(language.done.format('Reaver'))
                    
                print(language.note_tools2.format('Reaver','reaver','Terminal'))

        print(language.readmore.format('Reaver','http://bit.ly/2GRlTMY'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def zarp(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'Zarp')
            print(language.installing.format('Zarp'))
            system("""cd {} && sudo git clone https://github.com/hatRiot/zarp
            cd zarp && sudo pip2 install -r requirements.txt
            sudo pip2 install scapy mitmproxy config netlib paramiko odict""".format(paths))
            print(language.done.format('Zarp'))
            print(language.note_tools.format('Zarp','sudo python2 zarp.py'))

        print(language.readmore.format('Zarp','http://bit.ly/2H1sJ1f'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def xerosploit(language):
    try:
        if path.exists('/usr/bin/apt') == True:
            if path.exists('/usr/bin/xerosploit') == True:
                print(language.installed.format('Xerosploit'))

            else:
                paths = the_path(language,'Xerosploit')
                print(language.installing.format('Xerosploit'))
                system("""cd {} && sudo git clone https://github.com/LionSec/xerosploit
                cd xerosploit && sudo python2 install.py""".format(paths))
                print(language.done.format('Xerosploit'))

            print(language.note_tools2.format('Xerosploit','sudo xerosploit','Terminal'))

        else:
            if name == 'nt':
                print(language.doesnt_support_windows)
                print(language.wsl)

            else:
                print(language.run_well.format('Debian'))

        print(language.readmore.format('Xerosploit','http://bit.ly/2q4qpAD'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def seth(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'Seth')
                print(language.installing.format('Seth'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install tcpdump dsniff openssl && sudo pip3 install hexdump")

                elif path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S tcpdump dsniff openssl && sudo pip3 install hexdump")

                system("cd {} && sudo git clone https://github.com/SySS-Research/Seth".format(paths))
                print(language.done.format('Seth'))
                print(language.note_tools.format('Seth','sudo bash seth.sh'))

        print(language.readmore.format('Seth','http://bit.ly/2DamOVy'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def wifiphisher(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)

        else:
            if path.exists('/usr/bin/wifiphisher'):
                print(language.installed.format('Wifiphisher'))

            else:
                paths = the_path(language,'Wifiphisher')
                print(language.installing.format('Wifiphisher'))
                system("""cd {} && sudo git clone https://github.com/wifiphisher/wifiphisher
                cd wifiphisher && sudo python2 setup.py install""".format(paths))
                print(language.done.format('Wifiphisher'))
                
            print(language.note_tools2.format('Wifiphisher','sudo wifiphisher','Terminal'))

        print(language.readmore.format('Wifiphisher','http://bit.ly/2W3srhs'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def sharp(language):
    try:
        if name == 'nt':
            print(language.doesnt_supprt_windows)

        else:
            paths = the_path(language,'shARP')
            print(language.installing.format('shARP'))

            if path.exists('/usr/bin/apt') == True:
                system("sudo apt install aircrack-ng espeak")

            elif path.exists('/usr/bin/pacman') == True:
                system("sudo pacman -S aircrack-ng espeak")

            system("cd {} && https://github.com/europa502/shARP".format(paths))
            print(language.done.format('shARP'))
            print(language.note_tools.format('shARP','sudo bash shARP.sh'))

        print(language.readmore.format('shARP','http://bit.ly/2FxBwYk'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def sharp_2(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)

        else:
            paths = the_path(language,'shARP 2.0')
            print(language.installing.format('shARP 2.0'))

            if path.exists('/usr/bin/apt') == True:
                system("sudo apt install aircrack-ng espeak")

            elif path.exists('/usr/bin/pacman') == True:
                system("sudo pacman -S aircrack-ng espeak")

            system("cd {} && sudo git clone https://github.com/europa502/shARP_2.0 shARP2".format(paths))
            print(language.done.format('shARP 2.0'))
            print(language.note_tools.format('shARP 2.0','sudo bash shARP.sh'))

        print(language.readmore.format('shARP 2.0','http://bit.ly/2FZDMrQ'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def eviltwinframework(language):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(language,'EvilTwinFramework')
            print(language.installing.format('EvilTwinFramework'))
            system("""cd {} && sudo git clone https://github.com/Esser420/EvilTwinFramework
            cd EvilTwinFramework && sudo python2 setup.py""".format(paths))
            print(language.done.format('EviltwinFramework'))
            print(language.note_tools.format('EvilTwinFramework','sudo python2 etfconsole.py'))
            
        else:
            if name == 'nt':
                print(language.doesnt_support_windows)
            else:
                print(language.run_well.format('Debian'))

        print(language.readmore.format('EvilTwinFramework','http://bit.ly/2Hw6owh'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def the_rogue_toolkit(language):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(language,'The Rogue Toolkit')
            print(language.installing.format('The Rogue Toolkit'))
            system("""cd {} && sudo git clone https://github.com/InfamousSYN/rogue
            cd rogue && sudo python2 install.py""".format(paths))
            print(language.done.format('The Rogue Toolkit'))
            print(language.note_tools.format('The Rogue Toolkit','sudo python2 rogue.py'))

        else:
            if name == 'nt':
                print(language.doesnt_support_windows)
            else:
                print(language.run_well.format('Debian'))

        print(language.readmore.format('The Rogue Toolkit','http://bit.ly/2UR5UEE'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def sitebroker(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    sitebroker(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    sitebroker(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    sitebroker(language)

                else:
                    print(language.invalid)
                    sitebroker(language)

            print(language.installing.format('SiteBroker'))
            system("""cd C:\\ && git clone https://github.com/Anon-Exploiter/SiteBroker
            cd SiteBroker && pip install -r requirements.txt""")

        else:
            paths = the_path(language,'SiteBroker')
            print(language.installing.format('SiteBroker'))
            system("""cd {} && sudo git clone https://github.com/Anon-Exploiter/SiteBroker
            cd SiteBroker && sudo pip2 install -r requirements.txt""".format(paths))
            
        print(language.done.format('SiteBroker'))
        print(language.note_tools.format('SiteBroker','python2 SiteBroker.py'))
        print(language.readmore.format('SiteBroker','http://bit.ly/2MwTdeF'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def websploit(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'WebSploit')
            print(language.installing.format('WebSploit'))
            metasploit(language)

            if path.exists('/usr/bin/apt') == True:
                system("sudo apt install aircrack-ng xterm")

            elif path.exists('/usr/bin/pacman') == True:
                system("sudo pacman -S aircrack-ng xterm")

            system("cd {} && sudo git clone https://github.com/websploit/websploit/blob/master/websploit".format(paths))
            print(language.done.format('WebSploit'))
            print(language.note_tools.format('WebSploit','python2 websploit'))

        print(language.readmore.format('WebSploit','http://bit.ly/2MpIthn'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def wpsploit(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    wpsploit(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    wpsploit(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    wpsploit(language)

                else:
                    print(language.invalid)
                    wpsploit(language)

            print(language.installing.format('WPSploit'))
            system("cd C:\\ && git clone https://github.com/offshores/WPSploit")

        else:
            paths = the_path(language,'WPSploit')
            print(language.installing.format('WPSploit'))
            system("cd {} && sudo git clone https://github.com/offshores/WPSploit".format(paths))
            
        print(language.done.format('WPSploit'))
        print(language.note_tools.format('WPSploit', 'python2 wpsploit.py'))
        print(language.readmore.format('WPSploit','http://bit.ly/2MwTdeF'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def zoom(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    zoom(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    zoom(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    zoom(language)

                else:
                    print(language.invalid)
                    zoom(language)

            print(language.installing.format('Zoom'))
            system("""cd C:\\ && git clone https://github.com/gcxtx/Zoom
            cd Zoom && pip install -r requirements.txt""")

        else:
            paths = the_path(language,'Zoom')
            print(language.installing.format('Zoom'))
            system("""cd {} && sudo git clone https://github.com/gcxtx/Zoom
            cd Zoom && sudo pip2 install -r requirements.txt""".format(paths))
            
        print(language.done.format('Zoom'))
        print(language.note_tools.format('Zoom','python2 zoom.py'))
        print(language.readmore.format('Zoom','http://bit.ly/2HLR66h'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def nosqlmap(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'NoSQLMap')
            print(language.installing.format('NoSQLMap'))
            metasploit(language)
            system("""cd {} && sudo git clone https://github.com/codingo/NoSQLMap
            cd NoSQLMap && sudo python2 setup.py install""".format(paths))
            print(language.done.format('NoSQLMap'))
            print(language.note_tools.format('NoSQLMap','python2 nosqlmap.py'))

        print(language.readmore.format('NoSQLMap','http://bit.ly/2JcYuWF'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def sqlcake(language):
    try:
        if name == 'nt':
            ruby = str(input(language.installed_or_not.format('Ruby-lang')))
            action(language,ruby)

            if ruby[0].upper() == 'Y':
                pass

            elif ruby[0].upper() == 'N':
                print(language.downloading.format('rubyinstaller-2.6.3-1-x86.exe'))
                download('https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.3-1/rubyinstaller-2.6.3-1-x86.exe')
                print(language.note_ruby)
                system('.\\rubyinstaller-2.6.3-1-x86.exe')

            elif (ruby.upper() == 'HELP' or ruby.upper() == 'CHANGELOG' or ruby.upper() == 'ABOUT'):
                sqlcake(language)

            else:
                print(language.invalid)
                sqlcake(language)

            print(language.downloading.format('sqlcake-v1.1.tar'))
            download('https://excellmedia.dl.sourceforge.net/project/sqlcake/sqlcake-v1.1.tar')
            print(language.note_sqlcake)

        else:
            paths = the_path(language,'sqlcake')
            print(language.installing.format(language))
            system("""cd {} && sudo mkdir sqlcake
            cd sqlmake && sudo wget https://excellmedia.dl.sourceforge.net/project/sqlcake/sqlcake-v1.1.tar
            sudo tar -xf sqlcake-v1.1.tar""".format(paths))
            print(language.done.format('sqlcake'))
            print(language.note_tools.format('sqlcake','ruby sqlcake.rb'))

        print(language.readmore.format('sqlcake','http://bit.ly/2N0kOFl'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def bsqlinjector(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            ruby = str(input(language.installed_or_not.format('Ruby-lang'))).strip()
            action(language,ruby)

            if (git[0].upper() == 'Y' and ruby[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif ruby[0].upper() == 'N':
                    print(language.downloading.format('rubyinstaller-2.6.3-1-x86.exe'))
                    download('https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.3-1/rubyinstaller-2.6.3-1-x86.exe')
                    print(language.note_ruby)
                    system('.\\rubyinstaller-2.6.3-1-x86.exe')

                elif (git.upper() == 'HELP' or ruby.upper() == 'HELP'):
                    bsqlinjector(language)

                elif (git.upper() == 'CHANGELOG' or ruby.upper() == 'CHANGELOG'):
                    bsqlinjector(language)

                elif (git.upper() == 'ABOUT' or ruby.upper() == 'ABOUT'):
                    bsqlinjector(language)

                else:
                    print(language.invalid)
                    bsqlinjector(language)

            print(language.installing.format('BSQLinjector'))
            system("cd C:\\ && git clone https://github.com/enjoiz/BSQLinjector")

        else:
            paths = the_path(language,'BSQLinjector')
            print(language.installing.format('BSQLinjector'))
            system("cd {} && git clone https://github.com/enjoiz/BSQLinjector".format(paths))

        print(language.done.format('BSQLinjector'))
        print(language.note_tools.format('BSQLinjector','ruby BSQLinjector.rb'))
        print(language.readmore.format('BSQLinjector','http://bit.ly/2M0HGn5'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def xxeinjector(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            ruby = str(input(language.installed_or_not.format('Ruby-lang'))).strip()
            action(language,ruby)

            if (git[0].upper() == 'Y' and ruby[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif ruby[0].upper() == 'N':
                    print(language.downloading.format('rubyinstaller-2.6.3-1-x86.exe'))
                    download('https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.3-1/rubyinstaller-2.6.3-1-x86.exe')
                    print(language.note_ruby)
                    system('.\\rubyinstaller-2.6.3-1-x86.exe')

                elif (git.upper() == 'HELP' or ruby.upper() == 'HELP'):
                    xxeinjector(language)

                elif (git.upper() == 'CHANGELOG' or ruby.upper() == 'CHANGELOG'):
                    xxeinjector(language)

                elif (git.upper() == 'ABOUT' or ruby.upper() == 'ABOUT'):
                    xxeinjector(language)

                else:
                    print(language.invalid)
                    xxeinjector(language)

            print(language.installing.format('XXEinjector'))
            system("cd C:\\ && git clone https://github.com/enjoiz/XXEinjector")

        else:
            paths = the_path(language,'XXEinjector')
            print(language.installing.format('XXEinjector'))
            system("cd {} && git clone https://github.com/enjoiz/XXEinjector".format(paths))

        print(language.done.format('XXEinjector'))
        print(language.note_tools.format('XXEinjector','ruby XXEinjector.rb'))
        print(language.readmore.format('XXEinjector','http://bit.ly/2Opk8da'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def badmod(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'BadMod')
            print(language.installing.format('BadMod'))

            if path.exists('/usr/bin/apt') == True:
                system("sudo apt install php php-curl")

            elif path.exists('/usr/bin/pacman') == True:
                system("sudo pacman -S php curl")

            system("cd {} && sudo git clone https://github.com/MrSqar-Ye/BadMod".format(paths))
            print(language.done.format('BadMod'))
            print(language.note_tools.format('BadMod','sudo php BadMod.php'))

        print(language.readmore.format('BadMod','http://bit.ly/2IRyiRk'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def roxysploit(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_tools)

            else:
                paths = the_path(language,'roxysploit')
                print(language.installing.format('roxysploit'))

                if path.exists('/usr/bin/pacman') == True:
                    system("""cd {} && sudo git clone https://github.com/andyvaikunth/roxysploit && sudo pacman -S android-tools
                    sudo pip2 install logging impacket pysmb threading socket socks zipfile shutil io struct re optparse binascii base64 urllib2 urllib requests commands paramiko scapy whois rlcompleter readline terminaltables platform""".format(paths))
                    print(language.done.format('roxysploit'))
                    print(language.note_tools.format('roxysploit','sudo python2 roxy.py'))

                else:
                    system("""cd {} && sudo git clone https://github.com/andyvaikunth/roxysploit
                    cd roxwpsploitysploit && sudo bash install""".format(paths))
                    print(language.done.format('roxysploit'))
                    print(language.note_tools2.format('roxyspoit','sudo rsfc'))

        print(language.readmore.format('roxysploit','http://bit.ly/2HodbHU'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def lunar(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    lunar(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    lunar(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    lunar(language)

                else:
                    print(language.invalid)
                    lunar(language)

            print(language.installing.format('Lunar'))
            system("""cd C:\\ && git clone https://github.com/Zucccs/Lunar
            cd Lunar && .\\install.bat""")  
            print(language.done.format('Lunar'))
            print(language.note_tools.format('Lunar','python main.py'))

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'Lunar')
                print(language.installing.format('Lunar'))

                if path.exists('/usr/bin/pacman') == True:
                    system("""cd {} && sudo git clone https://github.com/Zucccs/Lunar/
                    sudo pip2 install requests datetime subprocess colorama cryptography urllib2
                    sudo pacman -S wireshark-cli wireshark-qt
                    sudo git clone https://github.com/vanhauser-thc/thc-hydra
                    cd thc-hydra && sudo ./configure
                    sudo make && sudo make install
                    cd hydra-gtk && sudo ./configure
                    sudo make && sudo make install""".format(paths))

                elif path.exists('/usr/bin/apt') == True:
                    system("""cd {} && sudo git clone https://github.com/Zucccs/Lunar
                    cd Lunar && sudo bash install.sh""".format(paths))

                print(language.done.format('Lunar'))
                print(language.note_tools.format('Lunar','python2 main.py'))

        print(language.readmore.format('Lunar','http://bit.ly/2IEOTvp'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def autordpwn(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            powershell = str(input(language.installed_or_not.format('PowerShell'))).strip()
            action(language,powershell)

            if (git.upper() == 'Y' and powershell.upper() == 'Y'):
                pass

            else:
                if git.upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif powershell.upper() == 'N':
                    print(language.note_powershell)

                elif (git.upper() == 'HELP' or powershell.upper() == 'HELP'):
                    autordpwn(language)

                elif (git.upper() == 'CHANGELOG' or powershell.upper() == 'CHANGELOG'):
                    autordpwn(language)

                elif (git.upper() == 'ABOUT' or powershell.upper() == 'ABOUT'):
                    autordpwn(language)

                else:
                    print(language.invalid)
                    autordpwn(language)

            print(language.installing.format('AutoRDPwn'))
            system("cd C:\\ && git clone https://github.com/JoelGMSec/AutoRDPwn/")
            print(language.done.format('AutoRDPwn'))
            print(language.note_tools.format('AutoRDPwn','.\\AutoRDPwn.ps1'))

        else:
            print(language.only_compatible.format('PowerShell'))

        print(language.readmore.format('AutoRDPwn','http://bit.ly/2VNcpck'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def expliot(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if path.exists('/bin/efconsole') == True:
                print(language.installed.format('eXpliot'))

            else:
                paths = the_path(language,'eXpliot')
                print(language.installing.format('eXpliot'))

                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S libusb glib")

                elif path.exists('/usr/bin/apt') == True:
                    system("sudo apt install libglib2.0-dev libusb-1.0")

                system("""cd {} && sudo git clone https://gitlab.com/expliot_framework/expliot
                cd expliot && sudo python3 setup.py install""".format(paths))
                print(language.done.format('eXpliot'))

            print(language.note_tools2.format('eXpliot','efconsole'))

        print(language.readmore.format('eXpliot','http://bit.ly/2mQTkWN'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def rootos(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'rootOS')
            print(language.installing.format('rootOS'))
            system("cd {} && sudo git clone https://github.com/thehappydinoa/rootOS".format(paths))
            print(language.done.format('rootOS'))
            print(language.note_tools.format('rootOS','python2 rootos.py'))

        print(language.readmore.format('rootOS','http://bit.ly/2GvBSSl'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def pure_blood(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'Pure Blood')
            print(language.installing.format('Pure Blood'))
            system("""cd {} && sudo git clone https://github.com/cr4shcod3/pureblood
            cd pureblood && sudo pip2 install -r requirements.txt""".format(paths))
            print(language.done.format('Pure Blood'))
            print(language.note_tools.format('Pure Blood','python2 pureblood.py'))

        print(language.readmore.format('Pure Blood','http://bit.ly/2LOFfIh'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def termineter(language):
    try:
        if name == 'nt':
            python3 = str(input(language.installed_or_not.format('Python 3.7')))
            action(language,python3)

            if python3[0].upper() == 'Y':
                pass

            elif python3[0].upper() == 'N':
                print(language.downloading.format('python-3.7.3.exe'))
                download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                print(language.note_python3)
                system('.\\python-3.7.3.exe')

            elif (python3.upper() == 'HELP' or python3.upper() == 'CHANGELOG' or python3.upper() == 'ABOUT'):
                termineter(language)

            else:
                print(language.invalid)
                termineter(language)

            print(language.installing.format('Termineter'))
            system("pip install termineter")
            print(language.done.format('Termineter'))

        else:
            if path.exists('/usr/bin/termineter') == True:
                print(language.installed.format('Termineter'))

            else:
                print(language.installing.format('Termineter'))
                system("sudo pip3 install termineter")
                print(language.done.format('Termineter'))
                
        print(language.note_tools2.format('Termineter','termineter','Terminal & CMD'))
        print(language.readmore.format('Termineter','http://bit.ly/2m5btzY'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def autosploit(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'AutoSploit')
            print(language.installing.format('AutoSploit'))

            if path.exists('/usr/bin/pacman') == True:
                system("""cd {} && sudo git clone https://github.com/NullArray/AutoSploit
                sudo pacman -S metasploit postgresql apache
                cd AutoSploit && sudo pip2 install -r requirements.txt""".format(paths))

            elif path.exists('/usr/bin/apt') == True:
                system("""cd {} && sudo git clone https://github.com/NullArray/AutoSploit
                cd AutoSploit && sudo pip2 install -r requirements.txt
                sudo bash install.sh""".format(paths))

            print(language.done.format('AutoSploit'))
            print(language.note_tools.format('AutoSploit','python2 autosploit.py'))

        print(language.readmore.format('AutoSploit','http://bit.ly/2xxvTu3'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def smod(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'smod')
            print(language.installing.format('smod'))
            system("""cd {} && sudo git clone https://github.com/Exploit-install/smod && sudo pip2 install scapy""".format(paths))
            print(language.done.format('smod'))
            print(language.note_tools.format('smod','python2 smod.py'))

        print(language.readmore.format('smod','http://bit.ly/2JS3C6f'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def thefatrat(language):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(language,'TheFatRat')
            print(language.installing.fomat('TheFatRat'))
            system("""cd {} && https://github.com/Screetsec/TheFatRat
            cd TheFatRat && sudo bash setup.sh""".format(paths))
            print(language.done.format('TheFatRat'))
            print(language.note_tools.format('TheFatRat','bash fatrat'))

        else:
            if name == 'nt':
                print(language.doesnt_support_windows)
                print(language.wsl)

            else:
                print(language.run_well.format('Debian'))

        print(language.readmore.format('TheFatRat','http://bit.ly/2BDa6PV'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def exploit_pack(language):
    try:
        if name == 'nt':
            java = str(input(language.installed_or_not.format('Java'))).strip()
            action(language,java)

            if java[0].upper() == 'Y':
                pass

            elif java[0].upper() == 'N':
                print(language.downloading.format('jre-8u211-windows-i586-iftw.exe'))
                download("https://sdlc-esd.oracle.com/ESD6/JSCDL/jdk/8u211-b12/478a62b7d4e34b78b671c754eaaf38ab/jre-8u211-windows-i586-iftw.exe?GroupName=JSC&FilePath=/ESD6/JSCDL/jdk/8u211-b12/478a62b7d4e34b78b671c754eaaf38ab/jre-8u211-windows-i586-iftw.exe&BHost=javadl.sun.com&File=jre-8u211-windows-i586-iftw.exe&AuthParam=1559705933_85bc6ea5c1eb928eabbe3a7733aca1df&ext=.exe")
                system(".\\jre-8u211-windows-i586-iftw.exe")

            elif (java.upper() == 'HELP' or java.upper() == 'CHANGELOG' or java.upper() == 'ABOUT'):
                exploit_pack(language)

            else:
                print(language.invalid)
                exploit_pack(language)

            print(language.downloading.format('exploitpack.zip'))
            download('https://github.com/ExploitPackBinaries/ExploitPack/raw/master/exploitpack.zip')
            print(language.note_exploit_pack)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'Exploit Pack')
                print(language.installing.format('Exploit Pack'))
                
                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -sS jdk-openjdk jre-openjdk ")

                elif path.exists('/usr/bin/apt') == True:
                    system("""sudo add-apt-repository ppa:linuxuprising/java
                    sudo apt update && sudo apt install oracle-java11-installer""")

                system("""cd {} && https://github.com/ExploitPackBinaries/ExploitPack/raw/master/exploitpack.zip
                unzip exploitpack.zip -d exploitpack""".format(paths))
                print(language.done.format('Exploit Pack'))
                print(language.note_tools.format('Exploit Pack','sudo bash RunExploitPack.sh'))

        print(language.readmore.format('Exploit Pack','http://bit.ly/2KWeeOe'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def mimikittenz(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            powershell = str(input(language.installed_or_not.format('PowerShell'))).strip()
            action(language,powershell)

            if (git[0].upper() == 'Y' and powershell[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif powershell[0].upper(language) == 'N':
                    print(language.note_powershell)

                elif (git.upper() == 'HELP' or powershell.upper() == 'HELP'):
                    mimikittenz(language)

                elif (git.upper() == 'CHANGELOG' or powershell.upper() == 'CHANGELOG'):
                    mimikittenz(language)

                elif (git.upper() == 'ABOUT' or powershell.upper() == 'ABOUT'):
                    mimikittenz(language)

                else:
                    print(language.invalid)
                    mimikittenz(language)

            print(language.installing.format('mimikittenz'))
            system("cd C:\\ && git clone https://github.com/putterpanda/mimikittenz")
            print(language.done.format('mimikittenz'))
            print(language.note_tools.format('mimikittenz','.\\Invoke-mimikittenz.ps1'))

        else:
            print(language.only_compatible.format('PowerShell'))

        print(language.readmore.format('mimikittenz','http://bit.ly/2FY0TD6'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def ezsploit(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'ezsploit')
                print(language.installing.format('ezsploit'))
                metasploit(language)
                system("cd {} && sudo git clone https://github.com/rand0m1ze/ezsploit".format(paths))
                print(language.done.format('ezsploit'))
                print(language.note_tools.format('ezsploit','ezsploit.sh'))

        print(language.readmore.format('ezsploit','http://bit.ly/2EO62B8'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def auto_root_exploit(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'Auto-Exploit-Root')
            print(language.installing.format('Auto-Exploit-Root'))
            system("cd {} && sudo git clone https://github.com/nilotpalbiswas/Auto-Root-Exploit".format(paths))
            print(language.done.format('Auto-Root-Exploit'))
            print(language.note_tools.format('Auto-Root-Exploit','bash autoroot.sh'))

        print(language.readmore.format('Auto-Root-Exploit','http://bit.ly/2UqdvsV'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def ahmyth_android_rat(language):
    try:
        if name == 'nt':
            java = str(input(language.installed_or_not.format('Java'))).strip()
            action(language,java)

            if java[0].upper() == 'Y':
                pass

            elif java[0].upper() == 'N':
                print(language.downloading.format('jre-8u211-windows-i586-iftw.exe'))
                download("https://sdlc-esd.oracle.com/ESD6/JSCDL/jdk/8u211-b12/478a62b7d4e34b78b671c754eaaf38ab/jre-8u211-windows-i586-iftw.exe?GroupName=JSC&FilePath=/ESD6/JSCDL/jdk/8u211-b12/478a62b7d4e34b78b671c754eaaf38ab/jre-8u211-windows-i586-iftw.exe&BHost=javadl.sun.com&File=jre-8u211-windows-i586-iftw.exe&AuthParam=1559705933_85bc6ea5c1eb928eabbe3a7733aca1df&ext=.exe")
                system(".\\jre-8u211-windows-i586-iftw.exe")

            elif (java.upper() == 'HELP' or java.upper() == 'CHANGELOG' or java.upper() == 'ABOUT'):
                ahmyth_android_rat(language)

            else:
                print(language.invalid)
                ahmyth_android_rat(language)

            print(language.installing.format('AhMyth-Android-RAT'))
            print(language.downloading.format('AhMyth_Win32.exe'))
            download('https://github.com/AhMyth/AhMyth-Android-RAT/releases/download/v1.0-beta.1/AhMyth_Win32.exe')
            system('.\\AhMyth_Win32.exe')

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                if path.exists('/usr/bin/pacman') == True:
                    paths = the_path(language,'AhMyth-Android-RAT')
                    print(language.installing.format('AhMyth-Android-RAT'))
                    system("""sudo pacman -sS jdk-openjdk jre-openjdk electron
                    cd {} && sudo git clone https://github.com/AhMyth/AhMyth-Android-RAT""".format(paths))
                    print(language.done.format('AhMyth-Android-RAT'))
                    print(language.note_tools2.format('AhMyth-Android-RAT','sudo nmp start','AhMyth-Android-RAT/AhMyth-Server'))


                elif path.exists('/usr/bin/apt') == True:
                    print(language.installing.format('AhMyth-Android-RAT'))
                    system("""sudo add-apt-repository ppa:linuxuprising/java
                    sudo apt update && sudo apt install oracle-java11-installer""")
                    system("wget https://github.com/AhMyth/AhMyth-Android-RAT/releases/download/v1.0-beta.1/AhMyth_linux32.deb && sudo dpkg -i AhMyth_linux32.deb")
                    print(language.done.format('AhMyth-Android-RAT'))
                    print(language.note_tools2.format('AhMyth-Android-RAT','sudo ahmyth','Terminal'))

        print(language.readmore.format('AhMyth-Android-RAT','http://bit.ly/2YuBQAm'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def exploit_framework(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    exploit_framework(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    exploit_framework(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    exploit_framework(language)

                else:
                    print(language.invalid)
                    exploit_framework(language)

            print(language.installing.format('Exploit-Framework'))
            system("cd C:\\ && git clone https://github.com/WangYihang/Exploit-Framework")

        else:
            paths = the_path(language,'Exploit-Framework')
            print(language.installing.format('Exploit-Framework'))
            system("cd {} && sudo git clone https://github.com/WangYihang/Exploit-Framework".format(paths))
            
        print(language.done.format('Exploit-Framework'))
        print(language.note_tools.format('Exploit-Framework', 'python2 framework.py'))
        print(language.readmore.format('Exploit-Framework','http://bit.ly/2L0UEjN'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def winroothelper(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            powershell = str(input(language.installed_or_not.format('PowerShell'))).strip()
            action(language,powershell)

            if (git[0].upper() == 'Y' and powershell[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif powershell[0].upper(language) == 'N':
                    print(language.note_powershell)

                elif (git.upper() == 'HELP' or powershell.upper() == 'HELP'):
                    winroothelper(language)

                elif (git.upper() == 'CHANGELOG' or powershell.upper() == 'CHANGELOG'):
                    winroothelper(language)

                elif (git.upper() == 'ABOUT' or powershell.upper() == 'ABOUT'):
                    winroothelper(language)

                else:
                    print(language.invalid)
                    winroothelper(language)

            print(language.installing.format('WinRootHelper'))
            system("cd C:\\ && git clone https://github.com/GreySec-Security-Forums/WinRootHelper")
            print(language.done.format('WinRootHelper'))
            print(language.note_tools.format('WinRootHelper','.\\winroot.ps1'))

        else:
            print(language.only_compatible.format('PowerShell'))

        print(language.readmore.format('WinRootHelper','http://bit.ly/2Uu0BKG'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def metasploit(language):
    try:
        if name == 'nt':
            print(language.installing.format('Metasploit Framework'))
            print(language.downloading.format('metasploitframework-latest.msi'))
            download('https://windows.metasploit.com/metasploitframework-latest.msi')
            system(".\\metasploitframework-latest.msi")
            print(language.done.format('Metasploit Framework'))
            print(language.note_tools.format('Metasploit Framework','"C:\\metasploit\\console.bat"','CMD'))

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                if path.exists('/usr/bin/msfconsole') == True:
                    print(language.installed.format('Metasploit Framework'))

                else:
                    print(language.installing.format('Metasploit Framework'))

                    if path.exists('/usr/bin/pacman') == True:
                        system("sudo pacman -S metasploit")

                    elif path.exists('/usr/bin/apt') == True:
                        system("""sudo curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
                        chmod 755 msfinstall && sudo ./msfinstall""")
                        
                    print(language.done.format('Metasploit Framework'))

                print(language.note_tools.format('Metasploit Framework','sudo msfconsole','Terminal'))

        print(language.readmore.format('Metasploit Framework','http://bit.ly/2JkoOl9'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def zerodoor(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'ZeroDoor')
                print(language.installing.format('ZeroDoor'))

                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S gcc && git clone https://aur.archlinux.org/mingw-w64-gcc.git && cd mingw-w64-gcc && makepkg -si")

                elif path.exists('/usr/bin/apt') == True:
                    system("sudo apt install gcc mingw-w64")

                system("cd {} && sudo git clone https://github.com/Souhardya/Zerodoor".format(paths))
                print(language.done.format('ZeroDoor'))
                print(language.note_tools.format('ZeroDoor','python2 zerodoor.py'))

        print(language.readmore.format('ZeroDoor','http://bit.ly/2LSjhnR'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def terminator(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'Terminator')
                print(language.installing.format('Terminator'))
                metasploit(language)
                system("cd {} && sudo git clone https://github.com/MohamedNourTN/Terminator".format(paths))
                print(language.done.format('Terminator'))
                print(language.note_tools.format('Terminator','python2 terminator.py'))

        print(language.readmore.format('Terminator','http://bit.ly/2vcD5If'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def winpayloads(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'WinPayloads')
                print(language.installing.format('WinPayloads'))
                metasploit(language)

                if path.exists('/usr/bin/pacman') == True:
                    system("""sudo pacman -S wine python2-crypto unzip curl wget libwbclient
                    sudo pip2 install requests netifaces blessed pyasn1
                    sudo pip2 install --force-reinstall prompt-toolkit==1.0.15""")

                system("""cd {} && sudo git clone https://github.com/nccgroup/Winpayloads
                cd Winpayloads && sudo bash setup.sh""".format(paths))
                print(language.done.format('WinPayloads'))
                print(language.note_tools.format('WinPayloads','sudo python2 WinPayloads.py'))

        print(language.readmore.format('WinPayloads','http://bit.ly/2MkvmT7'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def saint(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'sAINT')
                print(language.installing.format('sAINT'))

                if path.exists('/usr/bin/apt') == True:
                    system("""sudo add-apt-repository ppa:linuxuprising/java
                    sudo apt update && sudo apt install oracle-java8-installer
                    sudo apt install maven zlib1g-dev libncurses5-dev lib32z1 lib32ncurses6 -y""")

                elif path.exists('/usr/bin/apt') == True:
                    system("""sudo pacman -S jre8-openjdk jdk8-openjdk maven zlib ncurses lib32-ncurses""")

                system("""cd {} && sudo git clone https://github.com/tiagorlampert/sAINT
                cd sAINT && sudo bash configure.sh""".format(paths))
                print(language.done.format('sAINT'))
                print(language.note_tools.format('sAINT','java -jar sAINT.jar'))

        print(language.readmore.format('sAINT','http://bit.ly/2LPtpcV'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def beelogger(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'BeeLogger')
                print(language.installing.format('BeeLogger'))

                if path.exists('/usr/bin/pacman') == True:
                    system("""sudo pacman -S wine""")

                system("""cd {} && sudo git clone https://github.com/4w4k3/BeeLogger
                cd BeeLogger && sudo bash install.sh""".format(paths))
                print(language.done.formar('BeeLogger'))
                print(language.note_tools.format('BeeLogger','python2 bee.py'))

        print(language.readmore.format('BeeLogger','http://bit.ly/2LqJyJF'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def hacktheworld(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/pacman') == False and path.exists('/usr/bin/apt') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'HackTheWorld')
                print(language.installing.format('HackTheWorld'))

                if path.exists('/usr/bin/pacman') == True:
                    system("""git clone https://aur.archlinux.org/mingw-w64-gcc.git && cd mingw-w64 && makepkg -si
                    sudo pacman -S wine metasploit
                    cd {} && sudo git clone https://github.com/stormshadow07/HackTheWorld""".format(paths))

                elif path.exists('/usr/bin/apt') == True:
                    system("""cd {} && sudo git clone https://github.com/stormshadow07/HackTheWorld
                    cd HackTheWorld && sudo bash install.sh""".format(paths))

                print(language.done.format('HackTheWorld'))
                print(language.note_tools.format('HackTheWorld','python2 HackTheWorld.py'))

        print(language.readmore.format('HackTheWorld','http://bit.ly/2JhzBfZ'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def hatkey(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)
            powershell = str(input(language.installed_or_not.format('PowerShell'))).strip()
            action(language,powershell)

            if (git.upper() == 'Y' and python2.upper() == 'Y' and powershell.upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif powershell.upper() == 'N':
                    print(language.note_powershell)

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP' or powershell.upper() == 'HELP'):
                    hatkey(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG' or powershell.upper() == 'CHANGELOG'):
                    hatkey(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT' or powershell.upper() == 'ABOUT'):
                    hatkey(language)

                else:
                    print(language.invalid)
                    hatkey(language)

            system("cd C:\\ && git clone https://github.com/Naayouu/Hatkey")
            print(language.done.format('HatKey'))
            print(language.note_tools.format('HatKey','python2 HatKey.py'))

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/dnf') == False and path.exists('/usr/bin/yum') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'HatKey')
                print(language.installing.format('HatKey'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install powershell")

                elif path.exists('/usr/bin/yum') == True:
                    system("sudo yum install powershell")

                elif path.exists('/usr/bin/dnf') == True:
                    system("sudo dnf install powershell")

                elif path.exists('/usr/bin/pacman') == True:
                    system("git clone https://aur.archlinux.org/powershell.git && cd powershell && makepkg -si")

                system("cd {} && sudo git clone https://github.com/Naayouu/Hatkey".format(paths))
                print(language.done.format('HatKey'))
                print(language.note_tools.format('HatKey','python2 HatKey.py'))

        print(language.readmore.format('HatKey','http://bit.ly/2HOZbDZ'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def trolo(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == True and path.exists('/usr/bin/pacman') == True):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'trolo')
                print(language.installing.format('trolo'))
                metasploit(language)

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install powershell")

                elif path.exists('/usr/bin/pacman') == True:
                    system("git clone https://aur.archlinux.org/powershell.git && cd powershell && makepkg -si")

                system("cd {} && sudo git clone https://github.com/b3rito/trolo".format(paths))
                print(language.done.format('trolo'))
                print(language.note_tools.format('trolo','bash trolo.sh'))

        print(language.readmore.format('trolo','http://bit.ly/2Jj37Sj'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def getwin(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == True and path.exists('/usr/bin/pacman') == True):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'GetWin')
                print(language.installing.format('GetWin'))

                if path.exists('/usr/bin/pacman') == True:
                    system("""sudo pacman -S netcat php libssh2 openssh
                    git clone https://aur.archlinux.org/mingw-w64-gcc.git && cd mingw-w64-gcc && makepkg -si""")

                elif path.exists('/usr/bin/apt') == True:
                    system("sudo apt install netcat php ssh mingw-w64")

                system("cd {} && sudo git clone https://github.com/thelinuxchoice/getwin".format(paths))
                print(language.done.format('GetWin'))
                print(language.note_tools.format('GetWin','bash getwin.sh'))

        print(language.readmore.format('GetWin','http://bit.ly/2R0reH5'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def dkmc(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == True and path.exists('/usr/bin/pacman') == True):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'DKMC')
                print(language.installing.format('DKMC'))

                if path.exists('/usr/bin/apt') == True:
                    system("sudo apt install powershell")

                elif path.exists('/usr/bin/pacman') == True:
                    system("git clone https://aur.archlinux.org/powershell.git && cd powershell && makepkg -si")

                system("cd {} && sudo git clone https://github.com/Mr-Un1k0d3r/DKMC && cd DKMC && sudo mkdir output".format(paths))
                print(language.done.format('DKMC'))
                print(language.note_tools.format('DKMC','python2 dkmc.py'))

        print(language.readmore.format('DKMC','http://bit.ly/2IybKpD'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def parat(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git.upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2.upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    parat(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    parat(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    parat(language)

                else:
                    print(language.invalid)
                    parat(language)

            print(language.installing.format('Parat'))
            system("cd C:\\ && git clone https://github.com/fadinglr/Parat")

        else:
            paths = the_path(language,'Parat')
            print(language.installing.format('Parat'))
            system("cd {} && sudo git clone https://github.com/fadinglr/Parat".format(paths))

        print(language.done.format('Parat'))
        print(language.note_tools.format('Parat','python2 main.py'))
        print(language.readmore.format('Parat','http://bit.ly/2wa5LC6'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def mkvenom(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'mkvenom')
                print(language.installing.format('mkvenom'))
                metasploit(language)
                system("cd {} && sudo git clone https://github.com/phraxoid/mkvenom".format(paths))
                print(language.done.format('mkvenom'))
                print(language.note_tools.format('mkvenom','bash mkvenom.sh'))

        print(language.readmore.format('mkvenom','http://bit.ly/2MoYrg5'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def venom(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'venom')
                print(language.installing.format('venom'))
                metasploit(language)

                if path.exists('/usr/bin/apt') == True:
                    system("""sudo apt install wine gcc mingw32
                    git clone https://gitlab.com/kalilinux/packages/shellter && cd shellter/debian && sudo bash install""")

                elif path.exists('/usr/bin/pacman') == True:
                    system("""wget https://raw.githubusercontent.com/BlackArch/blackarch/37ad245e9b30abfc7fcc7e636c1df3675b134dee/packages/shellter/PKGBUILD && makepkg -si
                    git clone https://aur.archlinux.org/mingw-w64-gcc.git && cd mingw-w64-gcc && makepkg -si
                    sudo pacman -S wine gcc""")

                system("cd {} && sudo git clone https://github.com/r00t-3xp10it/venom".format(paths))
                print(language.done.format('venom'))
                print(language.note_tools.format('venom','sudo bash venom.sh'))

        print(language.readmore.format('venom','http://bit.ly/2MVHTc0'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def cloak(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'Cloak')
                metasploit(language)
                system("cd {} && sudo git clone https://github.com/s0md3v/Cloak".format(paths))
                print(language.done.format('Cloak'))
                print(language.note_tools.format('Cloak','python3 cloak.py'))

        print(language.readmore.format('Cloak','http://bit.ly/2OQ2tLb'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def avoid(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'Metasploit AV Evasion')
                print(language.installing.format('Metasploit AV Evasion'))
                metasploit(language)

                if path.exists('/usr/bin/pacman') == True:
                    system("sudo pacman -S gcc && git clone https://aur.archlinux.org/mingw-w64-gcc.git && cd mingw-w64-gcc && makepkg -si")

                elif path.exists('/usr/bin/apt') == True:
                    system("sudo apt install gcc mingw-w64")

                system("cd {} && sudo git clone https://github.com/nccgroup/metasploitavevasion".format(paths))
                print(language.done.format('Metasploit AV Evasion'))
                print(language.note_tools.format('Metasploit AV Evasion','bash avoid.sh'))

        print(language.readmore.format('Metasploit AV Evasion','http://bit.ly/2Kn3Q1p'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def avet(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if (path.exists('/usr/bin/apt') == False and path.exists('/usr/bin/pacman') == False):
                print(language.unknow_distro)

            else:
                paths = the_path(language,'AVET')
                print(language.installing.format('AVET'))
                metasploit(language)

                if path.exists('/usr/bin/pacman') == True:
                    system("""sudo pacman -S gcc wine && wget https://downloads.sourceforge.net/project/tdm-gcc/TDM-GCC%20Installer/tdm64-gcc-5.1.0-2.exe
                    sudo wine tdm64-gcc-5.1.0-2.exe && sudo rm tdm64-gcc-5.1.0-2.exe
                    cd {} && sudo git clone https://github.com/govolution/avet""".format(paths))

                elif path.exists('/usr/bin/apt') == True:
                    system("""cd {} && sudo git clone https://github.com/govolution/avet
                    cd avet && sudo bash setup.sh""".format(paths))

                print(language.done.format('AVET'))
                print(language.note_tools.format('AVET','python3 avet_fabric.py'))

        print(language.readmore.format('AVET','http://bit.ly/2TltIE3'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def nxcrypt(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP'):
                    nxcrypt(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG'):
                    nxcrypt(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT'):
                    nxcrypt(language)

                else:
                    print(language.invalid)
                    nxcrypt(language)

            print(language.installing.format('NXcrypt'))
            system("cd C:\\ && git clone https://github.com/Hadi999/NXcrypt")

        else:
            paths = the_path(language,'NXcrypt')
            print(language.installing.format('NXcrypt'))
            system("cd {} && sudo git clone https://github.com/Hadi999/NXcrypt".format(paths))

        print(language.done.format('NXcrypt'))
        print(language.note_tools.format('NXcrypt','python2 nxcrypt.py'))
        print(language.readmore.format('NXcrypt','http://bit.ly/2xcyR6P'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def slowloris(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            python3 = str(input(language.installed_or_not.format('Python 3.7'))).strip()
            action(language,python3)

            if python3[0].upper() == 'Y':
                pass
                    
            elif python3[0].upper() == 'N':
                print(language.downloading.format('python-3.7.3.exe'))
                download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                print(language.note_python3)
                system('.\\python-3.7.3.exe')

            elif (python3.upper() == 'HELP' or python3.upper() == 'ABOUT' or python3.upper() == 'CHANGELOG'):
                slowloris(language)

            else:
                print(language.invalid)
                slowloris(language)

            print(language.installing.format("SlowLoris"))
            system("pip3 install slowloris")

        else:
            print(language.installing.format("SlowLoris"))
            system("sudo pip3 install slowloris")

        print(language.done.format('SlowLoris'))
        print(language.note_tools2.format('SlowLoris','slowloris','Terminal & CMD'))
        print(language.readmore.format('SlowLoris','http://bit.ly/2VipeKA'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def zambie(language):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(language,'ZAmbIE')
            print(language.installing.format('ZAmbIE'))
            system("""cd {} sudo git clone https://github.com/zanyarjamal/zambie
            cd zambie && sudo bash Installer.sh""".format(paths))
            print(language.done.format('ZAmbIE'))
            print(language.note_tools.format('ZAmbIE','python zambie.py'))

        else:
            if name == 'nt':
                print(language.doesnt_support_windows)
                print(language.wsl)

            else:
                print(language.run_well.format('Debian'))

        print(language.readmore.format('ZAmbIE','http://bit.ly/2JymfeZ'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def ufonet(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            paths = the_path(language,'UFONet')
            print(language.installing.format('UFONet'))
            system("""cd {} && sudo git clone https://github.com/epsylon/ufonet
            cd ufonet && sudo python2 setup.py install""".format(paths))
            print(language.done.format('UFONet'))
            print(language.note_tools.format('UFONet','python2 ufonet'))

        print(language.readmore.format('UFONet','http://bit.ly/2C8i1YT'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def memcrashed(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python3 = str(input(language.installed_or_not.format('Python 3.7'))).strip()
            action(language,python3)

            if (git[0].upper() == 'Y' and python3[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')
                    
                elif python3[0].upper() == 'N':
                    print(language.downloading.format('python-3.7.3.exe'))
                    download('https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe')
                    print(language.note_python3)
                    system('.\\python-3.7.3.exe')

                elif (git.upper() == 'HELP' or python3.upper() == 'HELP'):
                    memcrashed(language)

                elif (git.upper() == 'CHANGELOG' or python3.upper() == 'CHANGELOG'):
                    memcrashed(language)

                elif (git.upper() == 'ABOUT' or python3.upper() == 'ABOUT'):
                    memcrashed(language)

                else:
                    print(language.invalid)
                    memcrashed(language)

            print(language.installing.format('Memcrashed-DDoS-Exploit'))
            system("""cd C:\\ && git clone https://github.com/649/Memcrashed-DDoS-Exploit Memcrashed
            cd Memcrashed && pip install -r requirements.txt""")

        else:
            paths = the_path(language,'Memcrashed-DDoS-Exploit')
            print(language.installing.format('Memcrashed-DDoS-Exploit'))
            system("""cd {} && git clone https://github.com/649/Memcrashed-DDoS-Exploit Memcrashed
            cd Memcrashed && pip install -r requirements.txt""".format(paths))

        print(language.done.format('Memcrashed-DDoS-Exploit'))
        print(language.note_tools.format('Memcrashed-DDoS-Exploit','python3 Memcrashed.py'))
        print(language.readmore.format('Memcrashed-DDoS-Exploit','http://bit.ly/2NVzF42'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def fsociety(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if path.exists('/usr/bin/pacman') == True:
                paths = the_path(language,'Fsociety')
                print(language.installing.format)
                system("cd {} && sudo git clone https://github.com/Manisso/fsociety".format(paths))
                print(language.done.format('Fsociety'))
                print(language.note_tools.format('Fsociety','python2 fsociety.py'))

            else:
                if path.exists('/usr/local/bin/fsociety') == True:
                    print(language.installed.format('Fsociety'))

                else:
                    paths = the_path(language,'Fsociety')
                    print(language.installing.format)
                    system("cd {} && sudo git clone https://github.com/Manisso/fsociety".format(paths))
                    print(language.done.format('Fsociety'))
                    
                print(language.note_tools2.format('Fsociety','fsociety','Terminal'))

        print(language.readmore.format('Fsociety','http://bit.ly/2mJIRwi'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def malicious(language):
    try:
        if name == 'nt':
            print(language.note_saved)
            git = str(input(language.installed_or_not.format('Git-scm'))).strip()
            action(language,git)
            python2 = str(input(language.installed_or_not.format('Python 2.7'))).strip()
            action(language,python2)
            ruby = str(input(language.installed_or_not.format('Ruby-lang'))).strip()
            action(language,ruby)

            if (git[0].upper() == 'Y' and python2[0].upper() == 'Y' and ruby[0].upper() == 'Y'):
                pass

            else:
                if git[0].upper() == 'N':
                    print(language.downloading.format('Git-2.21.0-32-bit.exe'))
                    download('https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-32-bit.exe')
                    print(language.note_git)
                    system('.\\Git-2.21.0-32-bit.exe')

                elif python2[0].upper() == 'N':
                    print(language.downloading.format('python-2.7.16.msi'))
                    download('https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi')
                    print(language.note_python2)
                    system('.\\python-2.7.16.msi')

                elif ruby[0].upper() == 'N':
                    print(language.downloading.format('rubyinstaller-2.6.3-1-x86.exe'))
                    download('https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.3-1/rubyinstaller-2.6.3-1-x86.exe')
                    print(language.note_ruby)
                    system('.\\rubyinstaller-2.6.3-1-x86.exe')

                elif (git.upper() == 'HELP' or python2.upper() == 'HELP' or ruby.upper() == 'HELP'):
                    malicious(language)

                elif (git.upper() == 'CHANGELOG' or python2.upper() == 'CHANGELOG' or ruby.upper() == 'CHANGELOG'):
                    malicious(language)

                elif (git.upper() == 'ABOUT' or python2.upper() == 'ABOUT' or ruby.upper() == 'ABOUT'):
                    malicious(language)

                else:
                    print(language.invalid)
                    malicious(language)

            print(language.installing.format('Malicious'))
            system("""cd C:\\ && git clone https://github.com/Hider5/Malicious
            cd Malicious && gem install lolcat && pip install -r requirements.txt""")

        else:
            paths = the_path(language,'Malicious')
            print(language.installing.format('Malicious'))

            if path.exists('/usr/bin/apt') == True:
                system("sudo apt install ruby")

            elif path.exists('/usr/bin/apt'):
                system("sudo pacman -S ruby")

            system("""cd {} && git clone https://github.com/Hider5/Malicious
            cd Malicious && gem install lolcat && pip install -r requirements.txt""".format(paths))

        print(language.done.format('Malicious'))
        print(language.note_tools.format('Malicious','python2 malicious.py'))
        print(language.readmore.format('Malicious','http://bit.ly/2VHtLKP'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def tool_x(language):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(language,'Tool-X')
            print(language.installing.format('Tool-X'))
            system("""cd {} && sudo git clone https://github.com/Rajkumrdusad/Tool-X
            cd Tool-X && sudo bash install.aex""".format(paths))
            print(language.done.format('Tool-X'))
            print(language.note_tools2.format('Tool-X','Tool-X','Terminal'))

        else:
            if name == 'nt':
                print(language.doesnt_support_windows)
                print(language.wsl)

            else:
                print(language.run_well.format('Debian'))

        print(language.readmore.format('Tool-X','http://bit.ly/2ITHrfN'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def katoolin(language):
    try:
        if path.exists('/usr/bin/apt') == True:
            if path.exists('/usr/bin/katoolin') == True:
                print(language.installed.format('Katoolin'))

            else:
                paths = the_path(language,'Katoolin')
                print(language.installing.format('Katoolin'))
                system("""cd {} && sudo git clone https://github.com/LionSec/katoolin
                cd katoolin && sudo cp katoolin.py /usr/bin/katoolin
                sudo chmod +x /usr/bin/katoolin""".format(paths))
                print(language.done.format('Katoolin'))

            print(language.note_tools2.format('Katoolin','sudo katoolin','Terminal'))

        else:
            if name == 'nt':
                print(language.doesnt_support_windows)
                print(language.wsl)

            else:
                print(language.run_well.format('Debian'))

        print(language.readmore.format('Katoolin','http://bit.ly/2EXOU8G'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def intrec_pack(language):
    try:
        if path.exists('/usr/bin/apt') == True:
            paths = the_path(language,'IntRec-Pack')
            print(language.installing.format('IntRec-Pack'))
            system("cd {} && sudo git clone https://github.com/NullArray/IntRec-Pack".format(paths))
            print(language.done.format('IntRec-Pack'))
            print(language.note_tools.format('IntRec-Pack','sudo bash intrec.sh'))

        else:
            if name == 'nt':
                print(language.doesnt_support_windows)
                print(language.wsl)

            else:
                print(language.run_well.format('Debian'))

        print(language.readmore.format('IntRec-Pack','http://bit.ly/2LI9vDL'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()


def ptf(language):
    try:
        if name == 'nt':
            print(language.doesnt_support_windows)
            print(language.wsl)

        else:
            if path.exists('/usr/local/bin/ptf') == True:
                print(language.installed.format('The PenTesters Framework'))

            else:
                paths = the_path(language,'The PenTesters Framework')
                print(language.installing.format('The PenTesters Framework'))
                system("""cd {} && sudo git clone https://github.com/trustedsec/ptf
                cd ptf && sudo python2 ptf""".format(paths))
                print(language.done.format('The PenTesters Framework'))

            print(language.note_tools2.format('The PenTesters Framework','sudo ptf','Terminal'))

        print(language.readmore.format('The PenTesters Framework','http://bit.ly/2K3rsYS'))

    except KeyboardInterrupt:
        print(language.exiting)
        exit()