import controller
from goody import type_as_str
import model  # Calls to update in update_all are passed a reference to model

# Use the reference to this module to pass it to update methods

from ball import Ball
from floater import Floater
from blackhole import Black_Hole
from pulsator import Pulsator
from hunter import Hunter
from special import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
balls = set()
current_object = "Ball"

# return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(), controller.the_canvas.winfo_height())


# reset all module variables to represent an empty/stopped simulation
def reset():
    global running, cycle_count, balls
    running = False
    cycle_count = 0
    balls = set()
    # print("done reset")


# start running the simulation
def start():
    global running
    running = True
    # print(cycle_count)


# stop running the simulation (freezing it)
def stop():
    global running
    running = False


# step just one update in the simulation
def step():
    global running, cycle_count
    cycle_count+=1
    running = False
    for b in balls:
        b.update()


# remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global current_object
    current_object = kind


# add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x, y):
    global current_object,balls
    if current_object == "Remove":
        balls_forloop = balls.copy()
        for b in balls_forloop:
            if b.contains((x,y)):
                balls.remove(b)
    else:
        # print(current_object)
        ob = str(current_object)
        # print(ob)
        balls.add(eval(ob+f"({x},{y})"))


# add simulton s to the simulation
def add(s):
    global balls
    balls.add(s)


# remove simulton s from the simulation    
def remove(s):
    global balls
    balls.remove(s)


# find/return a set of simultons that each satisfy predicate p
def find(p):
    result = set()
    for b in balls:
        if p(b):
            result.add(b)
    return result


# for each simulton in this simulation, call update (passing model to it) 
# this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count,balls
    if running:
        cycle_count += 1
        balls_copy = balls.copy()
        for b in balls_copy:
            b.update()

    # print(cycle_count)


# How to animate: 1st: delete all simultons on the canvas; 2nd: call display on
#  all simulton being simulated, adding each back to the canvas, maybe in a
#  new location; 3rd: update the label defined in the controller for progress 
# this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)

    for b in balls:
        b.display(controller.the_canvas)

    controller.the_progress.config(text=str(len(balls)) + " balls/" + str(cycle_count) + " cycles")
