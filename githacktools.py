#!/usr/bin/python3

from languages import english, vietnamese
from os import system, name, path
from tools import *
from banner import *

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def continue_or_not(language):
    try:
        choice = str(input(language.continue_or_not)).strip()
        action(language,choice)
        
        if choice[0].upper() == 'Y':
            clear()
            choose_lang(language)
        elif choice[0].upper() == 'N':
            print(language.exiting)
            exit()
        elif (choice.upper() == 'HELP' or choice.upper() == 'CHANGELOG' or choice.upper() == 'ABOUT'):
            continue_or_not(language)
        else:
            print(language.invalid)
            continue_or_not(language)

    except KeyboardInterrupt:
        print(language.exiting)
        exit()
    except IndexError:
        print(language.invalid)
        continue_or_not(language)

def choose_lang(language):
    try:
        print(language.language_list)
        choice = str(input(language.choose_language.format(2))).strip()
        action(language,choice)

        if choice == '0':
            exit()
        elif choice == '1':
            clear()
            githacktools_banner(english)
            home_page(english)
        elif choice == '2':
            clear()
            githacktools_banner(vietnamese)
            home_page(vietnamese)
        elif (choice.upper() == "HELP" or choice.upper() ==  "CHANGELOG" or choice.upper() == "ABOUT"):
            choose_lang(language)
        else:
            print(language.invalid)
            choose_lang(language)

    except KeyboardInterrupt:
        print(language.exiting)
        exit()
    except IndexError:
        print(language.invalid)
        choose_lang(language)

def home_page(language):
    try:
        print(language.home_page)
        choice = str(input(language.choose_category.format(12))).strip()
        clear()
        action(language,choice)

        if choice == '0':
            print(language.exiting)
            exit()
        elif choice == '1':
            info_gathering(language)
        elif choice == '2':
            vulner_analysis(language)
        elif choice == '3':
            passwd_attack(language)
        elif choice == '4':
            wireless_attack(language)
        elif choice == '5':
            web_apps(language)
        elif choice == '6':
            exploit_tools(language)
        elif choice == '7':
            sniff_spoof(language)
        elif choice == '8':
            ddos_tools(language)
        elif choice == '9':
            malware_bypass(language)
        elif choice == '10':
            downloader_installer(language)
        elif (choice.upper() == "HELP" or choice.upper() ==  "CHANGELOG" or choice.upper() == "ABOUT"):
            home_page(language)
        else:
            print(language.invalid)
            home_page(language)

    except KeyboardInterrupt:
        print(language.exiting)
        exit()
    except IndexError:
        clear()
        print(language.invalid)
        home_page(language)

