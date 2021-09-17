import getpass
import os
import shutil

path = fr"C:/Users/{getpass.getuser()}/Downloads"
target_images = fr"C:/Users/{getpass.getuser()}/Downloads/images"
target_audios = fr"C:/Users/{getpass.getuser()}/Downloads/audios"
target_videos = fr"C:/Users/{getpass.getuser()}/Downloads/videos"
target_apps = fr"C:/Users/{getpass.getuser()}/Downloads/exes"
target_zipfile = fr"C:/Users/{getpass.getuser()}/Downloads/zip files"
target_docs = fr"C:/Users/{getpass.getuser()}/Downloads/documents"

images = []
audios = []
videos = []
exes = []
zips = []
docs = []
try:
    os.mkdir(target_images)
    os.mkdir(target_audios)
    os.mkdir(target_videos)
    os.mkdir(target_apps)
    os.mkdir(target_zipfile)
    os.mkdir(target_docs)

except FileExistsError:
    pass

downloads = os.listdir(path)
for i in range(len(downloads)):
    if "jpg" in downloads[i].split("."):
        images.append(downloads[i])
    if "png" in downloads[i].split("."):
        images.append(downloads[i])
    if "jpeg" in downloads[i].split("."):
        images.append(downloads[i])
    if "tif" in downloads[i].split("."):
        images.append(downloads[i])
    if "tiff" in downloads[i].split("."):
        images.append(downloads[i])
    if "bmp" in downloads[i].split("."):
        images.append(downloads[i])
    if "gif" in downloads[i].split("."):
        images.append(downloads[i])
    if "eps" in downloads[i].split("."):
        images.append(downloads[i])
    if "raw" in downloads[i].split("."):
        images.append(downloads[i])
    if "cr2" in downloads[i].split("."):
        images.append(downloads[i])
    if "nef" in downloads[i].split("."):
        images.append(downloads[i])
    if "orf" in downloads[i].split("."):
        images.append(downloads[i])
    if "sr2" in downloads[i].split("."):
        images.append(downloads[i])

    if "m4a" in downloads[i].split("."):
        audios.append(downloads[i])
    if "flac" in downloads[i].split("."):
        audios.append(downloads[i])
    if "mp3" in downloads[i].split("."):
        audios.append(downloads[i])
    if "wav" in downloads[i].split("."):
        audios.append(downloads[i])
    if "wma" in downloads[i].split("."):
        audios.append(downloads[i])
    if "aac" in downloads[i].split("."):
        audios.append(downloads[i])

    if "mp4" in downloads[i].split("."):
        videos.append(downloads[i])
    if "mov" in downloads[i].split("."):
        videos.append(downloads[i])
    if "wmv" in downloads[i].split("."):
        videos.append(downloads[i])
    if "flv" in downloads[i].split("."):
        videos.append(downloads[i])
    if "AVI" in downloads[i].split("."):
        videos.append(downloads[i])
    if "AVCHD" in downloads[i].split("."):
        videos.append(downloads[i])
    if "webm" in downloads[i].split("."):
        videos.append(downloads[i])
    if "mkv" in downloads[i].split("."):
        videos.append(downloads[i])

    if "zip" in downloads[i].split("."):
        zips.append(downloads[i])
    if "rar" in downloads[i].split("."):
        zips.append(downloads[i])
    if "tar" in downloads[i].split("."):
        zips.append(downloads[i])
    if "gz" in downloads[i].split("."):
        zips.append(downloads[i])
    if "7z" in downloads[i].split("."):
        zips.append(downloads[i])

    if "exe" in downloads[i].split("."):
        exes.append(downloads[i])

    if "doc" in downloads[i].split("."):
        docs.append(downloads[i])
    if "docx" in downloads[i].split("."):
        docs.append(downloads[i])
    if "html" in downloads[i].split("."):
        docs.append(downloads[i])
    if "htm" in downloads[i].split("."):
        docs.append(downloads[i])
    if "odt" in downloads[i].split("."):
        docs.append(downloads[i])
    if "pdf" in downloads[i].split("."):
        docs.append(downloads[i])
    if "xls" in downloads[i].split("."):
        docs.append(downloads[i])
    if "xlsx" in downloads[i].split("."):
        docs.append(downloads[i])
    if "ods" in downloads[i].split("."):
        docs.append(downloads[i])
    if "ppt" in downloads[i].split("."):
        docs.append(downloads[i])
    if "pptx" in downloads[i].split("."):
        docs.append(downloads[i])
    if "txt" in downloads[i].split("."):
        docs.append(downloads[i])

for i in range(len(images)):
    shutil.move(f"{path}/{images[i]}", f"{target_images}/{images[i]}")

for i in range(len(audios)):
    shutil.move(f"{path}/{audios[i]}", f"{target_audios}/{audios[i]}")

for i in range(len(videos)):
    shutil.move(f"{path}/{videos[i]}", f"{target_videos}/{videos[i]}")

for i in range(len(exes)):
    shutil.move(f"{path}/{exes[i]}", f"{target_apps}/{exes[i]}")

for i in range(len(zips)):
    shutil.move(f"{path}/{zips[i]}", f"{target_zipfile}/{zips[i]}")

for i in range(len(docs)):
    shutil.move(f"{path}/{docs[i]}", f"{target_docs}/{docs[i]}")
