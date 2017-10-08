#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

import pyscreenshot as ImageGrab
import resize
import thresholding
import digitrecognition
# from tkColorChooser import askcolor

# Height and Width of the Canvas
WIDTH = 256
HEIGHT = 256
TESTIMAGEPATH = '/path/to/this/file/test.png'

class Paint(object):
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    # Constructor
    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text=' Pen ', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='Save ', command=self.save_image)
        self.brush_button.grid(row=0, column=1)

        self.eraser_button = Button(self.root, text='Erase', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=2)

        self.c = Canvas(self.root, bg='white', width=WIDTH, height=HEIGHT)
        self.c.grid(row=1, columnspan=4)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = 18
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)

    # To Choose Pen
    def use_pen(self):
        self.activate_button(self.pen_button)

    # To Save the Entered Input as Image
    def save_image(self):
        x = self.c.winfo_rootx()
        y = self.c.winfo_rooty()
        x1 = x + WIDTH
        y1 = y + HEIGHT
        canvas = (x, y, x1, y1)
        self.grabcanvas = ImageGrab.grab(bbox=canvas)
        self.grabcanvas.save("original.png")
        print("Image Saved!")

    # To Use Eraser
    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    # To Activate the Button When Clicked
    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=18, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y


# Main Function
if __name__ == '__main__':
    ge = Paint()
    resize.res()
    thresholding.thres()
    digitrecognition.whatNumIsThis(TESTIMAGEPATH)