def info_gathering(language):
    try:
        print(language.info_gathering)
        tool = str(input(language.which_tools.format(35))).strip()
        clear()
        action(language,tool)

        if tool == '0':
            home_page(language)

        elif tool == '1':
            print(language.category_info_garther.format('BillCipher'))
            billcipher_banner(language)
            billcipher(language)

        elif tool == '2':
            print(language.category_info_garther.format('Leaked'))
            leaked_banner(language)
            leaked(language)

        elif tool == '3':
            print(language.category_info_garther.format('Devploit'))
            devploit_banner(language)
            devploit(language)

        elif tool == '4':
            print(language.category_info_garther.format('Gorecon'))
            gorecon_banner(language)
            gorecon(language)

        elif tool == '5':
            print(language.category_info_garther.format('Dracnmap'))
            dracnmap_banner(language)
            dracnmap(language)

        elif tool == '6':
            print(language.category_info_garther.format('Nmap'))
            nmap_banner(language)
            nmap(language)

        elif tool == '7':
            print(language.category_info_garther.format('Sublist3r'))
            sublist3r_banner(language)
            sublist3r(language)

        elif tool == '8':
            print(language.category_info_garther.format('SSLScan'))
            sslscan_banner(language)
            sslscan(language)

        elif tool == '9':
            print(language.category_info_garther.format('DNSMaper'))
            dnsmaper_banner(language)
            dnsmaper(language)

        elif tool == '10':
            print(language.category_info_garther.format('ShodanHat'))
            shondanhat_banner(language)
            shodanhat(language)

        elif tool == '11':
            print(language.category_info_garther.format('HatCloud'))
            hatcloud_banner(language)
            hatcloud(language)

        elif tool == '12':
            print(language.category_info_garther.format('A2SV'))
            a2sv_banner(language)
            a2sv(language)

        elif tool == '13':
            print(language.category_info_garther.format('Sub6'))
            sub6_banner(language)
            sub6(language)

        elif tool == '14':
            print(language.category_info_garther.format('Masscan'))
            masscan_banner(language)
            masscan(language)

        elif tool == '15':
            print(language.category_info_garther.format('dnsmap'))
            dnsmap_banner(language)
            dnsmap(language)

        elif tool == '16':
            print(language.category_info_garther.format('InfoSploit'))
            infosploit_banner(language)
            infosploit(language)

        elif tool == '17':
            print(language.category_info_garther.format('Infoga'))
            infoga_banner(language)
            infoga(language)

        elif tool == '18':
            print(language.category_info_garther.format('HTTrack'))
            httrack_banner(language)
            httrack(language)

        elif tool == '19':
            print(language.category_info_garther.format('APT2'))
            apt2_banner(language)
            apt2(language)

        elif tool == '20':
            print(language.category_info_garther.format('InSpy'))
            inspy_banner(language)
            inspy(language)

        elif tool == '21':
            print(language.category_info_garther.format('SEToolkit'))
            setoolkit_banner(language)
            setoolkit(language)

        elif tool == '22':
            print(language.category_info_garther.format('PhishX'))
            phishx_banner(language)
            phishx(language)

        elif tool == '23':
            print(language.category_info_garther.format('PhisherMan'))
            phisherman_banner(language)
            phisherman(language)

        elif tool == '24':
            print(language.category_info_garther.format('Aron'))
            aron_banner(language)
            aron(language)

        elif tool == '25':
            print(language.category_info_garther.format('Evilginx 2'))
            evilginx2_banner(language)
            evilginx2(language)

        elif tool == '26':
            print(language.category_info_garther.format('Infinity'))
            infinity_banner(language)
            infinity(language)

        elif tool == '27':
            print(language.category_info_garther.format('CredSniper'))
            credsniper_banner(language)
            credsniper(language)

        elif tool == '28':
            print(language.category_info_garther.format('Striker'))
            striker_banner(language)
            striker(language)

        elif tool == '29':
            print(language.category_info_garther.format('WAScan'))
            wascan_banner(language)
            wascan(language)

        elif tool == '30':
            print(language.category_info_garther.format('Ghost Phisher'))
            ghost_phisher_banner(language)
            ghost_phisher(language)

        elif tool == '31':
            print(language.category_info_garther.format('Breacher'))
            breacher_banner(language)
            breacher(language)

        elif tool == '32':
            print(language.category_info_garther.format('SiteBroker'))
            sitebroker_banner(language)
            sitebroker(language)

        elif tool == '33':
            print(language.category_info_garther.format('WebSploit'))
            websploit_banner(language)
            websploit(language)

        elif tool == '34':
            print(language.category_info_garther.format('Pure Blood'))
            pure_blood_banner(language)
            pure_blood(language)

        elif tool == '35':
            print(language.category_info_garther.format('Subdomain Analyzer'))
            subdomain_analyzer_banner(language)
            subdomain_analyzer(language)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            info_gathering(language)

        else:
            print(language.invalid)
            info_gathering(language)

        continue_or_not(language)

    except KeyboardInterrupt:
        print(language.exiting)
        exit()
    except IndexError:
        clear()
        print(language.invalid)
        info_gathering(language)

