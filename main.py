import tkinter
import PIL.Image, PIL.ImageTk
import cv2
from functools import partial
import threading
import imutils
import time

stream = cv2.VideoCapture("") # This parth is incomplete cause video clip is not uploded
flag =True
def play(speed):
    global flag
    print(f"You Clicked on play. Speed {speed}")
    # play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
    grabbed,frame = stream.read()
    if not grabbed:
       exit()
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
     canvas.create_text(134,25,fill="green",font="Times 24 italic bold",text="Decision pending")
    flag = not flag
# width and length of our main screen
SET_WIDTH = 650
SET_HEIGHT = 433

def pending(decision):
    # 1. Display Decision pending image
    frame = cv2.cvtColor(cv2.imread("Decision.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))

    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    canvas.update()

    # 2. wait for 1 sec
    time.sleep(1)

    # 3. Display sponsored (not added yet)
    frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))

    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    canvas.update()
    # 4. wait for 1.5 sec
    time.sleep(1.5)
    # 5. Display out/notout image
 
    if decision.lower() == "out":
     decisionImage = "out.png"
    else:
     decisionImage = "not_out.png"

    frame = cv2.cvtColor(cv2.imread(decisionImage), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))

    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    canvas.update()


def out():
    thread = threading.Thread(target=pending, args=("Out",))
    thread.daemon = 1
    thread.start()
    print("Player is Out")

def not_out():
    thread = threading.Thread(target=pending, args=("Not Out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")

# tkinter gui starts here
window = tkinter.Tk()
window.title("The Sponsored Brand Name")

cv_img = cv2.cvtColor(cv2.imread("Welcome image.png"), cv2.COLOR_BGR2RGB)

canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_create = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()

# Buttons to control playback
btn = tkinter.Button(window, text="<< Previous(fast)", width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous(slow)", width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next(fast)>>", width=50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Next(slow)>>", width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="<< Give Out", width=50, command=out)
btn.pack()

btn = tkinter.Button(window, text="<< Give Notout", width=50, command=not_out)
btn.pack()
window.mainloop()
