from pytube import YouTube
from pytube import Playlist
import re


flags = [" -p", " -d"]
download_destination = 'downloads/'


def format(command: str) -> str:
    if any(word in command for word in flags):
        for flag in flags:
            command = re.sub(flag, "", command)
    return command


def download(link:str):
    global not_found_links
    try:
        YouTube(link).streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download(download_destination)
    except:
        if link not in flags:
            print(link, "was not found")




def download_playlist(p_list: str):
    playlist = Playlist(p_list)
    for video in playlist.videos:
        download(video)


def doc_download(command:str):
    while True:
        try:
            links = open(command, "r").readlines()
            break
        except:
            print(command, "was not found")

    for link in links:
        download(link)