def vulner_analysis(language):
    try:
        print(language.vulner_analysis)
        tool = str(input(language.which_tools.format(26))).strip()
        clear()
        action(language,tool)

        if tool == '0':
            home_page(language)

        elif tool == '1':
            print(language.category_vulner_analysis.format('Nmap'))
            nmap_banner(language)
            nmap(language)

        elif tool == '2':
            print(language.category_vulner_analysis.format('SQLMap'))
            sqlmap_banner(language)
            sqlmap(language)

        elif tool == '3':
            print(language.category_vulner_analysis.format('SQLMate'))
            sqlmate_banner(language)
            sqlmate(language)

        elif tool == '4':
            print(language.category_vulner_analysis.format('SearchSploit'))
            searchsploit_banner(language)
            searchsploit(language)

        elif tool == '5':
            print(language.category_vulner_analysis.format('Brakeman'))
            brakeman_banner(language)
            brakemen(language)

        elif tool == '6':
            print(language.category_vulner_analysis.format('WhatWeb'))
            whatweb_banner(language)
            whatweb(language)

        elif tool == '7':
            print(language.category_vulner_analysis.format('vulscan'))
            vulscan_banner(language)
            vulscan(language)

        elif tool == '8':
            print(language.category_vulner_analysis.format('TakeOver'))
            takeover_banner(language)
            takeover(language)

        elif tool == '9':
            print(language.category_vulner_analysis.format('OpenVAS'))
            openvas_banner(language)
            openvas(language)

        elif tool == '10':
            print(language.category_vulner_analysis.format('Droid-Hunter'))
            droid_hunter_banner(language)
            droid_hunter(language)

        elif tool == '11':
            print(language.category_vulner_analysis.format('PatrOwl'))
            patrowl_banner(language)
            patrowl(language)

        elif tool == '12':
            print(language.category_vulner_analysis.format('Zoom'))
            zoom_banner(language)
            zoom(language)

        elif tool == '13':
            print(language.category_vulner_analysis.format('Vuls'))
            vuls_banner(language)
            vuls(language)

        elif tool == '14':
            print(language.category_vulner_analysis.format('WPSeku'))
            wpseku_banner(language)
            wpseku(language)

        elif tool == '15':
            print(language.category_vulner_analysis.format('WPScan'))
            wpscan_banner(language)
            wpscan(language)

        elif tool == '16':
            print(language.category_vulner_analysis.format('RouterSploit'))
            routersploit_banner(language)
            routersploit(language)

        elif tool == '17':
            print(language.category_vulner_analysis.format('XSStrike'))
            xsstrike_banner(language)
            xsstrike(language)

        elif tool == '18':
            print(language.category_vulner_analysis.format('Striker'))
            striker_banner(language)
            striker(language)

        elif tool == '19':
            print(language.category_vulner_analysis.format('Raptor'))
            raptor_banner(language)
            raptor(language)

        elif tool == '20':
            print(language.category_vulner_analysis.format('XSSer'))
            xsser_banner(language)
            xsser(language)

        elif tool == '21':
            print(language.category_vulner_analysis.format('Breacher'))
            breacher_banner(language)
            breacher(language)

        elif tool == '22':
            print(language.category_vulner_analysis.format('A2SV'))
            a2sv_banner(language)
            a2sv(language)

        elif tool == '23':
            print(language.category_vulner_analysis.format('BadMod'))
            badmod_banner(language)
            badmod(language)

        elif tool == '24':
            print(language.category_vulner_analysis.format('Pure Blood'))
            pure_blood_banner(language)
            pure_blood(language)

        elif tool == '25':
            print(language.category_vulner_analysis.format('Infection Monkey'))
            infection_monkey_banner(language)
            infection_monkey(language)

        elif tool == '26':
            print(language.category_vulner_analysis.format('spectre-meltdown-checker'))
            spectre_meldown_checker_banner(language)
            spectre_meldown_checker(language)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            vulner_analysis(language)

        else:
            print(language.invalid)
            vulner_analysis(language)

        continue_or_not(language)

    except KeyboardInterrupt:
        print(language.exiting)
        exit()
    except IndexError:
        clear()
        print(language.invalid)
        vulner_analysis(language)

