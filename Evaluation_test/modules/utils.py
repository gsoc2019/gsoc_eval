import os,shutil

def image_file_extract(path_ds):
    path = path_ds.split('/')
    path.remove('')
    filter(None, path)
    file_name = '.'.join(path[:-1]) + '.png'
    
    return file_name



def make_dirs(dir_path,opt):

    def opts(arg):
        modes={
            'a':append,
            'r':replace
        }
        return modes.get(arg,'Invalid argument')

    def append():
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        else:
            pass

    def replace():
        pass

    return opts(opt)()
