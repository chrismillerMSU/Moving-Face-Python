import time, tkinter as tk
master = tk.Tk()
master.title( "Crazy Face" )
canvas_width = 800
canvas_height = 800
w = tk.Canvas(master,width=canvas_width,height=canvas_height, bg = "green")
w.pack()
w.create_oval(200,200,600,600)
w.create_line(300,475,500,475)

firstEye = w.create_oval(300,300,350,350)
secondEye= w.create_oval(450,300,500,350)
def moveEyes(event):
    for x in range(0, 7):
        w.move(firstEye,-5,-5)
        w.update()
        time.sleep(.1)
        w.move(secondEye,5,-5)
        w.update()
        time.sleep(.1)
    for x in range(0, 7):
        w.move(firstEye,5,5)
        w.update()
        time.sleep(.1)
        w.move(secondEye,-5,5)
        w.update()
        time.sleep(.1)
def moveMouth(even):
    lowerLip = w.create_line(325,500,475,500)
    leftLip = w.create_line(300,475,325,500)
    rightLip = w.create_line(475,500,500,475)
    for x in range(0,7):
        w.move(lowerLip,0,-2)
        w.delete(leftLip)
        w.delete(rightLip)
        leftLip = w.create_line(300,475,325,500-(2*(x+1)))
        rightLip = w.create_line(475,500-(2*(x+1)),500,475)
        w.update()
        time.sleep(.2)
    for x in range(0,7):
        w.move(lowerLip,0,2)
        w.delete(leftLip)
        w.delete(rightLip)
        leftLip = w.create_line(300,475,325,486+(2*(x+1)))
        rightLip = w.create_line(475,486+(2*(x+1)),500,475)
        w.update()
        time.sleep(.2)
    time.sleep(.35)
    w.delete(rightLip)
    w.delete(leftLip)
    w.delete(lowerLip)



quitButton = tk.Button(master, text='Quit', width=3, command=master.destroy)
quitButton.place(x = 400, y = 60, width=90, height=25)

mouthButton = tk.Button(master, text='Mouth', width = 3)
mouthButton.place(x=200, y=700, width = 90, height = 25)
mouthButton.bind('<Button-1>', moveMouth)

eyesButton = tk.Button(master, text='Eyes', width=3)
eyesButton.place(x = 600, y = 700, width=90, height=25)
eyesButton.bind('<Button-1>', moveEyes)

master.mainloop()
