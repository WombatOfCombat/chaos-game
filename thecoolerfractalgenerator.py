import tkinter
import random
import math
from tkinter import *
import numpy as np
from shapely.geometry import *
import shapely._geos
root=tkinter.Tk()
root.title("The olde fractal generator")
H,W=600,600
canvas=tkinter.Canvas(root,bg="black",height=H,width=W)
all_vertices=[
             'e','e','e',
             [[W/2,0],[W,519],[0,519]],
             [[0,0],[W,0],[W,H],[0,H]],
             [[0,217],[W/2,0],[W,217],[483,570],[113,570]],
             [[300,0],[559.8,150],[559.8,450],[300,600],[40.2,450],[40.2,150]],
             [[300, 14.812],[540.582, 130.67],[600, 391],[433.513, 599.771],[166.486, 599.771],[0, 391],[59.417, 130.67]],
             [[0,175.735],[0,424.264],[175.735,600],[424.264,600],[600,424.264],[600,175.735],[424.264,0],[175.735,0]],
             [[0,260.846],[104.188,80.385],[300,9.116],[495.811,80.385],[600,260.846],[563.815,466.058],[404.188,600],[195.811,600],[36.184,466.058]],
             [[0,300],[57.295,123.664],[207.295,14.683],[392.705,14.683],[542.705,123.664],[600,300],[542.705,476.336],[392.705,585.317],[207.295,585.317],[57.295,476.336]],
             [[214.637,0],[385.137,0],[528.57,92.179],[600,247.272],[575.134,416.036],[463.48,544.891],[300,592.927],[136.293,544.891],[24.639,416.036],[0,247.272],[71.203,92.179]],
             [[300,0],[450,40.192],[559.808,150],[600,300],[559.808,450],[450,559.808],[300,600],[150,559.808],[40.192,450],[0,300],[40.192,150],[150,40.192]]
             ]
all_ratios=['e','e','e',1/2,1-0.414214,0.618033988749895,2/3,1-0.307979,1-0.292893,1-0.257773,1-0.236068,1-0.2209,1-0.211325]
all_centers=['e','e','e',[300,345],[300,300],[300,315],[300,300],[300,321],[300,300],[300,313],[300,300],[300,290.328],[300,300]]
all_polygon_names=['e','e','e','triangular','square','pentagonal','hexagonal','heptagonal','octagonal','nonagonal','decagonal','hendecagonal','dodecagonal']
s=0
def get_random_point_in_polygon(polygon,number=1):
    points=[]
    minx,miny,maxx,maxy=polygon.bounds
    while True:
        pnt=[np.random.uniform(minx,maxx),np.random.uniform(miny,maxy)]
        if polygon.contains(Point(pnt)):
            return pnt
def get_line_division(division,p1,p2):
    if division<0 or division>1:
        raise ValueError("ratio of chaos game  must be between 0 and 1")
    x = p1[0]+division*(p2[0]-p1[0])
    y = p1[1]+division*(p2[1]-p1[1])
    if lc.get():
        print('new point:',x,y)
    return (x,y)

def generate_chaos_game(iterations,vertices,division):
    global s
    vertice_memory=list()
    if vertices=='' or int(vertices)<3:
        vertices='3'
    elif int(vertices)>len(all_vertices)-1:
        vertices='10'
    vertices=int(vertices)
    reccomend=all_ratios[vertices]
    center=all_centers[vertices]
    vertices=all_vertices[int(vertices)]
    if division=='':#or eval(division)>1 or eval(division)<0:
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
    for i in range(int(iterations)):
        s=fractal_point
        vertices_copy=vertices[:]
        remove_list=list()
        vertice_memory.append(vertice)
        if vnr.get():
            remove_list.append(vertice)
        if vnc.get() and vertice!=center:
            if vertices_copy.index(vertice)==0:
                remove_list.append(vertices_copy[-1])
            else:
                remove_list.append(vertices_copy[vertices_copy.index(vertice)-1])
        if vno.get() and vertice!=center:
            remove1=math.ceil((len(vertices_copy))/2)+vertices_copy.index(vertice)
            remove2=math.floor((len(vertices_copy))/2)+vertices_copy.index(vertice)
            remove_list.append(vertices_copy[remove1 % len(vertices_copy)])
            if remove1!=remove2:
                remove_list.append(vertices_copy[remove2 % len(vertices_copy)])
        if ivr_vcn.get() and i>=1 and vertice_memory[i]==vertice_memory[i-1] and vertice!=center:
            if vertices_copy.index(vertice)==len(vertices_copy)-1:
                remove_list.append(vertices_copy[0])
                remove_list.append(vertices_copy[-2])
            else:
                remove_list.append(vertices_copy[vertices_copy.index(vertice)-1])
                remove_list.append(vertices_copy[vertices_copy.index(vertice)+1])
        output_list = []
        for item in remove_list:
            if item not in output_list:
                output_list.append(item)
        if lc.get():
            print('vertices classed out:',output_list)
        if uc.get():
            vertices_copy.append(center)
        for remove in output_list:
            vertices_copy.remove(remove)
        vertice = random.choice(vertices_copy)
        fractal_point=get_line_division(division,p1=s,p2=vertice)
        if ba.get():
            generate_eye(fractal_point[0],fractal_point[1])
        else:
            canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        if animate.get():
            canvas.update()
    if pd.get():
        definition_text='{} n-flake\n'.format(all_polygon_names[len(vertices)])
        if vnr.get():
            definition_text+='-vertice selection does not repeat\n'
        if vnc.get():
            definition_text+='-vertice is not counterclockwise to last selected vertice\n'
        if vno.get():
            definition_text+='-vertice is not opposite to last selected vertice\n'
        if ivr_vcn.get():
            definition_text+='-vertice is not neighboring the last selected vertice if the last two selected vertices have the same value\n'
        if uc.get():
            definition_text+='-vertice can also be the center of the polygon\n'
        print(definition_text)

