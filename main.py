
from ptube_lib import *



def main_function():
    while True:
        command = input("Link to video > ")
        if command == "exit" or command == "end":
            break

        elif "-p" in command:
            command = format(command)
            download_playlist(command)

        elif "-d" in command:
            doc_download(command)

        else:
            download(command)




if __name__ == "__main__":
    main_function()
