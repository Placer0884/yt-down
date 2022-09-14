from turtle import down
from pytube import YouTube
from pytube import Playlist
import re
from ptube_lib import *

#print(Playlist("https://www.youtube.com/playlist?list=PLaIm748yXaWNghljhUxEE8mpPOoaMNMiX"))

def format():
    string = "www.google.com -p"


    print(" FLAG FOUND")
    command = re.sub(" -p", "", string)

    print(command)



#download_playlist("https://youtube.com/playlist?list=PL58sUHpK1HSCgWe_SfsBcqNSZYOVAjMv3")


download("pytube.__main__.YouTube object: videoId=KO_3ZPkezdQ")