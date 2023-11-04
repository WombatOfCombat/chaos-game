import tkinter
import random
import math
from tkinter import *
import numpy as np
from shapely.geometry import *
root=tkinter.Tk()
root.title("T.C.F.G.")
H,W=600,600
canvas=tkinter.Canvas(root,bg="black",height=H,width=W)
a,b,c=[W/2,0],[0,H-100],[W,H-100]
triangle_vertices=[a,b,c]
s1,s2,s3,s4,s5,s6,s7,s8,centre=[0,0],[W/2,0],[W,0],[W,H/2],[W,H],[W/2,H],[0,H],[0,H/2],[W/2,H/2]
square_vertices=[s1,s3,s5,s7]
p1,p2,p3,p4,p5=[0,217],[W/2,0],[W,217],[483,570],[113,570]
pentagon_vertices=[p1,p2,p3,p4,p5]
h1,h2,h3,h4,h5,h6=[300,0],[559.8,150],[559.8,450],[300,600],[40.2,450],[40.2,150]
hexagon_vertices=[h1,h2,h3,h4,h5,h6]
H1,H2,H3,H4,H5,H6,H7=[300, 14.812], [540.582, 130.67], [600, 391], [433.513, 599.771], [166.486, 599.771], [0, 391], [59.417, 130.67]
heptagon_vertices=[H1,H2,H3,H4,H5,H6,H7]
o1,o2,o3,o4,o5,o6,o7,o8=[0,175.735],[0,424.264],[175.735,600],[424.264,600],[600,424.264],[600,175.735],[424.264,0],[175.735,0]
octagon_vertices=[o1,o2,o3,o4,o5,o6,o7,o8]
n1,n2,n3,n4,n5,n6,n7,n8,n9=[0,600-339.154],[104.188,600-519.615],[300,600-590.884],[495.811,600-519.615],[600,600-339.154],[563.815,600-133.942],[404.188,600-0],[195.811,600-0],[36.184,600-133.942]
nonagon_vertices=[n1,n2,n3,n4,n5,n6,n7,n8,n9]
all_vertices=['e','e','e',triangle_vertices,square_vertices,pentagon_vertices,hexagon_vertices,heptagon_vertices,octagon_vertices,nonagon_vertices]
all_ratios=['e','e','e',1/2,1-0.414214,0.618033988749895,2/3,1-0.307979,1-0.292893,1-0.257773]
s=0
def get_random_point_in_polygon(polygon,number=1):
    points=[]
    minx,miny,maxx,maxy=polygon.bounds
    while True:
        pnt=[np.random.uniform(minx,maxx),np.random.uniform(miny,maxy)]
        if polygon.contains(Point(pnt)):
            return pnt
def get_line_division(division,p1,p2):
    if division <0 or division>1:
        raise ValueError("Division must be between 0 and 1")
    x = p1[0]+division*(p2[0]-p1[0])
    y = p1[1]+division*(p2[1]-p1[1])
    return (x, y)

