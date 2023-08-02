from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

def button_click():
    mile = input.get()
    km = round(float(mile) * 1.609344)
    result_label.config(text=km)

button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)









window.mainloop()