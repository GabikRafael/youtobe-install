import os

os.system("pkg update -y")
os.system("pkg install -y python ffmpeg")
os.system("pip install -U yt-dlp")

os.system("termux-setup-storage")

url = input("Link: ")

command = (
    f'yt-dlp -f "bv*+ba/b" '
    f'--merge-output-format mp4 '
    f'-o "/storage/emulated/0/Download/%(title)s.%(ext)s" '
    f'"{url}"'
)

os.system(command)
