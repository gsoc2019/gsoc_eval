
import sys,os,cgi
from urllib.request import urlopen
import requests
from tqdm import tqdm
import math



def fromURL(URL, path_to_dir, override_reporthook=None):

    link = URL
    remotefile = urlopen(link)

    params = cgi.parse_header(remotefile.info()['Content-Disposition'])[1]
    file_name = params["filename"]
    path_to_file = os.path.abspath(os.path.join(path_to_dir,file_name))

    print(path_to_file)

    r = requests.get(link, stream=True)


    #=============================== Progress bar =====================================#
    # Total size in bytes.
    total_size = int(r.headers.get('Content-Length', 0)); 
    block_size = 1024
    wrote = 0 
    with open(path_to_file, 'wb') as f:
        for data in tqdm(r.iter_content(block_size), total=math.ceil(total_size//block_size) , unit='KB'):
            wrote = wrote  + len(data)
            f.write(data)

    if total_size != 0 and wrote != total_size:
        raise Exception("ERROR, something went wrong while downloading")  

    #=============================== Progress bar =====================================#
    pass