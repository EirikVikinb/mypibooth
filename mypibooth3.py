from gpiozero import *
from picamera import *
from time import *
from guizero import *

def take_picture():
	global output
	#name of file
	output = strftime("/home/pi/mypibooth/image-%d-%m %H:%M:%S.png", gmtime())
	#take 3 pics
	for i in range(3):
		sleep(3)        
		camera.capture(output)

#GPIO button asignment
take_pic_btn = Button(25)
take_pic_btn.when_pressed = take_picture

#camera settings
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.hflip = True
camera.vflip = True

output = ""

#GUI
app = App("My Pi Booth")
app.attributes("-fullscreen", True)
camera.start_preview(alpha=50)
message = Text(app, "Text above button")
new_pic = PushButton(app, take_picture, text="Text on button")
app.display()
