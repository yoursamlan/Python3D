from tkinter import *
import graphics

root = Tk()
c = Canvas(root, width = 1000, height = 500)
c.pack()
c.configure(background="#252525")

def clear():
    c.delete('all')

s = graphics.shape(r"C:\Users\amlan\Desktop\LAB\simplestreet.obj",c)

s.color = "#ff0000"
s.scale = 1.0
s.location[1] = 10
s.rotation[1] = 90

def rotate(event):
    clear()
    if event.keycode==88:s.rotation[0] += 5
    elif event.keycode==89:s.rotation[1] += 5
    elif event.keycode==90:s.rotation[2] += 5
    s.render()

root.bind('<KeyPress>',rotate)
root.mainloop()
