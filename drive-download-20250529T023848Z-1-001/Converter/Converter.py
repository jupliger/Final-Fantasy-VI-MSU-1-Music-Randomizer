import os
import re
import shutil
import random
import subprocess

root = os.curdir
Music = os.listdir("Music")
MP3s = os.path.join(root, "MP3s")
under_score = ['(',')','[',']'] 
dot = [' ']
wav2msuExtensions = (".wav",".ogg",".flac")
ffmpegExtensions = (".mp3",".mp4")
normalizeExtensions = (".mp3",".mp4",".wav")
MP3Folder = os.path.abspath("Music")

os.chdir("Music")
for f in Music:
    copy_f = f
    for char in copy_f:
        if (char in dot): copy_f = copy_f.replace(char, '.')
        if (char in under_score): copy_f = copy_f.replace(char,'_')
    os.rename(f,copy_f)
os.chdir("..")

for root, dir, files in os.walk(os.curdir):
    for name in files:
        if name.endswith(normalizeExtensions):
            subprocess.call(["normalize.exe" , "-a 16dBFS", os.path.join(root, name)])

for root, dir, files in os.walk(os.curdir):
   for name in files:
       if name.endswith(ffmpegExtensions):
           subprocess.call(["mpg123.exe", "-w", os.path.join(MP3Folder, name).strip(".mp3")+".wav", os.path.join(MP3Folder, name)])

for root, dir, files in os.walk(os.curdir):
   for name in files:
       if name.endswith(wav2msuExtensions):
           subprocess.call(["wav2msu.exe" , os.path.join(root, name)])
