# importing libraries
#import cv2
#import threading
#from threading import Thread
#import numpy as np
#import os
import anvil.server
import subprocess
from subprocess import run

anvil.server.connect("3T4LX5TMNT6JILFBOJEN7EXH-VH6M3NJ4BWUOMHQD")
v = 0
p = 0
        
@anvil.server.callable
def play_video(video_file):
    global p
    global v
    if v == 0:
        p = subprocess.Popen("exec " + f"ffplay -loop 0 -fs {video_file}", stdout=subprocess.PIPE, shell=True)
    else:
        p.kill()
        p = subprocess.Popen("exec " + f"ffplay -loop 0 -fs {video_file}", stdout=subprocess.PIPE, shell=True)
    v = 1

@anvil.server.callable
def stop_video():
    global p
    global v
    v = 0
    p.kill()

@anvil.server.callable
def send_file(media, file_name):
    with open(f"RPI/{file_name}", "wb") as f:
        f.write(media.get_bytes())

anvil.server.wait_forever()
