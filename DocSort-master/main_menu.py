from tkinter import *
root=Tk()
subject_names = ["Data Structures(DS)", "Discrete Mathematics(DM)", "Economics and Finance for Engineers(EFE)", "Digital and Electronics Logic Design(DELD)", "Computer Organisation and Microprocessing Interface(COMI)"]
button1=Button(root,text=subject_names[0],fg="black")
button2=Button(root,text=subject_names[1],fg="black")
button3=Button(root,text=subject_names[2],fg="black")
button4=Button(root,text=subject_names[3],fg="black")
button5=Button(root,text=subject_names[4],fg="black")
label=Label(root,text="Select a Subject",fg="red")
label.grid(row=49,column=50)
button1.grid(row=50,column=50)
button2.grid(row=51,column=50)
button3.grid(row=52,column=50)
button4.grid(row=53,column=50)
button5.grid(row=54,column=50)
root.mainloop()