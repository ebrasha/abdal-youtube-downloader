"""
 # Project Name: Abdal Youtube Downloader
 # Programmer: Ebrahim Shafiei
 # Programmer WebSite: https://hackers.zone/
 # Programmer Email: Prof.Shafiei@Gmail.com
 # License : MIT
 # Current Date : 2023-02-08
 # Current Time : 5:26 PM
 # File Description: no description
"""
import os
from aydm import pubvars


def youtube_files_storage_hndl():
    if not os.path.exists(pubvars.YOUTUBE_FILE_DIR):
        os.makedirs(pubvars.YOUTUBE_FILE_DIR)

