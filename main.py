from tkinter import *
def button_clicked():
    new_text=float(input.get())
    km=new_text*1.609
    my_label4["text"]=km
window=Tk()
window.title("Mile To Km Converter")
window.minsize(width=200,height=200)
window.config(padx=50,pady=50)
my_label=Label(text="Miles")
my_label.grid(column=2,row=1)
my_label2=Label(text="is equal to")
my_label2.grid(column=0,row=2)
my_label3=Label(text="Km")
my_label3.grid(column=2,row=2)
my_label4=Label(text="0")
my_label4.grid(column=1,row=2)

button=Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=3)
# button2=Button(text="click")
# button2.grid(column=2,row=0 )
#
input=Entry()
input.grid(column=1,row=1)

window.mainloop()