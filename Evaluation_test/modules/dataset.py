from modules import utils
import h5py
import os,csv
import numpy as np
import scipy
import scipy.signal
from matplotlib import pyplot as plt



def scipy_filter(npArray):
        return scipy.signal.medfilt(npArray)



class HDF5:
    
    def __init__(self, hdf5_file):

        self.file_name = hdf5_file
        self.HEAD = h5py.File(hdf5_file,'r')
        self.CACHE = {}
        print(self.HEAD)
        pass


    def purge_cache(self, key = None):
        if not key:
            self.CACHE = {}
        else:
            self.CACHE[key] = None
    

    def cache_features(self, location):
        element = self.HEAD[location]
        if isinstance(element, h5py.Dataset):
            tree = location.split('/')
            name = tree.pop()
            group = '/'.join(tree)
        else:
            return
       
        try:
            dtype=str(element.dtype)
        except:
            dtype=str('unknown_dtype')

        features = {'group':group,'dataset':name, 'shape':element.shape,'size':element.size,'dtype':dtype}
        
        if 'features' not in self.CACHE.keys():
            self.CACHE['features'] = []
        self.CACHE['features'].append(features)

    

    def export_features(self, export_path):
        
        csv_name = 'dataset_' + os.path.basename(self.file_name).split('.')[-2] + '.csv'
        export_file = os.path.abspath(os.path.join(export_path,csv_name))

        self.HEAD.visit(self.cache_features)
        features = self.CACHE['features']

        with open(export_file,'w') as f:
            w = csv.writer(f)        
            try:
                attrs = features[0].keys()
                w.writerow(attrs)
                for feature in features:
                    row = tuple([ feature[attr] for attr in attrs ])
                    w.writerow(row)
            except:
                raise Exception('No features to export')
            


        print('\ndataset-features fetched in :\n'+csv_name)
        self.purge_cache()
        pass



    



    def export_image(self, export_dir, path_ds, height_ds, width_ds, filter = None ):

        flat_img = np.array(self.HEAD[path_ds])
        h = np.array(self.HEAD[height_ds])[0]
        w = np.array(self.HEAD[width_ds])[0]
        img = flat_img.reshape(h,w)

        if filter:
            img = filter(img)

        plt.imshow(img)


        png_name = utils.image_file_extract(path_ds)
        file_path = os.path.abspath(os.path.join(export_dir, png_name))
        plt.imsave(file_path,img)

        print('image saved as : ', file_path)