def passwd_attack(language):
    try:
        print(language.passwd_attack)
        tool = str(input(language.which_tools.format(7))).strip()
        clear()
        action(language,tool)

        if tool == '0':
            home_page(language)

        elif tool == '1':
            print(language.category_passwd_attack.format('BruteDum'))
            brutedum_banner(language)
            brutedum(language)

        elif tool == '2':
            print(language.category_passwd_attack.format('FTPBruter'))
            ftpbruter_banner(language)
            ftpbruter(language)

        elif tool == '3':
            print(language.category_passwd_attack.format('Leaked'))
            leaked_banner(language)
            leaked(language)

        elif tool == '4':
            print(language.category_passwd_attack.format('Ncrack'))
            ncrack_banner(language)
            ncrack(language)

        elif tool == '5':
            print(language.category_passwd_attack.format('SocialBox'))
            socialbox_banner(language)
            socialbox(language)

        elif tool == '6':
            print(language.category_passwd_attack.format('Blazy'))
            blazy_banner(language)
            blazy(language)

        elif tool == '7':
            print(language.category_passwd_attack.format('Hash-Buster'))
            hash_buster_banner(language)
            hash_buster(language)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            passwd_attack(language)

        else:
            print(language.invalid)
            passwd_attack(language)

        continue_or_not(language)
    
    except KeyboardInterrupt:
        print(language.exiting)
        exit()
    except IndexError:
        clear()
        print(language.invalid)
        passwd_attack(language)

def wireless_attack(language):
    try:
        print(language.wireless_attack)
        tool = str(input(language.which_tools.format(23))).strip()
        clear()
        action(language,tool)

        if tool == '0':
            home_page(language)

        elif tool == '1':
            print(language.category_wireless_attack.format('SniffAir'))
            sniffair_banner(language)
            sniffair(language)

        elif tool == '2':
            print(language.category_wireless_attack.format('WiFi-Pumpkin'))
            wifi_pumpkin_banner(language)
            wifi_pumpkin(language)

        elif tool == '3':
            print(language.category_wireless_attack.format('Airgeddon'))
            airgeddon_banner(language)
            airgeddon(language)

        elif tool == '4':
            print(language.category_wireless_attack.format('PiKarma'))
            pikarma_banner(language)
            pikarma(language)

        elif tool == '5':
            print(language.category_wireless_attack.format('Wifite 2'))
            wifite2_banner(language)
            wifite2(language)

        elif tool == '6':
            print(language.category_wireless_attack.format('PixieWPS'))
            pixiewps_banner(language)
            pixiewps(language)

        elif tool == '7':
            print(language.category_wireless_attack.format('Fluxion'))
            fluxion_banner(language)
            fluxion(language)

        elif tool == '8':
            print(language.category_wireless_attack.format('Reaver'))
            reaver_banner(language)
            reaver(language)

        elif tool == '9':
            print(language.category_wireless_attack.format('Ghost Phisher'))
            ghost_phisher_banner(language)
            ghost_phisher(language)

        elif tool == '10':
            print(language.category_wireless_attack.format('zarp'))
            zarp_banner(language)
            zarp(language)

        elif tool == '11':
            print(language.category_wireless_attack.format('Xerosploit'))
            xerosploit_banner(language)
            xerosploit(language)

        elif tool == '12':
            print(language.category_wireless_attack.format('Seth'))
            seth_banner(language)
            seth(language)

        elif tool == '13':
            print(language.category_wireless_attack.format('KickThemOut'))
            kickthemout_banner(language)
            kickthemout(language)

        elif tool == '14':
            print(language.category_wireless_attack.format('Dracnmap'))
            dracnmap_banner(language)
            dracnmap(language)

        elif tool == '15':
            print(language.category_wireless_attack.format('Wifiphisher'))
            wifiphisher_banner(language)
            wifiphisher(language)

        elif tool == '16':
            print(language.category_wireless_attack.format('PhishX'))
            phishx_banner(language)
            phishx(language)

        elif tool == '17':
            print(language.category_wireless_attack.format('CredSniper'))
            credsniper_banner(language)
            credsniper(language)

        elif tool == '18':
            print(language.category_wireless_attack.format('shARP'))
            sharp_banner(language)
            sharp(language)

        elif tool == '19':
            print(language.category_wireless_attack.format('PhisherMan'))
            phisherman_banner(language)
            phisherman(language)

        elif tool == '20':
            print(language.category_wireless_attack.format('shARP 2'))
            sharp_2_banner(language)
            sharp_2(language)

        elif tool == '21':
            print(language.category_wireless_attack.format('EvilTwinFramework'))
            eviltwinframework_banner(language)
            eviltwinframework(language)

        elif tool == '22':
            print(language.category_wireless_attack.format('The Rogue Toolkit'))
            the_rogue_toolkit_banner(language)
            the_rogue_toolkit(language)

        elif tool == '23':
            print(language.category_wireless_attack.format('WebSploit'))
            websploit_banner(language)
            websploit(language)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            wireless_attack(language)

        else:
            print(language.invalid)
            wireless_attack(language)

        continue_or_not(language)

    except KeyboardInterrupt:
        print(language.exiting)
        exit()
    except IndexError:
        clear()
        print(language.invalid)
        wireless_attack(language)

