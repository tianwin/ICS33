# A special is Ball; it updates by moving faster and
# away from the black hole for 20 times
# if the black hole like object is in 100.
# and then slow down for 20 times saving energy for the next speed up.



from ball import Ball
import model
from blackhole import Black_Hole
from math import pi, atan2

class Special(Ball):
    def __init__(self,x,y):
        Ball.__init__(self, x, y)
        self.set_speed(3)
        self.randomize_angle()
        self._hurry = 0



    def update(self):
        if self._hurry > 20:
            self._hurry = -20
            self.set_speed(3)
        if self._hurry<0:
            self._hurry+=1
        temp_list = list(model.find(lambda x: isinstance(x, Black_Hole) and 190 >= self.distance(x.get_location())))
        if temp_list != []:
            if self._hurry >= 0:
                self._hurry+=1
                self.set_speed(7)
            temp_list = [(x, self.distance(x.get_location())) for x in temp_list]
            temp_list = sorted(temp_list, key=lambda x: x[1])
            # print(temp_list)
            target = temp_list[0][0]
            self.set_angle(atan2(target._y - self._y, target._x - self._x)+pi)
        else:
            if self._hurry>0:
                self._hurry-=1
                self.set_speed(3)
        self.move()
        # print(self.get_speed())


