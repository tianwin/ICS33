# The Black_Hole class is derived from Simulton; for updating it finds+removes
#   objects (of any class derived from Prey) whose center is contained inside
#   its radius (returning a set of all eaten simultons), and displays as a
#   black circle with a radius of 10 (width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):
    def __init__(self, x, y):
        Simulton.__init__(self,x,y,20,20)
        self._radius = 10

    def set_dimension(self,width,height):
        Simulton.set_dimension(self,width,height)
        self._radius = width/2

    def update(self):
        temp_set=model.find(lambda x: isinstance(x, Prey) and self.contains(x.get_location()))
        for s in temp_set:
            model.remove(s)
        return temp_set

    def contains(self, xy):
        return self._radius >= self.distance(xy)

    def display(self, canvas):
        canvas.create_oval(self._x - self._radius, self._y - self._radius,
                           self._x + self._radius, self._y + self._radius,
                           fill='black')
