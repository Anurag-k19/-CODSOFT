#Creating window
from tkinter import *
window=Tk()
window.title("To-Do-List")
window.geometry('400x650+100+400')
window.configure(bg='#12181B')

#adding frame
frame=Frame(window) 
frame.pack(pady=40)

#Adding listbox to type in 
list=Listbox(frame,font='Poppins 20 italic bold ',height=10,selectbackground='#636569')
list.pack(side=LEFT,fill=BOTH)


#adding scrollbar
scroll_bar=Scrollbar(frame)
scroll_bar.pack(side=RIGHT,fill=BOTH)
list.config(yscrollcommand=scroll_bar)
scroll_bar.config(command=list.yview)

#Label for entering text
label=Label(window,text='Enter your Task',font='Poppins 18 bold',bg='#c78916')
label.pack(pady=20)

#entry box to add items
entry=Entry(window,font='Poppins 12')
entry.pack()

#functions to add and delete items
def delete_items():
   list.delete(ANCHOR)
def Add_items():
    list.insert(END,entry.get())
    entry.delete(0,END)
    


#Buttons to add and dekete
delete_button=Button(window,text='Delete Task ',font='Poppins 12 bold',bg='#eb1d46',command=delete_items)
delete_button.place(x=220,y=550)
Add_button=Button(window,text='Add Task ',font='Poppins 12 bold',bg='#eb1d46',command=Add_items)
Add_button.place(x=70,y=550)

window.mainloop()

