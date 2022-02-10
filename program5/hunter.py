# The Hunter class is derived (in order) from both Pulsator and Mobile_Simulton.
#   It updates/displays like its Pulsator base, but is also mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model

class Hunter(Pulsator, Mobile_Simulton):  
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        self._speed = 5
        Mobile_Simulton.randomize_angle(self)

    def update(self):
        temp_set = Pulsator.update(self)
        temp_list=list(model.find(lambda x: isinstance(x, Prey) and 200 >= self.distance(x.get_location())))
        if temp_list!=[]:
            temp_list = [(x,self.distance(x.get_location())) for x in temp_list]
            temp_list = sorted(temp_list,key=lambda x:x[1])
            # print(temp_list)
            target = temp_list[0][0]
            self.set_angle(atan2(target._y-self._y,target._x-self._x))
        Mobile_Simulton.move(self)
        return temp_set