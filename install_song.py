import os

os.system("pkg update -y && pkg upgrade -y")
os.system("pkg install -y python ffmpeg")
os.system("pip install yt-dlp")
os.system("termux-setup-storage")

url = input("Link: ")

os.system(
    f'yt-dlp -x --audio-format mp3 -o "/storage/emulated/0/Download/%(title)s.%(ext)s" "{url}"'
)
