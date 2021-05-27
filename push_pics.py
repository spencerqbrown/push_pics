from pushbullet import Pushbullet
from util import get_key
import os

def push_pics(files_list, key_file, device=None, channel=None):
    # initialize pushbullet
    pb = Pushbullet(get_key(key_file))
    
    # remove directories
    files_proc = [f for f in files_list if os.path.isfile(f)]

    # push each file
    for f in files_proc:
        # get filename
        fname = f.split("/")[-1]
        with open(f, "rb") as f_open:
            # upload file
            file_data = pb.upload_file(f_open, fname)
        # push file
        push = pb.push_file(**file_data)