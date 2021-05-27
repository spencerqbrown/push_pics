from pushbullet import Pushbullet
from util import get_key

pb = Pushbullet(get_key())
# push = pb.push_note("TEST TITLE 1", "TEST BODY 1")

with open("./test_dir/download.png", "rb") as test_pic:
    file_data = pb.upload_file(test_pic, "TEST PICTURE 1.png")

push = pb.push_file(**file_data)