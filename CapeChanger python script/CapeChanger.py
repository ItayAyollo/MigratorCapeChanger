import tkinter
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import os
from pathlib import Path
import shutil

root = Tk()
root.withdraw()

root.title("Migrator Cape Changer")

location = 'location.txt'
f = open(location, "r")
capeLocation = f.readline() + '/assets/skins/17'
print(capeLocation)

file_path = filedialog.askopenfilename()
print(file_path)
p = Path(file_path)
name_without_extension = p.stem
ext = p.suffix
newfilename = '17f76a23ff4d227a94ea3d5802dccae9f2ae9aa9'
try:
    os.remove(capeLocation + '/' + newfilename)
except:
    pass
shutil.move(file_path, capeLocation)
p = Path(capeLocation + '/' + name_without_extension + ext)
ext = ''
p.rename(Path(p.parent, newfilename + ext))
print(p)
tkinter.messagebox.showinfo("Success!","Cape has been updated! Restart Minecraft to see the changes")