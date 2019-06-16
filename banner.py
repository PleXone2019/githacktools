#!/usr/bin/python3

from languages import english, vietnamese, Color

def githacktools_banner(language):
    print(Color.white+"""   ___ _ _                    _    _____            _
  / _ (_) |_  /\  /\__ _  ___| | _/__   \___   ___ | |___
 / /_\/ | __|/ /_/ / _` |/ __| |/ / / /\/ _ \ / _ \| / __|
/ /_\\\| | |_/ __  / (_| | (__|   < / / | (_) | (_) | \__ \ 
\____/|_|\__\/ /_/ \__,_|\___|_|\_\\\/   \___/ \___/|_|___/ 0.1""")
    sticks = len(language.githacktools_description) * '-'
    print(sticks)
    print(language.githacktools_description)
    print(sticks)

def billcipher_banner(language):
    print(Color.yellow+"""
######                   #####                                
#     # # #      #      #     # # #####  #    # ###### #####  
#     # # #      #      #       # #    # #    # #      #    # 
######  # #      #      #       # #    # ###### #####  #    # 
#     # # #      #      #       # #####  #    # #      #####  
#     # # #      #      #     # # #      #    # #      #   #  
######  # ###### ######  #####  # #      #    # ###### #    #"""+Color.white)
    sticks = len(language.billcipher_description) * '-'
    print(sticks)
    print(language.billcipher_description)
    print(sticks,'\n')


def leaked_banner(language):
    print(Color.yellow+""" ___       _______   ________  ___  __    _______   ________  ________      
|\  \     |\  ___ \ |\   __  \|\  \|\  \ |\  ___ \ |\   ___ \|\_____  \     
\ \  \    \ \   __/|\ \  \|\  \ \  \/  /|\ \   __/|\ \  \_|\ \|____|\  \    
 \ \  \    \ \  \_|/_\ \   __  \ \   ___  \ \  \_|/_\ \  \ \\ \    \ \__\   
  \ \  \____\ \  \_|\ \ \  \ \  \ \  \\ \  \ \  \_|\ \ \  \_\\ \    \|__|   
   \ \_______\ \_______\ \__\ \__\ \__\\ \__\ \_______\ \_______\       ___ 
    \|_______|\|_______|\|__|\|__|\|__| \|__|\|_______|\|_______|      |\__\\"""+Color.white)

    sticks = len(language.leaked_description) * '-'
    print(sticks)
    print(language.leaked_description)
    print(sticks,'\n')


def devploit_banner(language):
    print(Color.white+"""    ______                 _       _ _   
    |  _  \               | |     (_) |  
    | | | |_____   ___ __ | | ___  _| |_ 
    | | | / _ \ \ / / '_ \| |/ _ \| | __|
    | |/ /  __/\ V /| |_) | | (_) | | |_ 
    |___/ \___| \_/ | .__/|_|\___/|_|\__|
                    | |
                    |_|""")

    sticks = len(language.devploit_description) * '-'
    print(sticks)
    print(language.devploit_description)
    print(sticks,'\n')


def gorecon_banner(language):
    print(Color.red+"""
██████╗  ██████╗ ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██║  ███╗██║   ██║██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██║   ██║██║   ██║██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
╚██████╔╝╚██████╔╝██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝"""+Color.white)

    sticks = len(language.gorecon_description) * '-'
    print(sticks)
    print(language.gorecon_description)
    print(sticks,'\n')


def dracnmap_banner(language):
    print(Color.green+"""________                                                    
\______ \____________    ____   ____   _____ _____  ______  
 |    |  \_  __ \__  \ _/ ___\ /    \ /     \\\__  \ \____ \ 
 |    `   \  | \// __ \\\  \___|   |  \  Y Y  \/ __ \|  |_> >
/_______  /__|  (____  /\___  >___|  /__|_|  (____  /   __/ 
        \/           \/     \/     \/      \/     \/|__|"""+Color.white)
    sticks = len(language.dracnmap_description) * '-'
    print(sticks)
    print(language.dracnmap_description)
    print(sticks,'\n')


def nmap_banner(language):
    print(Color.white+"""    _   __
   / | / /___ ___  ____ _____ 
  /  |/ / __ `__ \/ __ `/ __ \ 
 / /|  / / / / / / /_/ / /_/ /
/_/ |_/_/ /_/ /_/\__,_/ .___/ 
                     /_/""")
    sticks = len(language.nmap_description) * '-'
    print(sticks)
    print(language.nmap_description)
    print(sticks,'\n')

def sublist3r_banner(language):
    print(Color.red+"""     ____        _     _ _     _   _____
    / ___| _   _| |__ | (_)___| |_|___ / _ __
    \___ \| | | | '_ \| | / __| __| |_ \| '__|
     ___) | |_| | |_) | | \__ \ |_ ___) | |
    |____/ \__,_|_.__/|_|_|___/\__|____/|_|"""+Color.white)
    sticks = len(language.sublist3r_description) * '-'
    print(sticks)
    print(language.sublist3r_description)
    print(sticks,'\n')

def sslscan_banner(language):
    print(Color.white+"""         _
 ___ ___| |___  ___ __ _ _ __
/ __/ __| / __|/ __/ _` | '_ \ 
\__ \__ \ \__ \ (_| (_| | | | |
|___/___/_|___/\___\__,_|_| |_|""")
    sticks = len(language.sslscan_description) * '-'
    print(sticks)
    print(language.sslscan_description)
    print(sticks,'\n')

def dnsmaper_banner(language):
    print(Color.white+""" ____  _   _ ____  __  __
|  _ \| \ | / ___||  \/  | __ _ _ __   ___ _ __
| | | |  \| \___ \| |\/| |/ _` | '_ \ / _ \ '__|
| |_| | |\  |___) | |  | | (_| | |_) |  __/ |
|____/|_| \_|____/|_|  |_|\__,_| .__/ \___|_|
                               |_|""")
    sticks = len(language.dnsmaper_description) * '-'
    print(sticks)
    print(language.dnsmaper_description)
    print(sticks,'\n')

def a2sv_banner(language):
    print(Color.white+"""                                
 █████╗ ██████╗ ███████╗██╗   ██╗   A_A
██╔══██╗╚════██╗██╔════╝██║   ██║  (-.-)
███████║ █████╔╝███████╗██║   ██║  /   h
██╔══██║██╔═══╝ ╚════██║╚██╗ ██╔╝ |     |   __
██║  ██║███████╗███████║ ╚████╔╝  |  || |  |  t__  
╚═╝  ╚═╝╚══════╝╚══════╝  ╚═══╝    t_|| /_/""")
    sticks = len(language.a2sv_description) * '-'
    print(sticks)
    print(language.a2sv_description)
    print(sticks,'\n')

def shondanhat_banner(language):
    print(Color.green+"""
███████╗██╗  ██╗ ██████╗ ██████╗  █████╗ ███╗   ██╗██╗  ██╗ █████╗ ████████╗
██╔════╝██║  ██║██╔═══██╗██╔══██╗██╔══██╗████╗  ██║██║  ██║██╔══██╗╚══██╔══╝
███████╗███████║██║   ██║██║  ██║███████║██╔██╗ ██║███████║███████║   ██║   
╚════██║██╔══██║██║   ██║██║  ██║██╔══██║██║╚██╗██║██╔══██║██╔══██║   ██║   
███████║██║  ██║╚██████╔╝██████╔╝██║  ██║██║ ╚████║██║  ██║██║  ██║   ██║   
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝"""+Color.white)
    sticks = len(language.shodanhat_description) * '-'
    print(sticks)
    print(language.shodanhat_description)
    print(sticks,'\n')

def hatcloud_banner(language):
    print(Color.white+"""
██╗  ██╗ █████╗ ████████╗     ██████╗██╗      ██████╗ ██╗   ██╗██████╗ 
██║  ██║██╔══██╗╚══██╔══╝    ██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗
███████║███████║   ██║       ██║     ██║     ██║   ██║██║   ██║██║  ██║
██╔══██║██╔══██║   ██║       ██║     ██║     ██║   ██║██║   ██║██║  ██║
██║  ██║██║  ██║   ██║       ╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝""")
    sticks = len(language.hatcloud_description) * '-'
    print(sticks)
    print(language.hatcloud_description)
    print(sticks,'\n')

def sub6_banner(language):
    print(Color.red+"""   _________    ___.     ________
  /   _____/__ _\_ |__  /  _____/
  \_____  \|  |  \ __ \/   __  \   
  /        \  |  / \_\ \  |__\  \  
 /_______  /____/|___  /\_____  /
         \/          \/       \/"""+Color.white)
    sticks = len(language.sub6_description) * '-'
    print(sticks)
    print(language.sub6_description)
    print(sticks,'\n')

def masscan_banner(language):
    print(Color.white+""" __  __    _    ____ ____   ____    _    _   _ 
|  \/  |  / \  / ___/ ___| / ___|  / \  | \ | |
| |\/| | / _ \ \___ \___ \| |     / _ \ |  \| |
| |  | |/ ___ \ ___) |__) | |___ / ___ \| |\  |
|_|  |_/_/   \_\____/____/ \____/_/   \_\_| \_|""")
    sticks = len(language.masscan_description) * '-'
    print(sticks)
    print(language.masscan_description)
    print(sticks, '\n')

def dnsmap_banner(language):
    print(Color.white+"""     _                                 
  __| |_ __  ___ _ __ ___   __ _ _ __  
 / _` | '_ \/ __| '_ ` _ \ / _` | '_ \ 
| (_| | | | \__ \ | | | | | (_| | |_) |
 \__,_|_| |_|___/_| |_| |_|\__,_| .__/ 
                                |_|""")
    sticks = len(language.dnsmap_description) * '-'
    print(sticks)
    print(language.dnsmap_description)
    print(sticks, '\n')

def infosploit_banner(language):
    print(Color.blue+"""    ____      ____     _____       __      _ __ 
   /  _/___  / __/___ / ___/____  / /___  (_) /_
   / // __ \/ /_/ __ \\\__ \/ __ \/ / __ \/ / __/
 _/ // / / / __/ /_/ /__/ / /_/ / / /_/ / / /_  
/___/_/ /_/_/  \____/____/ .___/_/\____/_/\__/"""+Color.white)
    sticks = len(language.infosploit_description) * '-'
    print(sticks)
    print(language.infosploit_description)
    print(sticks,'\n')

