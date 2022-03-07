import turtle

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

import math
import turtle

def setupWindow (wn):
  wn.setworldcoordinates(-360,-1,360,1)
def setupAxis (dart):
  dart.goto(-360,0)
  dart.goto (360,0)
  dart.goto(0,0)
  dart.goto(0,-1)
  dart.goto (0,1)
  dart.up()
def drawSineCurve(dart):
 for i in range (-360,361):
    y = math.sin(math.radians(i))
    dart.goto(i,y)
    dart.down()
 dart.up() 

def drawCosineCurve(dart):
 for i in range (-360,361):
    y = math.cos(math.radians(i))
    dart.goto(i,y)
    dart.down()
 dart.up()   

def drawTangentCurve(dart):
 for i in range (-360,361):
    y = math.tan(math.radians(i))
    dart.goto(i,y)
    dart.down()










##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0.1)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
