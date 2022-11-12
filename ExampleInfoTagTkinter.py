from tkinter import *

class App:
    def __init__(self, master):
        canvas = Canvas(master, width=400, height=200, background='white')
        canvas.pack()
        # Top right x, y, Bottom Right x, y
        # Add 40 to every x value to go further right
        # Add 50 to every y value to go further down
        # After every block of info add another 20 bits of space
            # This means add 60 to go further right
        canvas.create_rectangle(20, 20, 50, 50, fill='black')
        canvas.create_rectangle(60, 20, 90, 50, outline="black", fill='white')
        canvas.create_rectangle(100, 20, 130, 50, fill='black')
        canvas.create_rectangle(140, 20, 170, 50, outline="black", fill='white')
        canvas.create_rectangle(200, 20, 230, 50, fill='black')
        canvas.create_rectangle(240, 20, 270, 50, outline="black", fill='white')
        canvas.create_rectangle(280, 20, 310, 50, fill='black')
        canvas.create_rectangle(320, 20, 350, 50, outline="black", fill='white')

        
        canvas.create_rectangle(20, 70, 50, 100, fill='black')
        


root = Tk()
app = App(root)
root.mainloop()