#!/usr/bin/env python3
from __future__ import print_function
import subprocess
import time
import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.slider import Slider
import time

Window.size = (480, 120)
image_label = 'Convert jpg, jpeg, png, or pdf\n          into video loop'
stream_name = "streamGUIfile"

class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        global x
        global z
        super(MyLayout, self).__init__(**kwargs)

        self.cols = 1
        self.z = 40

        self.startGrid = GridLayout()
        self.startGrid.cols = 3
        self.startGrid.padding = 4
        self.startGrid.spacing = 2
        self.startGrid.size_hint_y = .2
        self.add_widget(self.startGrid)

        self.ProcessButton = Button(text= image_label, background_color='gray', size_hint_x=0.45, size_hint_y=0.1)
        self.startGrid.add_widget(self.ProcessButton)
        self.ProcessButton.bind(on_press=self.Process)

        
        self.PlayButton = Button(text='Play Video Loop', background_color='gray', background_normal= '', size_hint_x=0.45, size_hint_y=0.1)
        self.startGrid.add_widget(self.PlayButton)
        self.PlayButton.bind(on_press=self.Play)

    
    def Process(self, instance):
        try:
             os.system("ffmpeg -framerate 1/10 -i /home/tylermorton670/video_looper/image_process/*.jpeg -c:v libx264 -y -r 1 -pix_fmt yuv420p /home/tylermorton670/video_looper/video_loops/loopSlide.mp4")
        except:
            pass
        try:
            os.system("ffmpeg -framerate 1/10 -i /home/tylermorton670/video_looper/image_process/*.jpg -c:v libx264 -y -r 1 -pix_fmt yuv420p /home/tylermorton670/video_looper/video_loops/loopSlide.mp4")
        except:
            pass
        try:
            os.system("ffmpeg -framerate 1/10 -i /home/tylermorton670/video_looper/image_process/*.png -c:v libx264 -y -r 1 -pix_fmt yuv420p /home/tylermorton670/video_looper/video_loops/loopSlide.mp4")
        except:
            pass
        try:
            os.system("pdftoppm -png /home/tylermorton670/video_looper/image_process/*.pdf /home/tylermorton670/video_looper/image_process/loopSlide")
            os.system("ffmpeg -framerate 1/10 -i /home/tylermorton670/video_looper/image_process/loopSlide-1.png -c:v libx264 -y -r 1 -pix_fmt yuv420p /home/tylermorton670/video_looper/video_loops/loopSlide.mp4")
        except:
            pass

#        try:
#            os.system("ffmpeg -i /home/tylermorton670/video_looper/image_process/*.mov -vcodec h264 -acodec mp3 -y /home/tylermorton670/video_looper/video_loops/loopSlide.mp4")
#        except:
#            pass

        self.ProcessButton.text = 'Image Processing Completed'

    def Play(self, instance):
        self.ProcessButton.text = image_label
        os.system("ffmpeg -re -stream_loop -1 -i /home/tylermorton670/video_looper/video_loops/*.mp4 -f opengl 'video_loop'")
        os.system("ffmpeg -re -stream_loop -1 -i /home/tylermorton670/video_looper/video_loops/*.mov -f opengl 'video_loop'")

class MyApp(App):
    def build(self):
        return MyLayout()


# run Say Hello App Calss
if __name__ == "__main__":
    MyApp().run()
