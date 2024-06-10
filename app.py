from pytube import YouTube
from sys import argv
import os

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Number of views: ", yt.views)

yd = yt.streams.get_highest_resolution()
download_path = os.path.expanduser("~/Documents/YoutubeDownloads")
yd.download(download_path)