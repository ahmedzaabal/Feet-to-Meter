from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title("Feet to Meter Conversion App")
window.configure(background="light green")
window.geometry("320x220")
window.resizable(width = False, height = False)


def convert():
    """
    docstring
    """
    value = float(feet_entry.get())
    meter = value * 0.3048
    meter_value.set("%.4f" %meter)

def clear():
    feet_value.set("")
    meter_value.set("")

    

feet_label = Label(window, text="Feet", bg = "purple", fg="white", width = 14)
feet_label.grid(column= 0 , row=-0, padx = 15, pady = 15)
feet_value = DoubleVar()
feet_entry = Entry(window, textvariable=feet_value, width = 14)
feet_entry.grid(column = 1, row = 0)
feet_entry.delete(0, 'end')

meter_label = Label(window, text="Meter", bg = "red", fg="white", width = 14)
meter_label.grid(column= 0 , row=1, padx = 15, pady = 15)
meter_value = DoubleVar()
meter_entry = Entry(window, textvariable=meter_value, width = 14)
meter_entry.grid(column = 1, row = 1)
meter_entry.delete(0, 'end')


convert_button = Button(window, text = "Convert" , bg = "blue", fg = "white", width = 14, command = functions.convert)
convert_button.grid(column=0 , row  = 2, padx = 15, pady = 20)

clear_button = Button(window, text = "Clear", bg = "black", fg = "white", width = 14, command = functions.clear)
clear_button.grid(column= 1 , row = 2, padx = 15)

window.mainloop()