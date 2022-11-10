# importing libraries
# import cv2
# import threading
# from threading import Thread
# import numpy as np
# import os
import time
import anvil.server
import subprocess
#from main import *
import asyncio
from datetime import datetime
from datetime import date
from subprocess import run

anvil.server.connect("CCU42CW2B2ZO4V27FQAYQHPC-CIIC57VJWOA7ZUBO")
v = 0
p = 0
x = 0
today = 0
now = 0
start_time_1 = ''
end_time_1 = ''
date_start_set_1 = ''
date_end_set_1 = ''

start_time_2 = ''
end_time_2 = ''
date_start_set_2 = ''
date_end_set_2 = ''

start_time_3 = ''
end_time_3 = ''
date_start_set_3 = ''
date_end_set_3 = ''

start_time_4 = ''
end_time_4 = ''
date_start_set_4 = ''
date_end_set_4 = ''

video_1_play = ''
video_2_play = ''
video_3_play = ''
video_4_play = ''

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
    print(p)

@anvil.server.callable
def stop_video():
    global p
    global v
    if v == 1:
        p.kill()
    v = 0

@anvil.server.callable
def send_file(media, file_name):
    with open(f"{file_name}", "wb") as f:
        f.write(media.get_bytes())

@anvil.server.callable
def send_date_and_time(start_1, end_1, date_start_1, date_end_1,
                       start_2, end_2, date_start_2, date_end_2,
                       start_3, end_3, date_start_3, date_end_3,
                       start_4, end_4, date_start_4, date_end_4,
                       video_1, video_2, video_3, video_4):
    global start_time_1, end_time_1, date_start_set_1, date_end_set_1, start_time_2, end_time_2, date_start_set_2, date_end_set_2, start_time_3, end_time_3, date_start_set_3, date_end_set_3, start_time_4, end_time_4, date_start_set_4, date_end_set_4, video_1_play, video_2_play, video_3_play, video_4_play
    global p
    start_time_1 = start_1
    end_time_1 = end_1
    date_start_set_1 = date_start_1
    date_end_set_1 = date_end_1
    start_time_2 = start_2
    end_time_2 = end_2
    date_start_set_2 = date_start_2
    date_end_set_2 = date_end_2
    start_time_3 = start_3
    end_time_3 = end_3
    date_start_set_3 = date_start_3
    date_end_set_3 = date_end_3
    start_time_4 = start_4
    end_time_4 = end_4
    date_start_set_4 = date_start_4
    date_end_set_4 = date_end_4
    video_1_play = video_1
    video_2_play = video_2
    video_3_play = video_3
    video_4_play = video_4

@anvil.server.background_task
def date_and_time():
    global start_time_1, end_time_1, date_start_set_1, date_end_set_1, start_time_2, end_time_2, date_start_set_2, date_end_set_2, start_time_3, end_time_3, date_start_set_3, date_end_set_3,start_time_4, end_time_4, date_start_set_4, date_end_set_4, video_1_play, video_2_play, video_3_play, video_4_play
    global p
    global v

    while True:
        send_date_and_time(start_time_1, end_time_1, date_start_set_1, date_end_set_1, start_time_2, end_time_2, date_start_set_2, date_end_set_2, start_time_3, end_time_3, date_start_set_3, date_end_set_3, start_time_4, end_time_4, date_start_set_4, date_end_set_4, video_1_play, video_2_play, video_3_play, video_4_play)
        video_file = ''
        print(start_time_1, end_time_1, date_start_set_1, date_end_set_1, start_time_2, end_time_2, date_start_set_2, date_end_set_2, start_time_3, end_time_3, date_start_set_3, date_end_set_3, start_time_4, end_time_4, date_start_set_4, date_end_set_4, video_1_play, video_2_play, video_3_play, video_4_play)
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(today, current_time)

        start_list = [start_time_1, start_time_2, start_time_3, start_time_4]
        end_list = [end_time_1, end_time_2, end_time_3, end_time_4]
        date_start_list = [date_start_set_1, date_start_set_2, date_start_set_3, date_start_set_4]
        date_end_list = [date_end_set_1, date_end_set_2, date_end_set_3, date_end_set_4]
        video_list = [video_1_play, video_2_play, video_3_play, video_4_play]
        print(p)
        x = 0
        for i in start_list:
            if current_time == end_list[x] and str(today) == str(date_end_list[x]):
                p.kill()
                v = 0

            if current_time == start_list[x] and str(today) == str(date_start_list[x]) and v == 0:
                p = subprocess.Popen("exec " + f"ffplay -loop 0 -fs {video_list[x]}", stdout=subprocess.PIPE, shell=True)
                v = 1
            x += 1

        time.sleep(1)

date_and_time()
anvil.server.wait_forever()
