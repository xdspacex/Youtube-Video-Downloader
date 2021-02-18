from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import pafy
from youtube_dl import YoutubeDL

def AudioDownload():
   audio_downloader = YoutubeDL({'format':'mp3'})
   audio_downloader.extract_info(ytdEntry.get())

def VideoDownload():
    YouTube(ytdEntry.get()).streams.first().download(Folder_Name)

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.Open()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="Please Choose a Folder",fg="red")


root = Tk()
root.title("YTD Downloader")
root.geometry("350x400") #set window
root.columnconfigure(0,weight=1)#set all content in center.


ytdLabel = Label(root,text="Enter the URL of the Video",font=("jost",15))
ytdLabel.grid()


ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

locationError = Label(root,text="",fg="red",font=("jost",10))
locationError.grid()

downloadVideobtn = Button(root,text="Download Video",width=13,bg="red",fg="white",command=VideoDownload)
downloadVideobtn.grid()

Space = Label(root,text="",font=("jost",1))
Space.grid()
downloadAudiobtn = Button(root,text="Download Audio",width=13,bg="red",fg="white",command=AudioDownload)
downloadAudiobtn.grid()



root.mainloop()