def generate_barnsley_fern():
    x=[0]
    y=[0]
    num=0
    for _ in range(60000):
        chance=random.randint(0,100)
        if chance==0:
            x.append(0)
            y.append(0.16*y[num])
        elif 7>=chance>=1:
            x.append(0.2*x[num]-0.26*y[num])
            y.append(0.23*x[num]+0.22*y[num]+1.6)
        elif 14>=chance>=8:
            x.append(-0.15*x[num]+0.28*y[num])
            y.append(0.26*x[num]+0.24*y[num]+0.44)
        else:
            x.append(0.85*x[num]+0.04*y[num])
            y.append(-0.04*x[num]+0.85*y[num]+1.6)
        if lc.get():
            print(x[-1],y[-1],chance)
        num+=1
        canvas.create_oval(300+60*x[num]-1-50,600-60*y[num]-1,300+60*x[num]+1-50,600-60*y[num]+1,fill='white',tags='all')

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

iterations_input=tkinter.Entry(input_frame)
iterations_input.pack(side='bottom')
il1=tkinter.Label(input_frame,text="iterations")
il1.pack(side='bottom')

vertices_input=tkinter.Entry(input_frame)
vertices_input.pack(side='bottom')
il2=tkinter.Label(input_frame,text="polygon vertice count (3-{})".format(len(all_vertices)-1))
il2.pack(side='bottom')

division_input=tkinter.Entry(input_frame)
division_input.pack(side='bottom')
il3=tkinter.Label(input_frame,text="ratio of chaos game")
il3.pack(side='bottom')

b1=tkinter.Button(button_frame,text='generate',command=lambda:generate_chaos_game(iterations_input.get(),vertices_input.get(),division_input.get()))
b1.pack(side='left')
b2=tkinter.Button(button_frame,text='delete',command=delete_all)
b2.pack(side='left')
b3=tkinter.Button(button_frame,text='barnsleys fern',command=generate_barnsley_fern)
b3.pack(side='left')

animate=tkinter.BooleanVar()
animate.set(False)
vnr=tkinter.BooleanVar()
vnr.set(False)
vnc=tkinter.BooleanVar()
vnc.set(False)
vno=tkinter.BooleanVar()
vno.set(False)
ivr_vcn=tkinter.BooleanVar()
ivr_vcn.set(False)
uc=tkinter.BooleanVar()
uc.set(False)
ba=tkinter.BooleanVar()
ba.set(False)
pd=tkinter.BooleanVar()
pd.set(False)
lc=tkinter.BooleanVar()
lc.set(False)

sb0=tkinter.Checkbutton(switch_frame,variable=ba)
sb0.pack(side='bottom')
sl0=tkinter.Label(switch_frame,text="biblically accurate")
sl0.pack(side='bottom')

sb1=tkinter.Checkbutton(switch_frame,variable=lc)
sb1.pack(side='bottom')
sl1=tkinter.Label(switch_frame,text="make me look cool")
sl1.pack(side='bottom')

sb2=tkinter.Checkbutton(switch_frame,variable=pd)
sb2.pack(side='bottom')
sl2=tkinter.Label(switch_frame,text="provide definition")
sl2.pack(side='bottom')

sb3=tkinter.Checkbutton(switch_frame,variable=animate)
sb3.pack(side='bottom')
sl3=tkinter.Label(switch_frame,text="animate")
sl3.pack(side='bottom')

sb4=tkinter.Checkbutton(switch_frame,variable=vnr)
sb4.pack(side='bottom')
sl4=tkinter.Label(switch_frame,text="do not repeat vertice")
sl4.pack(side='bottom')

sb5=tkinter.Checkbutton(switch_frame,variable=vnc)
sb5.pack(side='bottom')
sl5=tkinter.Label(switch_frame,text="do not use\nvertice counterclockwise to last")
sl5.pack(side='bottom')

sb6=tkinter.Checkbutton(switch_frame,variable=vno)
sb6.pack(side='bottom')
sl6=tkinter.Label(switch_frame,text="do not use\n vertice opposite to last")
sl6.pack(side='bottom')

sb7=tkinter.Checkbutton(switch_frame,variable=ivr_vcn)
sb7.pack(side='bottom')
sl7=tkinter.Label(switch_frame,text="if vertice repeats\ndo not use\nvertices neighboring last")
sl7.pack(side='bottom')

sb8=tkinter.Checkbutton(switch_frame,variable=uc)
sb8.pack(side='bottom')
sl8=tkinter.Label(switch_frame,text="use center")
sl8.pack(side='bottom')
canvas.pack()
root.mainloop() 
