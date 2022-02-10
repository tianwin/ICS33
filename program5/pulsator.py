# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole
import model

class Pulsator(Black_Hole):

    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self._timecount=0

    def update(self):
        self._timecount+=1
        eaten_set = Black_Hole.update(self)
        if len(eaten_set) !=0:
            self._timecount = 0
            self.set_dimension(self.get_dimension()[0]+1,self.get_dimension()[1]+1)
        elif self._timecount == 30:
            self._timecount=0
            self.set_dimension(self.get_dimension()[0]-1,self.get_dimension()[1]-1)
            if self._radius == 0:
                model.remove(self)
        return eaten_set