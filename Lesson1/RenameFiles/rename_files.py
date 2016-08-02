import os


def rename_files(path):

    for file_name in os.listdir(path):

        os.chdir(path)
        os.rename(file_name, file_name.translate(None, '0123456789'))
        print 'file {} changed name to {}'.format(file_name, file_name.translate(None, '0123456789'))

rename_files('/home/scandie/prank/')