def web_apps(language):
    try:
        print(language.web_apps)
        tool = str(input(language.which_tools.format(18))).strip()
        clear()
        action(language,tool)

        if tool == '0':
            home_page(language)

        elif tool == '1':
            print(language.category_web_apps.format('WhatWeb'))
            whatweb_banner(language)
            whatweb(language)

        elif tool == '2':
            print(language.category_web_apps.format('NoSQLMap'))
            nosqlmap_banner(language)
            nosqlmap(language)

        elif tool == '3':
            print(language.category_web_apps.format('SQLMate'))
            sqlmate_banner(language)
            sqlmate(language)

        elif tool == '4':
            print(language.category_web_apps.format('SQLMap'))
            sqlmap_banner(language)
            sqlmap(language)

        elif tool == '5':
            print(language.category_web_apps.format('sqlcake'))
            sqlcake_banner(language)
            sqlcake(language)

        elif tool == '6':
            print(language.category_web_apps.format('BSQLinjector'))
            bsqlinjector_banner(language)
            bsqlinjector(language)

        elif tool == '7':
            print(language.category_web_apps.format('XSSer'))
            xsser_banner(language)
            xsser(language)

        elif tool == '8':
            print(language.category_web_apps.format('XXeinjector'))
            xxeinjector_banner(language)
            xxeinjector(language)

        elif tool == '9':
            print(language.category_web_apps.format('XSStrike'))
            xsstrike_banner(language)
            xsstrike(language)

        elif tool == '10':
            print(language.category_web_apps.format('Striker'))
            striker_banner(language)
            striker(language)

        elif tool == '11':
            print(language.category_web_apps.format('WPScan'))
            wpscan_banner(language)
            wpscan(language)

        elif tool == '12':
            print(language.category_web_apps.format('WPSeku'))
            wpseku_banner(language)
            wpseku(language)

        elif tool == '13':
            print(language.category_web_apps.format('WAScan'))
            wascan_banner(language)
            wascan(language)

        elif tool == '14':
            print(language.category_web_apps.format('WebSploit'))
            websploit_banner(language)
            websploit(language)

        elif tool == '15':
            print(language.category_web_apps.format('WPSploit'))
            wpsploit_banner(language)
            wpsploit(language)

        elif tool == '16':
            print(language.category_web_apps.format('SiteBroker'))
            sitebroker_banner(language)
            sitebroker(language)

        elif tool == '17':
            print(language.category_web_apps.format('BadMod'))
            badmod_banner(language)
            badmod(language)

        elif tool == '18':
            print(language.category_web_apps.format('Zoom'))
            zoom_banner(language)
            zoom(language)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            web_apps(language)

        else:
            print(language.invalid)
            web_apps(language)

        continue_or_not(language)

    except KeyboardInterrupt:
        print(language.exiting)
        exit()
    except IndexError:
        clear()
        print(language.invalid)
        web_apps(language)

