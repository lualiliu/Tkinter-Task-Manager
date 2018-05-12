from tkinter import *
import psutil

list_items = psutil.pids()

def ini():
    Lstbox1.delete(0,END)
    global list_items
    list_items = psutil.pids()
    for item in list_items:
        p = psutil.Process(item);
        Lstbox1.insert(END,str(item)+','+p.name())

def kill():
    if Lstbox1.curselection()!=() :
        global list_items
        selected = Lstbox1.curselection()[0];
        print(selected,list_items[selected]);
        try:
            p = psutil.Process(list_items[selected])
            p.kill();
        except:
            pass
        ini();

        
root = Tk();
root.geometry('320x240')
root.title("任务管理器")

frame1 = Frame(root,relief=RAISED);
frame1.pack(fill=X)


Lstbox1=Listbox(frame1)
Lstbox1.pack();

btn1=Button(frame1,text="刷新",command=ini)
btn1.pack(fill=X)

btn1=Button(frame1,text="结束",command=kill)
btn1.pack(fill=X)
