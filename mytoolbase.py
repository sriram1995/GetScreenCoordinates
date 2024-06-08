from tkinter import *
import pyautogui, sys

mainwindow=Tk()

mainwindow.title("CO-ORDINATE")
mainwindow.geometry("200x100")

def coord():
        while True:
            x, y = pyautogui.position()
            positionStr = 'X:'+str(x).rjust(4)+'\n'+'Y:'+str(y).rjust(4)
	   #positionStr = 'X:'+str(x)+'Y:'+str(y).rjust(4)
            return positionStr
            #print('\b' * len(positionStr), end='', flush=True)

def display():
	pointer=coord()
	pointer_display=Text(master=mainwindow,height=5,width=10)
	pointer_display.grid(column=0,row=3)
	pointer_display.insert(END,pointer)

heading=Label(text="CO-ORDINATES")
heading.grid(column=0, row=0,)
button=Button(text="click",bitmap="info",bg="blue",command=display)
button.grid(column=0,row=1)
mainwindow.mainloop()