def exploit_tools(language):
    try:
        print(language.exploit_tools)
        tool = str(input(language.which_tools.format(32))).strip()
        clear()
        action(language,tool)

        if tool == '0':
            home_page(language)

        elif tool == '1':
            print(language.category_exploit_tools.format('roxysploit'))
            roxysploit_banner(language)
            roxysploit(language)

        elif tool == '2':
            print(language.category_exploit_tools.format('Lunar'))
            lunar_banner(language)
            lunar(language)

        elif tool == '3':
            print(language.category_exploit_tools.format('AutoRDPwn'))
            autordpwn_banner(language)
            autordpwn(language)

        elif tool == '4':
            print(language.category_exploit_tools.format('RouterSploit'))
            routersploit_banner(language)
            routersploit(language)

        elif tool == '5':
            print(language.category_exploit_tools.format('rootOS'))
            rootos_banner(language)
            rootos(language)

        elif tool == '6':
            print(language.category_exploit_tools.format('SearchSploit'))
            searchsploit_banner(language)
            searchsploit(language)

        elif tool == '7':
            print(language.category_exploit_tools.format('BSQLinjector'))
            bsqlinjector_banner(language)
            bsqlinjector(language)

        elif tool == '8':
            print(language.category_exploit_tools.format('eXpliot'))
            expliot_banner(language)
            expliot(language)

        elif tool == '9':
            print(language.category_exploit_tools.format('Pure Blood'))
            pure_blood_banner(language)
            pure_blood(language)

        elif tool == '10':
            print(language.category_exploit_tools.format('XXEinjector'))
            xxeinjector_banner(language)
            xxeinjector(language)

        elif tool == '11':
            print(language.category_exploit_tools.format('SQLMap'))
            sqlmap_banner(language)
            sqlmap(language)

        elif tool == '12':
            print(language.category_exploit_tools.format('SQLMate'))
            sqlmate_banner(language)
            sqlmate(language)

        elif tool == '13':
            print(language.category_exploit_tools.format('Termineter'))
            termineter_banner(language)
            termineter(language)

        elif tool == '14':
            print(language.category_exploit_tools.format('WebSploit'))
            websploit_banner(language)
            websploit(language)

        elif tool == '15':
            print(language.category_exploit_tools.format('sqlcake'))
            sqlcake_banner(language)
            sqlcake(language)

        elif tool == '16':
            print(language.category_exploit_tools.format('AutoSploit'))
            autosploit_banner(language)
            autosploit(language)

        elif tool == '17':
            print(language.category_exploit_tools.format('smod'))
            smod_banner(language)
            smod(language)

        elif tool == '18':
            print(language.category_exploit_tools.format('NoSQLMap'))
            nosqlmap_banner(language)
            nosqlmap(language)

        elif tool == '19':
            print(language.category_exploit_tools.format('TheFatRat'))
            thefatrat_banner(language)
            thefatrat(language)

        elif tool == '20':
            print(language.category_exploit_tools.format('Exploit Pack'))
            exploit_pack_banner(language)
            exploit_pack(language)

        elif tool == '21':
            print(language.category_exploit_tools.format('XSStrike'))
            xsstrike_banner(language)
            xsstrike(language)

        elif tool == '22':
            print(language.category_exploit_tools.format('mimikittenz'))
            mimikittenz_banner(language)
            mimikittenz(language)

        elif tool == '23':
            print(language.category_exploit_tools.format('Dracnmap'))
            dracnmap_banner(language)
            dracnmap(language)

        elif tool == '24':
            print(language.category_exploit_tools.format('XSSer'))
            xsser_banner(language)
            xsser(language)

        elif tool == '25':
            print(language.category_exploit_tools.format('ezsploit'))
            ezsploit_banner(language)
            ezsploit(language)

        elif tool == '26':
            print(language.category_exploit_tools.format('SEToolkit'))
            setoolkit_banner(language)
            setoolkit(language)

        elif tool == '27':
            print(language.category_exploit_tools.format('Auto-Root-Exploit'))
            auto_root_exploit_banner(language)
            auto_root_exploit(language)

        elif tool == '28':
            print(language.category_exploit_tools.format('AhMyth-Android-RAT'))
            ahmyth_android_rat_banner(language)
            ahmyth_android_rat(language)

        elif tool == '29':
            print(language.category_exploit_tools.format('Exploit-Framework'))
            exploit_framework_banner(language)
            exploit_framework(language)

        elif tool == '30':
            print(language.category_exploit_tools.format('WinRootHelper'))
            winroothelper_banner(language)
            winroothelper(language)

        elif tool == '31':
            print(language.category_exploit_tools.format('Metasploit Framework'))
            metasploit_banner(language)
            metasploit(language)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            exploit_tools(language)

        else:
            print(language.invalid)
            exploit_tools(language)

        continue_or_not(language)

    except KeyboardInterrupt:
        print(language.exiting)
        exit()
    except IndexError:
        clear()
        print(language.invalid)
        exploit_tools(language)

