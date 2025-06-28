from tkinter import *
from tkinter import ttk
# defintions
def new():
    en.set(' ')
    ea.set(0)
    e3.current(0)
    e4.current(0)
    es.set(0)
    e6.current(0)
def save():
    n1=en.get()
    n2=str(ea.get())
    n3=ed.get()
    n4=edp.get()
    n5=str(es.get())
    n6=ej.get()
    with open('data//data.txt','a') as file:
        saveText=n1+' '+n2+' '+n3+' '+n4+' '+n5+' '+n6+'\n'
        file.write(saveText)
def disAll():
    with open('data//data.txt','r') as file:
        eList=file.readlines()
        for i in eList:
            print(i)
# variables
font='calibri 14'
fixedX=10
fixedBtnX=250
# main
win=Tk()
win.title('Employees menu')
w=400 # window width
h=600 # window height
x=(win.winfo_screenwidth()//2)-(w//2)
y=(win.winfo_screenheight()//2)-(h//2)
win.geometry(f'{w}x{h}+{x}+{y}')
# window menu
l1=Label(win,text='Full Name:',font=font)
l1.place(x=fixedX,y=10)
en=StringVar()
e1=Entry(win,textvariable=en,font=font,width=20)
e1.place(x=fixedX,y=40)

l2=Label(win,text='Age:',font=font)
l2.place(x=fixedX,y=70)
ea=IntVar()
e2=Entry(win,textvariable=ea,font=font,width=20)
e2.place(x=fixedX,y=100)

l3=Label(win,text='Education Level:',font=font)
l3.place(x=fixedX,y=130)
ed=StringVar()
e3=ttk.Combobox(win,textvariable=ed,font=font,width=18)
e3.place(x=fixedX,y=160)
e3['value']=('Select','High School',"associate's","Bachelor's","Master's",'PhD')
e3.current(0)

l4=Label(win,text='Department:',font=font)
l4.place(x=fixedX,y=190)
edp=StringVar()
e4=ttk.Combobox(win,textvariable=edp,font=font,width=18)
e4.place(x=fixedX,y=220)
e4['value']=['Select','Finance','Administration','Sales', 'Human Resources', 'Engineering', 'IT Support']
e4.current(0)

l5=Label(win,text='Monthly Salary($):',font=font)
l5.place(x=fixedX,y=250)
es=IntVar()
e5=Entry(win,textvariable=es,font=font,width=20)
e5.place(x=fixedX,y=280)

l6=Label(win,text='Position:',font=font)
l6.place(x=fixedX,y=310)
ej=StringVar()
e6=ttk.Combobox(win,textvariable=ej,font=font,width=18)
e6.place(x=fixedX,y=340)
e6['value']=('Select','Intern','Junior Specialist','Senior Specialist','Team Lead', 'Manager', 'Director')
e6.current(0)

# buttons
b1=Button(win,text='New',font=font,width=10,command=new)
b1.place(x=fixedBtnX,y=20)
b2=Button(win,text='Save',font=font,width=10,command=save)
b2.place(x=fixedBtnX,y=70)
b3=Button(win,text='Display all',font=font,width=10,command=disAll)
b3.place(x=fixedBtnX,y=120)
b4=Button(win,text='Close',font=font,width=10,command=win.destroy)
b4.place(x=fixedBtnX,y=170)


win.mainloop()