def infoga_banner(language):
    print(Color.white+"""    ____      ____                 
   /  _/___  / __/___  ____ _____ _
   / // __ \/ /_/ __ \/ __ `/ __ `/
 _/ // / / / __/ /_/ / /_/ / /_/ / 
/___/_/ /_/_/  \____/\__, /\__,_/  
                    /____/""")
    sticks = len(language.infoga_description) * '-'
    print(sticks)
    print(language.infoga_description)
    print(sticks,'\n')

def httrack_banner(language):
    print(Color.white+""" _   _ _____ _____               _    
| | | |_   _|_   _| __ __ _  ___| | __
| |_| | | |   | || '__/ _` |/ __| |/ /
|  _  | | |   | || | | (_| | (__|   < 
|_| |_| |_|   |_||_|  \__,_|\___|_|\_\ """)
    sticks = len(language.httrack_description) * '-'
    print(sticks)
    print(language.httrack_description)
    print(sticks,'\n')

def apt2_banner(language):
    print(Color.white+"""       dM.    `MMMMMMMb. MMMMMMMMMM      
      ,MMb     MM    `Mb /   MM   \      
      d'YM.    MM     MM     MM   ____   
     ,P `Mb    MM     MM     MM  6MMMMb  
     d'  YM.   MM    .M9     MM MM'  `Mb 
    ,P   `Mb   MMMMMMM9'     MM      ,MM 
    d'    YM.  MM            MM     ,MM' 
   ,MMMMMMMMb  MM            MM   ,M'    
   d'      YM. MM            MM ,M'      
 _dM_     _dMM_MM_          _MM_MMMMMMMM""")
    sticks = len(language.apt2_description) * '-'
    print(sticks)
    print(language.apt2_description)
    print(sticks,'\n')

def inspy_banner(language):
    print(Color.white+"""  ___        ____              
 |_ _|_ __  /____| _ __  _   _ 
  | || '_ \ \___ \| '_ \| | | |
  | || | | | ___) | |_) | |_| |
 |___|_| |_||____/| .__/ \__, |
                  |_|    |___/ """)
    sticks = len(language.inspy_description) * '-'
    print(sticks)
    print(language.inspy_description)
    print(sticks,'\n')

def setoolkit_banner(language):
    print(Color.white+""" _____ _____ _____         _ _   _ _   
|   __|   __|_   _|___ ___| | |_|_| |_ 
|__   |   __| | | | . | . | | '_| |  _|
|_____|_____| |_| |___|___|_|_,_|_|_|""")
    sticks = len(language.setoolkit_description) * '-'
    print(sticks)
    print(language.setoolkit_description)
    print(sticks,'\n')

def ghost_phisher_banner(language):
    print(Color.white+"""  ____ _               _   ____  _     _     _               
 / ___| |__   ___  ___| |_|  _ \| |__ (_)___| |__   ___ _ __ 
| |  _| '_ \ / _ \/ __| __| |_) | '_ \| / __| '_ \ / _ \ '__|
| |_| | | | | (_) \__ \ |_|  __/| | | | \__ \ | | |  __/ |   
 \____|_| |_|\___/|___/\__|_|   |_| |_|_|___/_| |_|\___|_|""")
    sticks = len(language.ghost_phisher_description) * '-'
    print(sticks)
    print(language.ghost_phisher_description)
    print(sticks,'\n')

def phishx_banner(language):
    print(Color.white+"""    #################################"
                -PHISHX- "
    #################################"
        [+]: MADE BY WEEBSEC :[+]"
    #################################""")
    sticks = len(language.phishx_description) * '-'
    print(sticks)
    print(language.phishx_description)
    print(sticks,'\n')

def phisherman_banner(language):
    print(Color.blue+""" _______         _________ _______         _______ _______    _______ _______ _         
(  ____ )\     /|\__   __/(  ____ \\\     /|  ____ \  ____ )  (       )  ___  ) (    /|  
| (    )| )   ( |   ) (   | (    \/ )   ( | (    \/ (    )|  | () () | (   ) |  \  ( |  
| (____)| (___) |   | |   | (_____| (___) | (__   | (____)|  | || || | (___) |   \ | |  
|  _____)  ___  |   | |   (_____  )  ___  |  __)  |     __)  | |(_)| |  ___  | (\ \) |  
| (     | (   ) |   | |         ) | (   ) | (     | (\ (     | |   | | (   ) | | \   |  
| )     | )   ( |___) (___/\____) | )   ( | (____/\ ) \ \__  | )   ( | )   ( | )  \  |  
|/      |/     \|\_______/\_______)/     \|_______//   \__/  |/     \|/     \|/    )_)"""+Color.white)
    sticks = len(language.phisherman_description) * '-'
    print(sticks)
    print(language.phisherman_description)
    print(sticks,'\n')

def aron_banner(language):
    print(Color.green+"""    ___                                         
   /   |  _________  ___ 
  / /| | / ___/ __ \\/ __\\
 / ___ |/ /  / /_/ / / / /
/_/  |_/_/   \\____/_/ /_/"""+Color.white)
    sticks = len(language.aron_description) * '-'
    print(sticks)
    print(language.aron_description)
    print(sticks,'\n')

def evilginx2_banner(language):
    print(Color.white+"""___________     .__.__          .__               
\_   _____/__  _|__|  |    ____ |__| ____ ___  ___ 
 |    __)_\  \/ /  |  |   / ___\|  |/    \\\  \/  / 
 |        \\\   /|  |  |__/ /_/  >  |   |  \>    <  
/_______  / \_/ |__|____/\___  /|__|___|  /__/\_ \ 
        \/              /_____/         \/      \/""")
    sticks = len(language.evilginx2_description) * '-'
    print(sticks)
    print(language.evilginx2_description)
    print(sticks,'\n')

def infinity_banner(language):
    print("""  .      _ .     . ___
  | |\| /- | |\| |  |  `/
                       /""")
    sticks = len(language.infinity_description) * '-'
    print(sticks)
    print(language.infinity_description)
    print(sticks,'\n')

def credsniper_banner(language):
    print(Color.white+"""  ____              _ ____        _                 
 / ___|_ __ ___  __| / ___| _ __ (_)_ __   ___ _ __ 
| |   | '__/ _ \/ _` \___ \| '_ \| | '_ \ / _ \ '__|
| |___| | |  __/ (_| |___) | | | | | |_) |  __/ |   
 \____|_|  \___|\__,_|____/|_| |_|_| .__/ \___|_|   
                                   |_|""")
    sticks = len(language.credsniper_description) * '-'
    print(sticks)
    print(language.credsniper_description)
    print(sticks,'\n')

def subdomain_analyzer_banner(language):
    print(Color.white+""" ____        _     ____                        _          _                _                    
/ ___| _   _| |__ |  _ \  ___  _ __ ___   __ _(_)_ __    / \   _ __   __ _| |_   _ _______ _ __ 
\___ \| | | | '_ \| | | |/ _ \| '_ ` _ \ / _` | | '_ \  / _ \ | '_ \ / _` | | | | |_  / _ \ '__|
 ___) | |_| | |_) | |_| | (_) | | | | | | (_| | | | | |/ ___ \| | | | (_| | | |_| |/ /  __/ |   
|____/ \__,_|_.__/|____/ \___/|_| |_| |_|\__,_|_|_| |_/_/   \_\_| |_|\__,_|_|\__, /___\___|_|   
                                                                             |___/""")
    sticks = len(language.subdomain_analyzer_description) * '-'
    print(sticks)
    print(language.subdomain_analyzer_description)
    print(sticks,'\n')

def sqlmap_banner(language):
    print(Color.white+"""        ___
       __H__
 ___ ___[.]_____ ___ ___  
|_ -| . ["]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   """)
    sticks = len(language.sqlmap_description) * '-'
    print(sticks)
    print(language.sqlmap_description)
    print(sticks,'\n')

def sqlmate_banner(language):
    print(Color.white+"""        _H_          _       
 ___ ___|.|_____ ___| |_ ___ 
|_ -| . |.|     | .'|  _| -_|
|___|_  |.|_|_|_|__,|_| |___|
      |_|V""")
    sticks = len(language.sqlmate_description) * '-'
    print(sticks)
    print(language.sqlmate_description)
    print(sticks,'\n')

def searchsploit_banner(language):
    print(Color.white+""" ____                      _     ____        _       _ _   
/ ___|  ___  __ _ _ __ ___| |__ / ___| _ __ | | ___ (_) |_ 
\___ \ / _ \/ _` | '__/ __| '_ \\\___ \| '_ \| |/ _ \| | __|
 ___) |  __/ (_| | | | (__| | | |___) | |_) | | (_) | | |_ 
|____/ \___|\__,_|_|  \___|_| |_|____/| .__/|_|\___/|_|\__|
                                      |_|""")
    sticks = len(language.searchsploit_description) * '-'
    print(sticks)
    print(language.searchsploit_description)
    print(sticks,'\n')

def brakeman_banner(language):
    print(Color.white+""" ____            _                              
| __ ) _ __ __ _| | _____ _ __ ___   __ _ _ __  
|  _ \| '__/ _` | |/ / _ \ '_ ` _ \ / _` | '_ \ 
| |_) | | | (_| |   <  __/ | | | | | (_| | | | |
|____/|_|  \__,_|_|\_\___|_| |_| |_|\__,_|_| |_|""")
    sticks = len(language.brakeman_description) * '-'
    print(sticks)
    print(language.brakeman_description)
    print(sticks,'\n')

