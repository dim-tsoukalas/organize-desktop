import os
import shutil

destination_folder = 'C:/Users/tzima/Documents/Downloads/'
source_folder = 'C:/Users/tzima/Downloads/'

##The program moves the files from Downloads directory to Documents directory##

def org():

    for filename in os.listdir(source_folder):

        source = source_folder + filename
        destination = destination_folder + filename

        if filename.endswith('.txt'):
           shutil.move(source, get_destination(destination_folder, 'docsPdfFilesDownload', filename))

        elif filename.endswith('.jpeg' ) or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png')  :
            shutil.move(source, get_destination(destination_folder, 'photosDownload', filename))

        elif filename.endswith('.doc') or filename.endswith('.docx') or filename.endswith('.pdf') or filename.endswith('.pptx'):
            shutil.move(source, get_destination(destination_folder, 'docsPdfFilesDownload', filename))

        elif filename.endswith('.zip'):
           shutil.move(source, get_destination(destination_folder, 'zipFilesDownload', filename))

        elif filename.endswith('.exe'):
           shutil.move(source, get_destination(destination_folder, 'exeFilesDownload', filename))

        elif filename.endswith('.mp3'):
           shutil.move(source, get_destination(destination_folder, 'musicFilesDownload', filename))



def get_destination(d, f, n):
    return d + f +'/'+ n

#Code to run in background when added (or removed) files.

import time
before = dict ([(f, None) for f in os.listdir (source_folder)])
while 1:
    time.sleep (1)
    after = dict ([(f, None) for f in os.listdir (source_folder)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added: 
        print("add")
        org()
    if removed:
        print("remove")
    
    before = after
