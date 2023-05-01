from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ",yt.title)
print("Views: ",yt.views)
print("Description:\n",yt.description,sep='')
yd = yt.streams.get_highest_resolution()
print(yd)
yd.download('D:/Youtube')