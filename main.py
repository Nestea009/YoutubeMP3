from pytube import YouTube
import os

def mp3(url, path):
  try:
    yt = YouTube(url)
    print(f"Descargando {yt.title}...")
    yt.streams.get_highest_resolution().download(path)
    print(f"{yt.title} descargado correctamente!")
  except Exception as e:
    print("Ha habido un error descargano el vídeo :P")

url = ""
path = "C:/Users/Néstor/Downloads"

mp3(url, path)