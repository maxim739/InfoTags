# I want to input an ID # and have 

def notNull(x):     # This function will test whether the entered input is a real value
    if x == "":
        return False
    elif x == " ":
        return False
    else:
        return True


item = input(" Please enter the item numberical ID: ")

while notNull(item) == False:
    print("Please enter a real value")
    item = input(" Please enter the item numberical ID: ")

# Item enter date = time that the item is entered hms
# Use variable as an index, seperate out the h, m, and s and pass them to a function
print(" Please enter the time H/M/S that the object needs to leave: ")
leaveTimeH = input(" Hour: ")   
leaveTimeM = input(" Minutes: ")
leaveTimeS = input(" Seconds: ")
# Could use ymd, but don't expect something to sit in a warehouse for that long
# leaveMinutes = leavetime 
# Create function to convert hms to minutes in the day
def minuteConverter(H, M, S):
    CH = H * 60
    CM = M              # There could be a builtin function that does this
    CS = S / 60         # Look at documentation that sees the minutes of the day
    TM = CH + CM + CS
    return TM

print(" Please enter the bay and shelf number for the item: ")
endLocationBay = input(" Bay Number: ")
endLocationShelf = input(" Shelf Number: ")

print(item + " " + leaveTimeH + " " + leaveTimeM + " " + leaveTimeS + " " + endLocationBay + " " + endLocationShelf)