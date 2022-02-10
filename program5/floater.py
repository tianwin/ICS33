# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    def __init__(self,x,y):
        self._image = PhotoImage(file='ufo.gif')
        width, height = self._image.width(),self._image.height()
        Prey.__init__(self, x, y, width, height, 0, speed=5)
        self.randomize_angle()

    def update(self):
        if random()>0.7:
            speed = self.get_speed()+random()-0.5
            if speed<3:
                self.set_speed(3)
            elif speed>7:
                self.set_speed(7)
            else:
                self.set_speed(speed)
            self.set_angle(self.get_angle()+random()-0.5)
        self.move()

    def display(self,canvas):
        canvas.create_image(*self.get_location(),image = self._image)