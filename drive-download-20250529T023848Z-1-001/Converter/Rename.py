import os
import re
import shutil
import random
import subprocess

root = os.curdir
MP3s = os.path.join(root, "MP3s")
under_score = ['(',')','[',']'] 
dot = [' ']
wav2msuExtensions = (".wav",".ogg",".flac")
ffmpegExtensions = (".mp3",".mp4")
normalizeExtensions = (".mp3",".mp4",".wav")
MP3Folder = os.path.abspath("Music")
Music = os.listdir("Music")


os.chdir("Music")
for f in Music:
    copy_f = f
    for char in copy_f:
        if (char in dot): copy_f = copy_f.replace(char, '.')
        if (char in under_score): copy_f = copy_f.replace(char,'_')
    os.rename(f,copy_f)
os.chdir("..")
