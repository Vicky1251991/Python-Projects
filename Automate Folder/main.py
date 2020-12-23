import os
import sys


def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")


files = os.listdir()
files.remove("main.py")
createIfNotExist("Images")
createIfNotExist("Docs")
createIfNotExist("Media")
createIfNotExist("Zip")
createIfNotExist("Others")



imagesExt = [".jpeg", ".jpg", ".png", ".gif", ".raw"]
images = [file for file in files if os.path.splitext(file)[
    1].lower() in imagesExt]

docsExts = [".docx", ".txt", ".doc", ".pdf"]
docs = [file for file in files if os.path.splitext(file)[
    1].lower() in docsExts]

mediasExts = [
    ".mp4",
    ".mp3",
    ".mov",
    ".3gp",
    ".avi",
    ".flv",
    ".h264",
    ".m4v",
    ".mkv",
]
medias = [file for file in files if os.path.splitext(
    file)[1].lower() in mediasExts]

zipExts = [".zip"]
zips = [file for file in files if os.path.splitext(
    file)[1].lower() in zipExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (
        (ext not in imagesExt)
        and (ext not in docsExts)
        and (ext not in mediasExts)
        and (ext not in zipExts)
        and os.path.isfile(file)
    ):
        others.append(file)

print("WELCOME TO JUNK FILE ORGANIZER")
filter = int(input("If You want to sort by \n""1.Extension press 1: "))
if filter == 1:
    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("Zip", zips)
    move("Others", others)
    print("Done")
