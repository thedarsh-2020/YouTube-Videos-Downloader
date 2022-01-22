import sys
from pytube import YouTube
from pytube.cli import on_progress
from pytube import Playlist
from tkinter import Tk, filedialog


def v_or_pl():
    print("To download video press 1")
    print("To download PlayList press 2")


def check_res():
    print("\nEnter Resolution like (240, 360, 720,...) from the above list: ")
    while 1:
        r_bef = input()
        r = r_bef.replace(" ", "")
        if r == '2160' or r == '2160p':
            r = '2160p'
            return r
        elif r == '1440' or r == '1440p':
            r = '1440p'
            return r
        elif r == '1080' or r == '1080p':
            r = '1080p'
            return r
        elif r == '720' or r == '720p':
            r = '720p'
            return r
        elif r == '480' or r == '480p':
            r = '480p'
            return r
        elif r == '360' or r == '360p':
            r = '360p'
            return r
        elif r == '240' or r == '240p':
            r = '240p'
            return r
        elif r == '144' or r == '144p':
            r = '144p'
            return r
        else:
            print("Invalid input, please enter a valid resolution...")


def v_pl_inp():
    while 1:
        i_bef = input("1 or 2: ")
        i = i_bef.replace(" ", "")
        if i == '1':
            print("\nDownloading Highest Res. without choosing?!")
            while 1:
                x_bef = input("Y or N: ")
                x = x_bef.replace(" ", "")
                if x == 'Y' or x == 'y' or x == 'N' or x == 'n':
                    print("\nPlease input YouTube Video Link: ")

                    # taking video link
                    while 1:
                        link_bef = input()
                        link = link_bef.replace(" ", "")
                        try:
                            video = YouTube(link, on_progress_callback=on_progress)
                            break
                        except:
                            print("Invalid input, please enter a valid video link...")
                    # End of taking video link

                    # Download High Resolution
                    if x == 'Y' or x == 'y':
                        print("\nPlease enter file location:")
                        root = Tk()
                        root.withdraw()
                        root.attributes('-topmost', True)
                        file_loc = filedialog.askdirectory()
                        print(file_loc)
                        while 1:
                            input("\nPlease, be sure internet connection, then press ENTER to continue...")
                            print("Downloading in Progress...")
                            try:
                                video.streams.get_highest_resolution().download(output_path=file_loc)
                                break
                            except:
                                print("Error, no internet connection...")
                    # End of downloading High Resolution

                    # Selecting resolution & download it
                    else:
                        # Printing video res
                        while 1:
                            try:
                                input("\nPlease, be sure internet connection, then press ENTER to continue...")
                                print("\nVideo Resolution List:")
                                for stream in video.streams.filter(progressive=True, subtype='mp4'):
                                    print("res:", stream.resolution, "-", "size:",
                                          (stream.filesize / 1000000).__round__(), "MegaByte")
                                break
                            except:
                                print("Error, no internet connection...")
                        # End of printing video res

                        # taking input res
                        while 1:
                            r_e_s = check_res()
                            for stream2 in video.streams.filter(progressive=True, subtype='mp4'):
                                if r_e_s == stream2.resolution:

                                    # Choosing location
                                    print("\nPlease enter file location:")
                                    root = Tk()
                                    root.withdraw()
                                    root.attributes('-topmost', True)
                                    file_loc = filedialog.askdirectory()
                                    print(file_loc)
                                    # End of choosing a location

                                    # Download selected resolution
                                    while 1:
                                        input("\nPlease, be sure internet connection, then press ENTER to continue...")
                                        print("Downloading in Progress...")
                                        try:
                                            for down_res in video.streams.filter(progressive=True, subtype='mp4', res=r_e_s):
                                                down_res.download(output_path=file_loc)
                                                break
                                            break
                                        except:
                                            print("Error, no internet connection...")
                                    # Finish Downloading

                                    print("\nDownloading is Done, Enjoy 😉")
                                    input("Press ENTER to exit")
                                    sys.exit()
                            print("Resolution not found, please choose from the above list...")
                        # End of taking res

                    break
                    # End
                else:
                    print("Wrong input, please enter a valid input")
            break

        # Downloading PlayList
        elif i == '2':

            # taking playlist link
            print("\nPlease input YouTube PlayList Link: ")
            while 1:
                playlist_before = input()
                playlist_link = playlist_before.replace(" ", "")
                playlist_videos = Playlist(playlist_link)
                try:
                    if len(playlist_videos.playlist_id) == 34:
                        break
                    else:
                        print("link is not a playlist link, please enter a playlist link...")
                except:
                    print("Invalid input, please enter a valid playlist link...")
            # End of taking playlist link

            # Choosing location & downloading video
            print("\nPlease enter file location:")
            root = Tk()
            root.withdraw()
            root.attributes('-topmost', True)
            file_loc = filedialog.askdirectory()
            print(file_loc)
            # End of choosing a location

            # Downloading playlist
            while 1:
                input("\nPlease, be sure internet connection, then press ENTER to continue...")
                print("Downloading in Progress...")
                try:
                    for video in playlist_videos.videos:
                        video.streams.get_highest_resolution().download(output_path=file_loc)
                    break
                except:
                    print("Error, no internet connection...")
            # End of downloading a playlist

            break
        # End of PlayList
        else:
            print("Wrong input, please enter a valid input")


print("Hello 😊")
v_or_pl()
v_pl_inp()
print("\nDownloading is Done, Enjoy 😉")
input("Press ENTER to exit")