def sniff_spoof(language):
    try:
        print(language.sniff_spoof)
        tool = str(input(language.which_tools.format(8))).strip()
        clear()
        action(language,tool)

        if tool == '0':
            home_page(language)

        elif tool == '1':
            print(language.category_sniff_spoof.format('Airgeddon'))
            airgeddon_banner(language)
            airgeddon(language)

        elif tool == '2':
            print(language.category_sniff_spoof.format('Xerosploit'))
            xerosploit_banner(language)
            xerosploit(language)

        elif tool == '3':
            print(language.category_sniff_spoof.format('WebSploit'))
            websploit_banner(language)
            websploit(language)

        elif tool == '4':
            print(language.category_sniff_spoof.format('SniffAir'))
            sniffair_banner(language)
            sniffair(language)

        elif tool == '5':
            print(language.category_sniff_spoof.format('The Rogue Toolkit'))
            the_rogue_toolkit_banner(language)
            the_rogue_toolkit(language)

        elif tool == '6':
            print(language.category_sniff_spoof.format('zarp'))
            zarp_banner(language)
            zarp(language)

        elif tool == '7':
            print(language.category_sniff_spoof.format('WiFi-Pumpkin'))
            wifi_pumpkin_banner(language)
            wifi_pumpkin(language)

        elif tool == '8':
            print(language.category_sniff_spoof.format('Seth'))
            seth_banner(language)
            seth(language)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            sniff_spoof(language)

        else:
            print(language.invalid)
            sniff_spoof(language)

        continue_or_not(language)

    except KeyboardInterrupt:
        print(language.exiting)
        exit()
    except IndexError:
        clear()
        print(language.invalid)
        sniff_spoof(language)

def malware_bypass(language):
    try:
        print(language.malware_bypass)
        tool = str(input(language.which_tools.format(21))).strip()
        clear()
        action(language,tool)

        if tool == '0':
            home_page(language)

        elif tool == '1':
            print(language.category_malware_bypass.format('ZeroDoor'))
            zerodoor_banner(language)
            zerodoor(language)

        elif tool == '2':
            print(language.category_malware_bypass.format('Terminator'))
            terminator_banner(language)
            terminator(language)

        elif tool == '3':
            print(language.category_malware_bypass.format('WinPayloads'))
            winpayload_banner(language)
            winpayloads(language)

        elif tool == '4':
            print(language.category_malware_bypass.format('sAINT'))
            saint_banner(language)
            saint(language)

        elif tool == '5':
            print(language.category_malware_bypass.format('BeeLogger'))
            beelogger_banner(language)
            beelogger(language)

        elif tool == '6':
            print(language.category_malware_bypass.format('HackTheWorld'))
            hacktheworld_banner(language)
            hacktheworld(language)

        elif tool == '7':
            print(language.category_malware_bypass.format('HatKey'))
            hatkey_banner(language)
            hatkey(language)

        elif tool == '8':
            print(language.category_malware_bypass.format('ezsploit'))
            ezsploit_banner(language)
            ezsploit(language)

        elif tool == '9':
            print(language.category_malware_bypass.format('trolo'))
            trolo_banner(language)
            trolo(language)

        elif tool == '10':
            print(language.category_malware_bypass.format('GetWin'))
            getwin_banner(language)
            getwin(language)

        elif tool == '11':
            print(language.category_malware_bypass.format('The Fat Rat'))
            thefatrat_banner(language)
            thefatrat(language)

        elif tool == '12':
            print(language.category_malware_bypass.format('DKMC'))
            dkmc_banner(language)
            dkmc(language)

        elif tool == '13':
            print(language.category_malware_bypass.format('Parat'))
            parat_banner(language)
            parat(language)

        elif tool == '14':
            print(language.category_malware_bypass.format('mkvenom'))
            mkvenom_banner(language)
            mkvenom(language)

        elif tool == '15':
            print(language.category_malware_bypass.format('venom'))
            venom_banner(language)
            venom(language)

        elif tool == '16':
            print(language.category_malware_bypass.format('Metasploit Framework'))
            metasploit_banner(language)
            metasploit(language)

        elif tool == '17':
            print(language.category_malware_bypass.format('Cloak'))
            cloak_banner(language)
            cloak(language)

        elif tool == '18':
            print(language.category_malware_bypass.format('Metasploit AV Evasion'))
            avoid_banner(language)
            avoid(language)

        elif tool == '19':
            print(language.category_malware_bypass.format('AVET'))
            avet_banner(language)
            avet(language)

        elif tool == '20':
            print(language.category_malware_bypass.format('AhMyth-Android-RAT'))
            ahmyth_android_rat_banner(language)
            ahmyth_android_rat(language)

        elif tool == '21':
            print(language.category_malware_bypass.format('NXcrypt'))
            nxcrypt_banner(language)
            nxcrypt(language)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            malware_bypass(language)

        else:
            print(language.invalid)
            malware_bypass(language)

        continue_or_not(language)

    except KeyboardInterrupt:
        print(language.exiting)
        exit()

    except IndexError:
        clear()
        print(language.invalid)
        malware_bypass(language)

