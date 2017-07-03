from gpiozero import *
from picamera import *
from time import *
from guizero import *

#Takes 3 pictures
def take_picture():
        global output
        for i in range(3):
                #Timer
                message.set("\n 3")
                message.color("black")
                message.font_size(100)
                sleep(1)
                message.clear()
                message.set("\n 2")
		message.color("black")
                message.font_size(100)
                sleep(1)
                message.clear()
                message.set("\n 1")
		message.color("black")
                message.font_size(100)
                sleep(1)
                message.clear()
                message.set("SMILE!")
                message.color("red")
                message.font_size(150)
                sleep(1)
                message.clear()
                message.set("Saving image..")
                message.color("black")
                message.font_size(50)
                #image File Name
                output = strftime("/home/pi/mypibooth/photos/image-%d-%m_%H:%M:%S.png", gmtime())
                camera.capture(output, use_video_port=True)
                message.clear()
                message.set("Push the button to take three photos")
                message.color("black")
                message.font_size(50)

#GPIO button asignment
take_pic_btn = Button(25)
take_pic_btn.when_pressed = take_picture

#Camera settings
camera = PiCamera()
camera.resolution = (2556, 1600)
#camera.resolution = (2556, 1440)
#camera.resolution = (1920, 1080)
camera.hflip = True
camera.vflip = True

output = ""

#GUI
app = App("My Pi Booth")
app.attributes("-fullscreen", True)
camera.start_preview(alpha=200)
message = Text(app, "Push the button to take three photos", size=36, color="black", font="Helvetica", grid=None, align=None)
#onscreen button to test if you don't have a physical GPIO button plugged inn:
#new_pic = PushButton(app, take_picture, text="text on button")
app.display()
