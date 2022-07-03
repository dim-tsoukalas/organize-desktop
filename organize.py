import os
import shutil

destination_folder = 'C:/Users/tzima/Documents/Downloads/'
source_folder = 'C:/Users/tzima/Downloads/'

def org():

    for filename in os.listdir(source_folder):

        source = source_folder + filename
        destination = destination_folder + filename

        if filename.endswith('.txt'):
           shutil.copy(source, destination_folder+'docsPdfFilesDownload/' + filename)

        elif filename.endswith('.jpeg' ) or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png')  :
            shutil.copy(source, destination_folder+'photosDownload/' + filename)

        elif filename.endswith('.doc') or filename.endswith('.docx') or filename.endswith('.pdf'):
            shutil.copy(source, destination_folder+'docsPdfFilesDownload/' + filename)

        elif filename.endswith('.zip'):
           shutil.copy(source, destination_folder+'zipFilesDownload/' + filename)


org()