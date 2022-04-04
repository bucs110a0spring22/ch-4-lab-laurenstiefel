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
  """
        Sets up the window with an x axis ranging from -360 to 360 and the y axis from -1 to 1
        args: values for x and y coordinates, wn
        return: None
    """
def setupAxis (dart):
  dart.goto(-360,0)
  dart.goto (360,0)
  dart.goto(0,0)
  dart.goto(0,-1)
  dart.goto (0,1)
  dart.up()
  """
        Sets up the axis by specified ranges
        args: values for starting and stopping points for each line
        return: None
    """
def drawSineCurve(dart, i):
  dart.color("purple")
  sin1 = math.sin(math.radians(i))
  dart.goto(i,sin1)
  dart.down()
  sin2 = math.sin(math.radians(i+1))
  dart.goto(i+1,sin2)
  dart.up() 
  return {sin1, sin2}
"""
       Draws a sine curve in the color purple 
        args: dart, i, sin
        return: sin1, sin2
    """
def drawCosineCurve(dart, i):
  dart.color("red")
  cos1 = math.cos(math.radians(i))
  dart.goto(i,cos1)
  dart.down()
  cos2 = math.cos(math.radians(i+1))
  dart.goto(i+1,cos2)
  dart.up()
  return {cos1, cos2}
"""
       Draws a cosine curve in the color red
        args: dart, i, cos
        return: cos1, cos2
    """
def drawTangentCurve(dart, i):
  dart.color("green")
  tan1 = math.tan(math.radians(i))
  dart.goto(i,tan1)
  dart.down()
  tan2 = math.tan(math.radians(i+1))
  dart.goto(i+1,tan2)
  dart.up()
  return {tan1,tan2}
"""
       Draws a tangent curve in the color green
        args: dart, i, cos
        return: tan1, tan2
    """
def drawTangentCurveProduct(dart, i , sin1, sin2, cos1, cos2):
  dart.color("blue")
  tan1 = sin1/cos1
  tan2 = sin2/cos2
  dart.goto(i,tan1)
  dart.down()
  dart.goto(i,tan2)
  dart.up()
  return {tan1,tan2}
"""
       Draws a tangent curve in the color blue while regraphing the sine and cosine graphs in small incraments at the same time
        args: dart, i, sin, cos, tan
        return: tan1, tan2
    """  






##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0.1)

    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
  
    for function in {drawSineCurve, drawCosineCurve, drawTangentCurve}:
      print(function)
      for i in range(-360, 361, 2):
        function(dart, i)

    #Part B
    dart.speed(0)
    for i in range( -360, 361, 2):
      setupWindow(wn)
      setupAxis(dart)
      sin1, sin2 = drawSineCurve(dart, i)
      cos1, cos2 = drawCosineCurve(dart, i)
      drawTangentCurveProduct(dart, i, sin1, sin2, cos1, cos2)
    
    wn.exitonclick()
main()
