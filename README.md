# youtobe-install

A collection of Termux scripts for downloading audio and video from YouTube using `yt-dlp`.

## Files

### `install_song.py`
Downloads YouTube videos as **MP3 audio files** to your device's Downloads folder.

**What it does:**
1. Updates and upgrades Termux packages
2. Installs Python and FFmpeg
3. Installs yt-dlp tool
4. Requests storage permissions
5. Prompts for a YouTube URL
6. Downloads the video and converts it to MP3 format

**Usage:**
```bash
python install_song.py
```

### `install_video.py`
Downloads YouTube videos as **MP4 video files** to your device's Downloads folder.

**What it does:**
1. Updates Termux packages
2. Installs Python and FFmpeg
3. Installs/updates yt-dlp tool
4. Requests storage permissions
5. Prompts for a YouTube URL
6. Downloads the video in best available quality and merges it into MP4 format

**Usage:**
```bash
python install_video.py
```

## Requirements
- Termux environment
- Python 3
- FFmpeg
- yt-dlp

## Installation
Simply run either script with Python to automatically install all dependencies.
