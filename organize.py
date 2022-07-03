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

        elif filename.endswith('.doc') or filename.endswith('.docx') or filename.endswith('.pdf'):
            shutil.move(source, get_destination(destination_folder, 'docsPdfFilesDownload', filename))

        elif filename.endswith('.zip'):
           shutil.move(source, get_destination(destination_folder, 'zipFilesDownload', filename))

def get_destination(d, f, n):
    return d + '/' + n + f 


org()