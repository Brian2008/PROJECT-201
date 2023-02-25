from tkinter import *
window = Tk()

window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_interest():
    p = float(principal_entry.get())
    r = float(rot_entry.get())
    t = float(time_entry.get())
    i = (p*r*t)/100
    interest = round(i, 2)
    message.config(text="Interest on "+str(p)+" at rate of interest "+str(r)+" % for "+str(t)+" years is. "+str(interest))

heading_label = Label(window, text="SIMPLE INTEREST CALCULATOR", fg="black", bg="lightcyan", font=("Calibri", 20), bd=5)
heading_label.place(x=50, y=20)

principal_label = Label(window, text="Principal", fg="black", bg="lightcyan", font=("Calibri", 12), bd=1)
principal_label.place(x=50, y=90)
principal_entry = Entry(window, text="", bd=2, width=15)
principal_entry.place(x=150, y=90)

rot_label = Label(window, text="Rate of Interest", fg="black", bg="lightcyan", font=("Calibri", 12), bd=1)
rot_label.place(x=50, y=140)
rot_entry = Entry(window, text="", bd=2, width=15)
rot_entry.place(x=150, y=140)

time_label = Label(window, text="Time", fg="black", bg="lightcyan", font=("Calibri", 12), bd=1)
time_label.place(x=50, y=190)
time_entry = Entry(window, text="", bd=2, width=15)
time_entry.place(x=150, y=190)

calculate_button = Button(window, text="Calculate", fg="black", bg="cyan", bd=4, command=calculate_interest)
calculate_button.place(x=20, y=250)

result_frame = LabelFrame(window, text="Result", bg="lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20, y=300)

message = Label(result_frame, text="", bg="lightcyan", font=("Calibri", 12), width=55)
message.place(x=20, y=40)
message.pack()

window.mainloop()
