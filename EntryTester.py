from tkinter import *

class Importer:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        Label(frame, text='Enter something').grid(row=0, column=0)
        self.Variable = DoubleVar()
        Entry(frame, textvariable=self.Variable).grid(row=0, column=1)

        b1 = Button(frame, text='Test', command=self.printit)
        b1.grid(row=1, columnspan=2)
        

    def printit(self):
        value = self.Variable.get()
        print(value)


root = Tk()
root.wm_title('Importer App')
app = Importer(root)
root.mainloop()