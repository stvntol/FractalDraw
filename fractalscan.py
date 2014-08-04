'''
@author: Steven
'''
import fractal
import math
import math.pi as pi

#iteration= 400,points = 1920, prec=.0000002,x=-1.711114+.5,y=-0.002468

sides = 360

for i in range(sides):
    name = str(i) + "mandel360.png"
    zoom = 2*10 ** -5
    cx = math.cos(2*pi * i/sides)*.25
    cy = math.sin(2*pi * i /sides)*.25
	fractal.mandelbrot(iteration = 400, points = 500, prec = zoom ,x=-.5+cx,y=cy,  picname= name)