def ddos_tools(language):
    try:
        print(language.ddos_tools)
        tool = str(input(language.which_tools.format(7))).strip()
        clear()
        action(language,tool)

        if tool == '0':
            home_page(language)

        elif tool == '1':
            print(language.category_ddos_tools.format('SlowLoris'))
            slowloris_banner(language)
            slowloris(language)

        elif tool == '2':
            print(language.category_ddos_tools.format('ZAmbIE'))
            zambie_banner(language)
            zambie(language)

        elif tool == '3':
            print(language.category_ddos_tools.format('Airgeddon'))
            airgeddon_banner(language)
            airgeddon(language)

        elif tool == '4':
            print(language.category_ddos_tools.format('WebSploit'))
            websploit_banner(language)
            websploit(language)

        elif tool == '5':
            print(language.category_ddos_tools.format('UFONet'))
            ufonet_banner(language)
            ufonet(language)

        elif tool == '6':
            print(language.category_ddos_tools.format('zarp'))
            zarp_banner(language)
            zarp(language)

        elif tool == '7':
            print(language.category_ddos_tools.format('Memcrashed-DDoS-Exploit'))
            memcrashed_banner(language)
            memcrashed(language)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            ddos_tools(language)

        else:
            clear()
            print(language.invalid)
            ddos_tools(language)

        continue_or_not(language)

    except KeyboardInterrupt:
        print(language.exiting)
        exit()
    except IndexError:
        clear()
        print(language.invalid)
        ddos_tools(language)

def downloader_installer(language):
    try:
        print(language.downloader_installer)
        tool = str(input(language.which_tools.format(8))).strip()
        clear()
        action(language,tool)

        if tool == '0':
            home_page(language)

        elif tool == '1':
            print(language.category_downloader_installer.format('Fsociety'))
            fsociety_banner(language)
            fsociety(language)

        elif tool == '2':
            print(language.category_downloader_installer.format('Malicious'))
            malicious_banner(language)
            malicious(language)

        elif tool == '3':
            print(language.category_downloader_installer.format('Tool-X'))
            tool_x_banner(language)
            tool_x(language)

        elif tool == '4':
            print(language.category_downloader_installer.format('Katoolin'))
            katoolin_banner(language)
            katoolin(language)

        elif tool == '5':
            print(language.category_downloader_installer.format('IntRec-Pack'))
            intrec_pack_banner(language)
            intrec_pack(language)

        elif tool == '6':
            print(language.category_downloader_installer.format('ZAmbIE'))
            zambie_banner(language)
            zambie(language)

        elif tool == '7':
            print(language.category_downloader_installer.format('The PenTesters Framework'))
            ptf_banner(language)
            ptf(language)

        elif tool == '8':
            print(language.category_downloader_installer.format('Lunar'))
            lunar_banner(language)
            lunar(language)

        elif (tool.upper() == 'HELP' or tool.upper() == 'CHANGELOG' or tool.upper() == 'ABOUT'):
            downloader_installer(language)

        else:
            clear()
            print(language.invalid)
            downloader_installer(language)

        continue_or_not(language)

    except KeyboardInterrupt:
        print(language.exiting)
        exit()
    except IndexError:
        clear()
        print(language.invalid)
        downloader_installer(language)

action(english,"LANG")