def generate_chaos_game(iterations,vertices,division):
    global s
    vertice_memory=list()
    disable_vno=False
    vertices=int(vertices)
    reccomend=all_ratios[vertices]
    vertices=all_vertices[int(vertices)]
    if division=='' or division=='default':
        division=reccomend
    else:
        division=eval(division)
    if iterations=='':
        iterations='20000'
    if int(iterations)>=10000 and animate.get():
        iterations='10000'
    s=get_random_point_in_polygon(Polygon(vertices))
    vertice = random.choice(vertices)
    fractal_point=get_line_division(division,p1=s,p2=vertice)
    canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
    for i in range(int(iterations)):
        s=fractal_point
        vertices_copy=vertices[:]
        remove_list=list()
        vertice_memory.append(vertice)
        if vnr.get():
            remove_list.append(vertice)
        if vnc.get():
            if vertices_copy.index(vertice)==0:
                remove_list.append(vertices_copy[len(vertices_copy)-1])
            else:
                remove_list.append(vertices_copy[vertices_copy.index(vertice)-1])
        if (not disable_vno) and vno.get():
            remove1=math.ceil((len(vertices_copy))/2)+vertices_copy.index(vertice)
            remove2=math.floor((len(vertices_copy))/2)+vertices_copy.index(vertice)
            remove_list.append(vertices_copy[remove1 % len(vertices_copy)])
            if remove1!=remove2:
                remove_list.append(vertices_copy[remove2 % len(vertices_copy)])
        if ivr_vcn.get() and i>=1 and vertice_memory[i]==vertice_memory[i-1]:
            if vertices_copy.index(vertice)==0:
                remove_list.append(vertices_copy[1])
                remove_list.append(vertices_copy[len(vertices_copy)-1])
            elif vertices_copy.index(vertice)==len(vertices_copy)-1:
                remove_list.append(vertices_copy[0])
                remove_list.append(vertices_copy[len(vertices_copy)-2])
            else:
                remove_list.append(vertices_copy[vertices_copy.index(vertice)-1])
                remove_list.append(vertices_copy[vertices_copy.index(vertice)+1])
        output_list = []
        for item in remove_list:
            if item not in output_list:
                output_list.append(item)
        for i in range(len(output_list)):
            vertices_copy.remove(output_list[i])
        vertice = random.choice(vertices_copy)
        fractal_point=get_line_division(division,p1=s,p2=vertice)
        canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        #generate_eye(fractal_point[0],fractal_point[1])
        if animate.get():
            canvas.update()

def delete_all():
    canvas.delete('all')
    canvas.update()

def generate_eye(x,y):
    canvas.create_oval(x-10,y-5,x+10,y+5,fill='white',tags='all')
    canvas.create_oval(x-3,y-3,x+3,y+3,fill='black',tags='all')

button_frame=Frame()
button_frame.pack(side='bottom')

switch_frame=Frame()
switch_frame.pack(side='left')

input_frame=Frame()
input_frame.pack(side='right')

iterations_input = tkinter.Entry(input_frame)
iterations_input.pack(side='bottom')
il1 = tkinter.Label(input_frame, text="iterations")
il1.pack(side='bottom')

vertices_input = tkinter.Entry(input_frame)
vertices_input.pack(side='bottom')
il2 = tkinter.Label(input_frame, text="polygon vertice count (3-8)")
il2.pack(side='bottom')

division_input = tkinter.Entry(input_frame)
division_input.pack(side='bottom')
il3 = tkinter.Label(input_frame, text="ratio of chaos game")
il3.pack(side='bottom')

b1=tkinter.Button(button_frame,text='generate',command=lambda:generate_chaos_game(iterations_input.get(),vertices_input.get(),division_input.get()))
b1.pack(side='left')
b2=tkinter.Button(button_frame,text='delete',command=delete_all)
b2.pack(side='left')

animate = tkinter.BooleanVar()
animate.set(False)
vnr = tkinter.BooleanVar()
vnr.set(False)
vnc = tkinter.BooleanVar()
vnc.set(False)
vno = tkinter.BooleanVar()
vno.set(False)
ivr_vcn = tkinter.BooleanVar()
ivr_vcn.set(False)

sb1 = tkinter.Checkbutton(switch_frame, variable=animate)
sb1.pack(side='bottom')
sl1 = tkinter.Label(switch_frame, text="animate")
sl1.pack(side='bottom')

sb2 = tkinter.Checkbutton(switch_frame, variable=vnr)
sb2.pack(side='bottom')
sl2 = tkinter.Label(switch_frame, text="do not repeat vertice")
sl2.pack(side='bottom')

sb3 = tkinter.Checkbutton(switch_frame, variable=vnc)
sb3.pack(side='bottom')
sl3 = tkinter.Label(switch_frame, text="do not use\nvertice counterclockwise to last")
sl3.pack(side='bottom')

sb3 = tkinter.Checkbutton(switch_frame, variable=vno)
sb3.pack(side='bottom')
sl3 = tkinter.Label(switch_frame, text="do not use\n vertice opposite to last")
sl3.pack(side='bottom')

sb3 = tkinter.Checkbutton(switch_frame, variable=ivr_vcn)
sb3.pack(side='bottom')
sl3 = tkinter.Label(switch_frame, text="if vertice repeats\ndo not use\nvertices neighboring last")
sl3.pack(side='bottom')

canvas.pack()
root.mainloop() 