def whatweb_banner(language):
    print(Color.white+""".$$$     $.                                   .$$$     $.         
$$$$     $$. .$$$  $$$ .$$$$$$.  .$$$$$$$$$$. $$$$     $$. .$$$$$$$. .$$$$$$. 
$ $$     $$$ $ $$  $$$ $ $$$$$$. $$$$$ $$$$$$ $ $$     $$$ $ $$   $$ $ $$$$$$.
$ `$     $$$ $ `$  $$$ $ `$  $$$ $$' $ `$ `$$ $ `$     $$$ $ `$      $ `$  $$$'
$. $     $$$ $. $$$$$$ $. $$$$$$ `$  $. $  :' $. $     $$$ $. $$$$   $. $$$$$.
$::$  .  $$$ $::$  $$$ $::$  $$$     $::$     $::$  .  $$$ $::$      $::$  $$$$
$;;$ $$$ $$$ $;;$  $$$ $;;$  $$$     $;;$     $;;$ $$$ $$$ $;;$      $;;$  $$$$
$$$$$$ $$$$$ $$$$  $$$ $$$$  $$$     $$$$     $$$$$$ $$$$$ $$$$$$$$$ $$$$$$$$$'""")
    sticks = len(language.whatweb_description) * '-'
    print(sticks)
    print(language.whatweb_description)
    print(sticks,'\n')

def vulscan_banner(language):
    print(Color.white+"""             _                     
__   ___   _| |___  ___ __ _ _ __  
\ \ / / | | | / __|/ __/ _` | '_ \ 
 \ V /| |_| | \__ \ (_| (_| | | | |
  \_/  \__,_|_|___/\___\__,_|_| |_|""")
    sticks = len(language.vulscan_description) * '-'
    print(sticks)
    print(language.vulscan_description)
    print(sticks,'\n')

def takeover_banner(language):
    print(Color.white+"""   /~\ 
  C oo   ---------------
 _( ^)  |T|A|K|E|O|V|E|R|
/   ~\  ----------------""")
    sticks = len(language.takeover_description) * '-'
    print(sticks)
    print(language.takeover_description)
    print(sticks,'\n')

def openvas_banner(language):
    print(Color.white+"""   ____                 _    _____   _____
  / __ \____  ___  ____| |  / /   | / ___/
 / / / / __ \/ _ \/ __ \ | / / /| | \__ \ 
/ /_/ / /_/ /  __/ / / / |/ / ___ |___/ / 
\____/ .___/\___/_/ /_/|___/_/  |_/____/  
    /_/""")
    sticks = len(language.openvas_description) * '-'
    print(sticks)
    print(language.openvas_description)
    print(sticks,'\n')

def droid_hunter_banner(language):
    print(Color.white+"""╔╦╗╦═╗╔═╗╦╔╦╗   ╦ ╦╦ ╦╔╗╔╔╦╗╔═╗╦═╗
 ║║╠╦╝║ ║║ ║║───╠═╣║ ║║║║ ║ ║╣ ╠╦╝
═╩╝╩╚═╚═╝╩═╩╝   ╩ ╩╚═╝╝╚╝ ╩ ╚═╝╩╚═""")
    sticks = len(language.droid_hunter_description) * '-'
    print(sticks)
    print(language.droid_hunter_description)
    print(sticks,'\n')

def patrowl_banner(language):
    print(Color.white+""" ____       _         ___           _ 
|  _ \ __ _| |_ _ __ / _ \__      _| |
| |_) / _` | __| '__| | | \ \ /\ / / |
|  __/ (_| | |_| |  | |_| |\ V  V /| |
|_|   \__,_|\__|_|   \___/  \_/\_/ |_|""")
    sticks = len(language.patrowl_description) * '-'
    print(sticks)
    print(language.patrowl_description)
    print(sticks,'\n')

def infection_monkey_banner(language):
    print(Color.white+""" _____     ___         _   _         _____         _           
|     |___|  _|___ ___| |_|_|___ ___|     |___ ___| |_ ___ _ _ 
|-   -|   |  _| -_|  _|  _| | . |   | | | | . |   | '_| -_| | |
|_____|_|_|_| |___|___|_| |_|___|_|_|_|_|_|___|_|_|_,_|___|_  |
                                                          |___|""")
    sticks = len(language.infection_monkey_description) * '-'
    print(sticks)
    print(language.infection_monkey_description)
    print(sticks,'\n')

def vuls_banner(language):
    print(Color.white+"""____   ____    .__          
\   \ /   /_ __|  |   ______
 \   Y   /  |  \  |  /  ___/
  \     /|  |  /  |__\___ \ 
   \___/ |____/|____/____  >
                         \/""")
    sticks = len(language.vuls_description) * '-'
    print(sticks)
    print(language.vuls_description)
    print(sticks,'\n')

def wpseku_banner(language):
    print(Color.white+"""                   _       
 _ _ _ ___ ___ ___| |_ _ _ 
| | | | . |_ -| -_| '_| | |
|_____|  _|___|___|_,_|___|
      |_|""")
    sticks = len(language.wpseku_description) * '-'
    print(sticks)
    print(language.wpseku_description)
    print(sticks,'\n')

def wpscan_banner(language):
    print(Color.white+"""__          _______   _____
\ \        / /  __ \ / ____|
 \ \  /\  / /| |__) | (___   ___  __ _ _ __
  \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \ 
   \  /\  /  | |     ____) | (__| (_| | | | |
    \/  \/   |_|    |_____/ \___|\__,_|_| |_|""")
    sticks = len(language.wpscan_description) * '-'
    print(sticks)
    print(language.wpscan_description)
    print(sticks,'\n')

def routersploit_banner(language):
    print(Color.white+"""______            _            _____       _       _ _
| ___ \          | |          /  ___|     | |     (_) |
| |_/ /___  _   _| |_ ___ _ __\ `--. _ __ | | ___  _| |_
|    // _ \| | | | __/ _ \ '__|`--. \ '_ \| |/ _ \| | __|
| |\ \ (_) | |_| | ||  __/ |  /\__/ / |_) | | (_) | | |_
\_| \_\___/ \__,_|\__\___|_|  \____/| .__/|_|\___/|_|\__|
                                     | |
                                     |_|""")
    sticks = len(language.routersploit_description) * '-'
    print(sticks)
    print(language.routersploit_description)
    print(sticks,'\n')

def xsstrike_banner(language):
    print(Color.white+"""____  ___  _________ _________ __         .__ __           
\   \/  / /   _____//   _____//  |________|__|  | __ ____  
"""+Color.red+""" \     /  \_____  \ \_____  \\\   __\_  __ \  |  |/ // __ \ 
 /     \  /        \/        \|  |  |  | \/  |    <\  ___/"""+Color.white+""" 
/___/\  \/_______  /_______  /|__|  |__|  |__|__|_ \\\___  >
      \_/        \/        \/                     \/    \/""")
    sticks = len(language.xsstrike_description) * '-'
    print(sticks)
    print(language.xsstrike_description)
    print(sticks,'\n')

def striker_banner(language):
    print(Color.red+"""  _________ __         .__ __                 
 /   _____//  |________|__|  | __  ___________ 
 \_____  \\\   __\_  __ \  |  |/ / / __ \_  __ \ 
 /        \|  |  |  | \/  |    < \  ___/|  | \/
/_______  /|__|  |__|  |__|__|_ \ \___  >__|   
        \/                     \/    \/""")
    sticks = len(language.striker_description) * '-'
    print(sticks)
    print(language.striker_description)
    print(sticks,'\n')

def raptor_banner(language):
    print(Color.white+"""__________                __                
\______   \_____  _______/  |_  ___________ 
 |       _/\__  \ \____ \   __\/  _ \_  __ \ 
 |    |   \ / __ \|  |_> >  | (  <_> )  | \/
 |____|_  /(____  /   __/|__|  \____/|__|   
        \/      \/|__|""")
    sticks = len(language.raptor_description) * '-'
    print(sticks)
    print(language.raptor_description)
    print(sticks,'\n')

def breacher_banner(language):
    print(Color.blue+"""______   ______ _______ _______ _______ _     _ _______  ______
|_____] |_____/ |______ |_____| |       |_____| |______ |_____/
|_____] |    \_ |______ |     | |_____  |     | |______ |    \_"""+Color.white)
    sticks = len(language.breacher_description) * '-'
    print(sticks)
    print(language.breacher_description)
    print(sticks,'\n')

def wascan_banner(language):
    print(Color.white+""" _ _ _ _____ _____             
| | | |  _  |   __|___ ___ ___ 
| | | |     |__   |  _| .'|   |
|_____|__|__|_____|___|__,|_|_|""")
    sticks = len(language.wascan_description) * '-'
    print(sticks)
    print(language.wascan_description)
    print(sticks,'\n')

def xsser_banner(language):
    print(Color.white+""" __  ______ ____            
 \ \/ / ___/ ___|  ___ _ __ 
  \  /\___ \___ \ / _ \ '__|
  /  \ ___) |__) |  __/ |   
 /_/\_\____/____/ \___|_|""")
    sticks = len(language.xsser_description) * '-'
    print(sticks)
    print(language.xsser_description)
    print(sticks,'\n')

def spectre_meldown_checker_banner(language):
    print(Color.white+"""                 _                     _    _                    _           _           
 ____ __  ___ __| |_ _ _ ___ _ __  ___| |__| |_____ __ ___ _  __| |_  ___ __| |_____ _ _ 
(_-< '_ \/ -_) _|  _| '_/ -_) '  \/ -_) / _` / _ \ V  V / ' \/ _| ' \/ -_) _| / / -_) '_|
/__/ .__/\___\__|\__|_| \___|_|_|_\___|_\__,_\___/\_/\_/|_||_\__|_||_\___\__|_\_\___|_|  
   |_|""")
    sticks = len(language.spectre_meldown_checker_description) * '-'
    print(sticks)
    print(language.spectre_meldown_checker_description)
    print(sticks,'\n')

def brutedum_banner(language):
    print(Color.yellow+"""888888                           888888                BRUTE            
8    8   eeeee  e   e eeeee eeee 8    8 e   e eeeeeee  FORCE
8eeee8ee 8   8  8   8   8   8    8e   8 8   8 8  8  8  JUST
88     8 8eee8e 8e  8   8e  8eee 88   8 8e  8 8e 8  8  FOR
88     8 88   8 88  8   88  88   88   8 88  8 88 8  8  THE
88eeeee8 88   8 88ee8   88  88ee 88eee8 88ee8 88 8  8  DUMMIES"""+Color.white)
    sticks = len(language.brutedum_description) * '-'
    print(sticks)
    print(language.brutedum_description)
    print(sticks,'\n')

