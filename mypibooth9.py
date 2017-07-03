from gpiozero import *
from picamera import *
from time import *
from guizero import *

def take_picture():
        global output
        #take 3 pics
        for i in range(3):
                #timer
                message.set("\n 3")
                message.color("black")
                message.font_size(100)
                sleep(1)
                message.clear()
                message.set("\n 2")
                sleep(1)
                message.clear()
                message.set("\n 1")
                sleep(1)
                message.clear()
                message.set("SMIIIIL! \n*klikk*")
                message.color("red")
                message.font_size(100)
                sleep(1)
                message.clear()
                message.set("Lagrer bilde..")
                message.color("black")
                message.font_size(50)
                #image File Name
                output = strftime("/home/pi/mypibooth/photos/image-%d-%m_%H:%M:%S.png", gmtime())
                camera.capture(output, use_video_port=True)
                message.clear()
                message.set("Trykk pa knappen for a ta 3 bilder!")
                message.color("black")
                message.font_size(50)

#GPIO button asignment
take_pic_btn = Button(25)
take_pic_btn.when_pressed = take_picture

#camera settings
camera = PiCamera()
camera.resolution = (1920, 1200) #other resolution options 3000, 1700. 2556, 1600.2556, 1440.1920, 1080
camera.hflip = True
camera.vflip = True

output = ""

#GUI
app = App("My Pi Booth")
app.attributes("-fullscreen", True)
camera.start_preview(alpha=200)
message = Text(app, "Trykk pa knappen for a ta 3 bilder!", size=36, color="black", font="Helvetica", grid=None, align=None)
#new_pic = PushButton(app, take_picture, text="Ta bilde")
app.display()
