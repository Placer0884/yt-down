
from ptube_lib import *




while True:
    command = input("Link to video > ")
    if command == "exit" or command == "end":
        break

    elif "-p" in command:
        download_playlist(command)

    elif "-d" in command:
        doc_download(command)

    else:
        download(command)