def ftpbruter_banner(language):
    print(Color.yellow+""" ______   _______   _____    ____                   _                 
|  ____| |__   __| |  __ \  |  _ \                 | |                
| |__       | |    | |__) | | |_) |  _ __   _   _  | |_    ___   _ __ 
|  __|      | |    |  ___/  |  _ <  | '__| | | | | | __|  / _ \ | '__|
| |         | |    | |      | |_) | | |    | |_| | | |_  |  __/ | |   
|_|         |_|    |_|      |____/  |_|     \__,_|  \__|  \___| |_|"""+Color.white)
    sticks = len(language.ftpbruter_description) * '-'
    print(sticks)
    print(language.ftpbruter_description)
    print(sticks,'\n')

def hash_buster_banner(language):
    print(Color.white+"""_  _ ____ ____ _  _    ___  _  _ ____ ___ ____ ____
|__| |__| [__  |__|    |__] |  | [__   |  |___ |__/
|  | |  | ___] |  |    |__] |__| ___]  |  |___ |  \ """)
    sticks = len(language.hash_buster_description) * '-'
    print(sticks)
    print(language.hash_buster_description)
    print(sticks,'\n')

def socialbox_banner(language):
    print(Color.green+""".▄▄ ·        ▄▄· ▪   ▄▄▄· ▄▄▌      ▄▄▄▄·       ▐▄• ▄ 
▐█ ▀. ▪     ▐█ ▌▪██ ▐█ ▀█ ██•      ▐█ ▀█▪▪      █▌█▌▪
▄▀▀▀█▄ ▄█▀▄ ██ ▄▄▐█·▄█▀▀█ ██▪      ▐█▀▀█▄ ▄█▀▄  ·██· 
▐█▄▪▐█▐█▌.▐▌▐███▌▐█▌▐█ ▪▐▌▐█▌▐▌    ██▄▪▐█▐█▌.▐▌▪▐█·█▌
 ▀▀▀▀  ▀█▄▀▪·▀▀▀ ▀▀▀ ▀  ▀ .▀▀▀     ·▀▀▀▀  ▀█▄▀▪•▀▀ ▀▀"""+Color.white)
    sticks = len(language.socialbox_description) * '-'
    print(sticks)
    print(language.socialbox_description)
    print(sticks,'\n')

def blazy_banner(language):
    print(Color.white+""" ____   _                    
|  _ \ | |              
| |_) || |  __ _  ____ _   _ 
|  _ < | | / _` ||_  /| | | |
| |_) || || (_| | / / | |_| |
|____/ |_| \__,_|/___| \__, |
                        __/ |
 Made with <3 By D3V   |___/ """)
    sticks = len(language.blazy_description) * '-'
    print(sticks)
    print(language.blazy_description)
    print(sticks,'\n')

def ncrack_banner(language):
    print(Color.white+""" _   _                     _    
| \ | |                   | |   
|  \| | ___ _ __ __ _  ___| | __
| . ` |/ __| '__/ _` |/ __| |/ /
| |\  | (__| | | (_| | (__|   < 
|_| \_|\___|_|  \__,_|\___|_|\_\ """)
    sticks = len(language.ncrack_description) * '-'
    print(sticks)
    print(language.ncrack_description)
    print(sticks,'\n')

def kickthemout_banner(language):
    print(Color.green+"""█  █▀ ▄█ ▄█▄    █  █▀    ▄▄▄▄▀  ▄  █ ▄███▄   █▀▄▀█  ████▄   ▄      ▄▄▄▄▀
█▄█   ██ █▀ ▀▄  █▄█   ▀▀▀ █    █   █ █▀   ▀  █ █ █  █   █    █  ▀▀▀ █
█▀▄   ██ █   ▀  █▀▄       █    ██▀▀█ ██▄▄    █ ▄ █  █   █ █   █     █
█  █  ▐█ █▄  ▄▀ █  █     █     █   █ █▄   ▄▀ █   █  ▀████ █   █    █
 █    ▐ ▀███▀    █     ▀         █  ▀███▀      █         █▄ ▄█   ▀
 ▀               ▀               ▀             ▀           ▀▀▀"""+Color.white)
    sticks = len(language.kickthemout_description) * '-'
    print(sticks)
    print(language.kickthemout_description)
    print(sticks,'\n')

def sniffair_banner(language):
    print(Color.white+"""                                                                     % *        ., %                         
                                                                    % ( ,#     (..# %                        
    /@@@@@&,    *@@%        &@,    @@#    /@@@@@@@@@   .@@@@@@@@@. ,/ # # (%%%* % (.(.  .@@     &@@@@@@%.    
  .@@&   *&@    %@@@@.      &@,    @@%    %@@,,,,,,,   ,@@,,,,,,,  .( % %  %%#  # % #   ,@@     @@(,,,#@@@.  
  %@%           %@@(@@.     &@,    @@%    %@@          ,@@          /* #   /*,   %.,,   ,@@     @@*     #@@  
  ,@@&          %@@ ,@@*    &@,    @@%    %@@          ,@@           .#   //#(,   (,    ,@@     @@*     &@%  
   .@@@@@.      %@@  .@@(   &@,    @@%    %@@%%%%%%*   ,@@%%%%%%#         (# ##.        ,@@     @@&%%%@@@%   
       *@@@@    %@@   .@@/  &@,    @@%    %@@,,,,,,    ,@@,,,,,,.        %#####%        ,@@     @@(,,%@@%    
          @@%   %@@     @@( &@,    @@%    %@@          ,@@              %  (*/  #       ,@@     @@*    @@@   
          %@%   %@@      @@&&@,    @@%    %@@          ,@@             %  #  .# .#      ,@@     @@*     @@%  
 .@@&/,,#@@@    %@@       &@@@,    @@%    %@@          ,@@            /(*       /(#     ,@@     @@*      @@# 
   *%@@@&*      *%#        ,%#     #%/    *%#           %%            #############.    .%#     #%.      .%% 
                                                                  (@Tyl0us & @theDarracott)""")
    sticks = len(language.sniffair_description) * '-'
    print(sticks)
    print(language.sniffair_description)
    print(sticks,'\n')

def wifi_pumpkin_banner(language):
    print(Color.white+"""__        ___ _____ _ ____                        _    _       
\ \      / (_)  ___(_)  _ \ _   _ _ __ ___  _ __ | | _(_)_ __  
 \ \ /\ / /| | |_  | | |_) | | | | '_ ` _ \| '_ \| |/ / | '_ \ 
  \ V  V / | |  _| | |  __/| |_| | | | | | | |_) |   <| | | | |
   \_/\_/  |_|_|   |_|_|    \__,_|_| |_| |_| .__/|_|\_\_|_| |_|
                                           |_|""")
    sticks = len(language.wifi_pumpkin_description) * '-'
    print(sticks)
    print(language.wifi_pumpkin_description)
    print(sticks,'\n')

def airgeddon_banner(language):
    print(Color.yellow+"""       .__                         .___  .___             
_____  |__|______  ____   ____   __| _/__| _/____   ____  
\__  \ |  \_  __ \/ ___\_/ __ \ / __ |/ __ |/  _ \ /    \ 
 / __ \|  ||  | \/ /_/  >  ___// /_/ / /_/ (  <_> )   |  \ 
(____  /__||__|  \___  / \___  >____ \____ |\____/|___|  / 
     \/         /_____/      \/     \/    \/           \/ """+Color.white)
    sticks = len(language.airgeddon_description) * '-'
    print(sticks)
    print(language.airgeddon_description)
    print(sticks,'\n')

def pikarma_banner(language):
    print(Color.white+"""
██████╗ ██╗██╗  ██╗ █████╗ ██████╗ ███╗   ███╗ █████╗
██╔══██╗██║██║ ██╔╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗
██████╔╝██║█████╔╝ ███████║██████╔╝██╔████╔██║███████║
██╔═══╝ ██║██╔═██╗ ██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║
██║     ██║██║  ██╗██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝""")
    sticks = len(language.pikarma_description) * '-'
    print(sticks)
    print(language.pikarma_description)
    print(sticks,'\n')

def wifite2_banner(language):
    print(Color.white+"""   .               .    
 .´  ·  .     .  ·  `.  wifite 2
 :  :  :  (¯)  :  :  :  automated wireless auditor
 `.  ·  ` /¯\ ´  ·  .´  https://github.com/derv82/wifite2
   `     /¯¯¯\     ´""")
    sticks = len(language.wifite2_description) * '-'
    print(sticks)
    print(language.wifite2_description)
    print(sticks,'\n')

def pixiewps_banner(language):
    print(Color.white+""" _____ _     _     _ _ _ _____ _____ 
|  _  |_|_ _|_|___| | | |  _  |   __|
|   __| |_'_| | -_| | | |   __|__   |
|__|  |_|_,_|_|___|_____|__|  |_____|""")
    sticks = len(language.pixiewps_description) * '-'
    print(sticks)
    print(language.pixiewps_description)
    print(sticks,'\n')

def fluxion_banner(language):
    print(Color.red+""" ⌠▓▒▓▒   ⌠▓╗     ⌠█┐ ┌█   ┌▓\  /▓┐   ⌠▓╖   ⌠◙▒▓▒◙   ⌠█\  ☒┐             
 ║▒_     │▒║     │▒║ ║▒    \▒\/▒/    │☢╫   │▒┌╤┐▒   ║▓▒\ ▓║             
 ≡◙◙     ║◙║     ║◙║ ║◙      ◙◙      ║¤▒   ║▓║☯║▓   ♜◙\✪\◙♜             
 ║▒      │▒║__   │▒└_┘▒    /▒/\▒\    │☢╫   │▒└╧┘▒   ║█ \▒█║             
 ⌡▓      ⌡◘▒▓▒   ⌡◘▒▓▒◘   └▓/  \▓┘   ⌡▓╝   ⌡◙▒▓▒◙   ⌡▓  \▓┘             
¯¯¯     ¯¯¯¯¯¯  ¯¯¯¯¯¯¯  ¯¯¯    ¯¯¯ ¯¯¯¯  ¯¯¯¯¯¯¯  ¯¯¯¯¯¯¯¯"""+Color.white)
    sticks = len(language.fluxion_description) * '-'
    print(sticks)
    print(language.fluxion_description)
    print(sticks,'\n')

