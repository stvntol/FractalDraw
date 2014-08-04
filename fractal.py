'''
@author: Steven Toledo

Makes a Mandelbrot PNG on Desktop
'''
from PIL import Image
import winsound
import sys
from os import path, environ

desktop = environ['USERPROFILE'] + "/Desktop"

def function(x,iteration):
    n= 0
    for z in range(iteration):
        n = n**2 + x      
        try:
            a = complex.__abs__(n)
        except OverflowError:
            val = [True,z]
            return val
        if a >= 2:
            val = [True, z]
            return val
    val =[False,0]
    return val
    

colors =[]
 
def escape(x,iteration):
    a = (function(x,iteration))
    if a[0] == True:
        p =  (a[1] + 230) % 0xFF + 0x10
        q = "%X" %(p)
        if q[0] == "0":
            r = q[0:2]+ "0000" +  q[0:2]
        else:
            r = q[0:2] + "00"+  q[0:2] 
        p = eval("0x"+r)
        escapeColor = "0x"+r[0:6], "%d" % a[1]
        if escapeColor not in colors:
            colors.append(escapeColor)
    else:
        p = 0xffffff
    return uint(p)

def paramet(points,prec,offsetX, offsetY):
    x = []
    y = []
    for i in range(-points,points):
        x.append(i*prec)
        y.append(i*prec)
    if offsetY:
        for i in range(len(y)):
            y[i]= y[i] - offsetY    
    for i in range(len(x)):
        x[i]= x[i] + offsetX
    r = []
    s = []
    for i in range(len(x)):
        for n in range(len(y)):
            s.append(complex(x[i],y[n]))
        r.append(s)
        s = []
    return r

def shownum(plane):
    for i in range(len(plane)):
        print (plane[i])

def testgrid():
    f=[]
    g =[]
    for i in range(10):
        for n in range (10):
            f.append(n)
        g.append(f)
        f=[]
    
    for i in range(len(g)):
        print (g[i])
        
def show(plane,iteration):
    grid =[]
    for i in range(len(plane)):
        line = plane[i]
        p = []
        for n in range(len(line)):
            p.append(escape(line[n],iteration))
        grid.append(p)
    return grid

def make(grid, picname, location):        

    size = (len(grid),len(grid))
    mandel = Image.new("RGB",size)
    print (mandel.size)
    pixel = mandel.load()
    for i in range(len(grid)):
        for n in range(len(grid[i])):
            pixel[i,n]=grid[i][n]

    loc = path.join(location,picname)
    
    mandel.save(loc)
    print ("Done")
    Scolors = sorted(colors)
    for i in range(len(Scolors)):
        print (Scolors[i])
    winsound.Beep(400,250)
    winsound.Beep(800,250)
    winsound.Beep(400,500)
    
def uint(i):
    i = int(i)
    if i > sys.maxsize and i <= 2 * sys.maxsize + 1:
        return int((i & sys.maxsize) - sys.maxsize - 1)
    else:
        return i    

def mandelbrot(iteration = 30, points = 100, prec = .01,x=0,y=0,  picname= "fractal.png", location = desktop):
    """
    iteration = Max number of times to perform mandelbrot formula recursion
    points = half the side length of the image in pixels
    prec = distance between points in set (zoom resolution)
    """
    plane = paramet(points,prec,x,y)
    grid = show(plane,iteration)
    heimid = int(len(grid)/2)
    widmid= int(len(grid[heimid])/2)
    grid[heimid][widmid]=0x0000ff
    make(grid, picname, location)


#mandelbrot(iteration= 400,points = 1920, prec=.0000002,x=-1.711114+.5,y=-0.002468)
#mandelbrot(iteration= 300,points = 600, prec=.002,x=-.75 ,y=-0.00)
#mandelbrot(800,200,.00000000005, x=-.5+.0001, y=.52)
if __name__ == "__main__":
    mandelbrot(400,600,.002)
