"""
 # Project Name: Abdal Youtube Downloader
 # Programmer: Ebrahim Shafiei
 # Programmer WebSite: https://hackers.zone/
 # Programmer Email: Prof.Shafiei@Gmail.com
 # License : MIT
 # Current Date : 2023-02-08
 # Current Time : 4:36 PM
 # File Description: no description
"""
from colorama import Fore, Style, Back, init

# init for Colorama
init()



banner = """

 ,________________________________       
|__________,----------._ [____]  ""-,__  __...-----==="
        (_(||||||||||||)___________/   ""             |
           `----------' EbraSha [ ))"-,               |
                                ""    `,  _,--...___  |
                                        `/          \"""
===============================================================
Welcome to Abdal Youtube Downloader Ver 5.0
Programmer : Ebrahim Shafiei (EbraSha)
Mail: Prof.Shafiei@gmail.com
Github: https://github.com/ebrasha
"""


def banner_nit():
    print(Fore.GREEN + Style.DIM + f'{banner}')
    print(Style.RESET_ALL)


