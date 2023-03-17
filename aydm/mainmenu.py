"""
 # Project Name: Abdal Youtube Downloader
 # Programmer: Ebrahim Shafiei
 # Programmer WebSite: https://hackers.zone/
 # Programmer Email: Prof.Shafiei@Gmail.com
 # License : MIT
 # Current Date : 2023-02-08
 # Current Time : 5:49 PM
 # File Description: no description
"""
import os.path

from aydm import banner
from aydm import aydtools
from colorama import Fore, Style, Back, init
from aydm import youtubed

# init for Colorama
init()


class MainAYD:
    def __init__(self):
        aydtools.clear()
        banner.banner_nit()
        print(Fore.MAGENTA + Style.DIM)
        print(f"1. Download Youtube With Single Link ")
        print(f"2. Download Multi link Youtube")
        print(f"3. Download All Youtube Video By Channel ID ")
        print(f"4. Exit")
        print(Style.RESET_ALL)

    def main_menu(self):
        get_opt = input()
        if get_opt == "1":
            link = input("Enter the video URL: ")
            print(Fore.MAGENTA + Style.DIM)
            print("")
            print(f"1. 144p ")
            print(f"2. 240p ")
            print(f"3. 360p ")
            print(f"4. 480p ")
            print(f"5. 720p ")
            print(f"6. 1080p ")
            print(f"7. Highest Resolution ")
            print(f"8. Only Audio ")
            print(Style.RESET_ALL)
            resolution = input("Select the video resolution: ")

            youtube_obj = youtubed.ayddownloader()
            if resolution == "1":
                youtube_obj.single_link_download(link=link, resolution="144p")
            elif resolution == "2":
                youtube_obj.single_link_download(link=link, resolution="240p")
            elif resolution == "3":
                youtube_obj.single_link_download(link=link, resolution="360p")
            elif resolution == "4":
                youtube_obj.single_link_download(link=link, resolution="480p")
            elif resolution == "5":
                youtube_obj.single_link_download(link=link, resolution="720p")
            elif resolution == "6":
                youtube_obj.single_link_download(link=link, resolution="1080p")
            elif resolution == "7":
                youtube_obj.single_link_download(link=link, resolution="high")
            elif resolution == "8":
                youtube_obj.single_audio_link_download(link=link)
            else:
                print(Style.RESET_ALL)
                print(Fore.RED + Style.DIM)
                print("Wrong resolution selected")
                print(Style.RESET_ALL)

        elif get_opt == "2":
            link_file = input("Enter the video URL file: ")
            if not os.path.exists(link_file):
                print(Style.RESET_ALL)
                print(Fore.RED + Style.DIM)
                print("your file is no exists!!!")
                print(Style.RESET_ALL)
                exit()
            print(Fore.MAGENTA + Style.DIM)
            print("")
            print(f"1. 144p ")
            print(f"2. 240p ")
            print(f"3. 360p ")
            print(f"4. 480p ")
            print(f"5. 720p ")
            print(f"6. 1080p ")
            print(f"7. Highest Resolution ")
            print(f"8. Only Audio ")
            print(Style.RESET_ALL)
            resolution = input("Select the video resolution: ")

            youtube_obj = youtubed.ayddownloader()
            if resolution == "1":
                youtube_obj.multi_link_download(link_file=link_file, resolution="144p")
            elif resolution == "2":
                youtube_obj.multi_link_download(link_file=link_file, resolution="240p")
            elif resolution == "3":
                youtube_obj.multi_link_download(link_file=link_file, resolution="360p")
            elif resolution == "4":
                youtube_obj.multi_link_download(link_file=link_file, resolution="480p")
            elif resolution == "5":
                youtube_obj.multi_link_download(link_file=link_file, resolution="720p")
            elif resolution == "6":
                youtube_obj.multi_link_download(link_file=link_file, resolution="1080p")
            elif resolution == "7":
                youtube_obj.multi_link_download(link_file=link_file, resolution="high")
            elif resolution == "8":
                youtube_obj.multi_link_audio_download(link_file=link_file)
            else:
                print(Style.RESET_ALL)
                print(Fore.RED + Style.DIM)
                print("Wrong resolution selected")
                print(Style.RESET_ALL)

        elif get_opt == "3":
            channel_id = input("Enter the Channel ID (must be 24 char .Search in source for externalId): ")
            print(Fore.MAGENTA + Style.DIM)
            print("")
            print(f"1. 144p ")
            print(f"2. 240p ")
            print(f"3. 360p ")
            print(f"4. 480p ")
            print(f"5. 720p ")
            print(f"6. 1080p ")
            print(f"7. Highest Resolution ")
            print(Style.RESET_ALL)
            resolution = input("Select the video resolution: ")

            youtube_obj = youtubed.ayddownloader()
            if resolution == "1":
                youtube_obj.channel_scrap_link_download(channel_id=channel_id, resolution="144p")
            elif resolution == "2":
                youtube_obj.channel_scrap_link_download(channel_id=channel_id, resolution="240p")
            elif resolution == "3":
                youtube_obj.channel_scrap_link_download(channel_id=channel_id, resolution="360p")
            elif resolution == "4":
                youtube_obj.channel_scrap_link_download(channel_id=channel_id, resolution="480p")
            elif resolution == "5":
                youtube_obj.channel_scrap_link_download(channel_id=channel_id, resolution="720p")
            elif resolution == "6":
                youtube_obj.channel_scrap_link_download(channel_id=channel_id, resolution="1080p")
            elif resolution == "7":
                youtube_obj.channel_scrap_link_download(channel_id=channel_id, resolution="high")
            else:
                print(Style.RESET_ALL)
                print(Fore.RED + Style.DIM)
                print("Wrong resolution selected")
                print(Style.RESET_ALL)

        elif get_opt == "4":
            exit()
        else:
            print(Fore.RED + f"Wrong Option Selected")
            print(Style.RESET_ALL)
