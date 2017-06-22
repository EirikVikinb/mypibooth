from gpiozero import *
from picamera import *
from time import *
from guizero import *

def take_picture():
  global output
  #take 3 pics
  for i in range(3):
    #timer
		message = Text(app, "3", size=36)
		sleep(1)
		message.clear()
		message = Text(app, "2", size=36)
		sleep(1)
		message.clear()
		message = Text(app, "1", size=36)
		sleep(1)
		message.clear()
		message = Text(app, "SMILE!", size=50, color="red")
		sleep(1)
		message.clear()
    #image File Name
		output = strftime("/home/pi/mypibooth/photos/image-%d-%m_%H:%M:%S.png", gmtime())
		camera.capture(output, use_video_port=True)
		message.clear()

#GPIO button asignment
take_pic_btn = Button(25)
take_pic_btn.when_pressed = take_picture

#camera settings
camera = PiCamera()
camera.resolution = (3000, 1700) #other resolution options 2556, 1600.2556, 1440.1920, 1080
camera.hflip = True
camera.vflip = True

output = ""

#GUI
app = App("My Pi Booth")
app.attributes("-fullscreen", True)
camera.start_preview(alpha=200)
message = Text(app, "Push the big read button to take a picture", size=36, color="black", font="Helvetica", grid=None, align=None)
#new_pic = PushButton(app, take_picture, text="Ta bilde")
app.display()