def reaver_banner(language):
    print(Color.white+""" ____                           
|  _ \ ___  __ ___   _____ _ __ 
| |_) / _ \/ _` \ \ / / _ \ '__|
|  _ <  __/ (_| |\ V /  __/ |   
|_| \_\___|\__,_| \_/ \___|_|""")
    sticks = len(language.reaver_description) * '-'
    print(sticks)
    print(language.reaver_description)
    print(sticks,'\n')

def zarp_banner(language):
    print(Color.green+""" ____   __   ____  ____
(__  ) / _\ (  _ \(  _ '
 / _/ /    \ )   / ) __/
(____)\_/\_/(__\_)(__)"""+Color.white)
    sticks = len(language.zarp_description) * '-'
    print(sticks)
    print(language.zarp_description)
    print(sticks,'\n')

def xerosploit_banner(language):
    print(Color.white+"""
██╗  ██╗███████╗██████╗  ██████╗ ███████╗██████╗ ██╗      ██████╗ ██╗████████╗
╚██╗██╔╝██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
 ╚███╔╝ █████╗  ██████╔╝██║   ██║███████╗██████╔╝██║     ██║   ██║██║   ██║
 ██╔██╗ ██╔══╝  ██╔══██╗██║   ██║╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║
██╔╝ ██╗███████╗██║  ██║╚██████╔╝███████║██║     ███████╗╚██████╔╝██║   ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝""")
    sticks = len(language.xerosploit_description) * '-'
    print(sticks)
    print(language.xerosploit_description)
    print(sticks,'\n')

def seth_banner(language):
    print(Color.white+"""
███████╗███████╗████████╗██╗  ██╗
██╔════╝██╔════╝╚══██╔══╝██║  ██║
███████╗█████╗     ██║   ███████║
╚════██║██╔══╝     ██║   ██╔══██║
███████║███████╗   ██║   ██║  ██║
╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝""")
    sticks = len(language.seth_description) * '-'
    print(sticks)
    print(language.seth_description)
    print(sticks,'\n')

def wifiphisher_banner(language):
    print(Color.white+"""                     _  __ _       _     _     _               
                    (_)/ _(_)     | |   (_)   | |              
  ((.))    __      ___| |_ _ _ __ | |__  _ ___| |__   ___ _ __ 
    |      \ \ /\ / / |  _| | '_ \| '_ \| / __| '_ \ / _ \ '__|
   /_\      \ V  V /| | | | | |_) | | | | \__ \ | | |  __/ |   
  /___\      \_/\_/ |_|_| |_| .__/|_| |_|_|___/_| |_|\___|_|   
 /     \                    | |                                
                            |_|""")
    sticks = len(language.wifiphisher_description) * '-'
    print(sticks)
    print(language.wifiphisher_description)
    print(sticks,'\n')

def sharp_banner(language):
    print(Color.white+"""        ||                               _______       _______
        ||                  /\          |        ?    |        ?
        ||                 /  \         |         ?   |         ?
        ||                /    \        |         ?   |         ?
  //    ||-------        /      \       |________?    |________?
 //     ||      ||      /--------\      |     \       |
//_____ ||      ||     /          \     |      \      |
     // ||      ||    /            \    |       \     |
    //  ||      ||   /              \   |        \    |
   //   ||      ||  /                \  |         \   |""")
    sticks = len(language.sharp_description) * '-'
    print(sticks)
    print(language.sharp_description)
    print(sticks,'\n')

def sharp_2_banner(language):
    print(Color.white+"""        ||                               _______       _______
        ||                  /\          |        ?    |        ?
        ||                 /  \         |         ?   |         ?
        ||                /    \        |         ?   |         ?
  //    ||-------        /      \       |________?    |________?
 //     ||      ||      /--------\      |     \       |
//_____ ||      ||     /          \     |      \      |
     // ||      ||    /            \    |       \     |
    //  ||      ||   /              \   |        \    |
   //   ||      ||  /                \  |         \   |""")
    sticks = len(language.sharp_2_description) * '-'
    print(sticks)
    print(language.sharp_2_description)
    print(sticks,'\n')

def eviltwinframework_banner(language):
    print(Color.white+"""    ______      _ ________         _       ______                                             __  
   / ____/   __(_) /_  __/      __(_)___  / ____/________ _____ ___  ___ _      ______  _____/ /__
  / __/ | | / / / / / / | | /| / / / __ \/ /_  / ___/ __ `/ __ `__ \/ _ \ | /| / / __ \/ ___/ //_/
 / /___ | |/ / / / / /  | |/ |/ / / / / / __/ / /  / /_/ / / / / / /  __/ |/ |/ / /_/ / /  / ,<   
/_____/ |___/_/_/ /_/   |__/|__/_/_/ /_/_/   /_/   \__,_/_/ /_/ /_/\___/|__/|__/\____/_/  /_/|_|""")
    sticks = len(language.eviltwinframework_description) * '-'
    print(sticks)
    print(language.eviltwinframework_description)
    print(sticks,'\n')

def the_rogue_toolkit_banner(language):
    print(Color.white+""" _____ _       _____                 _____         _   _ _   
|_   _| |_ ___| __  |___ ___ _ _ ___|_   _|___ ___| |_|_| |_ 
  | | |   | -_|    -| . | . | | | -_| | | | . | . | '_| |  _|
  |_| |_|_|___|__|__|___|_  |___|___| |_| |___|___|_,_|_|_|  
                        |___|""")
    sticks = len(language.theroguetoolkit_description) * '-'
    print(sticks)
    print(language.theroguetoolkit_description)
    print(sticks,'\n')

def sitebroker_banner(language):
    print(Color.green+"""
  /$$$$$$  /$$   /$$               /$$$$$$$                      /$$
 /$$__  $$|__/  | $$              | $$__  $$                    | $$
| $$  \__/ /$$ /$$$$$$    /$$$$$$ | $$  \ $$  /$$$$$$   /$$$$$$ | $$   /$$  /$$$$$$   /$$$$$$
|  $$$$$$ | $$|_  $$_/   /$$__  $$| $$$$$$$  /$$__  $$ /$$__  $$| $$  /$$/ /$$__  $$ /$$__  $$
 \____  $$| $$  | $$    | $$$$$$$$| $$__  $$| $$  \__/| $$  \ $$| $$$$$$/ | $$$$$$$$| $$  \__/
 /$$  \ $$| $$  | $$ /$$| $$_____/| $$  \ $$| $$      | $$  | $$| $$_  $$ | $$_____/| $$
|  $$$$$$/| $$  |  $$$$/|  $$$$$$$| $$$$$$$/| $$      |  $$$$$$/| $$ \  $$|  $$$$$$$| $$
 \______/ |__/   \___/   \_______/|_______/ |__/       \______/ |__/  \__/ \_______/|__/"""+Color.white)
    sticks = len(language.sitebroker_description) * '-'
    print(sticks)
    print(language.sitebroker_description)
    print(sticks,'\n')

def websploit_banner(language):
    print(Color.white+""" __      __          __                      ___               __
/\ \  __/\ \        /\ \                    /\_ \           __/\ \__
\ \ \/\ \ \ \     __\ \ \____    ____  _____\//\ \     ___ /\_\ \ ,_\ 
 \ \ \ \ \ \ \  /'__`\ \ '__`\  /',__\/\ '__`\\ \ \   / __`\/\ \ \ \/
  \ \ \_/ \_\ \/\  __/\ \ \L\ \/\__, `\ \ \L\ \\_\ \_/\ \L\ \ \ \ \ \_
   \ `\___x___/\ \____\\ \_,__/\/\____/\ \ ,__//\____\ \____/\ \_\ \__\ 
    '\/__//__/  \/____/ \/___/  \/___/  \ \ \/ \/____/\/___/  \/_/\/__/
                                         \ \_\ 
                                          \/_/""")
    sticks = len(language.websploit_description) * '-'
    print(sticks)
    print(language.websploit_description)
    print(sticks,'\n')

def wpsploit_banner(language):
    print(Color.white+""" __      ____________  _________       __          __   __  
/  \    /  \______   \/   _____/_____ |  |   ____ |__|_/  |__ 
\   \/\/   /|     ___/\_____  \\\____ \|  |  /  _ \|  |_   ___|
 \        / |    |    /        \  |_) |  |_(  (_) )  | |  |
  \__/\  /  |____|   /_______  /   __/|____/\____/|__| |__|
       \/                    \/|__|""")
    sticks = len(language.wpsploit_description) * '-'
    print(sticks)
    print(language.wpsploit_description)
    print(sticks,'\n')

def zoom_banner(language):
    print(Color.yellow+""" ____                
/_  / ___  ___  ____ 
 / /_/ _ \/ _ \/    \ 
/___/\___/\___/_/_/_/"""+Color.white)
    sticks = len(language.zoom_description) * '-'
    print(sticks)
    print(language.zoom_description)
    print(sticks,'\n')

def nosqlmap_banner(language):
    print(Color.white+""" _  _     ___  ___  _    __  __           
| \| |___/ __|/ _ \| |  |  \/  |__ _ _ __ 
| .` / _ \__ \ (_) | |__| |\/| / _` | '_ \\ 
|_|\_\___/___/\__\_\____|_|  |_\__,_| .__/
                                    |_|""")
    sticks = len(language.nosqlmap_description) * '-'
    print(sticks)
    print(language.nosqlmap_description)
    print(sticks,'\n')

def sqlcake_banner(language):
    print(Color.white+""" _________________________________
/                                 \ 
     sql auto exploitation kit
\_________________________________/""")
    sticks = len(language.sqlcake_description) * '-'
    print(sticks)
    print(language.sqlcake_description)
    print(sticks,'\n')

