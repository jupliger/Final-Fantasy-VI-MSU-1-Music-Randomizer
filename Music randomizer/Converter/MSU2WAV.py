import os
import re
import subprocess

MP3Folder = os.path.abspath("Music")

for root, dir, files in os.walk(MP3Folder):
    for name in files:
        if name.endswith(".pcm"):
            subprocess.call(["msu2wav.exe", os.path.join(MP3Folder, name), os.path.join(MP3Folder, name).strip(".pcm")+".wav"])
