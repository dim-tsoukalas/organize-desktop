import os
import shutil

destination_folder = 'C:/Users/tzima/Documents/'
source_folder = 'C:/Users/tzima/Desktop/'

def org():

    for filename in os.listdir(source_folder):

        source = source_folder + filename
        destination = destination_folder + filename

        if filename.endswith('.txt'):
           shutil.copy(source, destination)

        elif filename.endswith('.jpeg' ) or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png')  :
            shutil.copy(source, destination)

        elif filename.endswith('.doc') or filename.endswith('.docx') or filename.endswith('.pdf'):
            shutil.copy(source, destination)

        elif os.path.isdir(filename):
            shutil.copy(source, destination)

