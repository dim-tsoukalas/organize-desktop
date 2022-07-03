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
           shutil.copy(source, get_destination(destination_folder, 'docsPdfFilesDownload', filename))

        elif filename.endswith('.jpeg' ) or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png')  :
            shutil.copy(source, get_destination(destination_folder, 'photosDownload', filename))

        elif filename.endswith('.doc') or filename.endswith('.docx') or filename.endswith('.pdf') or filename.endswith('.pptx'):
            shutil.copy(source, get_destination(destination_folder, 'docsPdfFilesDownload', filename))

        elif filename.endswith('.zip'):
           shutil.copy(source, get_destination(destination_folder, 'zipFilesDownload', filename))

        elif filename.endswith('.exe'):
           shutil.copy(source, get_destination(destination_folder, 'exeFilesDownload', filename))

        elif filename.endswith('.mp3'):
           shutil.copy(source, get_destination(destination_folder, 'musicFilesDownload', filename))



def get_destination(d, f, n):
    return d + f +'/'+ n


org()