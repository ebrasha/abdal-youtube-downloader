"""
 # Project Name:  Abdal Youtube Downloader
 # Programmer: Ebrahim Shafiei
 # Programmer WebSite: https://hackers.zone/
 # Programmer Email: Prof.Shafiei@Gmail.com
 # License : MIT
 # Current Date : 2023-02-08
 # Current Time : 5:51 PM
 # File Description: no description
"""

from os import system, name


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
