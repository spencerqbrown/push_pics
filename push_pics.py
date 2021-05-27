from pushbullet import Pushbullet
from util import get_key
import os

def push_pics(source_dir):
    # initialize pushbullet
    pb = Pushbullet(get_key())
    
    # get files in directory
    files_raw = os.listdir(source_dir)
    print("full files_raw:")
    print(files_raw)
    print("each element of files_raw:")
    
    # remove directories
    files_proc = [os.path.join(source_dir, f) for f in files_raw if os.path.isfile(os.path.join(source_dir, f))]

    # push each file
    for f in files_proc:
        # get filename
        fname = f.split("\\")[-1]
        with open(f, "rb") as f_open:
            # upload file
            file_data = pb.upload_file(f_open, "fname")
        # push file
        push = pb.push_file(**file_data)