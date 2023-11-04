import tkinter,random,math
from tkinter import *

root=tkinter.Tk()
H,W=600,600
canvas=tkinter.Canvas(root,bg="black",height=H,width=W)

a,b,c=[W/2,0],[0,H-100],[W,H-100]
s1,s2,s3,s4,s5,s6,s7,s8,centre=[0,0],[W/2,0],[W,0],[W,H/2],[W,H],[W/2,H],[0,H],[0,H/2],[W/2,H/2]
square_vertices=[s1,s3,s5,s7]
p1,p2,p3,p4,p5=[0,217],[W/2,0],[W,217],[483,570],[113,570]
pentagon_vertices=[p1,p2,p3,p4,p5]
h1,h2,h3,h4,h5,h6=[300,0],[559.8,150],[559.8,450],[300,600],[40.2,450],[40.2,150]
hexagon_vertices=[h1,h2,h3,h4,h5,h6]
iterations=50000
animate=False
txt='turn animation on'
polygon_list=['e','e','get_triangle_random_point','get_square_random_point','get_pentagon_random_point','get_hexagon_random_point']
def get_triangle_random_point(a=a,b=b,c=c):
    u,v=random.uniform(0,1),random.uniform(0,1)
    if u+v>1:
        u,v=1-u,1-v
    w=1-u-v
    return[u*a[0]+v*b[0]+w*c[0],u*a[1]+v*b[1]+w*c[1]] 
def get_square_random_point(p1=s1,p2=s5):
    return[random.randint(p1[0],p2[0]),random.randint(p1[1],p2[1])]
def get_pentagon_random_point():
    return random.choice([get_triangle_random_point(p1,p2,p3),get_triangle_random_point(p1,p3,p4),get_triangle_random_point(p1,p4,p5)])
def get_hexagon_random_point():
    return random.choice([get_triangle_random_point(h1,h2,h3),get_triangle_random_point(h1,h3,h4),get_triangle_random_point(h1,h4,h5),get_triangle_random_point(h1,h5,h6)])