def bsqlinjector_banner(language):
    print(Color.white+""" _____ _____ _____ __    _       _         _           
| __  |   __|     |  |  |_|___  |_|___ ___| |_ ___ ___ 
| __ -|__   |  |  |  |__| |   | | | -_|  _|  _| . |  _|
|_____|_____|__  _|_____|_|_|_|_| |___|___|_| |___|_|  
               |__|           |___|""")
    sticks = len(language.bsqlinjector_description) * '-'
    print(sticks)
    print(language.bsqlinjector_description)
    print(sticks,'\n')

def xxeinjector_banner(language):
    print(Color.white+""" __ __ __ __ _____ _       _         _           
|  |  |  |  |   __|_|___  |_|___ ___| |_ ___ ___ 
|-   -|-   -|   __| |   | | | -_|  _|  _| . |  _|
|__|__|__|__|_____|_|_|_|_| |___|___|_| |___|_|  
                        |___|""")
    sticks = len(language.xxeinjector_description) * '-'
    print(sticks)
    print(language.xxeinjector_description)
    print(sticks,'\n')

def badmod_banner(language):
    print(Color.white+"""                         __________
                      .~#########;;;~.
                     /############;;;`\ 
                    /######/~\/~\;;;,;,\ 
                   |#######\    /;;;;.,.|
                   |#########\/%;;;;;.,.|
      XX           |##/~~\####%;;;/~~\;,|       XX
    XX..X          |#|  o  \##%;/  o  |.|      X..XX
  XX.....X         |##\____/##%;\____/.,|     X.....XX
 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |########;;;;,.|     @#%,.@  X.....| X
X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X
 X# \.X        @#%,.@                  @#%,.@        X./  #
  ##  X          @#%,.@              @#%,.@          X   #
, '# #X            @#%,.@          @#%,.@            X ##
   `###X             @#%,.@      @#%,.@             ####'
  . ' ###              @#%.,@  @#%,.@              ###`'
            . ';'        @#%.@#%,.@                ;'` ' .
              '           @#%,.@                   ,.""")
    sticks = len(language.badmod_description) * '-'
    print(sticks)
    print(language.badmod_description)
    print(sticks,'\n')


def roxysploit_banner(language):
    print(Color.white+"""                         _     _ _   
 ___ ___ _ _ _ _ ___ ___| |___|_| |_ 
|  _| . |_'_| | |_ -| . | | . | |  _|
|_| |___|_,_|_  |___|  _|_|___|_|_|  
            |___|   |_|""")
    sticks = len(language.roxysploit_description) * '-'
    print(sticks)
    print(language.roxysploit_description)
    print(sticks,'\n')

def lunar_banner(language):
    print(Color.green+"""
      :::       :::    ::: ::::    :::     :::     :::::::::    
     :+:       :+:    :+: :+:+:   :+:   :+: :+:   :+:    :+:    
    +:+       +:+    +:+ :+:+:+  +:+  +:+   +:+  +:+    +:+     
   +#+       +#+    +:+ +#+ +:+ +#+ +#++:++#++: +#++:++#:       
  +#+       +#+    +#+ +#+  +#+#+# +#+     +#+ +#+    +#+       
 #+#       #+#    #+# #+#   #+#+# #+#     #+# #+#    #+#"""+Color.white)
    sticks = len(language.lunar_description) * '-'
    print(sticks)
    print(language.lunar_description)
    print(sticks,'\n')

def autordpwn_banner(language):
    print(Color.white+"""    ___          __       _________ _________ ________
  /  _  \  __ __|  |_ ___ \______   \_______  \______  \  _  ___ ___
 /  / \  \|  |  |   _| _  \|       _/| |    \  |    ___/\/ \/  /     \ 
/  /___\  \  |  |  |  (_)  |   |    \| |____/  |   | \        /   |   \\
\  _______/_____/__|\_____/|___|__  /_________/|___|  \__/\__/|___|_  /
 \/                               \/""")
    sticks = len(language.autordpwn_description) * '-'
    print(sticks)
    print(language.autordpwn_description)
    print(sticks,'\n')

def expliot_banner(language):
    print(Color.white+"""     __  __      _ _       _   
  ___\ \/ /_ __ | (_) ___ | |_ 
 / _ \\\  /| '_ \| | |/ _ \| __|
|  __//  \| |_) | | | (_) | |_ 
 \___/_/\_\ .__/|_|_|\___/ \__|
           |_|""")
    sticks = len(language.expliot_description) * '-'
    print(sticks)
    print(language.expliot_description)
    print(sticks,'\n')

def rootos_banner(language):
    print(Color.white+"""                  _    ___  ____  
  _ __ ___   ___ | |_ / _ \/ ___| 
 | '__/ _ \ / _ \| __| | | \___ \ 
 | | | (_) | (_) | |_| |_| |___) |
 |_|  \___/ \___/ \__|\___/|____/""")
    sticks = len(language.rootos_desscription) * '-'
    print(sticks)
    print(language.rootos_desscription)
    print(sticks,'\n')

def pure_blood_banner(language):
    print(Color.red+"""
 ██▓███   █    ██  ██▀███  ▓█████  ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄
▓██░  ██▒ ██  ▓██▒▓██ ▒ ██▒▓█   ▀ ▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌
▓██░ ██▓▒▓██  ▒██░▓██ ░▄█ ▒▒███   ▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌
▒██▄█▓▒ ▒▓▓█  ░██░▒██▀▀█▄  ▒▓█  ▄ ▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌
▒██▒ ░  ░▒▒█████▓ ░██▓ ▒██▒░▒████▒░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓
▒▓▒░ ░  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒
░▒ ░     ░░▒░ ░ ░   ░▒ ░ ▒░ ░ ░  ░▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒
░░        ░░░ ░ ░   ░░   ░    ░    ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░
            ░        ░        ░  ░ ░          ░  ░    ░ ░      ░ ░     ░
                                        ░                            ░"""+Color.white)
    sticks = len(language.pure_blood_description) * '-'
    print(sticks)
    print(language.pure_blood_description)
    print(sticks,'\n')

def termineter_banner(language):
    print(Color.white+"""  ______                    _            __
 /_  __/__  _________ ___  (_)___  ___  / /____  _____
  / / / _ \/ ___/ __ `__ \/ / __ \/ _ \/ __/ _ \/ ___/
 / / /  __/ /  / / / / / / / / / /  __/ /_/  __/ /
/_/  \___/_/  /_/ /_/ /_/_/_/ /_/\___/\__/\___/_/""")
    sticks = len(language.termineter_description) * '-'
    print(sticks)
    print(language.termineter_description)
    print(sticks,'\n')

def autosploit_banner(language):
    print(Color.red+""" _____     _       _____     _     _ _ 
|  _  |_ _| |_ ___|   __|___| |___|_| |_
|     | | |  _| . |__   | . | | . | |  _|
|__|__|___|_| |___|_____|  _|_|___|_|_|
                        |_|"""+Color.white)
    sticks = len(language.autosploit_description) * '-'
    print(sticks)
    print(language.autosploit_description)
    print(sticks,'\n')

def smod_banner(language):
    print(Color.white+""" _______ 
< SMOD >
 ------- 
        \   ^__^
         \  (xx)\_______
            (__)\       )\/\ 
             U  ||----w |
                ||     ||""")
    sticks = len(language.smod_description) * '-'
    print(sticks)
    print(language.smod_description)
    print(sticks,'\n')

def thefatrat_banner(language):
    print(Color.green+""" _____ _       _____     _   _____     _   
|_   _| |_ ___|   __|___| |_| __  |___| |_ 
  | | |   | -_|   __| .'|  _|    -| .'|  _|
  |_| |_|_|___|__|  |__,|_| |__|__|__,|_|"""+Color.white)
    sticks = len(language.thefatrat_description) * '-'
    print(sticks)
    print(language.thefatrat_description)
    print(sticks,'\n')

def exploit_pack_banner(language):
    print(Color.white+""" _____            _       _ _   ____            _    
| ____|_  ___ __ | | ___ (_) |_|  _ \ __ _  ___| | __
|  _| \ \/ / '_ \| |/ _ \| | __| |_) / _` |/ __| |/ /
| |___ >  <| |_) | | (_) | | |_|  __/ (_| | (__|   < 
|_____/_/\_\ .__/|_|\___/|_|\__|_|   \__,_|\___|_|\_\\
           |_|""")
    sticks = len(language.exploit_pack_description) * '-'
    print(sticks)
    print(language.exploit_pack_description)
    print(sticks,'\n')

def mimikittenz_banner(language):
    print(Color.white+"""       _       _ _   _ _   _               
 _____|_|_____|_| |_|_| |_| |_ ___ ___ ___ 
|     | |     | | '_| |  _|  _| -_|   |- _|
|_|_|_|_|_|_|_|_|_,_|_|_| |_| |___|_|_|___|""")
    sticks = len(language.mimikittenz_description) * '-'
    print(sticks)
    print(language.mimikittenz_description)
    print(sticks,'\n')

def ezsploit_banner(language):
    print(Color.white+"""                     ______
                  .-        -.
                 /            \      
    *                    * 
                |,  .-.  .-.  ,|        *
                | )(_ /  \_ )( |
                |/     /\     \|    *
      (@_       <__    ^^    __>         *
 _     ) \_______\__|IIIIII|__/_______________________
(_)@8@8{}<_____________________________________________>
       )_/         \ IIIIII /                    :::::
      (@            --------                        ::""")
    sticks = len(language.ezsploit_description) * '-'
    print(sticks)
    print(language.ezsploit_description)
    print(sticks,'\n')

def auto_root_exploit_banner(language):
    print(Color.white+""" _____     _       _____         _   _____         _     _ _
|  _  |_ _| |_ ___| __  |___ ___| |_|   __|_ _ ___| |___|_| |_
|     | | |  _| . |    -| . | . |  _|   __|_'_| . | | . | |  _|
|__|__|___|_| |___|__|__|___|___|_| |_____|_,_|  _|_|___|_|_|
                                              |_|""")
    sticks = len(language.auto_root_exploit_description) * '-'
    print(sticks)
    print(language.auto_root_exploit_description)
    print(sticks,'\n')

