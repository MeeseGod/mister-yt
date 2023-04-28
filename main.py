# imports
from tkinter import filedialog
from tkinter import *
from yt_dlp import YoutubeDL

def submit():
    URLS = entry.get()
    print(URLS)
    with YoutubeDL() as ydl:
        ydl.download(URLS)

window = Tk()
entry = Entry()

# set window resolution
window.geometry("500x200")

folderSelected = filedialog.askdirectory()

# textEntry widget
entry.insert(0, "Paste Youtube Link")
entry.pack()

# submitButton widget
submit = Button(window, text="submit", command=submit)
submit.pack(side = BOTTOM)

# starts window
window.mainloop()