def get_line_center(p1,p2):
    return[(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]
def get_line_two_thirds(p1,p2):
    return[p1[0]+(2/3)*(p2[0]-p1[0]),p1[1]+(2/3)*(p2[1]-p1[1])]
def get_line_golden_ratio(p1,p2):
    segment_length=((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5
    ratio = 1.61803398875
    new_x = p1[0]+(p2[0]-p1[0])/(ratio)
    new_y = p1[1]+(p2[1]-p1[1])/(ratio)
    return [new_x, new_y]
def generate_serpinski_triangle():
    s=get_triangle_random_point()
    fractal_point=get_line_center(s,random.choice([a,b,c]))
    canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
    for _ in range(iterations):
        s=fractal_point
        fractal_point=get_line_center(s,random.choice([a,b,c]))
        canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        animation()
def generate_barnsley_fern():
    x=[0]
    y=[0]
    num=0
    for _ in range(iterations):
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
        num+=1
        canvas.create_oval(300+50*x[num]-1,600-50*y[num]-1,300+50*x[num]+1,600-50*y[num]+1,fill='white',tags='all')
        animation()
def generate_serpinski_carpet():
    s=get_square_random_point()
    fractal_point=get_line_two_thirds(s,random.choice([s1,s2,s3,s4,s5,s6,s7,s8]))
    canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
    for _ in range(iterations):
        s=fractal_point
        fractal_point=get_line_two_thirds(s,random.choice([s1,s2,s3,s4,s5,s6,s7,s8]))
        canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        animation()
def generate_vicsek_fractal():
    s=get_square_random_point()
    fractal_point=get_line_two_thirds(s,random.choice([s1,s3,s5,s7,centre]))
    canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
    for _ in range(iterations):
        s=fractal_point
        fractal_point=get_line_two_thirds(s,random.choice([s1,s3,s5,s7,centre]))
        canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        animation()
def generate_restricted_chaos_game_vdr():
    s=get_square_random_point()
    vertice=random.choice([s1,s3,s5,s7])
    fractal_point=get_line_center(s,vertice)
    canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
    for _ in range(iterations):
        s=fractal_point
        vertices = [s1, s3, s5, s7]
        vertices.remove(vertice)
        vertice = random.choice(vertices)
        fractal_point=get_line_center(s,vertice)
        canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        animation()
def generate_restricted_chaos_game_vnc():
    s=get_square_random_point()
    vertice=random.choice([s1,s3,s5,s7])
    fractal_point=get_line_center(s,vertice)
    canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
    for _ in range(iterations):
        s=fractal_point
        if vertice==s1:
            vertice=s7
        elif vertice==s3:
            vertice=s1
        elif vertice==s5:
            vertice=s3
        else:
            vertice=s5
        vertices = [s1, s3, s5, s7]
        vertices.remove(vertice)
        vertice = random.choice(vertices)
        fractal_point=get_line_center(s,vertice)
        canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        animation()
def generate_restricted_chaos_game_vno():
    s=get_square_random_point()
    vertice=random.choice([s1,s3,s5,s7])
    fractal_point=get_line_center(s,vertice)
    canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
    for _ in range(iterations):
        s=fractal_point
        if vertice==s1:
            vertice=s5
        elif vertice==s3:
            vertice=s7
        elif vertice==s5:
            vertice=s1
        else:
            vertice=s3
        vertices = [s1, s3, s5, s7]
        vertices.remove(vertice)
        vertice = random.choice(vertices)
        fractal_point=get_line_center(s,vertice)
        canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        animation()
def generate_restricted_chaos_game_irnn():
    s=get_square_random_point()
    vertice=random.choice([s1,s3,s5,s7])
    fractal_point=get_line_center(s,vertice)
    canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
    vertice_old=['debug ','debug']
    for _ in range(iterations):
        s=fractal_point
        vertices = [s3,s1,s7,s5]
        if vertice_old==vertice:
            if vertice==s1 or vertice==s5:
                vertices.remove(s7)
                vertices.remove(s3)
            else:
                vertices.remove(s1)
                vertices.remove(s5)
        vertice_old=vertice
        vertice = random.choice(vertices)
        fractal_point=get_line_center(s,vertice)
        canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        animation()
def generate_pentagonal_n_flake():
    s=get_pentagon_random_point()
    fractal_point=get_line_golden_ratio(s,random.choice([p1,p2,p3,p4,p5]))
    canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
    for _ in range(iterations):
        s=fractal_point
        fractal_point=get_line_golden_ratio(s,random.choice([p1,p2,p3,p4,p5]))
        canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        animation()
def generate_pentagon_restricted_chaos_game_vdr():
    s=get_pentagon_random_point()
    vertice=random.choice([p1,p2,p3,p4,p5])
    fractal_point=get_line_center(s,vertice)
    canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
    for _ in range(iterations):
        s=fractal_point
        vertices = [p1,p2,p3,p4,p5]
        vertices.remove(vertice)
        vertice = random.choice(vertices)
        fractal_point=get_line_center(s,vertice)
        canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        animation()
def generate_pentagon_restricted_chaos_game_irnn_grv():
    s=get_pentagon_random_point()
    vertice=random.choice([p1,p2,p3,p4,p5])
    fractal_point=get_line_golden_ratio(s,vertice)
    canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
    vertice_old=['debug ','debug']
    for _ in range(iterations):
        s=fractal_point
        vertices = [p1,p2,p3,p4,p5]
        if vertice_old==vertice:
            if vertice==p1:
                vertices.remove(p2)
                vertices.remove(p5)
            elif vertice==p2:
                vertices.remove(p1)
                vertices.remove(p3)
            elif vertice==p3:
                vertices.remove(p2)
                vertices.remove(p4)
            elif vertice==p4:
                vertices.remove(p3)
                vertices.remove(p5)
            elif vertice==p5:
                vertices.remove(p4)
                vertices.remove(p1)
        vertice_old=vertice
        vertice = random.choice(vertices)
        fractal_point=get_line_golden_ratio(s,vertice)
        canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        animation()
def generate_pentagon_restricted_chaos_game_irnn():
    s=get_pentagon_random_point()
    vertice=random.choice([p1,p2,p3,p4,p5])
    fractal_point=get_line_center(s,vertice)
    canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
    vertice_old=['debug ','debug']
    for _ in range(iterations):
        s=fractal_point
        vertices = [p1,p2,p3,p4,p5]
        if vertice_old==vertice:
            if vertice==p1:
                vertices.remove(p2)
                vertices.remove(p5)
            elif vertice==p2:
                vertices.remove(p1)
                vertices.remove(p3)
            elif vertice==p3:
                vertices.remove(p2)
                vertices.remove(p4)
            elif vertice==p4:
                vertices.remove(p3)
                vertices.remove(p5)
            elif vertice==p5:
                vertices.remove(p4)
                vertices.remove(p1)
        vertice_old=vertice
        vertice = random.choice(vertices)
        fractal_point=get_line_center(s,vertice)
        canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        animation()
def generate_hexagonal_n_flake():
    s=get_hexagon_random_point()
    fractal_point=get_line_two_thirds(s,random.choice([h1,h2,h3,h4,h5,h6]))
    canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
    for _ in range(iterations):
        s=fractal_point
        fractal_point=get_line_two_thirds(s,random.choice([h1,h2,h3,h4,h5,h6]))
        canvas.create_oval(fractal_point[0]-1,fractal_point[1]-1,fractal_point[0]+1,fractal_point[1]+1,fill='white',tags='all')
        animation()
def delete_all():
    canvas.delete('all')
def animation():
    global animate
    if animate==True:
        canvas.update()
def animation_switch():
    global animate,txt,b21
    if animate==False:
        animate=True
        txt='turn animation off'
    else:
        animate=False
        txt='turn animation on'
    b21.pack_forget()
    b21=tkinter.Button(text=txt,command=animation_switch)
    b21.pack(side='left')
button_frame=Frame()
button_frame.pack(side='bottom')
button_frame1=Frame()
button_frame1.pack(side='bottom')
b1=tkinter.Button(button_frame,text='serpinski triangle',command=generate_serpinski_triangle)
b1.pack(side='left')
b2=tkinter.Button(button_frame,text='barnsley fern',command=generate_barnsley_fern)
b2.pack(side='left')
b3=tkinter.Button(button_frame,text='serpinski carpet',command=generate_serpinski_carpet)
b3.pack(side='left')
b4=tkinter.Button(button_frame,text='vicsek fractal',command=generate_vicsek_fractal)
b4.pack(side='left')
b5=tkinter.Button(button_frame,text='restricted chaos game\n vertice doesnt repeat',command=generate_restricted_chaos_game_vdr)
b5.pack(side='left')
b6=tkinter.Button(button_frame,text='restricted chaos game\n vertice is not counterclockwise',command=generate_restricted_chaos_game_vnc)
b6.pack(side='left')
b7=tkinter.Button(button_frame,text='restricted chaos game\n vertice is not opposite',command=generate_restricted_chaos_game_vno)
b7.pack(side='left')
b8=tkinter.Button(button_frame1,text='pentagonal n flake',command=generate_pentagonal_n_flake)
b8.pack(side='left')
b9=tkinter.Button(button_frame1,text='restricted pentagon chaos game\n vertice doesnt repeat',command=generate_pentagon_restricted_chaos_game_vdr)
b9.pack(side='left')
b10=tkinter.Button(button_frame,text='restricted chaos game\nif vertice repeats\nnext vertice cannot neighbor',command=generate_restricted_chaos_game_irnn)
b10.pack(side='left')
b11=tkinter.Button(button_frame1,text='restricted pentagon chaos game\nif vertice repeats\nnext vertice cannot neighbor\ngolden ratio version',command=generate_pentagon_restricted_chaos_game_irnn_grv)
b11.pack(side='left')
b12=tkinter.Button(button_frame1,text='restricted pentagon chaos game\nif vertice repeats\nnext vertice cannot neighbor',command=generate_pentagon_restricted_chaos_game_irnn)
b12.pack(side='left')
b13=tkinter.Button(button_frame,text='hexagonal n flake',command=generate_hexagonal_n_flake)
b13.pack(side='left')
b20=tkinter.Button(text='delete all',command=delete_all)
b20.pack(side='left')
b21=tkinter.Button(text=txt,command=animation_switch)
b21.pack(side='left')

canvas.pack()
root.mainloop() 