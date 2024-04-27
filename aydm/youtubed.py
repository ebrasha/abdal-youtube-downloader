"""
 # Project Name: Abdal Youtube Downloader
 # Programmer: Ebrahim Shafiei
 # Programmer WebSite: https://hackers.zone/
 # Programmer Email: Prof.Shafiei@Gmail.com
 # License : MIT
 # Current Date : 2023-02-08
 # Current Time : 4:29 PM
 # File Description: Youtube downloader
"""
import os

from pytube import YouTube
from aydm import dirhndl
from aydm import pubvars
from colorama import Fore, Style, Back, init
import scrapetube
from aydm import linkscrap

# init for Colorama
init()


class ayddownloader:

    def __init__(self):
        dirhndl.youtube_files_storage_hndl()

    def single_audio_link_download(self, link: str) -> None:
        if not linkscrap.LinkScrap.url_validator(link):
            print(Fore.RED + Style.DIM + f"Your link is not valid  => " + link)
            print(Style.RESET_ALL)
            exit()
        if linkscrap.LinkScrap.video_unavailable_checker(link):
            print(Fore.RED + Style.DIM + f"Video unavailable  => " + link)
            print(Style.RESET_ALL)
            exit()

        try:
            youtube_obj = YouTube(link)
            print(Fore.YELLOW + Style.DIM + f"Working on => " + link)
            print(Style.RESET_ALL)
            youtube_obj = youtube_obj.streams.get_audio_only()
            youtube_obj.download(output_path=pubvars.YOUTUBE_FILE_DIR, filename_prefix=pubvars.FILENAME_PREFIX,
                                 skip_existing=True)
            print(Style.RESET_ALL)
            print(Fore.GREEN + Style.DIM)
            print("Download is completed successfully")
            print(Style.RESET_ALL)
        except Exception as ex:
            print(Style.RESET_ALL)
            print(Fore.RED + Style.DIM)
            print("An error has occurred " + ex.__str__())
            print(Style.RESET_ALL)
            pass

    def single_link_download(self, link: str, resolution: str) -> None:
        if not linkscrap.LinkScrap.url_validator(link):
            print(Fore.RED + Style.DIM + f"Your link is not valid  => " + link)
            print(Style.RESET_ALL)
            exit()
        if linkscrap.LinkScrap.video_unavailable_checker(link):
            print(Fore.RED + Style.DIM + f"Video unavailable  => " + link)
            print(Style.RESET_ALL)
            exit()

        try:
            youtube_obj = YouTube(link)
            if resolution == "high":
                print(Fore.YELLOW + Style.DIM + f"Working on => " + link)
                print(Style.RESET_ALL)
                youtube_obj = youtube_obj.streams.get_highest_resolution()
            else:
                print(Fore.YELLOW + Style.DIM + f"Working on => " + link)
                print(Style.RESET_ALL)
                youtube_obj = youtube_obj.streams.get_by_resolution(resolution)
            youtube_obj.download(output_path=pubvars.YOUTUBE_FILE_DIR, filename_prefix=pubvars.FILENAME_PREFIX,
                                 skip_existing=True)
            print(Style.RESET_ALL)
            print(Fore.GREEN + Style.DIM)
            print("Download is completed successfully")
            print(Style.RESET_ALL)
        except Exception as ex:
            print(Style.RESET_ALL)
            print(Fore.RED + Style.DIM)
            print("An error has occurred " + ex.__str__())
            print(Style.RESET_ALL)
            pass

    def multi_link_audio_download(self, link_file: str) -> None:
        with open(link_file, 'r') as youtube_file_open:
            youtube_file_reader = youtube_file_open.readlines()
            total_file_counter = len(youtube_file_reader)
            current_file_counter = 0

            for youtube_link in youtube_file_reader:
                try:
                    if not linkscrap.LinkScrap.url_validator(youtube_link):
                        print(Fore.RED + Style.DIM + f"Your link is not valid  => " + youtube_link)
                        print(Style.RESET_ALL)
                        continue
                    if linkscrap.LinkScrap.video_unavailable_checker(youtube_link):
                        print(Fore.RED + Style.DIM + f"Video unavailable  => " + youtube_link)
                        print(Style.RESET_ALL)
                        continue

                    print(Fore.YELLOW + Style.DIM + f"Working on => " + youtube_link)
                    print(Style.RESET_ALL)
                    current_file_counter += 1
                    print("Statistic: [ " + str(current_file_counter) + " / " + str(total_file_counter) + "  ]")
                    print(Style.RESET_ALL)

                    youtube_obj = YouTube(youtube_link)
                    youtube_obj = youtube_obj.streams.get_audio_only()
                    youtube_obj.download(output_path=pubvars.YOUTUBE_FILE_DIR, filename_prefix=pubvars.FILENAME_PREFIX,
                                         skip_existing=True)

                    print(Fore.GREEN + Style.DIM)
                    print("Download is completed successfully")
                    print(Style.RESET_ALL)

                except Exception as ex:
                    print(Style.RESET_ALL)
                    print(Fore.RED + Style.DIM)
                    print("An error has occurred: " + str(ex))
                    print(Style.RESET_ALL)

    def multi_link_download(self, link_file: str, resolution: str) -> None:
        with open(link_file, 'r') as youtube_file_open:
            youtube_file_reader = youtube_file_open.readlines()
            total_file_counter = len(youtube_file_reader)
            current_file_counter = 0

            for youtube_link in youtube_file_reader:
                try:
                    if not linkscrap.LinkScrap.url_validator(youtube_link):
                        print(Fore.RED + Style.DIM + f"Your link is not valid  => " + youtube_link)
                        print(Style.RESET_ALL)
                        continue

                    if linkscrap.LinkScrap.video_unavailable_checker(youtube_link):
                        print(Fore.RED + Style.DIM + f"Video unavailable  => " + youtube_link)
                        print(Style.RESET_ALL)
                        continue

                    print(Fore.YELLOW + Style.DIM + f"Working on => " + youtube_link)
                    print(Style.RESET_ALL)
                    current_file_counter += 1
                    print("Statistic: [ " + str(current_file_counter) + " / " + str(total_file_counter) + "  ]")
                    print(Style.RESET_ALL)

                    youtube_obj = YouTube(youtube_link)
                    if resolution == "high":
                        youtube_obj = youtube_obj.streams.get_highest_resolution()
                    else:
                        youtube_obj = youtube_obj.streams.get_by_resolution(resolution)

                    youtube_obj.download(output_path=pubvars.YOUTUBE_FILE_DIR, filename_prefix=pubvars.FILENAME_PREFIX,
                                         skip_existing=True)

                    print(Fore.GREEN + Style.DIM)
                    print("Download is completed successfully")
                    print(Style.RESET_ALL)

                except Exception as ex:
                    print(Style.RESET_ALL)
                    print(Fore.RED + Style.DIM)
                    print("An error has occurred: " + str(ex))
                    print(Style.RESET_ALL)

    def channel_scrap_link_download(self, channel_id: str, resolution: str) -> None:
        link_file = "temp_link_ayd.txt"
        try:
            # os.remove(link_file) # Uncomment if you want to delete the file each time before use
            with open(link_file, 'w') as youtube_file_open:
                videos = scrapetube.get_channel(channel_id)
                print(Fore.YELLOW + Style.DIM + f"Start Scrapping on your channel => " + channel_id)
                print(Style.RESET_ALL)
                channel_link_counter = 0
                for video in videos:
                    youtube_file_open.write("https://www.youtube.com/watch?v=" + video['videoId'] + "\n")
                    channel_link_counter += 1
                    print(Fore.YELLOW + Style.DIM + f"find link :  => " + "https://www.youtube.com/watch?v=" + video[
                        'videoId'])
                    print(Style.RESET_ALL)

            if channel_link_counter < 1:
                print(Fore.RED + Style.DIM + "Something wrong. I can't get any link. Check the channel ID or network!")
                return  # Early return if no links were found

            with open(link_file, 'r') as youtube_file_open:
                youtube_file_reader = youtube_file_open.readlines()
                total_file_counter = len(youtube_file_reader)
                current_file_counter = 0

                for youtube_link in youtube_file_reader:
                    try:
                        if linkscrap.LinkScrap.video_unavailable_checker(youtube_link):
                            print(Fore.RED + Style.DIM + f"Video unavailable  => " + youtube_link)
                            print(Style.RESET_ALL)
                            continue

                        print(Fore.YELLOW + Style.DIM + f"Working on => " + youtube_link)
                        print(Style.RESET_ALL)
                        current_file_counter += 1
                        print("Statistic: [ " + str(current_file_counter) + " / " + str(total_file_counter) + "  ]")
                        print(Style.RESET_ALL)

                        youtube_obj = YouTube(youtube_link)
                        if resolution == "high":
                            youtube_obj = youtube_obj.streams.get_highest_resolution()
                        else:
                            youtube_obj = youtube_obj.streams.get_by_resolution(resolution)
                        youtube_obj.download(output_path=pubvars.YOUTUBE_FILE_DIR,
                                             filename_prefix=pubvars.FILENAME_PREFIX, skip_existing=True)

                        print(Fore.GREEN + Style.DIM)
                        print("Download is completed successfully")
                        print(Style.RESET_ALL)

                    except Exception as ex:
                        print(Style.RESET_ALL)
                        print(Fore.RED + Style.DIM)
                        print("An error has occurred: " + str(ex))
                        print(Style.RESET_ALL)

        except Exception as ex:
            print(Style.RESET_ALL)
            print(Fore.RED + Style.DIM)
            print("An error has occurred: " + str(ex))
            print(Style.RESET_ALL)
