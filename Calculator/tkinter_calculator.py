from tkinter import *
root=Tk()
root.title("Calculator")
root.minsize(500,500)
root.geometry("700x700")
root.wm_iconbitmap("cal_icon.ico")

#creating screen
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="lucida 15 bold")
screen.pack(fill=X,padx=7,pady=7)

#click function
solve=False
def click(event):
    global solve
    text = event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.set())
        else:
            try:
                value = eval(screen.get())
                solve=True
            except:
                value="Error"
        scvalue.set(value)
        screen.update()
    elif text== "C":
        scvalue.set("")
        screen.update()
        solve=False
    else:
        if solve:
            scvalue.set("")
            screen.update()
            solve=False
        scvalue.set(scvalue.get()+text)
        screen.update()




#creating frame-1
frame_1=Frame(root,bg="grey")
bton7=Button(frame_1,text="7",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton7.pack(side=LEFT,padx=7,pady=7)
bton7.bind("<Button-1>",click)

bton8=Button(frame_1,text="8",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton8.pack(side=LEFT,padx=7,pady=7)
bton8.bind("<Button-1>",click)

bton9=Button(frame_1,text="9",font=("Arial",13),width=7,height=3,bg="Black",fg="white")
bton9.pack(side=LEFT,padx=7,pady=7)
bton9.bind("<Button-1>",click)

bton_div=Button(frame_1,text="/",font=("Arial",13),width=7,height=3,bg="Black",fg="White")
bton_div.pack(side=LEFT,padx=7,pady=7)
bton_div.bind("<Button-1>",click)

frame_1.pack()

#creating frame-2
frame_2=Frame(root,bg="grey")
bton4= Button(frame_2,text="4",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton4.pack(side=LEFT,padx=7,pady=7)
bton4.bind("<Button-1>",click)

bton5=Button(frame_2,text="5",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton5.pack(side=LEFT,padx=7,pady=7)
bton5.bind("<Button-1>",click)

bton6=Button(frame_2,text="6",font=("Arial",13),width=7,height=3,bg="Black",fg="white")
bton6.pack(side=LEFT,padx=7,pady=7)
bton6.bind("<Button-1>",click)

bton_mul=Button(frame_2,text="*",font=("Arial",13),width=7,height=3,bg="Black",fg="white")
bton_mul.pack(side=LEFT,padx=7,pady=7)
bton_mul.bind("<Button-1>",click)

frame_2.pack()

#creating frame_3
frame_3=Frame(root,bg="grey")
bton1= Button(frame_3,text="1",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton1.pack(side=LEFT,padx=7,pady=7)
bton1.bind("<Button-1>",click)

bton2=Button(frame_3,text="2",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton2.pack(side=LEFT,padx=7,pady=7)
bton2.bind("<Button-1>",click)

bton3=Button(frame_3,text="3",font=("Arial",13),width=7,height=3,bg="Black",fg="white")
bton3.pack(side=LEFT,padx=7,pady=7)
bton3.bind("<Button-1>",click)

bton_sub=Button(frame_3,text="-",font=("Arial",13),width=7,height=3,bg="Black",fg="white")
bton_sub.pack(side=LEFT,padx=7,pady=7)
bton_sub.bind("<Button-1>",click)

frame_3.pack()

#creating frame_4
frame_4=Frame(root,bg="grey")
bton_C=Button(frame_4,text="C",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton_C.pack(side=LEFT,padx=7,pady=7)
bton_C.bind("<Button-1>",click)

bton0=Button(frame_4,text="0",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton0.pack(side=LEFT,padx=7,pady=7)
bton0.bind("<Button-1>",click)

bton_add=Button(frame_4,text="+",font=("Arial",13),width=7,height=3,bg="Black",fg="white")
bton_add.pack(side=LEFT,padx=7,pady=7)
bton_add.bind("<Button-1>",click)

bton_equal=Button(frame_4,text="=",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton_equal.pack(side=LEFT,padx=7,pady=7)
bton_equal.bind("<Button-1>",click)

frame_4.pack()

root.mainloop()


'''
from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("350x500")
root.wm_iconbitmap("cal_icon.ico")
#Creating display bar
scvalue= StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font='lucida 15 bold')
screen.pack(fill=X,padx=7,pady=7)

#creating global variable
solve = False

#creating function click
def click(event):
    global solve
    text=event.widget.cget("text")
    #print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value= eval(screen.get())
                solve = True
            except:
                value="Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
        solve = False
    else:
        if solve:
            scvalue.set("")
            screen.update()
            solve = False
        scvalue.set(scvalue.get()+text)
        screen.update()


#creating frame 1 contain 7,8,9,multiplication
frame_1=Frame(root,bg="grey")
bton7=Button(frame_1,text="7",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton7.pack(side=LEFT,padx=7,pady=7)
bton7.bind("<Button-1>",click)

bton8=Button(frame_1,text="8",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton8.pack(side=LEFT,padx=7,pady=7)
bton8.bind("<Button-1>",click)

bton9=Button(frame_1,text="9",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton9.pack(side=LEFT,padx=7,pady=7)
bton9.bind("<Button-1>",click)

btonx=Button(frame_1,text="*",font=("Arial",13),width=7,height=3,bg="black",fg="white")
btonx.pack(side=LEFT,padx=7,pady=7)
btonx.bind("<Button-1>",click)

frame_1.pack()

#creating frame 2 contain 4,5,6,subtract
frame_2=Frame(root,bg="grey")
bton4=Button(frame_2,text="4",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton4.pack(side=LEFT,padx=7,pady=7)
bton4.bind("<Button-1>",click)

bton5=Button(frame_2,text="5",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton5.pack(side=LEFT,padx=7,pady=7)
bton5.bind("<Button-1>",click)

bton6=Button(frame_2,text="6",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton6.pack(side=LEFT,padx=7,pady=7)
bton6.bind("<Button-1>",click)

bton_sub=Button(frame_2,text="-",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton_sub.pack(side=LEFT,padx=7,pady=7)
bton_sub.bind("<Button-1>",click)

frame_2.pack()

#creating frame 3 contain 1,2,3,addition
frame_3=Frame(root,bg="grey")
bton1=Button(frame_3,text="1",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton1.pack(side=LEFT,padx=7,pady=7)
bton1.bind("<Button-1>",click)

bton2=Button(frame_3,text="2",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton2.pack(side=LEFT,padx=7,pady=7)
bton2.bind("<Button-1>",click)

bton3=Button(frame_3,text="3",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton3.pack(side=LEFT,padx=7,pady=7)
bton3.bind("<Button-1>",click)

bton_add=Button(frame_3,text="+",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton_add.pack(side=LEFT,padx=7,pady=7)
bton_add.bind("<Button-1>",click)

frame_3.pack()

#creating frame 4 contain 0,/,C,=
frame_4=Frame(root,bg="grey")

bton_C=Button(frame_4,text="C",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton_C.pack(side=LEFT,padx=7,pady=7)
bton_C.bind("<Button-1>",click)

bton0=Button(frame_4,text="0",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton0.pack(side=LEFT,padx=7,pady=7)
bton0.bind("<Button-1>",click)

bton_div=Button(frame_4,text="/",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton_div.pack(side=LEFT,padx=7,pady=7)
bton_div.bind("<Button-1>",click)

bton_equal=Button(frame_4,text="=",font=("Arial",13),width=7,height=3,bg="black",fg="white")
bton_equal.pack(side=LEFT,padx=7,pady=7)
bton_equal.bind("<Button-1>",click)

frame_4.pack()

root.mainloop()
'''





















