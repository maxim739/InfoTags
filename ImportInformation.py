# Create checker to make sure all fields are entered
# Make sure not all fields close when error pops up

import customtkinter
from tkinter import *
import tkinter.messagebox as mb
from datetime import datetime
from xlwt import Workbook

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme('blue')

class Importer:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.current = datetime.now()
        self.currentTime = str(self.current.hour) + ":" + str(self.current.minute) + ":" + str(self.current.second)

        self.wb = Workbook()
        self.sheet = self.wb.add_sheet('Sheet')


        # Make the ID Enterer block
        Label(frame, text='Enter the ID # here: ').grid(row=0, column=0)
        self.IDVar = IntVar()
        Entry(frame, textvariable=self.IDVar).grid(row=0, column=1)
        self.sheet.write(0, self.rowFinder(), str(self.IDVar))


        # The time of arrival block
        Label(frame, text='Current Time: ' + self.currentTime).grid(row=1, column=0)
        self.EntryVar = StringVar()
        b1 = Button(frame, text="Import Current Time? ", command=self.buttonImportTime)
        b1.grid(row=1, column=1)
        Entry(frame, textvariable=self.EntryVar).grid(row=1, column=2)
        self.sheet.write(1, self.rowFinder(), str(self.EntryVar))


        # Time of departure block
        # Enter the departure time from entry time
        Label(frame, text='Desired Departure Time From Entry Time (min): ').grid(row=2, column=0)
        self.DepartVarMins = IntVar()
        Entry(frame, textvariable=self.DepartVarMins).grid(row=2, column=1)
        # Or enter the desired departure time
        Label(frame, text='Or Enter Desired Departure Time: ').grid(row=3, column=0)
        self.DepartVarTime = StringVar()
        Entry(frame, textvariable=self.DepartVarTime).grid(row=3, column=1)

        self.sheet.write(2, self.rowFinder(), str(self.DepartVarMins))


        # Desired location block
        # Desired Bay
        Label(frame, text='Select the desired Bay location: ').grid(row=4, column=0)
        self.BayVar = IntVar()
        Entry(frame, textvariable=self.BayVar).grid(row=5, column=0)
        # Desired Shelf
        Label(frame, text='Select the desired Shelf location: ').grid(row=4, column=1)
        self.ShelfVar = IntVar()
        Entry(frame, textvariable=self.ShelfVar).grid(row=5, column=1)
        # Enter Location String
        self.sheet.write(3, self.rowFinder(), self.locationString())
        # Submit all
        b2 = Button(frame, text="Import All Values ", command=self.buttonImport)
        b2.grid(row=6, columnspan=2, )


        # Convert all the data into binary
        self.binaryConverter()

        self.finalSaveXLS()


    def buttonImportTime(self):
        #print(str(self.current.hour) + ":" + str(self.current.minute) + ":" + str(self.current.second))
        value = self.currentTime
        self.EntryVar.set(value)


    def buttonImport(self):
        # This button will submit everything that has been placed into the app
        self.timeConverter()
        print("ID " + str(self.IDVar.get()) + ", Entry Time " + str(self.EntryVar.get()) + ", Departure Time " + str(self.DepartVarTime.get()) + ", Bay " + str(self.BayVar.get()) + ", Shelf " + str(self.ShelfVar.get()))
        self.IDVar.set(0)
        self.BayVar.set(0)
        self.ShelfVar.set(0)
        self.EntryVar.set(0)
        self.DepartVarMins.set(0)
        print("ID " + str(self.IDVar.get()) + ", Entry Time " + str(self.EntryVar.get()) + ", Departure Time " + str(self.DepartVarTime.get()) + ", Bay " + str(self.BayVar.get()) + ", Shelf " + str(self.ShelfVar.get()))

       

    def timeConverter(self):
        if self.DepartVarTime.get() == '' and self.DepartVarMins.get() == 0:
            mb.showerror("Error", "Please Enter Either a Departure Time or Minutes From Entry Time")
        if self.DepartVarTime.get() != '' and self.DepartVarMins.get() != 0:
            mb.showerror("Error", "Please Enter Either a Departure Time or Minutes From Entry Time")
        else:
            if self.DepartVarMins.get() == 0:
                return("Test2")
                # Find the time delta between EntryVal and DepartureVal
            if self.DepartVarTime.get() == '':
                return("Test3")
                # Add mins to entryval to get the departuretime


    def locationString(self):
        string = ("Bay " + str(self.BayVar.get()) + ", Shelf " + str(self.ShelfVar.get()))
        return(string)


    def finalSaveXLS(self):
        self.wb.save('ImporterSheet.xls')


    def XLSChecker(self):
        return("Test1")
        # Want to make sure that we open the xls file we want to open, and we have header row


    def timeDifference(self):
        return("test")


    def rowFinder(self):
        return(2)
         # This function senses which rows have been taken, and places the new data in the first unused row
         # If rows excede 100 rows, then create a new xls file with the range of dates that have been submitted
            # Need to find how many sheets have already been made inside of the xls file?
            # Create header row 


    def binaryConverter(self):
        return("Test3")
         # Find the ID# and convert it to the index in a dictionary, then convert index to binary
         # Convert only the useful information (numbers) from entry date into binary
         # Convert departure time into minutes, and minutes into binary
         # Convert shelf # and bay # to binary
        self.sheet.write(4, self.rowFinder(), self.binaryConverter())


#root = Tk()
root = customtkinter.CTk()
root.geometry("400x200")
root.wm_title('Importer App')
app = Importer(root)
root.mainloop()