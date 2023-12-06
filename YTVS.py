"""written by Mr.Nill"""
from pytube import YouTube
from os import system as nill
nill("clear")
try:nill("mkdir /sdcard/YT-VIDEO")
except:pass
nill("clear")
logo = """-----------------
  ╦ ╦╔╦╗╦  ╦╔═╗
  ╚╦╝ ║ ╚╗╔╝╚═╗
   ╩  ╩  ╚╝ ╚═╝
-----------------"""
save_path = "/sdcard/YT-VIDEO/"
def cls():
    nill("clear")
    print(logo)
def download_video(url, save_path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        cls()
        print("Downloading Video")
        video.download(save_path)
        cls()
        print("Download successful!")
    except Exception as e:
        exit("Error")
def download_shorts(url, save_path):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(file_extension="mp4").first()
        cls()
        print(f"Downloading Shorts")
        video.download(save_path)
        cls()
        print("Shorts download successful!")
    except Exception as e:
        exit("Error")
cls()
option = input("[1] VIDEO Download\n[2] Shorts Download\n\n[?] Choice : ")
if option == '1':
    cls()
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url, save_path)
elif option == '2':
    cls()
    shorts_url = input("Enter the YouTube Shorts URL: ")
    download_shorts(shorts_url, save_path)
else:
    exit("Invalid option")
  