def ahmyth_android_rat_banner(language):
    print(Color.white+"""    _    _     __  __       _   _     
   / \  | |__ |  \/  |_   _| |_| |__
  / _ \ | '_ \| |\/| | | | | __| '_ \ 
 / ___ \| | | | |  | | |_| | |_| | | |
/_/   \_\_| |_|_|  |_|\__, |\__|_| |_|
                      |___/""")
    sticks = len(language.ahmyth_android_rat_description) * '-'
    print(sticks)
    print(language.ahmyth_android_rat_description)
    print(sticks,'\n')

def exploit_framework_banner(language):
    print(Color.white+""" _____         _     _ _   _____                                 _
|   __|_ _ ___| |___|_| |_|   __|___ ___ _____ ___ _ _ _ ___ ___| |_
|   __|_'_| . | | . | |  _|   __|  _| .'|     | -_| | | | . |  _| '_|
|_____|_,_|  _|_|___|_|_| |__|  |_| |__,|_|_|_|___|_____|___|_| |_,_|
          |_|""")
    sticks = len(language.expliot_framework_description) * '-'
    print(sticks)
    print(language.expliot_framework_description)
    print(sticks,'\n')

def winroothelper_banner(language):
    print(Color.green+""" _ _ _ _     _____         _           
| | | |_|___| __  |___ ___| |_         
| | | | |   |    -| . | . |  _|        
|_____|_|_|_|__|__|___|___|_|
   _____     _             
  |  |  |___| |___ ___ ___ 
  |     | -_| | . | -_|  _|
  |__|__|___|_|  _|___|_|  
                      |_|"""+Color.white)
    sticks = len(language.winroothelper_description) * '-'
    print(sticks)
    print(language.winroothelper_description)
    print(sticks,'\n')

def metasploit_banner(language):
    print(Color.white+""" _                                                    _
/ \\    /\\         __                         _   __  /_/ __
| |\  / | _____   \\ \\           ___   _____ | | /  \\ _   \\ \\
| | \/| | | ___\\ |- -|   /\    / __\\ | -__/ | || | || | |- -|
|_|   | | | _|__  | |_  / -\ __\ \   | |    | | \__/| |  | |_
      |/  |____/  \___\\/ /\ \\\___/   \/     \__|    |_\\  \\___\\ """)
    sticks = len(language.metasploit_description) * '-'
    print(sticks)
    print(language.metasploit_description)
    print(sticks,'\n')

def zerodoor_banner(language):
    print(Color.white+""" _____________________________________________________________ 
|                                                   ^^^^^^^^\ |
|                                                   |       | |
|      *  ZeroDoor Backdoor Generator *             |_ __   | | 
|                                                   (.(. )  | |
|       ~ Created By Souhardya Sardar  ~    _      (_       ) |
|            Happy Hacking to all :)        \\\     /___/'  /  |  
|                                           _\\\_     \    |   |
|                                          ((   )     /====|  |
|                                           \  <.__._-      \ |
|___________________________________________ <//___.         ||""")
    sticks = len(language.zerodoor_description) * '-'
    print(sticks)
    print(language.zerodoor_description)
    print(sticks,'\n')

def terminator_banner(language):
    print(Color.red+"""_________ _______  _______  _______ _________ _        _______ _________ _______  _______ 
\__   __/(  ____ \(  ____ )(       )\__   __/( (    /|(  ___  )\__   __/(  ___  )(  ____ )
   ) (   | (    \/| (    )|| () () |   ) (   |  \  ( || (   ) |   ) (   | (   ) || (    )|
   | |   | (__    | (____)|| || || |   | |   |   \ | || (___) |   | |   | |   | || (____)|
   | |   |  __)   |     __)| |(_)| |   | |   | (\ \) ||  ___  |   | |   | |   | ||     __)
   | |   | (      | (\ (   | |   | |   | |   | | \   || (   ) |   | |   | |   | || (\ (   
   | |   | (____/\| ) \ \__| )   ( |___) (___| )  \  || )   ( |   | |   | (___) || ) \ \__
   )_(   (_______/|/   \__/|/     \|\_______/|/    )_)|/     \|   )_(   (_______)|/   \__/"""+Color.white)
    sticks = len(language.terminator_description) * '-'
    print(sticks)
    print(language.terminator_description)
    print(sticks,'\n')

def winpayload_banner(language):
    print(Color.red+""" _       ___       ____              __                __    
| |     / (_)___  / __ \\____ ___  __/ /___  ____ _____/ /____
| | /| / / / __ \\/ /_/ / __ `/ / / / / __ \\/ __ `/ __  / ___/
| |/ |/ / / / / / ____/ /_/ / /_/ / / /_/ / /_/ / /_/ (__  ) 
|__/|__/_/_/ /_/_/    \__,_/\\__, /_/\\____/\\__,_/\\__,_/____/  
                           /____/"""+Color.white)
    sticks = len(language.winpayloads_description) * '-'
    print(sticks)
    print(language.winpayloads_description)
    print(sticks,'\n')

def saint_banner(language):
    print(Color.red+"""
  pd'      `bq        db      `7MMF'`7MN.   `7MF'MMP\\"\\"MM\\"\\"YMM
 6P          YA      ;MM:       MM    MMN.    M  P'   MM   `7
6M' ,pP\\"Ybd `Mb    ,V^MM.      MM    M YMb   M       MM
MN  8I   `\\"  8M   ,M  `MM      MM    M  `MN. M       MM
MN  `YMMMa.   8M   AbmmmqMA     MM    M   `MM.M       MM
YM. L.   I8  ,M9  A'     VML    MM    M     YMM       MM
 Mb M9mmmP'  dM .AMA.   .AMMA..JMML..JML.    YM     .JMML.
  Yq.      .pY
      ``   '' """+Color.white)
    sticks = len(language.saint_description) * '-'
    print(sticks)
    print(language.saint_description)
    print(sticks,'\n')

def beelogger_banner(language):
    print(Color.yellow+"""         .' '. I BEE YOU  __
.        .   .          \\(__\\_/             
 .         .         . -{{#(|8)
   ' .  . ' ' .  . '    /(__/ \\"""+Color.white)
    sticks = len(language.beelogger_description) * '-'
    print(sticks)
    print(language.beelogger_description)
    print(sticks,'\n')

def hacktheworld_banner(language):
    print(Color.green+""" _   _            _      _____ _           __        __         _     _ 
| | | | __ _  ___| | __ |_   _| |__   ___  \ \      / /__  _ __| | __| |
| |_| |/ _` |/ __| |/ /   | | | '_ \ / _ \  \ \ /\ / / _ \| '__| |/ _` |
|  _  | (_| | (__|   <    | | | | | |  __/   \ V  V / (_) | |  | | (_| |
|_| |_|\__,_|\___|_|\_\   |_| |_| |_|\___|    \_/\_/ \___/|_|  |_|\__,_|"""+Color.white)
    sticks = len(language.hacktheworld_dewcription) * '-'
    print(sticks)
    print(language.hacktheworld_dewcription)
    print(sticks,'\n')

def hatkey_banner(language):
    print(Color.white+""" _______ 
< HatKey >
 ------- 
        \   ^__^
         \  (xx)\_______
            (__)\       )\/\ 
             U  ||----w | 
                ||     ||""")
    sticks = len(language.hatkey_description) * '-'
    print(sticks)
    print(language.hatkey_description)
    print(sticks,'\n')

def trolo_banner(language):
    print(Color.white+"""
               +(\\
      ______ +/  .|   _____  ____  ____  _     ____
 >== '|     b3  \_|  /__ __\\/  __\\/  _ \\/ \   /  _ \\
   /  |trust| \/       / \  |  \/|| / \|| |   | / \|
   |_ | me  |__|       | |  |    /| \_/|| |_/\| \_/|
  (  )|_____(  )       \\_/  \\_/\\_\\\____/\\____/\\____/
  (__)      (__)         KEEPING IT SIMPLE!""")
    sticks = len(language.trolo_description) * '-'
    print(sticks)
    print(language.trolo_description)
    print(sticks,'\n')

def getwin_banner(languages):
    print(Color.white+"""     _______                _  _  _  _         
    (_______)          _   (_)(_)(_)(_)        
     _   ___  _____  _| |_  _  _  _  _  ____   
    | | (_  || ___ |(_   _)| || || || ||  _ \  
    | |___) || ____|  | |_ | || || || || | | | 
     \_____/ |_____)   \__) \_____/ |_||_| |_|v1.2 

.:.: FUD win32 payload generator and listener :.:.""")
    sticks = len(languages.getwin_description) * '-'
    print(sticks)
    print(languages.getwin_description)
    print(sticks,'\n')

def dkmc_banner(language):
    print(Color.white+"""     |\      _,,,---,,_
    /,`.-'`'    -.  ;-;;,_
   |,4-  ) )-,_..;\ (  `'-'
  '---''(_/--'  `-'\_)    The sleepy cat""")
    sticks = len(language.dkmc_description) * '-'
    print(sticks)
    print(language.dkmc_description)
    print(sticks,'\n')

def parat_banner(language):
    print(Color.blue+"""  ____                 _   
 |  _ \\ __ _ _ __ __ _| |_ 
 | |_) / _` | '__/ _` | __|
 |  __/ (_| | | | (_| | |_ 
 |_|   \\__,_|_|  \\__,_|\\__|"""+Color.white)
    sticks = len(language.parat_description) * '-'
    print(sticks)
    print(language.parat_description)
    print(sticks,'\n')

def mkvenom_banner(language):
    print(Color.yellow+"""         __                                  __ 
  __ _  / /___  _____ ___  ___  __ _    ___ / / 
 /  ' \\/  '_/ |/ / -_) _ \/ _ \/  ' \\_ (_-</ _ \\
/_/_/_/_/\\_\\|___/\\__/_//_/\\___/_/_/_(_)___/_//_/"""+Color.white)
    sticks = len(language.mkvenom_description) * '-'
    print(sticks)
    print(language.mkvenom_description)
    print(sticks,'\n')

def venom_banner(language):
    print(Color.white+""" __    _ ______  ____   _  _____  ____    __  
\  \  //|   ___||    \ | |/     \|    \  /  |
 \  \// |   ___||     \| ||     ||     \/   |
  \__/  |______||__/\____|\_____/|__/\__/|__|
   |S|h|e|l|l|c|0|d|e| |G|e|n|e|r|a|t|0|r|""")
    sticks = len(language.venom_description) * '-'
    print(sticks)
    print(language.venom_description)
    print(sticks,'\n')

