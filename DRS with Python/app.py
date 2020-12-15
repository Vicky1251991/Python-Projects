import tkinter  # inbuilt package
import cv2  # pip install opencv-python
import PIL.Image  # pip install opencv-python
import PIL.ImageTk  # pip install pillow
from functools import partial
import threading
import time
import imutils  # pip install imutils

stream = cv2.VideoCapture("clip.mp4")
flag = True


def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(180, 50, fill="black ",
                           front="Times 30 italic bold", text="Decision Pending")
    flag = not flag


def pending(decision):
    # 1.Display decission pending image
    frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 2.Wait for 1 second
    time.sleep(1)

    # 3.Display sponser image
    frame = cv2.cvtColor(cv2.imread("sponser.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 4.Wait for 1.5 second
    time.sleep(1.5)

    # 5.Display no ball/out/not out image
    if decision == "out":
        decisionImg = "out.jpg"

    else:
        decisionImg = "not_out.jpg"

    if decision == "no ball":
        decisionImg = "no_ball.jpg"

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 6.Wait for 1.5 second
    time.sleep(1.5)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is OUT")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is NOT OUT")


def no_ball():
    thread = threading.Thread(target=pending, args=("no ball",))
    thread.daemon = 1
    thread.start()
    print("NO BALL")


# Width and Height of our main screen
SET_WIDTH = 600
SET_HEIGHT = 366

# thinter gui starts here
window = tkinter.Tk()
window.title("Third Umpire Decision Review Kit...")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

# buttons to control playback
btn = tkinter.Button(window, text="<< Previous (fast)",
                     width=100, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow)",
                     width=100, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (slow) >>",
                     width=100, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Next (fast) >>",
                     width=100, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Give NO BALL", width=100, command=no_ball)
btn.pack()

btn = tkinter.Button(window, text="Give OUT", width=100, command=out)
btn.pack()

btn = tkinter.Button(window, text="Give NOT OUT", width=100, command=not_out)
btn.pack()


window.mainloop()
