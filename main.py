import sys

import wordGen
import wpmTest
import settings
import json
from colorama import Fore, Style

cattype = """                                                                                                                                            
                                                                                                                                            
                                              tttt               tttt                                                                       
                                           ttt:::t            ttt:::t                                                                       
                                           t:::::t            t:::::t                                                                       
                                           t:::::t            t:::::t                                                                       
    cccccccccccccccc  aaaaaaaaaaaaa  ttttttt:::::tttttttttttttt:::::tttttttyyyyyyy           yyyyyyyppppp   ppppppppp       eeeeeeeeeeee    
  cc:::::::::::::::c  a::::::::::::a t:::::::::::::::::tt:::::::::::::::::t y:::::y         y:::::y p::::ppp:::::::::p    ee::::::::::::ee  
 c:::::::::::::::::c  aaaaaaaaa:::::at:::::::::::::::::tt:::::::::::::::::t  y:::::y       y:::::y  p:::::::::::::::::p  e::::::eeeee:::::ee
c:::::::cccccc:::::c           a::::atttttt:::::::tttttttttttt:::::::tttttt   y:::::y     y:::::y   pp::::::ppppp::::::pe::::::e     e:::::e
c::::::c     ccccccc    aaaaaaa:::::a      t:::::t            t:::::t          y:::::y   y:::::y     p:::::p     p:::::pe:::::::eeeee::::::e
c:::::c               aa::::::::::::a      t:::::t            t:::::t           y:::::y y:::::y      p:::::p     p:::::pe:::::::::::::::::e 
c:::::c              a::::aaaa::::::a      t:::::t            t:::::t            y:::::y:::::y       p:::::p     p:::::pe::::::eeeeeeeeeee  
c::::::c     ccccccca::::a    a:::::a      t:::::t    tttttt  t:::::t    tttttt   y:::::::::y        p:::::p    p::::::pe:::::::e           
c:::::::cccccc:::::ca::::a    a:::::a      t::::::tttt:::::t  t::::::tttt:::::t    y:::::::y         p:::::ppppp:::::::pe::::::::e          
 c:::::::::::::::::ca:::::aaaa::::::a      tt::::::::::::::t  tt::::::::::::::t     y:::::y          p::::::::::::::::p  e::::::::eeeeeeee  
  cc:::::::::::::::c a::::::::::aa:::a       tt:::::::::::tt    tt:::::::::::tt    y:::::y           p::::::::::::::pp    ee:::::::::::::e  
    cccccccccccccccc  aaaaaaaaaa  aaaa         ttttttttttt        ttttttttttt     y:::::y            p::::::pppppppp        eeeeeeeeeeeeee  
                                                                                 y:::::y             p:::::p                                
                                                                                y:::::y              p:::::p                                
                                                                               y:::::y              p:::::::p                               
                                                                              y:::::y               p:::::::p                               
                                                                             yyyyyyy                p:::::::p                               
                                                                                                    ppppppppp                               
                                                                                                                                            """


print(Fore.BLUE + cattype)
print(Style.RESET_ALL)


def initialise():
    with open("settings.json", "r") as infile:
        settingss = json.load(infile)
    if settingss["name"] == "":
        settings.get_name()
        settings.get_language()
        mainScreen()
    else:
        print("Welcome back, " + settingss["name"] + ".")
        mainScreen()


def mainScreen():
        exit = False
        while exit is False:
            print("-------------------")
            print("1 | Start WPM Test")
            print("2 | Change Settings")
            print("3 | Exit")
            mainChoice = input("\n")
            if mainChoice == "1":
                wpmTest.wpmTest()
            elif mainChoice == "2":
                settings.get_language()
            elif mainChoice == "3":
                sys.exit()


if __name__ == "__main__":
    initialise()