def cloak_banner(language):
    print(Color.white+"""_________ .__                __    
\_   ___ \|  |   _________  |  | __
/    \  \/|  |  /  _ \__  \ |  |/ /
\     \___|  |_(  <_> ) __ \|    < 
 \______  /____/\____(____  /__|_ \ 
        \/                \/     \/""")
    sticks = len(language.cloak_description) * '-'
    print(sticks)
    print(language.cloak_description)
    print(sticks,'\n')

def avoid_banner(language):
    print(Color.white+""" _____     _               _     _ _   _____ _____ _____             _         
|     |___| |_ ___ ___ ___| |___|_| |_|  _  |  |  |   __|_ _ ___ ___|_|___ ___ 
| | | | -_|  _| .'|_ -| . | | . | |  _|     |  |  |   __| | | .'|_ -| | . |   |
|_|_|_|___|_| |__,|___|  _|_|___|_|_| |__|__|\___/|_____|\_/|__,|___|_|___|_|_|
                      |_|""")
    sticks = len(language.avoid_description) * '-'
    print(sticks)
    print(language.avoid_description)
    print(sticks,'\n')

def avet_banner(language):
    print(Color.white+"""    ___     _______ _____ 
   / \ \   / / ____|_   _|
  / _ \ \ / /|  _|   | |  
 / ___ \ V / | |___  | |  
/_/   \_\_/  |_____| |_|""")
    sticks = len(language.avet_description) * '-'
    print(sticks)
    print(language.avet_description)
    print(sticks,'\n')

def nxcrypt_banner(language):
    print(Color.blue+"""
d8b   db db    db  .o88b. d8888b. db    db d8888b. d888888b
888o  88 `8b  d8' d8P  Y8 88  `8D `8b  d8' 88  `8D `~~88~~'
88V8o 88  `8bd8'  8P      88oobY'  `8bd8'  88oodD'    88
88 V8o88  .dPYb.  8b      88`8b      88    88~~~      88
88  V888 .8P  Y8. Y8b  d8 88 `88.    88    88         88
VP   V8P YP    YP  `Y88P' 88   YD    YP    88         YP
                                        (python backdoor framework)"""+Color.white)
    sticks = len(language.nxcrypt_description) * '-'
    print(sticks)
    print(language.nxcrypt_description)
    print(sticks,'\n')

def slowloris_banner(language):
    print(Color.white+""" _____ _           __            _     
|   __| |___ _ _ _|  |   ___ ___|_|___ 
|__   | | . | | | |  |__| . |  _| |_ -|
|_____|_|___|_____|_____|___|_| |_|___|""")
    sticks = len(language.slowloris_description) * '-'
    print(sticks)
    print(language.slowloris_description)
    print(sticks,'\n')

def zambie_banner(language):
    print(Color.yellow+"""
 /$$$$$$$$  /$$$$$$                /$$      /$$$$$$ /$$$$$$$$
|_____ $$  /$$__  $$              | $$     |_  $$_/| $$_____/
      /$$/ | $$  \ $$ /$$$$$$/$$$$ | $$$$$$$  | $$  | $$
     /$$/  | $$$$$$$$| $$_  $$_  $$| $$__  $$ | $$  | $$$$$
    /$$/   | $$  | $$| $$ \ $$ \ $$| $$  \ $$ | $$  | $$__/
   /$$/    | $$  | $$| $$ | $$ | $$| $$  | $$ | $$  | $$
  /$$$$$$$$| $$  | $$| $$ | $$ | $$| $$$$$$$//$$$$$$| $$$$$$$$
 |________/|__/  |__/|__/ |__/ |__/|_______/|______/|________/"""+Color.white)
    sticks = len(language.zambie_description) * '-'
    print(sticks)
    print(language.zambie_description)
    print(sticks,'\n')

def ufonet_banner(language):
    print(Color.white+"""
888     888 8888888888 .d88888b.  888b    888          888    
888     888 888        d88PY888b  8888b   888          888    
888     888 888       888     888 88888b  888          888    
888     888 8888888   888     888 888Y88b 888  .d88b.  888888 
888     888 888       888     888 888 Y88b888 d8P  Y8b 888    
888     888 888       888     888 888  Y88888 88888888 888    
Y88b. .d88P 888       Y88b. .d88P 888   Y8888 Y8b.     Y88b.  
 'Y88888P'  888        'Y88888P'  888    Y888  'Y8888   'Y8888""")
    sticks = len(language.ufonet_description) * '-'
    print(sticks)
    print(language.ufonet_description)
    print(sticks,'\n')

def memcrashed_banner(language):
    print(Color.white+"""
███╗   ███╗███████╗███╗   ███╗ ██████╗██████╗  █████╗ ███████╗██╗  ██╗███████╗██████╗ 
████╗ ████║██╔════╝████╗ ████║██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
██╔████╔██║█████╗  ██╔████╔██║██║     ██████╔╝███████║███████╗███████║█████╗  ██║  ██║
██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║     ██╔══██╗██╔══██║╚════██║██╔══██║██╔══╝  ██║  ██║
██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╗██║  ██║██║  ██║███████║██║  ██║███████╗██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝""")
    sticks = len(language.memcrashed_description) * '-'
    print(sticks)
    print(language.memcrashed_description)
    print(sticks,'\n')

def fsociety_banner(language):
    print(Color.yellow+"""
d88888b .d8888.  .d88b.   .o88b. d888888b d88888b d888888b db    db
88'     88'  YP .8P  Y8. d8P  Y8   `88'   88         88    `8b  d8'
88ooo   `8bo.   88    88 8P         88    88ooooo    88     `8bd8'
88        `Y8b. 88    88 8b         88    88         88       88
88      db   8D `8b  d8' Y8b  d8   .88.   88.        88       88
YP      `8888Y'  `Y88P'   `Y88P' Y888888P Y88888P    YP       YP"""+Color.white)
    sticks = len(language.fsociety_description) * '-'
    print(sticks)
    print(language.fsociety_description)
    print(sticks,'\n')

def malicious_banner(language):
    print(Color.white+""" __  __       _ _      _                 
|  \/  | __ _| (_) ___(_) ___  _   _ ___ 
| |\/| |/ _` | | |/ __| |/ _ \| | | / __|
| |  | | (_| | | | (__| | (_) | |_| \__ \ 
|_|  |_|\__,_|_|_|\___|_|\___/ \__,_|___/""")
    sticks = len(language.malicious_description) * '-'
    print(sticks)
    print(language.malicious_description)
    print(sticks,'\n')

def tool_x_banner(language):
    print(Color.yellow+""" _____           _     __  __
|_   _|__   ___ | |    \ \/ /
  | |/ _ \ / _ \| |_____\  / 
  | | (_) | (_) | |_____/  \ 
  |_|\___/ \___/|_|    /_/\_\ """+Color.white)
    sticks = len(language.tool_x_description) * '-'
    print(sticks)
    print(language.tool_x_description)
    print(sticks,'\n')

def katoolin_banner(language):
    print(Color.white+"""
$$\   $$\             $$\                         $$\ $$\           
$$ | $$  |            $$ |                        $$ |\__|          
$$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
$$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
$$  $$<    $$$$$$$ |  Kali linux tools installer |$$ |$$ |$$ |  $$ |
$$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
$$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
\__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__|""")
    sticks = len(language.katoolin_description) * '-'
    print(sticks)
    print(language.katoolin_description)
    print(sticks,'\n')

def intrec_pack_banner(language):
    print(Color.green+""" _____ _____ _____ _____ _____ _____     _____ _____ _____ _____ 
|     |   | |_   _| __  |   __|     |___|  _  |  _  |     |  |  |
|-   -| | | | | | |    -|   __|   --|___|   __|     |   --|    -|
|_____|_|___| |_| |__|__|_____|_____|   |__|  |__|__|_____|__|__|"""+Color.white)
    sticks = len(language.intrec_pack_description) * '-'
    print(sticks)
    print(language.intrec_pack_description)
    print(sticks,'\n')

def ptf_banner(language):
    print(Color.red+"""                     ______  __ __    ___
                    |      T|  T  T  /  _]
                    |      ||  l  | /  [_
                    l_j  l_j|  _  |Y    _]
                      |  |  |  |  ||   [_
                      |  |  |  |  ||     T
                      l__j  l__j__jl_____j
 ____     ___  ____   ______    ___   _____ ______    ___  ____    _____
|    \   /  _]|    \ |      T  /  _] / ___/|      T  /  _]|    \  / ___/
|  o  ) /  [_ |  _  Y|      | /  [_ (   \_ |      | /  [_ |  D  )(   \_
|   _/ Y    _]|  |  |l_j  l_jY    _] \__  Tl_j  l_jY    _]|    /  \__  T
|  |   |   [_ |  |  |  |  |  |   [_  /  \ |  |  |  |   [_ |    \  /  \ |
|  |   |     T|  |  |  |  |  |     T \    |  |  |  |     T|  .  Y \    |
l__j   l_____jl__j__j  l__j  l_____j  \___j  l__j  l_____jl__j\_j  \___j
 _____  ____    ____  ___ ___    ___  __    __   ___   ____   __  _
|     ||    \  /    T|   T   T  /  _]|  T__T  T /   \ |    \ |  l/ ]
|   __j|  D  )Y  o  || _   _ | /  [_ |  |  |  |Y     Y|  D  )|  ' /
|  l_  |    / |     ||  \_/  |Y    _]|  |  |  ||  O  ||    / |    \ 
|   _] |    \ |  _  ||   |   ||   [_ l  `  '  !|     ||    \ |     Y
|  T   |  .  Y|  |  ||   |   ||     T \      / l     !|  .  Y|  .  |
l__j   l__j\_jl__j__jl___j___jl_____j  \_/\_/   \___/ l__j\_jl__j\_j"""+Color.white)
    sticks = len(language.ptf_description) * '-'
    print(sticks)
    print(language.ptf_description)
    print(sticks,'\n')